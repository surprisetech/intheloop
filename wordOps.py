

def countWords(textList, punctRm, excludeWordsList):
    """
    :param textList: a list of str, the text to count up
    :param punctRm: a str, all punctuation characters to remove
    :param excludeWordsList:
    :return: A list of str of counted words, sorted most common word to least common word.
    """
    wordCount = dict()
    for post in textList:
        punctLess = post.translate(punctRm)
        print(punctLess)
        words = map(lambda x: x.lower(), punctLess.split())
        for word in words:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1
    sortedWords = sorted([tuple(reversed(x)) for x in wordCount.items()], key=lambda x: x[0], reverse=True)
    sortedWords = [item for item in sortedWords if item[1] not in excludeWordsList]
    return sortedWords
