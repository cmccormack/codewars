from __future__ import print_function


def spin_words(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word
                    for word in sentence.split()])



print(spin_words('this is a longer test Christopher'))
