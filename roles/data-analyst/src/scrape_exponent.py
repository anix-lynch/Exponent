"""
Automated scraper for Exponent Data Analyst questions
Handles pagination and extracts questions with categories
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from typing import List, Dict

def scrape_page(page_num: int = 1) -> List[Dict]:
    """Scrape a single page of questions"""
    url = f"https://www.tryexponent.com/questions?role=data-analyst&page={page_num}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        questions = []
        
        # Find all question elements (adjust selectors based on actual HTML)
        question_cards = soup.find_all(['article', 'div'], class_=lambda x: x and ('question' in x.lower() or 'card' in x.lower()))
        
        print(f"Page {page_num}: Found {len(question_cards)} question elements")
        
        for card in question_cards:
            # Extract question text
            title_elem = card.find(['h2', 'h3', 'h4', 'a'])
            if title_elem:
                question_text = title_elem.get_text(strip=True)
                
                # Extract category/tags
                category_elem = card.find(['span', 'div'], class_=lambda x: x and ('tag' in x.lower() or 'category' in x.lower() or 'badge' in x.lower()))
                category = category_elem.get_text(strip=True) if category_elem else 'Uncategorized'
                
                # Extract URL
                link = card.find('a', href=True)
                question_url = link['href'] if link else ''
                if question_url and not question_url.startswith('http'):
                    question_url = f"https://www.tryexponent.com{question_url}"
                
                questions.append({
                    'question': question_text,
                    'category': category,
                    'url': question_url,
                    'page': page_num
                })
        
        return questions
    
    except Exception as e:
        print(f"Error scraping page {page_num}: {e}")
        return []

def scrape_all_pages(total_pages: int = 6) -> List[Dict]:
    """Scrape all pages of questions"""
    all_questions = []
    
    for page in range(1, total_pages + 1):
        print(f"\nScraping page {page}/{total_pages}...")
        questions = scrape_page(page)
        all_questions.extend(questions)
        
        # Be polite - add delay between requests
        if page < total_pages:
            time.sleep(1)
    
    return all_questions

def save_questions(questions: List[Dict], filepath: str = '../data/questions.json'):
    """Save questions to JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Saved {len(questions)} questions to {filepath}")

def organize_by_category(questions: List[Dict]) -> Dict[str, List[str]]:
    """Organize questions by category"""
    organized = {}
    
    for q in questions:
        category = q.get('category', 'Uncategorized')
        if category not in organized:
            organized[category] = []
        organized[category].append(q['question'])
    
    return organized

if __name__ == "__main__":
    print("🚀 Starting Exponent Data Analyst Questions Scraper")
    print("=" * 60)
    
    # Scrape all 6 pages (120 questions total, 20 per page)
    questions = scrape_all_pages(total_pages=6)
    
    if questions:
        # Save raw questions
        save_questions(questions, '../data/questions_raw.json')
        
        # Organize by category
        organized = organize_by_category(questions)
        save_questions(organized, '../data/questions_by_category.json')
        
        # Print summary
        print("\n" + "=" * 60)
        print(f"📊 Summary:")
        print(f"Total questions: {len(questions)}")
        print(f"Categories found: {len(organized)}")
        print("\nQuestions per category:")
        for cat, qs in sorted(organized.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"  {cat}: {len(qs)}")
    else:
        print("❌ No questions extracted. The page might require JavaScript rendering.")
        print("Switching to Selenium-based approach...")
