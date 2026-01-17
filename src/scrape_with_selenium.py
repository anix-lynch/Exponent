"""
Selenium-based scraper for Exponent Data Analyst questions
Handles JavaScript rendering and pagination
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time
from typing import List, Dict

def setup_driver():
    """Setup Chrome driver with options"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in background
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36')
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def extract_questions_from_page(driver) -> List[Dict]:
    """Extract questions from current page"""
    questions = []
    
    # Wait for content to load
    time.sleep(2)
    
    # Try multiple selectors to find question elements
    selectors = [
        "//article",
        "//div[contains(@class, 'question')]",
        "//div[contains(@class, 'card')]",
        "//a[contains(@href, '/questions/')]"
    ]
    
    for selector in selectors:
        try:
            elements = driver.find_elements(By.XPATH, selector)
            if elements:
                print(f"  Found {len(elements)} elements with selector: {selector[:50]}")
                
                for elem in elements:
                    try:
                        # Get question text
                        text = elem.text.strip()
                        if not text or len(text) < 10:
                            continue
                        
                        # Try to get the link
                        try:
                            link = elem.get_attribute('href') or elem.find_element(By.TAG_NAME, 'a').get_attribute('href')
                        except:
                            link = ''
                        
                        # Extract first line as question (usually the title)
                        question_text = text.split('\n')[0].strip()
                        
                        # Try to find category (usually in a badge/tag)
                        category = 'Uncategorized'
                        try:
                            category_elem = elem.find_element(By.XPATH, ".//*[contains(@class, 'badge') or contains(@class, 'tag') or contains(@class, 'category')]")
                            category = category_elem.text.strip()
                        except:
                            pass
                        
                        if question_text and len(question_text) > 10:
                            questions.append({
                                'question': question_text,
                                'category': category,
                                'url': link,
                                'full_text': text
                            })
                    except Exception as e:
                        continue
                
                if questions:
                    break  # Found questions, no need to try other selectors
        except Exception as e:
            continue
    
    return questions

def scrape_all_pages(total_pages: int = 6) -> List[Dict]:
    """Scrape all pages"""
    driver = setup_driver()
    all_questions = []
    
    try:
        for page in range(1, total_pages + 1):
            url = f"https://www.tryexponent.com/questions?role=data-analyst&page={page}"
            print(f"\n📄 Scraping page {page}/{total_pages}...")
            print(f"   URL: {url}")
            
            driver.get(url)
            
            # Wait for page to load
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
            except:
                print("  ⚠️  Timeout waiting for page")
            
            questions = extract_questions_from_page(driver)
            print(f"  ✓ Extracted {len(questions)} questions")
            
            all_questions.extend(questions)
            
            # Small delay between pages
            time.sleep(1)
        
    finally:
        driver.quit()
    
    return all_questions

def save_questions(questions: List[Dict], filepath: str):
    """Save questions to JSON"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Saved {len(questions)} questions to {filepath}")

def organize_by_category(questions: List[Dict]) -> Dict[str, List[Dict]]:
    """Organize questions by category"""
    organized = {}
    
    for q in questions:
        category = q.get('category', 'Uncategorized')
        if category not in organized:
            organized[category] = []
        organized[category].append({
            'question': q['question'],
            'url': q.get('url', '')
        })
    
    return organized

if __name__ == "__main__":
    print("🚀 Exponent Data Analyst Questions Scraper (Selenium)")
    print("=" * 70)
    
    try:
        # Scrape all pages
        questions = scrape_all_pages(total_pages=6)
        
        if questions:
            # Remove duplicates
            seen = set()
            unique_questions = []
            for q in questions:
                if q['question'] not in seen:
                    seen.add(q['question'])
                    unique_questions.append(q)
            
            print(f"\n📊 Total unique questions: {len(unique_questions)}")
            
            # Save raw data
            save_questions(unique_questions, '../data/questions_raw.json')
            
            # Organize by category
            organized = organize_by_category(unique_questions)
            save_questions(organized, '../data/questions_by_category.json')
            
            # Print summary
            print("\n" + "=" * 70)
            print("📋 Questions per category:")
            for cat, qs in sorted(organized.items(), key=lambda x: len(x[1]), reverse=True):
                print(f"  • {cat}: {len(qs)}")
        else:
            print("\n❌ No questions extracted")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
