from sys import argv
from collections import OrderedDict


script, filename = argv

in_file = open(filename)
indata = in_file.read()

cleanup_data = indata.lower().replace('?', ' ').replace('.', ' ').replace(
                '!', ' ').replace(',', ' ').replace('--', ' ').replace(
                '"', ' ').replace(';', ' ').replace('_', ' ').replace(
                ':', ' ')

create_words = cleanup_data.split()

wordcount_dict = {}

for word in create_words:
	wordcount_dict[word] = wordcount_dict.get(word,0) + 1   

# for key, value in wordcount_dict.iteritems():
# 	print key, value

list_of_dict = sorted(wordcount_dict.items())


# Learn about lambda, etc.
# http://stackoverflow.com/questions/13781981/lambda-function-in-sorted-dictionary-list-comprehension


print sorted(list_of_dict, key=lambda t: t[1], reverse=True)