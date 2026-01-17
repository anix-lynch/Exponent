"""
Scrape Finance & Strategy interview questions from Exponent
"""
import requests
from bs4 import BeautifulSoup
import json
import time
import os

def scrape_exponent_page(url, page):
    """Scrape a single page of Finance & Strategy questions"""
    print(f"📄 Scraping page {page}...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find question cards
        question_elements = soup.find_all('a', class_='question-card')
        
        page_questions = []
        for element in question_elements:
            question_text_tag = element.find(['h3', 'h2'])
            if question_text_tag:
                question_text = question_text_tag.get_text(strip=True)
                
                # Filter out non-questions
                if len(question_text) > 20 and '?' in question_text:
                    question_url = element.get('href', '')
                    
                    page_questions.append({
                        "question": question_text,
                        "categories": [],  # Will be categorized later
                        "url": f"https://www.tryexponent.com{question_url}" if question_url and not question_url.startswith('http') else question_url,
                        "page": page
                    })
        
        print(f"  ✓ Found {len(page_questions)} questions")
        return page_questions
        
    except Exception as e:
        print(f"  ✗ Error on page {page}: {e}")
        return []

def main():
    """Scrape all Finance & Strategy questions"""
    
    base_url = "https://www.tryexponent.com/questions?page={}&role=finance-strategy"
    all_questions = []
    
    print("🚀 Starting Finance & Strategy scraper...")
    print("="*70)
    
    # Try up to 10 pages
    for page in range(1, 11):
        url = base_url.format(page)
        questions = scrape_exponent_page(url, page)
        
        if not questions:
            print(f"\n📊 No more questions found after page {page-1}")
            break
        
        all_questions.extend(questions)
        time.sleep(1)  # Be nice to the server
    
    # Remove duplicates
    unique_questions = []
    seen = set()
    for q in all_questions:
        if q['question'] not in seen:
            seen.add(q['question'])
            unique_questions.append(q)
    
    print("="*70)
    print(f"✅ Scraped {len(unique_questions)} unique Finance & Strategy questions")
    
    # Save to JSON
    output_dir = os.path.join(os.path.dirname(__file__), '../data')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, 'questions_raw.json')
    with open(output_path, 'w') as f:
        json.dump(unique_questions, f, indent=2)
    
    print(f"💾 Saved to {output_path}")

if __name__ == "__main__":
    main()
