# wyrde's terribly complicated multi latent fixing and fiddling

Makes extensive use of [WAS nodes.](https://github.com/WASasquatch/was-node-suite-comfyui)
* Make sure WAS suit is installed to avoid a mess of red boxes.

<img src="wyrde multi random WAS lora x3 HRF x10 landscape x10 portrait x10 A.png" width="80%" align="middle"><img src="wyrde multi random WAS lora x3 HRF x10 landscape x10 portrait x10 B.png"  width="20%" align="middle">

## The goal of this workflow was three-fold
* generate a bunch of series of images which SD repeatedly samples.
  * they tend to improve slowly, but sometimes have wild changes
* Use a prompt with a high degree of randomness
* have the complete prompt be sharable with a resulting image
  * In comfyui, words in {curly braces | separated by | pipes are | used to | generate} random results. Due to the way comfyui functions, an image's workflow will contain only the items in the prompt which were evaluated for the image. Other random elements will be dropped.


## The workflow
* Generates a text prompt from several randomized lists
* the sections are concated together
* the prompt is sampled
* sampled again
* and again -- 10 times
* switches aspect ratio
* and does all that again.
* total output is 20 images



Includes a couple lora. There's also a places where moving noodles changes the generation.

## resources

Model
* https://civitai.com/models/4384/dreamshaper

Lora
* https://civitai.com/models/8858/maplestory2game-chibi-style-hn
* https://civitai.com/models/21670/astrobabes
* https://civitai.com/models/25803/battle-angels

Embeds
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main


<p align="right"><a href="..">[back]</a><a href="../../../.."> [home]</a></p>
