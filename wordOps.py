import string

def countWords(textList, punctRm, excludeWordsList):
    """
    :param textList: a list of str, the text to count up
    :param punctRm: a str, all punctuation characters to remove
    :param excludeWordsList:
    :return: A dict of str of counted words, sorted most common word to least common word.
    """
    wordCount = dict()
    for post in textList:
        punctLess = post.translate(punctRm)
        words = map(lambda x: x.lower(), punctLess.split())
        for word in words:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1
    sortedWords = [item for item in wordCount.items() if item[0] not in excludeWordsList]
    sortedWords = sorted([x for x in sortedWords], key=lambda x: x[1], reverse=True)

    return sortedWords

def totalKarmaOfWords(wordList, funct, subreddit):
    """
    :param wordList: a list of str, the words to be examined
    :param submission: a list of submission objects, they contain the score to be tallied
    :return: A list containing pairs, the first object of the pair is the word, and the second
             is the total score for that word.
    """
    karmaList = list()
    for word in wordList:
        totalKarma = 0
        for submission in funct(subreddit):
            post = (submission.selftext + " " + submission.title)
            if word[0] in post:
                totalKarma += submission.score
        karmaList.append((word[0], totalKarma))
    #print(karmaList)
    return karmaList

#Shows the users that have posted within the searched subreddit
def contributorsToSubreddit(funct, subreddit):
    submissions = funct(subreddit)
    contributors = filter(lambda x: x != None, [x.author for x in submissions])
    return contributors

#Compare words user posts in a subreddit to their other subreddits
#can this be added to the /u search?
def compareUserReddits(user, sr, category, funct, subreddit):
    submissions = funct(subreddit)
    posts = list()
    for i in submissions:
        if i.author.name == user:
            posts.append(i.selftext + " " + i.title)
    return posts[0]

punctRm = str.maketrans('', '', string.punctuation + "“”’")
excludeWordsList = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on',
                    'at', 'to', 'from', 'by', 'we', 'of', 'as', 'do', 'up', 'if', 'i', 'you', 'are', 'they',
                    'it', 'our', 'be', 'is', 'in', 'my', 'with', 'have', 'has', 'no', 'how', 'was', 'very',
                    'this', 'he', 'that', 'it\'s', 'him', 'like', 'not', 'your', 'don\'t', 'she',
                    'his', 'her', 'just', 'when', 'so', 'got', 'get', 'what', 'why', 'who', 'how', 'would',
                    'should', 'could', 'some', 'can', 'you\'re', 'about', 'which', 'had', 'want', 'made']
