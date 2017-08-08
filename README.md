N-Grams for novel generation.
=============================
This project is a tiny implementation of [slp4:N-grams](https://lagunita.stanford.edu/c4x/Engineering/CS-224N/asset/slp4.pdf).I wrote some chinese notes for that article:[N-Grams模型初探](http://ringo.pub/2017/08/05/n-gram/).

# About the project
There are 2 files in project: one is for English version of novel generation, the other is for Chinese. I used some simple
ways when constructing my *N-Grams* model, so for further research you may need:
* a better trick of smoothing/discount.
* use *back-off* method for high-dimension of N.
* validation set, test set. and use *perplexity* to measure your model.
* process *unknown words*.

# English novel generation
```bash
python ngram-en.py
```
## example
The pre-words we set is:
```
There was an edge to this
```

The next 50 words generated from *Game of Thrones 01* based on **3-grams** is:
```
There was an edge to this . if i have a name to make the seas rise and saw her first man
was more cunning than she had never known defeat . " i am a sworn sword , and a third of those creatures ,
whatever it takes . i have a name ? oh
```

# Chinese novel generation
```bash
pip install jieba
python ngram-cn.py
```
## Generation sample
The pre-words we set is:
```
不愧是家族中种子级别的人物
```

The next 200 words generated from *《斗破苍穹》* based on **3-grams** is:
```
不愧是家族中种子级别的人物，她似乎便是从未见过萧炎白白吃亏过，即便如今已经晋入五星斗皇，
那是一种凌驾这片天地之上的气息巨蟒逐渐消散，最后一卷被能量层所包裹的人影，萧炎也只得停下介绍，
对着身旁那身姿欣长，脸色淡漠地举步走出，平静的声音，缓缓传出，青色斗气急速凝聚成火球之状，
然后火球裂开一道缝隙，一颗足有半个拳头大小。
在萧炎等人，也是逐渐地出现一丝晨辉时，萧炎却是一笑，道：“我知道你的一些事，只不过令得他感到意外，
微微点了点头：“好了…”
在萧炎等人为逃出一劫而松气时，那紧闭的眼眸，猛然睁开！
在那众多惊骇目光中缓缓松开了手掌，切记，以你如今在加玛帝国，也顶多只能伤到二阶魔兽，想要击杀，
却是必须跟老夫老老实实的交代，也是逐渐地变得黯淡
```
