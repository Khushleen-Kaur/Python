#    4. Word Analyzer 

# Total characters:
# Total words:
# Total vowels:
# Total consonants:
# Longest word:
# Number of digits:
# Number of special characters:

import re

def characterCounter(s):
    total = 0
    for i in s:
        if(i != ' '):
            total += 1
    return total

def wordCounter(s):
    words = s.split(' ')
    return len(words)

def vowelCounter(s):
    
    countVowel = 0
    for i in s.lower():
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            countVowel += 1
    return countVowel

def consonantCounter(s):
    count = 0
    for i in s:
        x = re.search(r"[A-Za-z]", i)
        if ( x != None):
            count += 1
    return (count - vowelCounter(s))

def LongestWord(s):
    words = s.split(" ")
    wordLength = []
    max = len(words[0])
    for i in range (len(words)):
        count = len(words[i])
        wordLength.append(count)
        if(count > max):
            max = count
    for i in words:
        if (len(i) == max):
            return i

def digitCounter(s):
    count = 0
    for i in s:
        x = re.search(r"[0-9]", i)
        if(x != None):
            count += 1
    return count

def specialCharacterCounter(s):
    count = 0
    for i in s:
        x = re.search(r"[^A-Za-z0-9 ]", i)
        if(x != None):
            count += 1
    return count

def WordAnalyzer():

    loop = ""

    while(loop.lower() != "exit"):
        str = input("Enter a Sentence for Analysis: ")

        if(str == ""):
            print("Please, Enter a Sentence.")
        else:
            print(f"\nSentence Analysis Results:")
            print(f"Total characters: {characterCounter(str)}")
            print(f"Total words: {wordCounter(str)}")
            print(f"Total vowels: {vowelCounter(str)}")
            print(f"Total consonants: {consonantCounter(str)}")
            print(f"Longest word: {LongestWord(str)}")
            print(f"Number of digits: {digitCounter(str)}")
            print(f"Number of special characters: {specialCharacterCounter(str)}")
            print(f" ---- Analysis Completed! ----")

        loop = input("DO you want to analyze a new sentence? (Enter 'exit' to): ").lower()

        
        

        

WordAnalyzer()