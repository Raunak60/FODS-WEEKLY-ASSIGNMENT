# Function to find common letters in two words.

def word_intersection(word1, word2):
    return set(word1) & set(word2)

word1, word2 = input("Enter first word: "), input("Enter second word: ")
print("Common letters:", word_intersection(word1, word2))
