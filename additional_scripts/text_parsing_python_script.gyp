# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
# Author: Ousmane Sow
# Program Function: Open txt files give word count of files and give top 30 words
# Top 30 words list code 
# function print_file_stats (location 5347)

# User promt 
fname = input('Enter file name: ')
# confirm file exists
try:
    fhand = open(fname, 'r').read()
# error msg if not file exists
except: 
    print('File cannot be opened:', fname)
    exit()
    
# make everything lower characters 
fhand = fhand.lower()
# count characters
nchar = len(fhand)
print('Characters: ', nchar)
# count lines
nlines = fhand.count('\n')
print('Lines: ', nlines)

# making a stop word list for more accurate analysis
stpwrdlst = [' the', ' to', ' are', ' from', ' or', ' and', 'we ', ' of', ' your', ' you', 'may ', ' our', ' this'
            , ' with', ' that', ' for', ' such', ' other', 'when', ' is', ' by', ' as', ' on', ' will', ' a', ' can',
             ' it', ' if ', ' be', 'in ', '*', 'who ', 'how ', 'more ', 'many ', 'not ', 'like ', 'have ', 'do ', 'which',
            'so ', '�']
# loop to remove stop words
for word in stpwrdlst:
    fhand = fhand.replace(word, '')
    

# my dictionary named d
d = dict()
words = fhand.split()
# for each word in dictionary, if it exists in dictionary, up count by one for that word 
for word in words: 
    d[word] = d.get(word, 0) + 1
# computing the total numer of words  
nwords = sum(d[word] for word in d )
print('numer of words (without stop words): ', nwords)


# Top 30 words
wlst = [(d[word], word) for word in d]
# sort list
wlst.sort()
# count word totals descending
wlst.reverse()
# print sentence elowe on new line
print('\n The 30 most frequent words are\n')
# set i to 1
# print count of top 30 (from 1st word to 30th word) word (sums) from the text file 
i = 1
for count, word in wlst[:30]:
    print('%2s.  %4s %s' % (i, count, word))
    i += 1



