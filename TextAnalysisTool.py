#Veranos Inteligencia Artificial // Jan Carlos Morales Rives 1905790

import re
from collections import Counter

def textAnalysis(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        text = file.read()

    # Counting words
    words = re.findall(r'\b\w+\b', text)
    wordCount = len(words)
    
    # Counting sentences
    sentences = re.findall(r'[^.!?]+[.!?]', text)
    sentenceCount = len(sentences)
    
    # Counting paragraphs
    paragraphs = text.split('\n\n')
    paragraphCount = len(paragraphs)
    
    # Calculating average word length
    totalWordLength = sum(len(word) for word in words)
    avgWordLength = totalWordLength / wordCount if wordCount != 0 else 0
    
    # Finding most common words
    wordFrequencies = Counter(words)
    mostCommonWords = wordFrequencies.most_common(10)

    print(f"Title: Poem of End")
    print(f"Word Count: {wordCount}")
    print(f"Sentence Count: {sentenceCount}")
    print(f"Paragraph Count: {paragraphCount}")
    print(f"Average Word Length: {avgWordLength:.2f}")
    print("Most Common Words:")
    for word, freq in mostCommonWords:
        print(f"{word}: {freq}")

# Usage
textAnalysis('EndPoem.txt')