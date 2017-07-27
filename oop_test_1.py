import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
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

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
# print(WORDS)

snippets = list(PHRASES.keys())


snippet = snippets[2]
phrase = PHRASES[snippet]

print(f"The snippet is: {snippet}.")
print("-" * 20)

snippet_count = snippet.count("%%%")
print(f"snippet.count is: {snippet_count}.")

random_sample = random.sample(WORDS, snippet_count)
print(f"random.sample is: {random_sample}.")

class_names = [w.capitalize() for w in
    random_sample]

print(f"class_names is: {class_names}.")
print("-" * 20)

results = []
param_names = []

for i in range(0, snippet.count("@@@")):
    param_count = random.randint(1,3)
    param_names.append(', '.join(random.sample(WORDS, param_count)))

print(f"param_names is: {param_names}.")
print(f"param_names first is: {param_names[0]}.")
print("-" * 20)

for sentence in snippet, phrase:
    print(f"sentence is: {sentence}.")
    result = sentence[:]
    print(f"result is: {result}.")

print("-" * 20)
