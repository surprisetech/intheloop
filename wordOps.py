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

def totalKarmaOfWords(wordList, submissions):
    """
    :param wordList: a list of str, the words to be examined
    :param submission: a list of submission objects, they contain the score to be tallied
    :return: A list containing pairs, the first object of the pair is the word, and the second
             is the total score for that word.
    """
    karmaList = list()
    for word in wordList:
        submissionsWithWord = list()
        for submission in submissions:
            if word in submission.selftext or submission.title:
                submissionsWithWord.append(submission)
        totalKarma = 0
        for submission in submissionsWithWord:
            totalKarma += submission.score
        karmaList.append((word, totalKarma))
    #print(karmaList)
    return karmaList


punctRm = str.maketrans('', '', string.punctuation + "“”’")
excludeWordsList = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on',
                    'at', 'to', 'from', 'by', 'we', 'of', 'as', 'do', 'up', 'if', 'i', 'you', 'are', 'they',
                    'it', 'our', 'be', 'is', 'in', 'my', 'with', 'have', 'has', 'no', 'how', 'was', 'very',
                    'this', 'he', 'that', 'it\'s', 'cunt', 'fuck', 'like', 'not', 'your', 'don\'t', 'she',
                    'his', 'her', 'just', 'when', 'so', 'got', 'get', 'what', 'why', 'who', 'how', 'would',
                    'should', 'could', 'some', 'can', 'you\'re', 'about', 'which', 'had', 'want', 'made']
