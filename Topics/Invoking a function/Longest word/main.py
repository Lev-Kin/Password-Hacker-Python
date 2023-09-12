word1 = input()
word2 = input()

# How many letters does the longest word contain?
longest_length = len(max(word1, word2, key=len))

print(longest_length)
