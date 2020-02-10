# Fungkiat Phadejtaku
# 60070069
# github: https://github.com/CokeFung/introduction2NLP2020

#python3
#import nltk
#nltk.download("book")
from nltk.book import *
import os
from os import path
import matplotlib.pyplot as pyplot

def check_word(string):
	alp = "abcdefghijklmnopqrstuvwxyz".upper()
	if len(string) < 2:
		return False
	for i in alp:
		if i in string:
			return True
	return False

def list2string(word_list):
	text = " "
	for i in word_list:
		#print("%04d" % word_list[i], i)
		text += (i[0]+"#")*i[1]
	#print(text)
	return text

def plot_graph_of_k(k_list, num):
	#(list(k_list.values()))
	pyplot.figure()
	pyplot.plot(list(k_list.keys()), list(k_list.values()))
	pyplot.xlabel('Rank')
	pyplot.ylabel('k value (Freq x Rank)')
	pyplot.title('Book ' + str(num))
	pyplot.savefig('./graph/book'+str(num)+".png")

def writeFreq2File(text, num):
	text2write = "Rank\tWord\t\tFrequency\tFreq x Rank\n"
	k_list = {}
	for i in range(len(text)):
		k_of_rank = (i+1)*text[i][1]
		k_list[i+1] = k_of_rank
		text2write += ("%02d" % (i+1))+"\t"+text[i][0]+"\t\t"+str(text[i][1])+"\t\t"+("%d" % k_of_rank)+"\n"
	f = open(("./word_freq/word_freq_text"+str(num)+".txt"), "w+")
	f.write(text2write)
	f.close()
	plot_graph_of_k(k_list, num)

def doWordCloud(words_from_book, num):
	words_fd = FreqDist(words_from_book)
	words = {}
	for i in words_fd:
		#print(i, words_fd[i])
		tmp = i.upper()
		if check_word(tmp):
			if tmp in words:
				words[tmp] += words_fd[i]
			else:
				words[tmp] = words_fd[i]
	text = sorted(sorted(words.items()), key=lambda x:x[1]*-1)[:30]
	#print(text)
	text2 = list2string(text)
	writeFreq2File(text, num)

def main():
	#generate text books's name
	for i in range(1, 10):
		doWordCloud(eval('text'+str(i)), i)

main()
