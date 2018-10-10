# def countWords(textList, punctRm, excludeWordsList):

from wordOps import countWords
from app import punctRm, excludeWordsList

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


print ('Done Testing')
