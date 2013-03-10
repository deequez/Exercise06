    i 
import string

#Takes in a file, and reads it, and sets it to a string. 
def returns_a_string(file):
  try:
    f  = open(file)
  except ValueError: 
    print "Try again. The file must end in '.txt'"
    exit()
  s = f.read()
  f.close()
# Removes white spaces at beginning and end of text 
  s.strip()
  s.lower()
  s = s.replace('\n', ' ')
  return s


user_file = raw_input("Please enter your file")
x =returns_a_string(user_file)
#converts string to a list of words
l = x.split()

# creates a dictionary and maps words in the string of text to a number of how often it occurred(count)
count = 0
word_count  = {}
for word in l:
  if len(word) == 0:
    continue
  if word in word_count:
    count += 1
    word_count[word] = count 
  else:
    count = 1
    word_count[word] = count
# generates sorted list of occurring words  
list_of_words = word_count.keys()
sorted_words  = sorted(list_of_words) 


#creates new dictionary that maps numeric count to a list of words that it starts corresponds with  
frequency_to_word_list_dict = {}

#because iterating thru sorted_keys, which is a list of keys taken from w_c dict, we know there will be no reoccurring items in the list
for word in sorted_words:
# if count from word_count dictionary- it was a value- is not in the dictionary, add it as a key and its corresponding words as values
  count = word_count[word]
  if count  not in frequency_to_word_list_dict:
    frequency_to_word_list_dict[count] = [word]
# if count is in dictionary, we add the corresponding value to the end of the list and update with a new list 
  else:
    newlist = frequency_to_word_list_dict[count]
    newlist.append(word)
    frequency_to_word_list_dict[count] = newlist

list_of_freq_keys = frequency_to_word_list_dict.keys()
high_to_low_freq_keys = list_of_freq_keys[::-1]


#

for number in high_to_low_freq_keys:
#is value list a variable or a list?
  valuelist = frequency_to_word_list_dict[number]
  newvaluelist= sorted(valuelist)
  for word in newvaluelist:
    print "%s: %s" % (word, word_count[word])

    
    
    



