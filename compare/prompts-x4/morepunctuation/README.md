# wyrde's punctuation noise comparisons

Uses of [WAS](https://github.com/WASasquatch/was-node-suite-comfyui) and [omar](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92) nodes.
* Install the suits to avoid a mess of red boxes.

<img src="../compare-prompt-diff-x4-v0.4.png" align="middle">
<a href="./compare-prompt-diff-x4-v0.10punctuation.json">[compare-prompt-diff-x4-v0.10punctuation.json]</a>

## Comparing Things

Tests showing the noise caused by punctuation

Takes advantage of text boxes, concatenate, and cli output.

## Punctuation in Prompts


 | prompt A | prompt B | prompt C | prompt D
 |:----:|:----:|:----:|:----:|
 |`Is, This, Different, Than` | `Is; This; Different; Than` | `Is: This: Different: Than` | `Is. This. Different. Than` |
 | <img src="./img/compare-prompt-diff-x4_00105_.png">|<img src="./img/compare-prompt-diff-x4_00106_.png">|<img src="./img/compare-prompt-diff-x4_00107_.png">|<img src="./img/compare-prompt-diff-x4_00108_.png">
 | prompt A | prompt B | prompt C | prompt D
 | `,.;` | `,.;,.;` | `,.;,.;,.;,.;,.;,.;` | `,.;,.;,.;,.;,.;,.;,.;,.;,.;,.;` |
 |<img src="./img/compare-prompt-diff-x4_00004_.png">|<img src="./img/compare-prompt-diff-x4_00003_.png">|<img src="./img/compare-prompt-diff-x4_00002_.png">|<img src="./img/compare-prompt-diff-x4_00001_.png"> 
 |<img src="./img/compare-prompt-diff-x4_00109_.png">|<img src="./img/compare-prompt-diff-x4_00110_.png">|<img src="./img/compare-prompt-diff-x4_00111_.png">|<img src="./img/compare-prompt-diff-x4_00112_.png"> 
 | prompt A | prompt B | prompt C | prompt D
 | ` ` | `,,,,,,` | `......` | `;;;;;;` |
 |<img src="./img/compare-prompt-diff-x4_00101_.png">|<img src="./img/compare-prompt-diff-x4_00102_.png">|<img src="./img/compare-prompt-diff-x4_00103_.png">|<img src="./img/compare-prompt-diff-x4_00104_.png"> 
 |<img width=288px>|<img width=288px>|<img width=288px>|<img width=288px>|
 | ` ` | `Is, This, Different, Than` | `,.;,.;,.;,.;,.;,.;,.;,.;,.;,.;` | `,,,,,,` |
 |<img src="./img/compare-prompt-diff-x4_00113_.png">|<img src="./img/compare-prompt-diff-x4_00114_.png">|<img src="./img/compare-prompt-diff-x4_00115_.png">|<img src="./img/compare-prompt-diff-x4_00116_.png"> 
 | ` ` | `<o.o>` | `;o.o;` | `\|o.o\|` |
 |<img src="./img/compare-prompt-diff-x4_00120_.png">|<img src="./img/compare-prompt-diff-x4_00117_.png">|<img src="./img/compare-prompt-diff-x4_00118_.png">|<img src="./img/compare-prompt-diff-x4_00119_.png"> 
 | ` ` | `<o.o;` | `;o.o>` | `-o.o-` |
 |<img src="./img/compare-prompt-diff-x4_00121_.png">|<img src="./img/compare-prompt-diff-x4_00122_.png">|<img src="./img/compare-prompt-diff-x4_00123_.png">|<img src="./img/compare-prompt-diff-x4_00124_.png"> 
 | `\|O.O\|` | `OTL` | `¯\(°_o)/¯`| `:-)` |
 |<img src="./img/compare-prompt-diff-x4_00125_.png">|<img src="./img/compare-prompt-diff-x4_00126_.png">|<img src="./img/compare-prompt-diff-x4_00127_.png">|<img src="./img/compare-prompt-diff-x4_00128_.png">|
 | ` ` | `  ` | `   `| `    ` |
 |<img src="./img/compare-prompt-diff-x4_00129_.png">|<img src="./img/compare-prompt-diff-x4_00130_.png">|<img src="./img/compare-prompt-diff-x4_00131_.png">|<img src="./img/compare-prompt-diff-x4_00132_.png">|
 | `\|o,o\|` | `:o.o:` | `:-.-:`| `: : : :` |
 |<img src="./img/compare-prompt-diff-x4_00133_.png">|<img src="./img/compare-prompt-diff-x4_00134_.png">|<img src="./img/compare-prompt-diff-x4_00135_.png">|<img src="./img/compare-prompt-diff-x4_00136_.png">|
 | `\|o.o\|` | `\|o;o\|` | `\|o?o\|`| `\|o'o\|` |
 |<img src="./img/compare-prompt-diff-x4_00137_.png">|<img src="./img/compare-prompt-diff-x4_00138_.png">|<img src="./img/compare-prompt-diff-x4_00139_.png">|<img src="./img/compare-prompt-diff-x4_00140_.png">|
 | `\|o.o\|` | `:` | `::::`| `:::::::::` |
 |<img src="./img/compare-prompt-diff-x4_00144_.png">|<img src="./img/compare-prompt-diff-x4_00145_.png">|<img src="./img/compare-prompt-diff-x4_00146_.png">|<img src="./img/compare-prompt-diff-x4_00147_.png">|
 |`                           `|`                            `|`                            `|`                           `|


## resources

<!-- things people might want to duplicate results -->

Model
* animatrix https://civitai.com/models/21916/animatrix

Embedding
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main

Custom Nodes
* [WAS Suite](https://github.com/WASasquatch/was-node-suite-comfyui)
* [omar QoL suit](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92)

<!-- will likely forget to doublecheck this -->
<p align="right"><a href="..">[back]</a><a href="../../../../.."> [home]</a></p>
