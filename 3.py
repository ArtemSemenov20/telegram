text = input("Введіть текст: ")

ignored_words = {'i', 'you', 'he', 'she', 'it', 'we', 'they',
                 'me', 'him', 'her', 'us', 'them',
                 'my', 'your', 'his', 'its', 'our', 'their',
                 'mine', 'yours', 'hers', 'ours', 'theirs',
                 'is', 'am', 'are', 'was', 'were',
                 'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while',
                 'of', 'in', 'on', 'at', 'by', 'with', 'about', 'against', 'for'}

full_text = text
words = full_text.lower().split()
filtered_words = [word.strip(".,!?") for word in words if word.lower() not in ignored_words]
word_counts = {}
for word in filtered_words:
    word_counts[word] = word_counts.get(word, 0) + 1
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
top_10_words = sorted_word_counts[:10]

print("Top 10 найчастіше зустрічаються слова:", top_10_words)
