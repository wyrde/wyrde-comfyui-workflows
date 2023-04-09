# wyrde's terribly complicated multi latent fixing and fiddling

Makes extensive use of [WAS nodes.](https://github.com/WASasquatch/was-node-suite-comfyui)
* Install WAS suit and avoid a mess of red boxes.

<img src="workflow smaller.png" align="middle">

## The goal of this workflow was three-fold
* generate a bunch of series of images which SD repeatedly samples.
  * they tend to improve slowly, but sometimes have wild changes
  * it is interesting how the forground will be nearly identical but dramatic changes in the background
* Use a prompt with a high degree of randomness
  * figure, hair, ears, & clothing. More elements can be randomized with these as examples.
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

The big box at the end has spare nodes for easy copy pasting

Includes some lora. There's also a places where moving noodles changes the generation.

## Example Results
* Portrait Row

<img src="img/multi latent chain_00084_.png" width="10%"><img src="img/multi latent chain_00086_.png" width="10%"><img src="img/multi latent chain_00087_.png" width="10%"><img src="img/multi latent chain_00088_.png" width="10%"><img src="img/multi latent chain_00089_.png" width="10%"><img src="img/multi latent chain_00090_.png" width="10%"><img src="img/multi latent chain_00091_.png" width="10%"><img src="img/multi latent chain_00092_.png"  width="10%"><img src="img/multi latent chain_00093_.png" width="10%"><img src="img/multi latent chain_00094_.png" width="10%">

* Landscape Row

<img src="img/multi latent chain_00085_.png" width="9%"><img src="img/multi latent chain_00095_.png" width="9%"><img src="img/multi latent chain_00096_.png" width="9%"><img src="img/multi latent chain_00097_.png" width="9%"><img src="img/multi latent chain_00098_.png" width="9%">
<img src="img/multi latent chain_00099_.png" width="9%"><img src="img/multi latent chain_00100_.png" width="9%"><img src="img/multi latent chain_00101_.png"  width="9%"><img src="img/multi latent chain_00102_.png" width="9%"><img src="img/multi latent chain_00103_.png" width="9%">

<!-- <img src="" width="10%"> -->

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
