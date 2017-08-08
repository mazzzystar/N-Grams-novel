# coding:utf-8
"""
N-Grams for Shakespeare corpus.
"""
import random


def text_clean(text_file):
    """
    delimiter will be used for prediction.
    """
    all_text = ""
    with open(text_file, 'r') as f:
        for line in f:
            # For spilt convenience.
            line = line.replace(',', ' , ').replace('.', ' . ').replace('!', ' ! ')\
                .replace('?', ' ? ').replace('"', ' " ')
            # To lower.
            line = line.lower()
            all_text += line
    return all_text


def ngram(text, grams):
    """
    generate the n-gram vocabulary.
    """
    model = []
    text = text.split()
    count = 0
    for token in text[:len(text) - grams+1]:
        model.append(' '.join(text[count:count + grams]))
        count += 1
    return model


def count_gram(text_file, grams):
    """
    Count the frequency of n-grams and (n-1) grams,
    and use add-one smoothing to make it less sparse.
    """
    text = text_clean(text_file)
    model = ngram(text, grams)
    lower_model = ngram(text, grams-1)

    # n grams dict
    mdict = {}
    for item in model:
        if item not in mdict:
            mdict[item] = 0
        mdict[item] += 1

    # (n-1) grams dict
    lower_dict = {}
    for item in lower_model:
        if item not in lower_dict:
            lower_dict[item] = 0
        lower_dict[item] += 1

    # count all unique vocabulary
    text_dict = text.split()
    voca_set = set()
    for item in text_dict:
        voca_set.add(item)

    # Add-One Smoothing
    voca_prob_dict = {}
    for item in model:
        item_list = item.split()
        back_str = ' '.join(item_list[:-1])
        prob = float(mdict[item] + 1) / (lower_dict[back_str] + len(voca_set))
        voca_prob_dict[item] = prob

    return voca_prob_dict


def generate_word(voca_prob_dict, pre, grams, word_length):
    """
    :param pre: the pre sequence provided.
    :param grams:
    :param word_length:
    :return:
    """
    print "The pre is: " + pre + '\n'
    pre_list = pre.split()
    for i in xrange(word_length):
        str_len = len(pre_list)
        back_voca = ' '.join(pre_list[str_len-grams+1:])
        predict_voca_list = []
        for item in voca_prob_dict:
            item_list = item.split()
            back = ' '.join(item_list[:-1])
            if back_voca == back:
                predict_voca_list.append(item_list[-1])

        if len(predict_voca_list):
            next_word = random.choice(predict_voca_list)
            pre_list.append(next_word)
        else:
            break

    s = ' '.join(pre_list)
    print s


if __name__ == '__main__':
    print "********"
    print "Generate text with 'Game Of Thrones 01.txt'."
    print "grams = 3"
    print "word length = 50"
    f1 = "novel/GameOfThrones01.txt"
    grams = 3
    word_length = 50
    vab = count_gram(f1, grams)
    pre1 = "There was an edge to this"
    generate_word(vab, pre1, grams, word_length)
    print "********\n"

    print "Generate text with 'shakespeare.txt'."
    f2 = "novel/shakespeare.txt"
    print "grams = 4"
    print "word length = 100"
    grams = 4
    word_length = 100
    vab = count_gram(f2, grams)
    pre2 = "track them , and we"
    generate_word(vab, pre2, grams, word_length)
    print "********\n"




