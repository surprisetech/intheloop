

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
