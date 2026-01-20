#!/usr/bin/env python3
"""
Categorize questions from 26_IGNORE_ANALYZED.csv into buckets A, B, C, D, E
Based on ChatGPT's classification strategy
"""

import csv
import re

def categorize_question(question_text, notes):
    """Categorize a question into bucket A, B, C, D, or E"""
    q_lower = question_text.lower()
    notes_lower = notes.lower() if notes else ""
    
    # Bucket A: Hard ignore (needs implementation/code)
    # Keywords: implement, write, build, code, create function, design algorithm
    bucket_a_keywords = [
        'implement', 'write a', 'write function', 'build a', 'code', 
        'create function', 'design algorithm', 'design a', 'debug',
        'given.*write', 'given.*implement', 'given.*return', 'given.*find',
        'leetcode', 'algorithm implementation', 'coding', 'programming'
    ]
    
    # Bucket B: Vocab-only (high salvage - definition + when-to-use)
    # Keywords: what is, explain, define, differences between, how does X work
    bucket_b_keywords = [
        'what is', 'explain', 'define', 'differences between', 'difference between',
        'how does.*work', 'what are', 'what does', 'what happens when',
        'encapsulation', 'oop', 'inheritance', 'composition', 'ram vs rom',
        'median vs mean', 'overfitting', 'underfitting', 'polymorphism',
        'virtual function', 'interface vs', 'abstract class', 'stack vs heap',
        'multithreading', 'multiprocessing', 'garbage collection', 'hash map',
        'callback', 'malloc', 'calloc', 'realloc', 'cpu', 'gpu', 'rom'
    ]
    
    # Bucket C: ML concept + guardrails (medium-high salvage)
    # Keywords: ML/ML-related concepts, production testing, monitoring, hallucinations, privacy
    bucket_c_keywords = [
        'overfitting', 'underfitting', 'imbalanced data', 'test.*production',
        'monitor.*model', 'hallucination', 'sensitive data', 'privacy',
        'model.*production', 'deploy.*model', 'evaluate.*model', 'loss function',
        'regularization', 'cross-validation', 'bias-variance', 'cnn', 'rnn',
        'lstm', 'transformer', 'bert', 'logistic regression', 'linear regression',
        'decision tree', 'random forest', 'k-means', 'clustering', 'neural network',
        'gradient descent', 'batch normalization', 'semantic segmentation',
        'computer vision', 'nlp', 'natural language', 'reinforcement learning',
        'semi-supervised', 'tf-idf', 'auto-regression', 'relu', 'sigmoid',
        'l1', 'l2', 'regression', 'classification', 'feature selection',
        'model selection', 'hyperparameter', 'training', 'validation', 'testing'
    ]
    
    # Bucket D: Brain teasers / math puzzles (frozen zone)
    # Keywords: probability, dice, cards, estimation puzzles, true positive, false positive
    bucket_d_keywords = [
        'probability', 'dice', 'card', 'roll.*dice', 'coin.*flip', 'biased coin',
        'how many', 'estimate', 'chicken', 'ping pong', 'tennis ball', 'helicopter',
        'airplane', 'parking spot', 'wedding', 'breath', 'wine', 'grain.*rice',
        'autobahn', 'shoe', 'laundry', 'oil.*barrel', 'traffic light', 'swimming pool',
        'true positive', 'false positive', 'true negative', 'false negative',
        'precision', 'recall', 'f1', 'confusion matrix', 'roc', 'auc',
        'hypothesis testing', 'p-value', 'statistical test', 'bayes.*theorem',
        'expected value', 'distribution.*uniform', 'math calculation', 'brain teaser',
        'estimation', 'puzzle'
    ]
    
    # Bucket E: Behavioral / personal (salvage - storytelling)
    # Keywords: tell me about, why did you, how do you work, experience with, strategies
    bucket_e_keywords = [
        'tell me about', 'why did you', 'how do you work', 'experience with',
        'strategies.*communicate', 'distributed team', 'geographically dispersed',
        'day as a', 'become.*engineer', 'become.*software', 'trip', 'travel',
        'where would you', 'activities.*motivate', 'project.*worked', 'outcome',
        'research topic.*interesting', 'approach to', 'handle trade-off',
        'behavioral', 'personal', 'self-assessment'
    ]
    
    # Check Bucket A first (hard ignore - needs code)
    for keyword in bucket_a_keywords:
        if re.search(keyword, q_lower) or re.search(keyword, notes_lower):
            # But exclude if it's clearly ML concept (Bucket C) or behavioral (Bucket E)
            if any(ml_kw in q_lower for ml_kw in ['model', 'ml', 'machine learning', 'neural', 'training', 'evaluate']):
                # Check if it's actually asking for implementation vs concept
                if any(impl_kw in q_lower for impl_kw in ['implement', 'write', 'code', 'build', 'create function']):
                    return 'A'
                # Otherwise might be C
            elif any(beh_kw in q_lower for beh_kw in ['tell me', 'why did', 'experience', 'strategies']):
                return 'E'
            else:
                return 'A'
    
    # Check Bucket E (Behavioral - put back)
    for keyword in bucket_e_keywords:
        if re.search(keyword, q_lower) or re.search(keyword, notes_lower):
            return 'E'
    
    # Check Bucket C (ML concepts - put back to LHF)
    for keyword in bucket_c_keywords:
        if re.search(keyword, q_lower) or re.search(keyword, notes_lower):
            # But exclude if it's asking for implementation
            if any(impl_kw in q_lower for impl_kw in ['implement', 'write', 'code', 'build']):
                return 'A'  # ML implementation = hard ignore
            return 'C'
    
    # Check Bucket D (Brain teasers / math - frozen zone)
    for keyword in bucket_d_keywords:
        if re.search(keyword, q_lower) or re.search(keyword, notes_lower):
            return 'D'
    
    # Check Bucket B (Vocab-only - high salvage)
    for keyword in bucket_b_keywords:
        if re.search(keyword, q_lower) or re.search(keyword, notes_lower):
            return 'B'
    
    # Default: if notes say "coding" or "implementation", it's A
    if 'coding' in notes_lower or 'implementation' in notes_lower or 'algorithm' in notes_lower:
        return 'A'
    
    # Default: if notes say "behavioral", it's E
    if 'behavioral' in notes_lower:
        return 'E'
    
    # Default: if notes say "ml" or "machine learning", it's C
    if 'ml' in notes_lower or 'machine learning' in notes_lower:
        return 'C'
    
    # Default: if notes say "math" or "probability", it's D
    if 'math' in notes_lower or 'probability' in notes_lower or 'estimation' in notes_lower:
        return 'D'
    
    # Unknown - default to A (hard ignore) if unclear
    return 'A'

