# wyrde multi sample sharpening with model upscale

<img src="wyrde multi sample sharpening w model upscale.png" width="90%">

Takes an image from text prompt and
* samples it
* latent upscales
* resamples it
* repeats
* uses a 4x upscale model to increase the size again
* saves it at a total of x8 size

Basically a series of hi-res fixes then an model upscale

Moving noodles switches between model vae and vae loader.

## Example
1st Gen: 512x512
<img src="ComfyUI_00012_.png" width="33%" align="middle">

2nd Gen: 640x640
<img src="ComfyUI_00013_.png" width="33%" align="middle">

3rd Gen: 768x768
<img src="ComfyUI_00014_.png" width="33%" align="middle">

4tth Gen 1024x1024
<img src="latent upscale wf_00003_.png" width="33%" align="middle">

then image is model upscaled with lollypop x4 (not shown since 26mb image)

## Variations
Changing Schedulers and Samplers (not to mention models) can dramatically change results

* Changed scheduler to noromal
* steps to 12
<img src="latent upscale wf_00009_.png" width="33%" align="middle">

* Switched to regular VAE decode
<img src="std vaedecode latent upscale wf_00011_.png" width="33%" align="middle">

* Dreamshaper model
<img src="dreamshaper latent upscale wf_00013_.png" width="33%" align="middle">

## Resources

WAS nodes
* https://github.com/WASasquatch/was-node-suite-comfyui

Model
* https://civitai.com/models/8281/perfect-world

Uspcale
* Lollypop https://drive.google.com/u/1/uc?id=10h8YXKKOQ61ANnwLjjHqXJdn4SbBuUku&export=download

Embeds
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main

## Credit
Original workflow from davemane42
<img src="davemane2 ComfyUI_01275_.png" width="20%" align="middle">
* https://www.reddit.com/r/StableDiffusion/comments/124xv9v/paradise_and_stone/



<p align="right"><a href="..">[back]</a><a href="../../../.."> [home]</a></p>
