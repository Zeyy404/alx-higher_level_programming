#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        len_sentence = len(sentence)
        first_char = sentence[0]
        return len_sentence, first_char
    else:
        return 0, None
