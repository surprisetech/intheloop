# def countWords(textList, punctRm, excludeWordsList):

import string
from wordOps import countWords, punctRm

# sample excludeWordsList
excludeWordsList = ['abbra','kadabra','hoccus','poccus']

# uncomment to use production exclusion list
#from app import excludeWordsList

#Testing passing empty textList to wordOps
#Length should = 0

test = countWords([],[],[])
assert len(test) == 0

test = countWords([],['\''],[])
assert len(test) == 0

test = countWords([],['\''],['a'])
assert len(test) == 0

test = countWords([],['\''],['word'])
assert len(test) == 0

test = countWords([],['\''],['a','word'])
assert len(test) == 0

test = countWords([],['\''],[1])
assert len(test) == 0

test = countWords([],['\''],[0])
assert len(test) == 0

test = countWords([],['\''],[-1])
assert len(test) == 0

test = countWords([],['\''],['a','word', 1, 0 , -1])
assert len(test) == 0

test = countWords([],['\''],excludeWordsList)
assert len(test) == 0

test = countWords([],[1],excludeWordsList)
assert len(test) == 0

test = countWords([],[0],excludeWordsList)
assert len(test) == 0

test = countWords([],[-1],excludeWordsList)
assert len(test) == 0

test = countWords([],[punctRm],excludeWordsList)
assert len(test) == 0


#Testing countWords does not remove intended words
test = countWords(['a'],[],[])
assert len(test) == 1
assert test[0] == ('a',1)

test = countWords(['a','a'],[],[])
assert len(test) == 1
assert test[0] == ('a',2)

test = countWords(['a b','a'],[],[])
assert len(test) == 2
assert test[0] == ('a',2)
assert test[1] == ('b',1)

test = countWords(['a b','a b'],[],[])
assert len(test) == 2
assert test[0] == ('a',2)
assert test[1] == ('b',2)

test = countWords(['The quick brown fox','jumped over the lazy dog'],[],[])
assert len(test) == 8
assert test[0] == ('the',2)
assert test[1] == ('quick',1)
assert test[2] == ('brown',1)
assert test[3] == ('fox',1)
assert test[4] == ('jumped',1)
assert test[5] == ('over',1)
assert test[6] == ('lazy',1)
assert test[7] == ('dog',1)

test = countWords(['a','b'],[],[])
assert len(test) == 2
assert test[0] == ('a',1)
assert test[1] == ('b',1)

test = countWords(['a','a','b'],[],[])
assert len(test) == 2
assert test[0] == ('a',2)
assert test[1] == ('b',1)

test = countWords(['a'],['c'],[])
assert len(test) == 1
assert test[0] == ('a',1)

test = countWords(['a','a'],['c'],[])
assert len(test) == 1
assert test[0] == ('a',2)

test = countWords(['a','b'],['c'],[])
assert len(test) == 2
assert test[0] == ('a',1)
assert test[1] == ('b',1)

test = countWords(['a','a','b'],['c'],[])
assert len(test) == 2
assert test[0] == ('a',2)
assert test[1] == ('b',1)

test = countWords(['The quick brown fox','jumped over the lazy dog'],['!'],[])
assert len(test) == 8
assert test[0] == ('the',2)
assert test[1] == ('quick',1)
assert test[2] == ('brown',1)
assert test[3] == ('fox',1)
assert test[4] == ('jumped',1)
assert test[5] == ('over',1)
assert test[6] == ('lazy',1)
assert test[7] == ('dog',1)

test = countWords(['a'],[],['c'])
assert len(test) == 1
assert test[0] == ('a',1)

test = countWords(['a','a'],[],['c'])
assert len(test) == 1
assert test[0] == ('a',2)

test = countWords(['a','b'],[],['c'])
assert len(test) == 2
assert test[0] == ('a',1)
assert test[1] == ('b',1)

test = countWords(['a','a','b'],[],['c'])
assert len(test) == 2
assert test[0] == ('a',2)
assert test[1] == ('b',1)

test = countWords(['a'],['c'],['c'])
assert len(test) == 1
assert test[0] == ('a',1)

