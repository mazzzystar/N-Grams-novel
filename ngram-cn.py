# coding:utf-8
"""
N-Grams for Chines corpus.
"""
import random
import operator
import jieba


def text_clean(text):
    all_text = ""
    voca_set = set()
    with open(text, 'r') as f:
        for line in f:
            words_list = jieba.lcut(line.lower())
            voca_set.update(words_list)
            line = "@".join(words_list)
            all_text += line
    return all_text, len(voca_set)


def ngram(text, grams):
    model = []
    text_list = text.split("@")
    count = 0
    for token in text_list[:len(text_list) - grams+1]:
        model.append('@'.join(text_list[count:count + grams]))
        count += 1
    return model


def count_gram(file, grams):
    text, voca_len = text_clean(file)

    model = ngram(text, grams)
    lower_model = ngram(text, grams-1)

    mdict = {}
    for item in model:
        if item not in mdict:
            mdict[item] = 0
        mdict[item] += 1

    lower_dict = {}
    for item in lower_model:
        if item not in lower_dict:
            lower_dict[item] = 0
        lower_dict[item] += 1

    # add one smooth
    voca_prob_dict = {}
    for item in model:
        item_list = item.split("@")
        back_words = "@".join(item_list[:-1])
        prob = float(mdict[item] + 1) / (lower_dict[back_words] + voca_len)
        voca_prob_dict[item] = prob

    return voca_prob_dict


def generate_word(voca_prob_dict, pre, grams, length):
    print "The pre is: " + pre + '\n'
    pre_list = jieba.lcut(pre)
    for i in xrange(length):
        str_len = len(pre_list)
        back_voca = ''.join(pre_list[str_len-grams+1:])
        predict_voca_dict = {}
        for item in voca_prob_dict:
            item_list = item.split("@")
            back = ''.join(item_list[:-1])
            if back_voca == back:
                predict_voca_dict[item_list[-1]] = voca_prob_dict[item]

        if len(predict_voca_dict):
            sorted_next_word = sorted(predict_voca_dict.items(), key=operator.itemgetter(1))
            if len(sorted_next_word) >= 3:
                next_word = random.choice(sorted_next_word[-3:])
            else:
                next_word = random.choice(sorted_next_word)
            pre_list.append(next_word[0])
        else:
            break

    s = ''.join(pre_list)
    print s


if __name__ == '__main__':
    f = "novel/dpcq.txt"
    grams = 4
    vab = count_gram(f, grams)
    pre = "不愧是家族中种子级别的人物"
    generate_word(vab, pre, grams, length=200)
