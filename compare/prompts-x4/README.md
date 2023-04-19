# wyrde's 4-prompt comparision

Uses of [WAS](https://github.com/WASasquatch/was-node-suite-comfyui) and [omar](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92) nodes.
* Install the suits to avoid a mess of red boxes.

<img src="compare-prompt-diff-x4-v0.4.png" align="middle">

## Comparing Things

Stable Diffusion can be _weird_. Sometimes it helps to examine the weirdness with pretty pictures. This worfklow runs 4 different prompts with the same settings and outputs the image results.

Takes advantage of text boxes, concatenate, and cli output.

## xformers enabled
 | prompt A | prompt B | prompt C | prompt D
 |:----:|:----:|:----:|:----:|
 |`Is, This, Different, Than` | `Is; This; Different; Than` | `Is: This: Different: Than` | `Is. This. Different. Than` |
 | <img src="./img/compare-prompt-diff-x4_00009_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00010_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00011_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00012_.png"   align="middle">

## xformers disabled
 | prompt A | prompt B | prompt C | prompt D
 |:----:|:----:|:----:|:----:|
 |`Is, This, Different, Than` | `Is; This; Different; Than` | `Is: This: Different: Than` | `Is. This. Different. Than` |
 | <img src="./img/compare-prompt-diff-x4_00013_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00014_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00015_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00016_.png"   align="middle">

<details>
  <summary>$\color{pink}{To\ disable\ xformers}$</summary>
To disable xformers:
* windows portable standalone
  * add ` --disable-xformers` after `.\python_embeded\python.exe -s ComfyUI\main.py` in the file `run_nvidia_gpu.bat`
  * so it looks llke
  * `.\python_embeded\python.exe -s ComfyUI\main.py --disable-xformers`
* github clone
  * add ` --disable-xformers` to the start command.
  * `python .\main.py --disable-xformers`
</details>

<!-- <img src=""  align="middle"> -->

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
