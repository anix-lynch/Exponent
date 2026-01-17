"""
Simple scraper using requests - works immediately without browser automation
"""
import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_exponent_page(page_num=1):
    """Scrape one page of Exponent questions"""
    url = f"https://www.tryexponent.com/questions?role=data-analyst&page={page_num}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all question links
        questions = []
        question_links = soup.find_all('a', href=lambda x: x and '/questions/' in x)
        
        for link in question_links:
            # Get question text (usually in h3 or as link text)
            question_text = link.get_text(strip=True)
            
            # Skip if too short or looks like metadata
            if len(question_text) < 15 or question_text.lower() in ['save', 'add answer', 'see full answer']:
                continue
            
            # Try to find category badges nearby
            parent = link.find_parent(['div', 'article'])
            categories = []
            if parent:
                badges = parent.find_all(['span', 'div'], class_=lambda x: x and any(term in str(x).lower() for term in ['badge', 'tag', 'category', 'chip']))
                categories = [b.get_text(strip=True) for b in badges if b.get_text(strip=True)]
            
            questions.append({
                'question': question_text,
                'categories': categories if categories else ['Uncategorized'],
                'url': f"https://www.tryexponent.com{link.get('href')}" if link.get('href', '').startswith('/') else link.get('href', ''),
                'page': page_num
            })
        
        return questions
    
    except Exception as e:
        print(f"Error scraping page {page_num}: {e}")
        return []

def scrape_all_pages(total_pages=6):
    """Scrape all pages"""
    all_questions = []
    
    for page in range(1, total_pages + 1):
        print(f"📄 Scraping page {page}/{total_pages}...")
        questions = scrape_exponent_page(page)
        print(f"   Found {len(questions)} questions")
        all_questions.extend(questions)
        
        if page < total_pages:
            time.sleep(1)  # Be polite
    
    # Remove duplicates
    seen = set()
    unique_questions = []
    for q in all_questions:
        if q['question'] not in seen:
            seen.add(q['question'])
            unique_questions.append(q)
    
    return unique_questions

if __name__ == "__main__":
    print("🚀 Scraping Exponent Data Analyst Questions")
    print("=" * 60)
    
    questions = scrape_all_pages(6)
    
    print(f"\n✅ Extracted {len(questions)} unique questions")
    
    # Save to file
    import os
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'questions_raw.json')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Saved to {output_file}")
    
    # Organize by category
    by_category = {}
    for q in questions:
        for cat in q['categories']:
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(q['question'])
    
    print(f"\n📊 Questions by category:")
    for cat, qs in sorted(by_category.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"   {cat}: {len(qs)}")
