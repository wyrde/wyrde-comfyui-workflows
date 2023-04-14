# Token Random Values Example

Makes extensive use of [WAS nodes.](https://github.com/WASasquatch/was-node-suite-comfyui)
* Install WAS suit and avoid a mess of red boxes.

<img src="./token random values example.png" align="middle" width="90%">

Was tokens are used to inject random values into the positive prompt.


* In comfyui, words in {curly braces | separated by | pipes are | used to | generate} random results. Due to the way comfyui functions, an image's workflow will contain only the items in the prompt which were evaluated for the image. Other random elements will be dropped.
* Because of how the backend evaluates the text boxes, it doesn't know the contents of the tokens have changed when parsing the prompts. There's two ways to fix this:
  * put `{ | | }` in the prompt. It will evaluate the space each time and run the prompt, thus also evaluating tokens.
  * make a new multiline node→random line node→text concatenate (the random result and the prompt) → text parse tokens → text to conditioning
    * this is more complex, but preserves the text prompt in the image workflow.

<img src="some image" align="middle">

## some heading

stuff

This workflow
* more
* stuff
  * here

## another heading

## Versions

## Example Results

* images
<!-- <img src="" width="10%" align="middle"> -->

## resources

* [WAS nodes.](https://github.com/WASasquatch/was-node-suite-comfyui)

<!-- things people might want to duplicate results -->

Model
* https://civitai.com/models/4384/dreamshaper

Lora
* https://civitai.com/models/8858/maplestory2game-chibi-style-hn
* https://civitai.com/models/21670/astrobabes
* https://civitai.com/models/25803/battle-angels

Embeds
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main

Custom Nodes
* [WAS Suite](https://github.com/WASasquatch/was-node-suite-comfyui)


<!-- will likely forget to doublecheck this -->
<p align="right"><a href="..">[back]</a><a href="../../../.."> [home]</a></p>
