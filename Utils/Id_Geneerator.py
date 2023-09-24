from random import randint, seed, choices, shuffle

#tuples represent the upper and lower bounds of ascii numbers for different character sets
symbols = {
    'symGroup1': (32, 47),
    'symGroup2': (58, 64),
    'symGroup3': (91, 96),
    'symGroup4': (123, 126)
}
letters = {
    'upperGroup': (65, 47),
    'lowerGroup': (97, 122)
}

@staticmethod
def generateId():
    seed(1)
    # generate id in 00000xxx format
    generatedId = generateNumbers(5)
    generatedId += generateLetters(3)
    return generatedId


@staticmethod
def generatePwd(pwdLen, numLetters, numNumbs, numSymbols):
    try:
        # generate a string for each number of characters concat them then return the shuffled version
        if numLetters + numNumbs + numSymbols > pwdLen:
            raise ValueError('The number of characters cannot be greater than the entire password length')
        pwd = generateRandomPassword(numLetters, numNumbs, numSymbols)
        return shuffleString(pwd)
    except Exception as err:
        print(err)


def generateLetters(numberChrs):
    generatedString = ''
    cases = ['upperGroup', 'lowerGroup']
    for letter in range(numberChrs):
        case = choices(cases)[0]
        selectedCase = letters[case]
        generatedString += chr(randint(selectedCase[0], selectedCase[1]))
    return generatedString


def generateNumbers(numberDigits):
    generatedString = ''

    for number in range(numberDigits):
        generatedString += str(randint(0, 9))
    return generatedString


def generateRandomPassword(numberLetters, numberNums, numberSymbols):
    randomString = ''
    cases = ['upperGroup', 'lowerGroup']

    for letter in range(numberLetters + 1):
        # will return the number range based on case
        case = choices(cases)[0]
        selectedCase = letters[case]
        randomString += chr(randint(selectedCase[0], selectedCase[1]))

    for number in range(numberNums + 1):
        randomString += str(randint(0, 9))

    symblGroups = ['symGroup1', 'symGroup2', 'symGroup3', 'symGroup4']
    for symbol in range(numberSymbols):
        group = choices(symblGroups)[0]
        selectedGroup = symbols[group]
        randomString += chr(randint(selectedGroup[0], selectedGroup[1]))

        return shuffleString(randomString)


def shuffleString(str):
    shuffledString = ''
    listOfChrs = [character for character in str]
    shuffle(listOfChrs)
    for char in listOfChrs:
        shuffledString += char
    return shuffledString