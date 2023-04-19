# wyrde's generic tile

Uses of [WAS](https://github.com/WASasquatch/was-node-suite-comfyui) and [omar](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92) nodes.
* Install the suits to avoid a mess of red boxes.

<img src="compare-prompt-diff-x4-v0.4.png" align="middle">

## Comparing Things

stuff

This workflow
* more
* stuff
  * here

## with xformers enabled
 | prompt A | prompt B | prompt C | prompt D
 |:----:|:----:|:----:|:----:|
 |Is, This, Different, Than | Is; This; Different; Than | Is: This: Different: Than | Is. This. Different. Than |
 | <img src="compare-prompt-diff-x4_00009_.png" width="10%" width="22%" align="middle">
 | <img src="compare-prompt-diff-x4_00010_.png" width="10%" width="22%" align="middle">
 | <img src="compare-prompt-diff-x4_00011_.png" width="10%" width="22%" align="middle">
 | <img src="compare-prompt-diff-x4_00012_.png" width="10%" width="22%" align="middle">

## xformers disabled
To disable xformers:

* windows portable standalone
  * add ` --disable-xformers` after `.\python_embeded\python.exe -s ComfyUI\main.py` in the file `run_nvidia_gpu.bat`
  * so it looks llke
  * `.\python_embeded\python.exe -s ComfyUI\main.py --disable-xformers`
* github clone
  * add ` --disable-xformers` to the start command.
  * `python .\main.py --disable-xformers`

 | prompt A | prompt B | prompt C | prompt D
 |:----:|:----:|:----:|:----:|
 |Is, This, Different, Than | Is; This; Different; Than | Is: This: Different: Than | Is. This. Different. Than |
 | <img src="compare-prompt-diff-x4_00013_.png" width="10%" width="22%" align="middle">
 | <img src="compare-prompt-diff-x4_00014_.png" width="10%" width="22%" align="middle">
 | <img src="compare-prompt-diff-x4_00015_.png" width="10%" width="22%" align="middle">
 | <img src="compare-prompt-diff-x4_00016_.png" width="10%" width="22%" align="middle">


<!-- <img src="" width="10%" align="middle"> -->

## resources

<!-- things people might want to duplicate results -->

Model
* https://civitai.com/models/4384/dreamshaper

* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main

Custom Nodes
* [WAS Suite](https://github.com/WASasquatch/was-node-suite-comfyui)
* [omar QoL suit](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92)

<!-- will likely forget to doublecheck this -->
<p align="right"><a href="..">[back]</a><a href="../../../.."> [home]</a></p>