def main():
    input_file = '26_IGNORE_ANALYZED.csv'
    
    buckets = {
        'A': [],  # Hard ignore (needs code)
        'B': [],  # Vocab-only (separate list)
        'C': [],  # ML concepts (put back to main)
        'D': [],  # Brain teasers/math (keep in ignore)
        'E': []   # Behavioral (put back to main)
    }
    
    # Read and categorize
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            bucket = categorize_question(row['question_text'], row['notes'])
            buckets[bucket].append(row)
    
    # Print statistics
    total = sum(len(b) for b in buckets.values())
    print(f"\n{'='*60}")
    print(f"Categorization Results (Total: {total} questions)")
    print(f"{'='*60}")
    print(f"Bucket A (Hard Ignore - needs code): {len(buckets['A'])} ({len(buckets['A'])/total*100:.1f}%)")
    print(f"Bucket B (Vocab-only - separate list): {len(buckets['B'])} ({len(buckets['B'])/total*100:.1f}%)")
    print(f"Bucket C (ML concepts - put back): {len(buckets['C'])} ({len(buckets['C'])/total*100:.1f}%)")
    print(f"Bucket D (Brain teasers/math - frozen): {len(buckets['D'])} ({len(buckets['D'])/total*100:.1f}%)")
    print(f"Bucket E (Behavioral - put back): {len(buckets['E'])} ({len(buckets['E'])/total*100:.1f}%)")
    print(f"{'='*60}\n")
    
    # Write separate files
    fieldnames = ['question_id', 'question_text', 'priority', 'pattern_id', 'pattern_name', 
                  'solving_formula', 'notes', 'salvageable', 'simple_explanation', 'bucket']
    
    # Bucket A: Hard ignore
    with open('26_BUCKET_A_HARD_IGNORE.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in buckets['A']:
            row['bucket'] = 'A'
            writer.writerow(row)
    
    # Bucket B: Vocab-only (separate list)
    with open('26_BUCKET_B_VOCAB_ONLY.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in buckets['B']:
            row['bucket'] = 'B'
            writer.writerow(row)
    
    # Bucket C: ML concepts (put back to main)
    with open('26_BUCKET_C_ML_CONCEPTS.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in buckets['C']:
            row['bucket'] = 'C'
            writer.writerow(row)
    
    # Bucket D: Brain teasers/math (keep in ignore)
    with open('26_BUCKET_D_FROZEN_ZONE.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in buckets['D']:
            row['bucket'] = 'D'
            writer.writerow(row)
    
    # Bucket E: Behavioral (put back to main)
    with open('26_BUCKET_E_BEHAVIORAL.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in buckets['E']:
            row['bucket'] = 'E'
            writer.writerow(row)
    
    # Combined: C + E (put back to main)
    with open('26_TO_PUT_BACK.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in buckets['C'] + buckets['E']:
            row['bucket'] = 'C' if row in buckets['C'] else 'E'
            writer.writerow(row)
    
    print("Files created:")
    print("  - 26_BUCKET_A_HARD_IGNORE.csv (hard ignore)")
    print("  - 26_BUCKET_B_VOCAB_ONLY.csv (separate list)")
    print("  - 26_BUCKET_C_ML_CONCEPTS.csv (put back)")
    print("  - 26_BUCKET_D_FROZEN_ZONE.csv (keep in ignore)")
    print("  - 26_BUCKET_E_BEHAVIORAL.csv (put back)")
    print("  - 26_TO_PUT_BACK.csv (C + E combined)")

if __name__ == '__main__':
    main()
