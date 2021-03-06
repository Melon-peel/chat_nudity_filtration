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

Of all the categories in the dataset, **Neutral pictures**; **Male, underwear**; and **Female, underwear**, referred to as $SAFE$, are those containing SFW pictures, so the logic used was as follows.

For the first three models, the answer a model returns is right if one of the following conditions if satisfied: 
- $P(NSFW) > t$ and $PIC \not\in {SAFE}$
- $P(SFW) < t$ and $PIC \in {SAFE}$
Where $t$ is a hyperparameter (for each model, it is optimized to maximize the accuracy).

### Multiclass classifiers
#### Descriptive statistics
The last three models return probabilities for a picture to be classified as *hentai*, *pornography*, *drawing*, *sexy*, or *neutral* (for more info, see [the repository](nsfw_model)). 

For each model, I looked at the mean values and standard deviations of probabilities of each class we're interested in (*Sexy, Hentai, Porn*):

<table cellspacing="0" border="0">
	<colgroup span="8" width="85"></colgroup>
	<tr>
		<td height="17" align="left"><font face="Liberation Serif"><br></font></td>
		<td align="left"><font face="Liberation Serif"><br></font></td>
		<td colspan=2 align="center" valign=middle><b><font face="Liberation Serif">Model 4</font></b></td>
		<td colspan=2 align="center" valign=middle><b><font face="Liberation Serif">Model 5</font></b></td>
		<td colspan=2 align="center" valign=middle><b><font face="Liberation Serif">Model 6</font></b></td>
		</tr>
	<tr>
		<td height="17" align="left"><font face="Liberation Serif"><br></font></td>
		<td align="left"><font face="Liberation Serif"><br></font></td>
		<td align="left"><b><font face="Liberation Serif">Mean</font></b></td>
		<td align="left"><b><font face="Liberation Serif">Std</font></b></td>
		<td align="left"><b><font face="Liberation Serif">Mean</font></b></td>
		<td align="left"><b><font face="Liberation Serif">Std</font></b></td>
		<td align="left"><b><font face="Liberation Serif">Mean</font></b></td>
		<td align="left"><b><font face="Liberation Serif">Std</font></b></td>
	</tr>
	<tr>
		<td rowspan=4 height="68" align="center" valign=middle><b><font face="Liberation Serif">NSFW</font></b></td>
		<td align="left"><font face="Liberation Serif">Sexy</font></td>
		<td align="right" sdval="0.179" sdnum="1033;"><font face="Liberation Serif">0.179</font></td>
		<td align="right" sdval="0.277" sdnum="1033;"><font face="Liberation Serif">0.277</font></td>
		<td align="right" sdval="0.112" sdnum="1033;"><font face="Liberation Serif">0.112</font></td>
		<td align="right" sdval="0.225" sdnum="1033;"><font face="Liberation Serif">0.225</font></td>
		<td align="right" sdval="0.22" sdnum="1033;"><font face="Liberation Serif">0.22</font></td>
		<td align="right" sdval="0.307" sdnum="1033;"><font face="Liberation Serif">0.307</font></td>
	</tr>
	<tr>
		<td align="left"><font face="Liberation Serif">Porn</font></td>
		<td align="right" sdval="0.324" sdnum="1033;"><font face="Liberation Serif">0.324</font></td>
		<td align="right" sdval="0.371" sdnum="1033;"><font face="Liberation Serif">0.371</font></td>
		<td align="right" sdval="0.402" sdnum="1033;"><font face="Liberation Serif">0.402</font></td>
		<td align="right" sdval="0.424" sdnum="1033;"><font face="Liberation Serif">0.424</font></td>
		<td align="right" sdval="0.279" sdnum="1033;"><font face="Liberation Serif">0.279</font></td>
		<td align="right" sdval="0.336" sdnum="1033;"><font face="Liberation Serif">0.336</font></td>
	</tr>
	<tr>
		<td align="left"><font face="Liberation Serif">Hentai</font></td>
		<td align="right" sdval="0.419" sdnum="1033;"><font face="Liberation Serif">0.419</font></td>
		<td align="right" sdval="0.452" sdnum="1033;"><font face="Liberation Serif">0.452</font></td>
		<td align="right" sdval="0.422" sdnum="1033;"><font face="Liberation Serif">0.422</font></td>
		<td align="right" sdval="0.461" sdnum="1033;"><font face="Liberation Serif">0.461</font></td>
		<td align="right" sdval="0.389" sdnum="1033;"><font face="Liberation Serif">0.389</font></td>
		<td align="right" sdval="0.419" sdnum="1033;"><font face="Liberation Serif">0.419</font></td>
	</tr>
	<tr>
		<td align="left"><font face="Liberation Serif">Neutral</font></td>
		<td align="right" sdval="0.044" sdnum="1033;"><font face="Liberation Serif">0.044</font></td>
		<td align="right" sdval="0.149" sdnum="1033;"><font face="Liberation Serif">0.149</font></td>
		<td align="right" sdval="0.042" sdnum="1033;"><font face="Liberation Serif">0.042</font></td>
		<td align="right" sdval="0.155" sdnum="1033;"><font face="Liberation Serif">0.155</font></td>
		<td align="right" sdval="0.057" sdnum="1033;"><font face="Liberation Serif">0.057</font></td>
		<td align="right" sdval="0.129" sdnum="1033;"><font face="Liberation Serif">0.129</font></td>
	</tr>
	<tr>
		<td rowspan=4 height="68" align="center" valign=middle><b><font face="Liberation Serif">SFW</font></b></td>
		<td align="left"><font face="Liberation Serif">Sexy</font></td>
		<td align="right" sdval="0.343" sdnum="1033;"><font face="Liberation Serif">0.343</font></td>
		<td align="right" sdval="0.424" sdnum="1033;"><font face="Liberation Serif">0.424</font></td>
		<td align="right" sdval="0.286" sdnum="1033;"><font face="Liberation Serif">0.286</font></td>
		<td align="right" sdval="0.399" sdnum="1033;"><font face="Liberation Serif">0.399</font></td>
		<td align="right" sdval="0.302" sdnum="1033;"><font face="Liberation Serif">0.302</font></td>
		<td align="right" sdval="0.368" sdnum="1033;"><font face="Liberation Serif">0.368</font></td>
	</tr>
	<tr>
		<td align="left"><font face="Liberation Serif">Porn</font></td>
		<td align="right" sdval="0.092" sdnum="1033;"><font face="Liberation Serif">0.092</font></td>
		<td align="right" sdval="0.166" sdnum="1033;"><font face="Liberation Serif">0.166</font></td>
		<td align="right" sdval="0.099" sdnum="1033;"><font face="Liberation Serif">0.099</font></td>
		<td align="right" sdval="0.225" sdnum="1033;"><font face="Liberation Serif">0.225</font></td>
		<td align="right" sdval="0.075" sdnum="1033;"><font face="Liberation Serif">0.075</font></td>
		<td align="right" sdval="0.144" sdnum="1033;"><font face="Liberation Serif">0.144</font></td>
	</tr>
	<tr>
		<td align="left"><font face="Liberation Serif">Hentai</font></td>
		<td align="right" sdval="0.011" sdnum="1033;"><font face="Liberation Serif">0.011</font></td>
		<td align="right" sdval="0.028" sdnum="1033;"><font face="Liberation Serif">0.028</font></td>
		<td align="right" sdval="0.006" sdnum="1033;"><font face="Liberation Serif">0.006</font></td>
		<td align="right" sdval="0.013" sdnum="1033;"><font face="Liberation Serif">0.013</font></td>
		<td align="right" sdval="0.038" sdnum="1033;"><font face="Liberation Serif">0.038</font></td>
		<td align="right" sdval="0.05" sdnum="1033;"><font face="Liberation Serif">0.05</font></td>
	</tr>
	<tr>
		<td align="left"><font face="Liberation Serif">Neutral</font></td>
		<td align="right" sdval="0.508" sdnum="1033;"><font face="Liberation Serif">0.508</font></td>
		<td align="right" sdval="0.43" sdnum="1033;"><font face="Liberation Serif">0.43</font></td>
		<td align="right" sdval="0.566" sdnum="1033;"><font face="Liberation Serif">0.566</font></td>
		<td align="right" sdval="0.437" sdnum="1033;"><font face="Liberation Serif">0.437</font></td>
		<td align="right" sdval="0.521" sdnum="1033;"><font face="Liberation Serif">0.521</font></td>
		<td align="right" sdval="0.394" sdnum="1033;"><font face="Liberation Serif">0.394</font></td>
	</tr>
