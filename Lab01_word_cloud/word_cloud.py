#python3
#import nltk
#nltk.download("book")

from nltk.book import *

def check_word(string):
	alp = "abcdefghijklmnopqrstuvwxyz"
	for i in alp:
		if i in string:
			return True
	return False

def main():
	text_fd = FreqDist(text1)
	text = {}
	for i in text_fd:
		#print(i, text_fd[i])
		tmp = i.lower()
		if check_word(tmp):
			if text_fd[tmp] in text:
				text[tmp] += text_fd[i]
			else:
				text[tmp] = text_fd[i]
	print(text)
	print(len(text_fd), len(text))

main()
