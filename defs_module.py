def string_cleaner(word):
    if not isinstance(word, str):
        return 'Введена не строка'
    word = word.lower()
    clean_word = ''
    for i in word:
        if 97 <= ord(i) <= 122:
            clean_word += i
    return clean_word


def nato_code_maker(word):
    if len(word) == 1:
        return NATO_DICT[word]
    return NATO_DICT[word[0]] + ' ' + nato_code_maker(word[1:])


NATO_DICT = {'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo', 'f': 'Foxtrot', 'g': 'Golf',
             'h': 'Hotel', 'i': 'India', 'j': 'Juliet', 'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o':
                 'Oscar', 'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango', 'u': 'Uniform',
             'v': 'Victor', 'w': 'Whiskey', 'x': 'Xray', 'y': 'Yankee', 'z': 'Zulu'}


