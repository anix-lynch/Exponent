#!/usr/bin/env python3
import csv
import re

def get_simple_explanation(question_text, notes):
    """Provide ELI5 explanation for salvageable questions"""
    text_lower = question_text.lower()
    notes_lower = notes.lower()
    
    # Hash Map / Lookup patterns
    if any(x in text_lower for x in ['hash', 'hashmap', 'hash map', 'key-value', 'dictionary']):
        return "Use a lookup table - store things by name so you can find them instantly. Like a phone book: name → number"
    
    if 'duplicate' in text_lower and 'array' in text_lower:
        return "Use a hash map to remember what you've seen before. Check each item: have I seen this? If yes, it's a duplicate"
    
    if 'two sum' in text_lower or 'target sum' in text_lower:
        return "Use hash map: for each number, check if (target - number) exists. Like: I need 10, I have 7, do I have 3?"
    
    # Math/Probability - MUST check before frequency (since 'count' appears in probability questions)
    if 'expected' in text_lower and ('cost' in text_lower or 'value' in text_lower):
        return "Expected value = sum of (probability × value). For each outcome, multiply chance by cost, add them up"
    
    if 'probability' in text_lower:
        return "Probability = favorable outcomes / total outcomes. Calculate chance of something happening"
    
    if 'distribution' in text_lower:
        return "Distribution = how values are spread. Describe shape: normal (bell curve), skewed, uniform, etc."
    
    # Frequency Counting - check after probability
    if any(x in text_lower for x in ['frequency', 'how many times', 'most frequent', 'top k']):
        return "Count how many times each thing appears. Use hash map: thing → count++. Then find the biggest counts"
    
    if 'anagram' in text_lower:
        return "Group words that have same letters. Sort letters of each word, use that as key in hash map"
    
    # Stack patterns
    if 'parentheses' in text_lower or 'balanced' in text_lower:
        return "Use a stack - last opened must be first closed. Like stacking plates: last in, first out"
    
    if 'next greater' in text_lower or 'next smaller' in text_lower:
        return "Use a stack to remember previous numbers. Compare current with top of stack"
    
    # Two Pointers
    if any(x in text_lower for x in ['palindrome', 'reverse', 'two pointers', 'left', 'right']):
        return "Use two pointers - one from left, one from right. Compare and move them toward each other"
    
    if 'container with most water' in text_lower or 'trapping rainwater' in text_lower:
        return "Two pointers from both ends. Move the shorter one inward, calculate area at each step"
    
    # Sliding Window
    if any(x in text_lower for x in ['sliding window', 'substring', 'subarray', 'longest', 'shortest']):
        return "Use sliding window - expand right until condition met, then shrink left. Like a rubber band"
    
    if 'longest substring without repeating' in text_lower:
        return "Sliding window + hash map. Expand right, if duplicate found, shrink left until no duplicates"
    
    # Binary Search
    if any(x in text_lower for x in ['sorted array', 'binary search', 'closest', 'search in rotated']):
        return "Binary search: cut problem in half each time. Compare middle with target, eliminate half"
    
    # Tree traversal
    if any(x in text_lower for x in ['tree', 'binary tree', 'bst', 'traversal', 'ancestor']):
        return "Visit nodes in order (left → root → right or root → left → right). Use recursion or stack"
    
    # Graph traversal
    if any(x in text_lower for x in ['graph', 'shortest path', 'island', 'bfs', 'dfs']):
        return "Graph = nodes connected by edges. Visit neighbors, mark visited. Use queue (BFS) or stack (DFS)"
    
    # Dynamic Programming
    if 'knapsack' in text_lower:
        return "DP: For each item, decide take or skip. Build table: capacity × items. Remember best value for each capacity"
    
    if any(x in text_lower for x in ['dp', 'dynamic programming', 'memoization', 'climbing stairs', 'coin change']):
        return "Break into smaller problems. Solve each once, remember answers. Build up from small to big"
    
    # Greedy
    if any(x in text_lower for x in ['greedy', 'minimum', 'maximum', 'optimal']):
        return "Greedy: pick best option at each step. Don't look back, just take what's best now"
    
    # Sorting
    if 'sort' in text_lower:
        return "Arrange items in order. Compare pairs, swap if needed. Many ways: quick sort, merge sort"
    
    # String manipulation
    if any(x in text_lower for x in ['string', 'substring', 'pattern', 'match']):
        return "Work with text. Compare characters, find patterns, extract parts"
    
    # Array manipulation
    if 'array' in text_lower and not any(x in text_lower for x in ['tree', 'graph', 'matrix']):
        return "Loop through items, check conditions, collect results. Basic: for each item → if condition → act"
    
    # Math/Probability - check before frequency
    if 'expected' in text_lower and 'cost' in text_lower:
        return "Expected value = sum of (probability × value). For each outcome, multiply chance by cost, add them up"
    
    if 'probability' in text_lower:
        return "Probability = favorable outcomes / total outcomes. Calculate chance of something happening"
    
    if 'distribution' in text_lower:
        return "Distribution = how values are spread. Describe shape: normal (bell curve), skewed, uniform, etc."
    
    # Estimation questions
    if any(x in text_lower for x in ['estimate', 'how many', 'how much', 'how long']):
        return "Break into parts, estimate each, multiply. Show your thinking: assumptions → calculations → answer"
    
    # ML Theory - salvageable with simple concepts
    if 'overfitting' in text_lower:
        return "Model memorizes training data too well, fails on new data. Fix: more data, simpler model, regularization"
    
    if 'bias-variance' in text_lower:
        return "Bias = too simple (underfitting). Variance = too complex (overfitting). Need balance"
    
    if 'cross-validation' in text_lower:
        return "Split data into parts. Train on some, test on others. Rotate to check if model works well"
    
    if 'regularization' in text_lower:
        return "Penalize complex models. Add cost for complexity to prevent overfitting"
    
    if any(x in text_lower for x in ['cnn', 'convolutional', 'rnn', 'recurrent', 'neural network']):
        return "CNN = good for images (spatial patterns). RNN = good for sequences (time patterns)"
    
    if 'transformer' in text_lower or 'bert' in text_lower:
        return "Attention mechanism: focus on important parts. Like reading - pay attention to key words"
    
    # Data structures - simple concepts
    if 'queue' in text_lower:
        return "First in, first out. Like a line: first person in line is first served"
    
    if 'stack' in text_lower and 'parentheses' not in text_lower:
        return "Last in, first out. Like a stack of plates: add to top, remove from top"
    
    if 'linked list' in text_lower:
        return "Chain of nodes. Each node points to next. Easy to add/remove, but must traverse to find"
    
    if 'trie' in text_lower:
        return "Tree for strings. Each level = one character. Fast prefix search"
    
    # General algorithm concepts
    if 'backtracking' in text_lower:
        return "Try a path, if it fails, go back and try another. Like solving a maze"
    
    if 'divide and conquer' in text_lower or 'merge sort' in text_lower:
        return "Break problem in half, solve each half, combine results"
    
    # If it's a coding implementation question but salvageable
    if 'implement' in text_lower or 'build' in text_lower or 'create' in text_lower:
        return "Break into steps. Identify data structures needed. Write functions for each operation"
    
    # Default for salvageable questions
    return "Understand the concept, break into steps, use appropriate data structure (hash map, array, tree, etc.)"

