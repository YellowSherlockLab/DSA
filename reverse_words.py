def reverse_words(sentence):
	""" This function takes a sentence and reverses the order of words in it"""
	words = sentence.split()
	words = words[::-1]
	return " ".join(words)

print(reverse_words("Hello world"))