test = countWords(['a','a'],['c'],['c'])
assert len(test) == 1
assert test[0] == ('a',2)

test = countWords(['a','b'],['c'],['c'])
assert len(test) == 2
assert test[0] == ('a',1)
assert test[1] == ('b',1)

test = countWords(['a','a','b'],['c'],['c'])
assert len(test) == 2
assert test[0] == ('a',2)
assert test[1] == ('b',1)

test = countWords(['a','a','b'],[punctRm],[])
assert len(test) == 2
assert test[0] == ('a',2)
assert test[1] == ('b',1)

test = countWords(['hello','hello','world'],punctRm,excludeWordsList)
assert len(test) == 2
assert test[0] == ('hello',2)
assert test[1] == ('world',1)

test = countWords(['The quick brown fox','jumped over the lazy dog'],['!'],['remove me'])
assert len(test) == 8
assert test[0] == ('the',2)
assert test[1] == ('quick',1)
assert test[2] == ('brown',1)
assert test[3] == ('fox',1)
assert test[4] == ('jumped',1)
assert test[5] == ('over',1)
assert test[6] == ('lazy',1)
assert test[7] == ('dog',1)

# Test removal of punctuation

# Test removing strings made up of puncuation
punctRm = str.maketrans('', '', '!')
test = countWords(['!'], punctRm,excludeWordsList)
assert len(test) == 0

punctRm = str.maketrans('', '', '!')
test = countWords(['!!'], punctRm,excludeWordsList)
assert len(test) == 0

punctRm = str.maketrans('', '', '!?')
test = countWords(['?'], punctRm,excludeWordsList)
assert len(test) == 0

punctRm = str.maketrans('', '', '!?')
test = countWords(['!?'], punctRm,excludeWordsList)
assert len(test) == 0

punctRm = str.maketrans('', '', '!?')
test = countWords(['?!'], punctRm,excludeWordsList)
assert len(test) == 0

punctRm = str.maketrans('', '', '!?@')
test = countWords(['?!','!!', '??', '@!?'], punctRm,excludeWordsList)
assert len(test) == 0

from wordOps import punctRm
test = countWords(['!@#%%!','??/\'!@#', '&^%$', '?!@#>!@$'], punctRm,excludeWordsList)
assert len(test) == 0

# Tests that countWords removes puncuation from strings

punctRm = str.maketrans('', '', '!')
test = countWords(['a!'], punctRm,[])
assert len(test) == 1
assert test[0] == ('a', 1)

punctRm = str.maketrans('', '', '!?')
test = countWords(['a!'], punctRm,[])
assert len(test) == 1
assert test[0] == ('a', 1)

punctRm = str.maketrans('', '', '!?')
test = countWords(['!a'], punctRm,[])
assert len(test) == 1
assert test[0] == ('a', 1)

punctRm = str.maketrans('', '', '!?')
test = countWords(['!a!'], punctRm,[])
assert len(test) == 1
assert test[0] == ('a', 1)

punctRm = str.maketrans('', '', '!?')
test = countWords(['a!?'], punctRm,[])
assert len(test) == 1
assert test[0] == ('a', 1)

punctRm = str.maketrans('', '', '!?')
test = countWords(['a?!'], punctRm,[])
assert len(test) == 1
assert test[0] == ('a', 1)

punctRm = str.maketrans('', '', '!?')
test = countWords(['a!?'], punctRm,[])
assert len(test) == 1
assert test[0] == ('a', 1)

punctRm = str.maketrans('', '', '!?@')
test = countWords(['a!?', 'b'], punctRm,[])
assert len(test) == 2
assert test[0] == ('a', 1)
assert test[1] == ('b', 1)

punctRm = str.maketrans('', '', '!?@')
test = countWords(['a!?', 'b?'], punctRm,[])
assert len(test) == 2
assert test[0] == ('a', 1)
assert test[1] == ('b', 1)

punctRm = str.maketrans('', '', '!?@')
test = countWords(['a!?', 'b?', '?a?'], punctRm,[])
assert len(test) == 2
assert test[0] == ('a', 2)
assert test[1] == ('b', 1)

print ('Done Testing')
