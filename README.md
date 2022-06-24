# chat_nudity_filtration

This repository contains the comparison of different NSFW-detection models found on GitHub with respect to their performance and Python scripts for the detection (and optionally, extraction and removal) of nude pictures in social media chats.

---

## Content

1. List of models
2. Dataset
3. Performance comparison
4. Nudity detection in VK chats (In process)
5. Nudity detection in Telegram chats (In process)

---

## List of models

+ [NudeNet](NudeNet)
+ [NSFW-detection](NSFW-detection)
+ [tensorflow-open_nsfw](tensorflow-open_nsfw)
+ [nsfw_model](nsfw_model)
  * [Mobilenet v2 Model (v1.1): Keras 224x224 Image model](https://github.com/GantMan/nsfw_model/releases/tag/1.1.0)
  * [Mobilenet v2 Model (v1.0): Keras 224x224 Image model](https://s3.amazonaws.com/ir_public/nsfwjscdn/nsfw_mobilenet2.224x224.h5)
  * [Inception v3 Model (v1.0):  Keras 299x299 Image model](https://s3.amazonaws.com/nsfwdetector/nsfw.299x299.h5)

---

## Dataset

The models were tested on the set of pictures manually collected from the Internet, mainly from web-sites containing explicit content. Inspired by the list of classes described in [NudeNet)[NudeNet], this is the list of categories I searched for:

|Category name|Number of pictures|Description|
|--------|:------------------------------------:|-----------|
|Drawing, female anus| 20 | Drawings of naked females, anus exposed|
|Drawing, female buttocks| 20 | Drawings of naked females, buttocks exposede|
|Drawing, female breast| 20| Drawings of naked females, breast exposed|
|Drawing, female genitals| 20| Drawings of naked females, genitals exposed|
|Drawing, male genitals| 20 | Drawings of naked males, genitals exposed|
|Female anus| 20 | Naked females, anus exposed|
|Female buttocks| 20 | Naked females, buttocks exposed|
|Female breast| 20 | Naked females, breast exposed|
|Female genitals| 20 | Naked females, genitals exposed|
|Male anus| 20 | Naked males, anus exposed|
|Male genitals| 20 | Naked males, genitals exposed|
|Female, underwear| 20 | Females in underwear|
|Male, underwear| 20 | Males in underwear|
|Neutral pictures| 50 | Neutral pictures (memes, dressed people [full height and faces only], etc.)|

---

## Performance comparison

### Binary classifiers
The first three models are binary classifiers returning probabilities for a picture to be [NSFW and SFW](https://en.wikipedia.org/wiki/Not_safe_for_work), where $P(NSFW) + P(SFW) = 1$ for a given picture.

Of all the categories in the dataset, <mark>Neutral pictures</mark>, *Male, underwear*, and *Female, underwer*, referred to as $SAFE_a$ are those containing SFW pictures, so the logic used was as follows.

For the first three models, the answer a model returns is right if one of the following conditions if satisfied: 
- $P(NSFW) > t$ and $PIC \not\in {SAFE_a}$
- $P(SFW) < t$ and $PIC \in {SAFE_a}$
Where $t$ is a hyperparameter (for each model, it is optimized to maximize the accuracy).

### Multiclass classifiers
The last three models return probabilities for a picture to be classified as *hentai*, *pornography*, *drawing*, *sexy*, or *neutral* (for more info, see [the repository](nsfw_model)). I refer to these categories as follows:
- $P(unsafe) = P(hentai)+P(porn)$
- $P(safe) = P(drawing) + P(neutral)$
- $PIC \in {UNSAFE_b}$ means the picture doesn't belong to the Male, underwear and Female, underwear categoriese

For the last three models, the answer a model returns is right if one of the following conditions if satisfied: 
- $PIC \not\in {SAFE_b}$ and $P(unsafe) > P(safe)$
- $PIC \in SAFE_a$  and $P(sexy) > P(unsafe)$
- $PIC \in neutral$ and $P(safe) > P(unsafe)$

### Accuracy 
|Model name|Accuracy|Optimal t, if applicable|
|--------|:----------:|------------------------|
|NSFW-detection| 0.745 | 0.5|
|NudeNet| 0.829 | 0.5|
|tensorflow-open_nsfw|0.89|0.53|
|Keras, 224 $\times$ 224 v1.0| 0.916| -|
|Keras, 299 $\times$ 299 v1.0| 0.919 | - |
|Keras, 224 $\times$ 224 v1.1| 0.897 | - |

---
## Nudity detection in VK chats (In process)
---
## Nudity detection in Telegram chats (In process)
