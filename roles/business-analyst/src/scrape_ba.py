"""
Scrape Business Analyst questions from Exponent
"""
import requests
from bs4 import BeautifulSoup
import json
import time
import os

def scrape_page(page_num: int = 1):
    url = f"https://www.tryexponent.com/questions?page={page_num}&role=business-analyst"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        questions = []
        
        question_links = soup.find_all('a', href=lambda x: x and '/questions/' in x and '/questions/contribute' not in x)
        print(f"Page {page_num}: Found {len(question_links)} potential question links")
        
        seen_questions = set()
        for link in question_links:
            question_text = link.get_text(strip=True)
            question_url = link.get('href', '')
            
            if (len(question_text) > 15 and 
                question_text not in seen_questions and
                'answer' not in question_text.lower() and
                'asked this' not in question_text.lower() and
                'share interview' not in question_text.lower()):
                
                if not question_url.startswith('http'):
                    question_url = f"https://www.tryexponent.com{question_url}"
                
                questions.append({
                    'question': question_text,
                    'categories': [],
                    'url': question_url,
                    'page': page_num
                })
                seen_questions.add(question_text)
        
        print(f"  -> Extracted {len(questions)} valid questions")
        return questions
    except Exception as e:
        print(f"Error scraping page {page_num}: {e}")
        return []

def main():
    all_questions = []
    print("🚀 Starting Business Analyst scraper...")
    print("="*70)
    
    for page in range(1, 15):
        print(f"\nScraping page {page}...")
        questions = scrape_page(page)
        if not questions:
            print(f"No more questions found after page {page-1}")
            break
        all_questions.extend(questions)
        time.sleep(1)
    
    unique_questions = []
    seen = set()
    for q in all_questions:
        if q['question'] not in seen:
            seen.add(q['question'])
            unique_questions.append(q)
    
    print("="*70)
    print(f"✅ Scraped {len(unique_questions)} unique Business Analyst questions")
    
    output_dir = os.path.join(os.path.dirname(__file__), '../data')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'questions_raw.json')
    with open(output_path, 'w') as f:
        json.dump(unique_questions, f, indent=2)
    print(f"💾 Saved to {output_path}")

if __name__ == "__main__":
    main()
