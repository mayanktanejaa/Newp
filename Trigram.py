import re

def remove_tags(filename):
    file = open(filename)
    word_file = file.read()
    word_file = re.sub('<[^<]+>', "",word_file)
    word_file = re.sub(r'[^\w\s]','',word_file)
    word_file = re.sub(r"[\n\t]*",'',word_file)
    #word_file = word_file.isalpha()
    #print (word_file)
    file.close()
    return word_file


def read_words(words_file):
    print (words_file)
    ret = []
    ret = words_file.split(' ')
        #print (ret)
    return ret

final_lst = []
import os
x = []
for i in os.listdir("/Users/mayank/Desktop/Pythoncode/Trigram"):
    if i.endswith('.txt'):
        x.append("/Users/mayank/Desktop/PythonCode/Trigram/"+i)
#x= ['Anthony and Cleopatra.txt','As You Like It.txt']
for filename in x:
    lst = read_words(remove_tags(filename))
    print (lst)
    final_lst.extend(lst)



# Joining 3 words to create final three words combination list
trigram_final = []
for x in range (0, len(final_lst) - 3):
    trigram_list = []
    for y in range (x, x + 3):
        if final_lst[y].isalpha():
            trigram_list.append (final_lst[y].upper())
        else:
            break
    val = ' '.join(trigram_list)
    trigram_final.append (val)

# Creating dictionary to increment the count of three words - keys
trigram_dic = {}
for a in trigram_final:
    if not a in trigram_dic:
        trigram_dic[a] = 1
    else:
        trigram_dic[a] += 1
# Sorting from top to bottom
trigram_dic_sorted_keys = sorted(trigram_dic, key=trigram_dic.get, reverse=True)
# Printing the top 50
for r in trigram_dic_sorted_keys [:50]:
    print (r, trigram_dic[r])
