"""
Scrape Program Manager questions from Exponent
"""
import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_page(page_num):
    url = f"https://www.tryexponent.com/questions?page={page_num}&role=program-manager"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        questions = []
        links = soup.find_all('a', href=True)
        
        for link in links:
            href = link.get('href', '')
            
            if '/questions/' not in href or href == '/questions/contribute':
                continue
            if 'basedOn=' in href or '#answers' in href:
                continue
                
            question_text = link.get_text(strip=True)
            
            if len(question_text) < 10:
                continue
            if question_text in ['Share interview', '+ Share interview', 'I was asked this']:
                continue
            if 'answers' in question_text.lower() and len(question_text) < 20:
                continue
                
            question_url = href if href.startswith('http') else f"https://www.tryexponent.com{href}"
            
            questions.append({
                "question": question_text,
                "categories": ["Uncategorized"],
                "url": question_url,
                "page": page_num
            })
        
        return questions
    except Exception as e:
        print(f"Error on page {page_num}: {e}")
        return []

def main():
    all_questions = []
    page = 1
    max_pages = 5
    
    print(f"🚀 Scraping Program Manager questions from Exponent...")
    
    while page <= max_pages:
        print(f"📄 Scraping page {page}...")
        questions = scrape_page(page)
        
        if not questions:
            print(f"✅ No more questions found. Stopping at page {page-1}")
            break
        
        all_questions.extend(questions)
        print(f"   Found {len(questions)} questions")
        
        page += 1
        time.sleep(1)
    
    # Remove duplicates
    seen = set()
    unique_questions = []
    for q in all_questions:
        if q['question'] not in seen:
            seen.add(q['question'])
            unique_questions.append(q)
    
    # Save to JSON
    output_file = 'data/questions_raw.json'
    with open(output_file, 'w') as f:
        json.dump(unique_questions, f, indent=2)
    
    print(f"\n✅ Scraped {len(unique_questions)} unique Program Manager questions")
    print(f"💾 Saved to {output_file}")

if __name__ == "__main__":
    main()
