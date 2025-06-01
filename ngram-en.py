# coding:utf-8
import random
import operator

def text_clean(text_file):
    all_text = ""
    with open(text_file, 'r') as f:
        for line in f:
            line = line.replace(',', ' , ').replace('.', ' . ').replace('!', ' ! ')\
                .replace('?', ' ? ').replace('"', ' " ').lower()
            all_text += line
    return all_text

def ngram(text, grams):
    text = text.split()
    return [' '.join(text[i:i+grams]) for i in range(len(text) - grams + 1)]

def count_gram(text_file, grams):
    text = text_clean(text_file)
    model, lower_model = ngram(text, grams), ngram(text, grams - 1)

    mdict, lower_dict = {}, {}
    for item in model:
        mdict[item] = mdict.get(item, 0) + 1
    for item in lower_model:
        lower_dict[item] = lower_dict.get(item, 0) + 1

    voca_set = set(text.split())
    voca_prob_dict = {}
    for item in model:
        back = ' '.join(item.split()[:-1])
        prob = float(mdict[item] + 1) / (lower_dict[back] + len(voca_set))
        voca_prob_dict[item] = prob

    return voca_prob_dict

def generate_word(voca_prob_dict, pre, grams, word_length):
    print "The pre is: " + pre + '\n'
    pre_list = pre.split()
    for _ in range(word_length):
        back = ' '.join(pre_list[-grams+1:])
        candidates = {item.split()[-1]: prob for item, prob in voca_prob_dict.items()
                      if ' '.join(item.split()[:-1]) == back}
        if candidates:
            sorted_next = sorted(candidates.items(), key=operator.itemgetter(1))
            next_word = random.choice(sorted_next[-3:] if len(sorted_next) >= 3 else sorted_next)[0]
            pre_list.append(next_word)
        else:
            break
    print ' '.join(pre_list)

if __name__ == '__main__':
    print "********"
    print "Generate text with 'Game Of Thrones 01.txt'."
    f1, grams, word_length = "novel/GameOfThrones01.txt", 3, 50
    generate_word(count_gram(f1, grams), "There was an edge to this", grams, word_length)
    print "********\n"

    print "Generate text with 'shakespeare.txt'."
    f2, grams, word_length = "novel/shakespeare.txt", 4, 100
    generate_word(count_gram(f2, grams), "track them , and we", grams, word_length)
    print "********\n"
