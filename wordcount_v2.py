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

for x in create_words:
    if x not in wordcount_dict:
        wordcount_dict[x] = 1
    elif x in wordcount_dict:
        wordcount_dict[x] += 1

for key, value in wordcount_dict.iteritems():
	print key, value


# ordered_dict =  OrderedDict(sorted(wordcount_dict.items(), key=lambda t: t[0]))
# print ordered_dict