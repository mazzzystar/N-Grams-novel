# coding:utf-8
"""
N-Grams for Chinese corpus.
"""
import random
import operator
import jieba

def text_clean(file):
    all_text, voca_set = "", set()
    with open(file, 'r') as f:
        for line in f:
            words = jieba.lcut(line.lower())
            voca_set.update(words)
            all_text += "@".join(words)
    return all_text, len(voca_set)

def ngram(text, grams):
    text_list = text.split("@")
    return ['@'.join(text_list[i:i+grams]) for i in range(len(text_list) - grams + 1)]

def count_gram(file, grams):
    text, voca_len = text_clean(file)
    model, lower_model = ngram(text, grams), ngram(text, grams - 1)

    mdict, lower_dict = {}, {}
    for item in model:
        mdict[item] = mdict.get(item, 0) + 1
    for item in lower_model:
        lower_dict[item] = lower_dict.get(item, 0) + 1

    voca_prob_dict = {}
    for item in model:
        back = "@".join(item.split("@")[:-1])
        prob = float(mdict[item] + 1) / (lower_dict[back] + voca_len)
        voca_prob_dict[item] = prob

    return voca_prob_dict

def generate_word(voca_prob_dict, pre, grams, length):
    print "The pre is: " + pre + '\n'
    pre_list = jieba.lcut(pre)
    for _ in range(length):
        back = ''.join(pre_list[-grams+1:])
        candidates = {item.split("@")[-1]: prob for item, prob in voca_prob_dict.items()
                      if ''.join(item.split("@")[:-1]) == back}
        if candidates:
            sorted_next = sorted(candidates.items(), key=operator.itemgetter(1))
            next_word = random.choice(sorted_next[-3:] if len(sorted_next) >= 3 else sorted_next)[0]
            pre_list.append(next_word)
        else:
            break
    print ''.join(pre_list)

if __name__ == '__main__':
    f, grams = "novel/dpcq.txt", 4
    pre = "不愧是家族中种子级别的人物"
    generate_word(count_gram(f, grams), pre, grams, length=200)
