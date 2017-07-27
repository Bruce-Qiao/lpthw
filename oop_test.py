import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {                        # %%% are class names; @@@ represent params names; *** represents other names.
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
        }

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
# print(WORDS)

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in # capitalize each list item
                    random.sample(WORDS, snippet.count("%%%"))] # random.sample take {snippet.count("%%%")}'s items from WORDS list to build a new list.
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        print(f"sentence is: {sentence}.")
        result = sentence[:]
        print(f"result0 is: {result}.")

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        print(f"result1 is: {result}.")

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        print(f"result2 is: {result}.")

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        print(f"result3 is: {result}.")

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys()) # take keys from PHRASES dict and transform it to a list
        random.shuffle(snippets)    # random shuffle snippets list

        for snippet in snippets:    # take snippet from snippets list one by one
            phrase = PHRASES[snippet]   # take value from PHRASES dict
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                answer, question = question, answer

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye!")