def is_salvageable(question_text, notes):
    """Determine if question is salvageable with simple explanation"""
    text_lower = question_text.lower()
    notes_lower = notes.lower()
    
    # NOT salvageable - truly hard
    hard_patterns = [
        'red-black tree', 'avl tree', 'b-tree',
        'gpu', 'cuda', 'memory management', 'garbage collection', 'malloc',
        'multithreading', 'multiprocessing', 'concurrency',
        'sql parser', 'regex parser', 'compiler',
        'web crawler', 'distributed system',
        'proof', 'mathematical proof', 'limit',
        'batch normalization', 'mask r-cnn', 'semantic segmentation',
        'ray tracing', '3d graphics', 'directx',
        'jvm', 'java internals', 'c internals',
        'system design', 'architecture',
        'incomplete question', 'unclear',
        'personal question', 'behavioral', 'not relevant',
        'philosophical', 'abstract concept'
    ]
    
    if any(pattern in text_lower or pattern in notes_lower for pattern in hard_patterns):
        return False
    
    # Salvageable - can explain concept
    salvageable_patterns = [
        'array', 'string', 'hash', 'map', 'tree', 'graph', 'stack', 'queue',
        'sort', 'search', 'duplicate', 'palindrome', 'two sum', 'frequency',
        'sliding window', 'two pointers', 'binary search',
        'dynamic programming', 'greedy', 'backtracking', 'knapsack',
        'overfitting', 'bias', 'variance', 'regularization', 'cross-validation',
        'neural network', 'cnn', 'rnn', 'transformer',
        'estimate', 'probability', 'distribution',
        'implement', 'build', 'create', 'design'
    ]
    
    if any(pattern in text_lower or pattern in notes_lower for pattern in salvageable_patterns):
        return True
    
    # Default: not salvageable if unclear
    return False

# Process the file
with open('26_IGNORE.csv', 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# Add analysis
output_rows = []
for row in rows:
    salvageable = is_salvageable(row['question_text'], row.get('notes', ''))
    simple_explanation = get_simple_explanation(row['question_text'], row.get('notes', '')) if salvageable else 'N/A - Too complex or not relevant'
    
    new_row = row.copy()
    new_row['salvageable'] = 'YES' if salvageable else 'NO'
    new_row['simple_explanation'] = simple_explanation
    output_rows.append(new_row)

# Write output
with open('26_IGNORE_ANALYZED.csv', 'w', encoding='utf-8', newline='') as outfile:
    fieldnames = list(rows[0].keys()) + ['salvageable', 'simple_explanation']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(output_rows)

# Print summary
salvageable_count = sum(1 for row in output_rows if row['salvageable'] == 'YES')
print(f"Total questions: {len(output_rows)}")
print(f"Salvageable: {salvageable_count} ({salvageable_count/len(output_rows)*100:.1f}%)")
print(f"Not salvageable: {len(output_rows) - salvageable_count}")
