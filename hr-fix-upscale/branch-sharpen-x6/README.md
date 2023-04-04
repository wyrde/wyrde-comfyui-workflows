# wyrde branch sharpen HR-Fix model upscaling x4 (many images)

<img src="branching sharpen WF 2023-04-04 15_49_05-Mozilla Firefox.png" width="50%">

Takes an image from text prompt (or image) and
* samples it
* uses an upscale model on it
* reduces it again and sends to a pair of samplers
* they upscale and reduce
* then send results to another pair of samplers

Not quite a true double-pass sharpen, but the results are decent. Lots of variation.

Unhook noodles to reduce undesired images and paths. Move noodles to switch VAE and img2img.

## example
1st image
<img src="wyrde branch sharp_00033_.png" width=20%>

Images 2A and 2B
<img src="wyrde branch sharp_00035_.png" width=20%><img src="wyrde branch sharp_00037_.png" width=20%>

Images 3A - 3D
<img src="wyrde branch sharp_00039_.png" width=20%><img src="wyrde branch sharp_00041_.png" width=20%><img src="wyrde branch sharp_00043_.png" width=20%><img src="wyrde branch sharp_00045_.png" width=20%>

## resources

WAS nodes. https://github.com/WASasquatch/was-node-suite-comfyui

Model
* https://civitai.com/models/8281/perfect-world

Lora
* none this time, but can be added easily

Uspcale
* Lollypop https://drive.google.com/u/1/uc?id=10h8YXKKOQ61ANnwLjjHqXJdn4SbBuUku&export=download

Embeds
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main
* bad-artist: https://huggingface.co/nick-x-hacker/bad-artist