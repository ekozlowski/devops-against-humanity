black_list = [x.strip() for x in open('./black_list.txt', 'r', encoding="utf-8").readlines() if x.strip()]
white_list = [x.strip() for x in open('./white_list.txt', 'r', encoding="utf-8").readlines() if x.strip()]
import sys
import random

def make_random_statement():
    # First, choose a black card.
    black = random.choice(black_list)
    # Find out how many words it has with "_" in them, and choose a white-list answer,
    # replacing the underscores with the answer.
    words = black.split()
    white_cards = []
    new_string = []
    for w in words:
        if '_' in w:
            w = random.choice(white_list) + w.replace('_', '')  #<-- keep the punctuation.
        new_string.append(w)
    return ' '.join(new_string)

if __name__ == "__main__":
    print(make_random_statement())