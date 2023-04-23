# wyrde's prompt noise comparisons

Uses of [WAS](https://github.com/WASasquatch/was-node-suite-comfyui) and [omar](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92) nodes.
* Install the suits to avoid a mess of red boxes.

<img src="../compare-prompt-diff-x4-v0.4.png" align="middle">

## Comparing Things

Tests showing the noise caused by punctuation

Takes advantage of text boxes, concatenate, and cli output.

## Punctuation in Prompts


 | prompt A | prompt B | prompt C | prompt D
 |:----:|:----:|:----:|:----:|
 |`Is, This, Different, Than` | `Is; This; Different; Than` | `Is: This: Different: Than` | `Is. This. Different. Than` |
 | <img src="../img/compare-prompt-diff-x4_00009_.png">|<img src="../img/compare-prompt-diff-x4_00010_.png">|<img src="../img/compare-prompt-diff-x4_00011_.png">|<img src="../img/compare-prompt-diff-x4_00012_.png">
 | prompt A | prompt B | prompt C | prompt D
 | `,.;` | `,.;,.;` | `,.;,.;,.;,.;,.;,.;` | `,.;,.;,.;,.;,.;,.;,.;,.;,.;,.;` |
 |<img src="./img/compare-prompt-diff-x4_00004_.png">|<img src="./img/compare-prompt-diff-x4_00003_.png">|<img src="./img/compare-prompt-diff-x4_00002_.png">|<img src="./img/compare-prompt-diff-x4_00001_.png"> 
 | prompt A | prompt B | prompt C | prompt D
 | ` ` | `,,,,,,` | `......` | `;;;;;;` |
 |<img src="./img/compare-prompt-diff-x4_00101_.png">|<img src="./img/compare-prompt-diff-x4_00102_.png">|<img src="./img/compare-prompt-diff-x4_00103_.png">|<img src="./img/compare-prompt-diff-x4_00104_.png"> 
 |<img width=288px>|<img width=288px>|<img width=288px>|<img width=288px>|

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
<p align="right"><a href="..">[back]</a><a href="../../../.."> [home]</a></p>
