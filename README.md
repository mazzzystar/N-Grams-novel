N-Grams for novel generation.
=============================
This project is a tiny implementation of [slp4:N-grams](https://lagunita.stanford.edu/c4x/Engineering/CS-224N/asset/slp4.pdf).I wrote some chinese notes for that article:[N-Grams模型初探](http://ringo.pub/2017/08/05/n-gram/).

# About the project
There are 2 files in project. One is for English version of novel generation, the other is for Chinese. I merely use some basic
ways when constructing my *N-Grams* model. So for further research, you may need:
* a better trick of smoothing/discount like.
* use *back-off* method for high-dimension of N.
* validation set, test set. and use *perplexity* to measure your model.
* process *unknown words*.

# English novel generation
```bash
python ngram-en.py
```
## Generation sample
The pre-words we set is:
>There was an edge to this

The next 50 words generated from *Game of Thrones 01* based on **3-grams** is:
>There was an edge to this frozen desolation . what chance would a coward hides behind stone walls it cracked easily .
 we've taken close to a pier . moreo came scrambling across the tumblestone that they felt as wicked as arya could see all the padding made him feel to say farewell to make ned

# Chinese novel generation
```bash
pip install jieba
python ngram-cn.py
```
## Generation sample
The pre-words we set is:
>传出了一种

The next 200 words generated from *斗破苍穹* based on 3-grams is:
>传出了一种束缚，调皮的裸露了出来吧！
　　从始至终，曹颖眼瞳，熏儿的漂亮小脸终于是引起过不少实力强大的实力太强。”然而这些攻击，虽说有着不可伤及性命的对魂殿手中，放心去弄过。在众人那好奇与敬畏地盯了玄黄天涧，便是射向古元二人。此时就算你真是越来越炉火纯青，想必对方士气必定大跌，特别棒！”本来俏脸惨白地发出呼呼声响，黑影身形旋动，澎湃雄厚的身家，恐怕暗中也会留在九幽地冥蟒结成盟友。
　“老师全心缠出那家伙便行，其他的围观者们方才带着震碎空间的这些胭脂俗粉可比。他没想到这女人使用某种炼制傀儡
　　数以百计的天阶高级的火莲子变更换六阶魔核便已经令得他们深有同感的呢喃声突然在云层中降临而去。他老人家向老爷子问个好。等日后龙皇大人此次需要相当长的异样吸引力，自然能够看出眼前的