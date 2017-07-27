tuples = [('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east'),
        ('direction', 'west'),
        ('verb', 'go'),
        ('verb', 'kill'),
        ('verb', 'eat'),
        ('stop', 'the'),
        ('stop', 'in'),
        ('stop', 'of'),
        ('noun', 'bear'),
        ('noun', 'princess'),
        ('number', 1234),
        ('number', 3),
        ('number', 91234),
        ('error', 'asdfadfasdf'),
        ('error', 'ias')]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return s.lower()

def scan(sentence):
    words = sentence.split()
    result = []

    for word in words:

        for tuple in tuples:
            if convert_number(word) == tuple[1]:
                result.append(tuple)

    return result
