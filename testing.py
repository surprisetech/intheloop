import praw

class RedditConfig:
    id = '3iaAttC7v0D96Q'
    secret = 'Dm-EfQSVyl8skVenes3DH25QfkY'
    userAgent = 'userAgent'

reddit = praw.Reddit(client_id=RedditConfig.id,
                     client_secret=RedditConfig.secret,
                     user_agent=RedditConfig.userAgent)

posts = reddit.subreddit("tifu").hot(limit=100)

for p in posts:
    print(dir(p))
    break

allText = ""
for p in posts:
    allText += p.selftext

print(allText)

import string
punctRm = str.maketrans('', '', string.punctuation)

excludeWordsList = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on',
                    'at', 'to', 'from', 'by', 'we', 'of', 'as', 'do', 'up', 'if', 'i', 'you', 'are', 'they',
                    'it', 'our', 'be', 'is', 'in', 'my', 'with', 'have', 'has', 'no', 'how', 'was', 'very',
                    'this', 'he', 'that', 'it\'s', 'cunt', 'fuck', 'like', 'not', 'your', 'don\'t', 'she',
                    'his', 'her', 'just', 'when', 'so', 'got', 'get', 'what', 'why', 'who', 'how', 'would',
                    'should', 'could', 'some', 'can', 'you\'re', 'about', 'which', 'had', 'want', 'made']


print(excludeWordsList)

punctLess = allText.translate(punctRm)
print(punctLess)

wordCount = dict()
words = map(lambda x: x.lower(), punctLess.split())
for word in words:
    print(word)
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

for key, value in wordCount.items():
    print(key, ' ', value)

print(wordCount)

filtered = [item for item in wordCount.items() if item[0] not in excludeWordsList]
print(filtered)

sortedWords = sorted([x for x in filtered], key=lambda x: x[1], reverse=True)
print(sortedWords)

top10 = sortedWords[:10]
print(top10)

#%matplotlib inline

import numpy
import matplotlib.pyplot as plt

labels = [x[0] for x in top10]
values = [x[1] for x in top10]

print(labels)
print(values)

positions = [i+1 for i in range(0, len(top10))]
print(positions)

plt.bar(positions, values, tick_label=labels, bottom=50)
plt.show()
