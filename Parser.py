import pandas as pd 
from textblob import TextBlob 
import numpy as np 

def get_tags(sentence):
	for item in sentence:
		label_list = []
		tag = TextBlob(item).tags
		for i in range(0, len(tag)):
			label = tag[i][1]
			label_list.append(label)
	return label_list

def count_verb(sentence):
	verb_list = ["VBN", "VBG", "VB", "VBP", "VBZ", "VBD"]
	labels = []
	verb_count = []
	verb_per_sent = []

	for i in range(0, len(sentence)):
		item = sentence[i]
		label_list = []
		tag = TextBlob(item).tags
		num_of_verb = []
		for j in range(0, len(tag)):
			label = tag[j][1]
			label_list.append(label)
			count = np.sum(label in verb_list)
			num_of_verb.append(count)

		numberofverb = np.sum(num_of_verb)
		verb_per_sent.append(numberofverb)
		labels.append(verb_per_sent)

	return verb_per_sent

def get_real_sentence(num_of_verbs, sentence):
	real_sentence = []
	for i in range(0, len(num_of_verbs)):
		if num_of_verbs[i] >= 2:
			real_sentence.append(sentence[i])
	return real_sentence
	