</table>
As for the NSFW category, I tested it on both drawings and human pictures, so the deviations are rather high. To fix that, I calculated the same statistics but with differentiation:

<table cellspacing="0" border="0">
	<colgroup span="8" width="85"></colgroup>
	<tr>
		<td height="17" align="left"><br></td>
		<td align="left"><br></td>
		<td colspan=2 align="center" valign=middle><b>Model 4</b></td>
		<td colspan=2 align="center" valign=middle><b>Model 5</b></td>
		<td colspan=2 align="center" valign=middle><b>Model 6</b></td>
		</tr>
	<tr>
		<td height="17" align="left"><br></td>
		<td align="left"><br></td>
		<td align="left"><b>Mean</b></td>
		<td align="left"><b>Std</b></td>
		<td align="left"><b>Mean</b></td>
		<td align="left"><b>Std</b></td>
		<td align="left"><b>Mean</b></td>
		<td align="left"><b>Std</b></td>
	</tr>
	<tr>
		<td rowspan=4 height="68" align="center" valign=middle><b>NSFW Humans</b></td>
		<td style="border-top: 1px solid #000000; border-left: 1px solid #000000" align="left">Sexy</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.328" sdnum="1033;">0.328</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.303" sdnum="1033;">0.303</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.205" sdnum="1033;">0.205</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.272" sdnum="1033;">0.272</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.386" sdnum="1033;">0.386</td>
		<td style="border-top: 1px solid #000000; border-right: 1px solid #000000" align="right" sdval="0.336" sdnum="1033;">0.336</td>
	</tr>
	<tr>
		<td style="border-left: 1px solid #000000" align="left">Porn</td>
		<td align="right" sdval="0.582" sdnum="1033;">0.582</td>
		<td align="right" sdval="0.326" sdnum="1033;">0.326</td>
		<td align="right" sdval="0.724" sdnum="1033;">0.724</td>
		<td align="right" sdval="0.318" sdnum="1033;">0.318</td>
		<td align="right" sdval="0.467" sdnum="1033;">0.467</td>
		<td style="border-right: 1px solid #000000" align="right" sdval="0.344" sdnum="1033;">0.344</td>
	</tr>
	<tr>
		<td style="border-left: 1px solid #000000" align="left">Hentai</td>
		<td align="right" sdval="0.032" sdnum="1033;">0.032</td>
		<td align="right" sdval="0.085" sdnum="1033;">0.085</td>
		<td align="right" sdval="0.016" sdnum="1033;">0.016</td>
		<td align="right" sdval="0.049" sdnum="1033;">0.049</td>
		<td align="right" sdval="0.03" sdnum="1033;">0.03</td>
		<td style="border-right: 1px solid #000000" align="right" sdval="0.021" sdnum="1033;">0.021</td>
	</tr>
	<tr>
		<td style="border-bottom: 1px solid #000000; border-left: 1px solid #000000" align="left">Neutral</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.055" sdnum="1033;">0.055</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.149" sdnum="1033;">0.149</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.056" sdnum="1033;">0.056</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.165" sdnum="1033;">0.165</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.069" sdnum="1033;">0.069</td>
		<td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000" align="right" sdval="0.132" sdnum="1033;">0.132</td>
	</tr>
	<tr>
		<td rowspan=4 height="68" align="center" valign=middle><b>NSFW Drawings</b></td>
		<td style="border-top: 1px solid #000000; border-left: 1px solid #000000" align="left">Sexy</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.0004" sdnum="1033;">0.0004</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.0012" sdnum="1033;">0.0012</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.0004" sdnum="1033;">0.0004</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.002" sdnum="1033;">0.002</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.02" sdnum="1033;">0.02</td>
		<td style="border-top: 1px solid #000000; border-right: 1px solid #000000" align="right" sdval="0.014" sdnum="1033;">0.014</td>
	</tr>
	<tr>
		<td style="border-left: 1px solid #000000" align="left">Porn</td>
		<td align="right" sdval="0.014" sdnum="1033;">0.014</td>
		<td align="right" sdval="0.022" sdnum="1033;">0.022</td>
		<td align="right" sdval="0.015" sdnum="1033;">0.015</td>
		<td align="right" sdval="0.015" sdnum="1033;">0.015</td>
		<td align="right" sdval="0.042" sdnum="1033;">0.042</td>
		<td style="border-right: 1px solid #000000" align="right" sdval="0.05" sdnum="1033;">0.05</td>
	</tr>
	<tr>
		<td style="border-left: 1px solid #000000" align="left">Hentai</td>
		<td align="right" sdval="0.88" sdnum="1033;">0.88</td>
		<td align="right" sdval="0.214" sdnum="1033;">0.214</td>
		<td align="right" sdval="0.909" sdnum="1033;">0.909</td>
		<td align="right" sdval="0.169" sdnum="1033;">0.169</td>
		<td align="right" sdval="0.819" sdnum="1033;">0.819</td>
		<td style="border-right: 1px solid #000000" align="right" sdval="0.215" sdnum="1033;">0.215</td>
	</tr>
	<tr>
		<td style="border-bottom: 1px solid #000000; border-left: 1px solid #000000" align="left">Neutral</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.0302" sdnum="1033;">0.0302</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.148" sdnum="1033;">0.148</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.026" sdnum="1033;">0.026</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.14" sdnum="1033;">0.14</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.042" sdnum="1033;">0.042</td>
		<td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000" align="right" sdval="0.125" sdnum="1033;">0.125</td>
	</tr>
	<tr>
		<td rowspan=4 height="68" align="center" valign=middle><b>SFW</b></td>
		<td style="border-top: 1px solid #000000; border-left: 1px solid #000000" align="left">Sexy</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.343" sdnum="1033;">0.343</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.424" sdnum="1033;">0.424</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.286" sdnum="1033;">0.286</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.399" sdnum="1033;">0.399</td>
		<td style="border-top: 1px solid #000000" align="right" sdval="0.302" sdnum="1033;">0.302</td>
		<td style="border-top: 1px solid #000000; border-right: 1px solid #000000" align="right" sdval="0.368" sdnum="1033;">0.368</td>
	</tr>
	<tr>
		<td style="border-left: 1px solid #000000" align="left">Porn</td>
		<td align="right" sdval="0.092" sdnum="1033;">0.092</td>
		<td align="right" sdval="0.166" sdnum="1033;">0.166</td>
		<td align="right" sdval="0.099" sdnum="1033;">0.099</td>
		<td align="right" sdval="0.225" sdnum="1033;">0.225</td>
		<td align="right" sdval="0.075" sdnum="1033;">0.075</td>
		<td style="border-right: 1px solid #000000" align="right" sdval="0.144" sdnum="1033;">0.144</td>
	</tr>
	<tr>
		<td style="border-left: 1px solid #000000" align="left">Hentai</td>
		<td align="right" sdval="0.011" sdnum="1033;">0.011</td>
		<td align="right" sdval="0.028" sdnum="1033;">0.028</td>
		<td align="right" sdval="0.006" sdnum="1033;">0.006</td>
		<td align="right" sdval="0.013" sdnum="1033;">0.013</td>
		<td align="right" sdval="0.038" sdnum="1033;">0.038</td>
		<td style="border-right: 1px solid #000000" align="right" sdval="0.05" sdnum="1033;">0.05</td>
	</tr>
	<tr>
		<td style="border-bottom: 1px solid #000000; border-left: 1px solid #000000" align="left">Neutral</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.507" sdnum="1033;">0.507</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.432" sdnum="1033;">0.432</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.567" sdnum="1033;">0.567</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.437" sdnum="1033;">0.437</td>
		<td style="border-bottom: 1px solid #000000" align="right" sdval="0.521" sdnum="1033;">0.521</td>
		<td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000" align="right" sdval="0.394" sdnum="1033;">0.394</td>
	</tr>
