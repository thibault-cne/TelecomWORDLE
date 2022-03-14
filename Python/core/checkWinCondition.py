#  Copyright (c) 2022/3/14.

# Import needed modules
from typing import Dict

# Import personal modules
from Python.core.countWordLetters import countWordLetters


def checkWinCondition(userWord: str, requiredWord: str, currentTry: int) -> Dict[str, bool]:
    wordData = countWordLetters(requiredWord)

    data = {
        'css': {},
        'winStatement': False
    }

    if currentTry <= 5 and requiredWord != userWord:
        data['statement'] = True
    else:
        data['statement'] = False

    if requiredWord == userWord:
        data['winStatement'] = True

    for i in range(0, len(userWord)):
        if userWord[i] in requiredWord:
            if userWord[i] == requiredWord[i]:
                data['css'][i] = "good-place"
            elif wordData[userWord[i]] > 0:
                data['css'][i] = "bad-place"
                wordData[userWord[i]] -= 1
            else:
                data['css'][i] = "not-found"
        else:
            data['css'][i] = "not-found"

    return data
