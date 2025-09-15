
paragraph = """Python is a high-level programming language that is widely used for web development, data analysis, artificial intelligence, and scientific computing. Its simple syntax and readability make it an excellent choice for beginners, yet it is powerful enough for experts. Many companies, from startups to tech giants, rely on Python for building applications, automating tasks, and analyzing large datasets."""


import re

# Count characters
num_characters = len(paragraph)

# Count sentences (split by '.', '!', or '?')
sentences = re.split(r'[.!?]+', paragraph)
# Remove empty strings from list
sentences = [s.strip() for s in sentences if s.strip()]
num_sentences = len(sentences)

# Count words
words = re.findall(r'\b\w+\b', paragraph.lower())  # lowercase for uniformity
num_words = len(words)

# Count unique words
unique_words = set(words)
num_unique_words = len(unique_words)

# Bonus: non-whitespace characters
num_non_whitespace = len(paragraph.replace(" ", "").replace("\n", ""))

# Bonus: average words per sentence
avg_words_per_sentence = num_words / num_sentences if num_sentences > 0 else 0

# Bonus: number of non-unique words
num_non_unique_words = num_words - num_unique_words

# Print nicely formatted output
print(f"Paragraph Analysis:")
print(f"- Total characters: {num_characters}")
print(f"- Total sentences: {num_sentences}")
print(f"- Total words: {num_words}")
print(f"- Unique words: {num_unique_words}")
print(f"- Non-whitespace characters: {num_non_whitespace}")
print(f"- Average words per sentence: {avg_words_per_sentence:.2f}")
print(f"- Non-unique words count: {num_non_unique_words}")