</table>
To give a brief overview:

- NSFW drawings receive distinctly high *Hentai* score
- Human pornography has a moderate to high *Porn* score across 3 models
- SFW pictures have higher *Neutral* scores on average


#### Optimal parameters
With this information in mind, I looked for optimal parameters for each model to maximize the accuracy. Specifically, I optimized *HentaiParam*, *PornParam*, and *NeutralParam*, so that a picture is considered NSFW if one of the following is satisfied:

- $P(Hentai) > HentaiParam$
- $P(Porn) > PornParam$
- $P(Neutral) < NeutralParam$

I compared the optimization with and without the last condition (for the $NeutralParam$), and it turned that it didn't make any improvements to the value of accuracy, thus it was discarded.


### Accuracy 

The accuracy scores are presented in the table below (with hyperparameters, if applicable):

|Model name|Accuracy|Optimal t|Optimal hentai_param| Optimal porn_param| 
|--------|:----------:|------------------------|-----|-----|
|NSFW-detection| 0.745 | 0.5|- | - | 
|NudeNet| 0.829 | 0.5|- | - | 
|tensorflow-open_nsfw|0.89|0.53|- | - | 
|Keras, 224 $\times$ 224 v1.0| 0.884| - | 0.02 | 0.08 |
|Keras, 299 $\times$ 299 v1.0| 0.913 | - |0.1 | 0.2 |
|Keras, 224 $\times$ 224 v1.1| 0.852 | - | 0.1 | 0.1 |

From that, the Keras model (299 $\times$ 299) was picked as demonstrating the best performance
To use the script, get the [model](https://s3.amazonaws.com/nsfwdetector/nsfw.299x299.h5), [main script](https://github.com/Melon-peel/chat_nudity_filtration/blob/main/filter_nudity.py) and [json of default params](https://github.com/Melon-peel/chat_nudity_filtration/blob/main/vars.json), and the [module](https://github.com/Melon-peel/chat_nudity_filtration/tree/main/nsfw_detector) for classification and model loading, which I took from [nsfw_model](nsfw_model) and turned off verbosity for model.predict (you can download the model from the initial repo and will be jut fine, but that might lead to visual problems with a progress bar).

All is assumed to be put in the same directory by default.
The use of the script is:

```sh
python filter_nudity.py --vars vars.json

# --vars: optional path to the vars.json file (will look in the current directory if not specified)
```

---
## Nudity detection in VK chats (In process)
---
## Nudity detection in Telegram chats (In process)
