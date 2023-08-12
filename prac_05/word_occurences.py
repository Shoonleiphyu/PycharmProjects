text = input("Enter a string: ")
words = text.split()

word_counts = {}
max_word_length = 0

for word in words:
    word = word.lower()  # Convert to lowercase to ensure case-insensitive counting
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        max_word_length = max(max_word_length, len(word))

sorted_word_counts = sorted(word_counts.items())

for word, count in sorted_word_counts:
    formatted_output = f"{word:{max_word_length}} : {count}"
    print(formatted_output)
