"""
Scraper for Product Manager interview questions from Exponent
"""
import requests
from bs4 import BeautifulSoup
import json
import time
import os
from typing import List, Dict

def scrape_page(page_num: int = 1) -> List[Dict]:
    """Scrape a single page of PM questions"""
    url = f"https://www.tryexponent.com/questions?role=product-manager&page={page_num}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        questions = []
        
        # Find all question elements
        question_cards = soup.find_all(['article', 'div'], class_=lambda x: x and ('question' in x.lower() or 'card' in x.lower()))
        
        print(f"Page {page_num}: Found {len(question_cards)} question elements")
        
        for card in question_cards:
            title_elem = card.find(['h2', 'h3', 'h4', 'a'])
            if title_elem:
                question_text = title_elem.get_text(strip=True)
                
                if len(question_text) > 10:
                    category_elem = card.find(['span', 'div'], class_=lambda x: x and ('tag' in x.lower() or 'category' in x.lower() or 'badge' in x.lower()))
                    category = category_elem.get_text(strip=True) if category_elem else 'Uncategorized'
                    
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

def scrape_all_pages(total_pages: int = 10) -> List[Dict]:
    """Scrape all pages of PM questions"""
    all_questions = []
    
    for page in range(1, total_pages + 1):
        print(f"\n📄 Scraping page {page}/{total_pages}...")
        questions = scrape_page(page)
        all_questions.extend(questions)
        
        if page < total_pages:
            time.sleep(1)
    
    # Remove duplicates
    seen = set()
    unique_questions = []
    for q in all_questions:
        if q['question'] not in seen:
            seen.add(q['question'])
            unique_questions.append(q)
    
    return unique_questions

if __name__ == "__main__":
    print("🚀 Scraping Exponent Product Manager Questions")
    print("=" * 60)
    
    # Scrape pages (adjust total_pages based on actual count)
    questions = scrape_all_pages(total_pages=10)
    
    if questions:
        # Save raw questions
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        os.makedirs(data_dir, exist_ok=True)
        output_file = os.path.join(data_dir, 'questions_raw.json')
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Saved {len(questions)} questions to {output_file}")
        
        # Print summary
        print(f"\n📊 Total unique questions: {len(questions)}")
