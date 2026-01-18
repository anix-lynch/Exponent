"""
Scrape Product Marketing Manager interview questions from Exponent
"""
import requests
from bs4 import BeautifulSoup
import json
import time
import os

def scrape_exponent_page(url, page):
    """Scrape a single page of Product Marketing Manager questions"""
    print(f"📄 Scraping page {page}...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <a> tags with href containing /questions/
        all_links = soup.find_all('a', href=True)
        
        page_questions = []
        for link in all_links:
            href = link.get('href', '')
            
            # Only process links that are question links
            if '/questions/' in href and 'contribute' not in href.lower():
                # Get the text from the link (usually in an h3)
                question_text_tag = link.find(['h3', 'h2'])
                if question_text_tag:
                    question_text = question_text_tag.get_text(strip=True)
                    
                    # Basic validation
                    if len(question_text) > 10:
                        full_url = f"https://www.tryexponent.com{href}" if not href.startswith('http') else href
                        
                        page_questions.append({
                            "question": question_text,
                            "categories": [],  # Will be categorized later
                            "url": full_url,
                            "page": page
                        })
        
        print(f"  ✓ Found {len(page_questions)} questions")
        return page_questions
        
    except Exception as e:
        print(f"  ✗ Error on page {page}: {e}")
        return []

def main():
    """Scrape all Product Marketing Manager questions"""
    
    base_url = "https://www.tryexponent.com/questions?page={}&role=pmm"
    all_questions = []
    
    print("🚀 Starting Product Marketing Manager scraper...")
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
    print(f"✅ Scraped {len(unique_questions)} unique Product Marketing Manager questions")
    
    # Save to JSON
    output_dir = os.path.join(os.path.dirname(__file__), '../data')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, 'questions_raw.json')
    with open(output_path, 'w') as f:
        json.dump(unique_questions, f, indent=2)
    
    print(f"💾 Saved to {output_path}")

if __name__ == "__main__":
    main()
