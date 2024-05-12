import nltk
import random
from nltk.corpus import words

nltk.download('words')

# Load the existing words
existing_words = []

# Filter the nltk word list for words of similar length
new_words = [word for word in words.words() if 5 <= len(word) <= 10]

# Add random new words to the existing words until we have 1000 words
while len(existing_words) < 1000:
    word = random.choice(new_words)
    if word not in existing_words:
        existing_words.append(word)

# Write the words to the file
with open("/Users/jakuboleksy/Documents/GitHub/HangMan/src/words.txt", "w") as f:
    for word in existing_words:
        f.write(word + "\n")