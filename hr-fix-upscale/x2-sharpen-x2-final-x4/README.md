# wyrde HR-Fix model upscaling x2 x2 (x4 final)

Includes WAS nodes. https://github.com/WASasquatch/was-node-suite-comfyui

Takes an image from text prompt (or image) and
* samples it
* uses an upscale model to double the size
* hi-rez fixes the image through a sampler
* uses a 4x upscale model to increase the size again
* saves it at a total of x4 size

Includes a couple lora. There's also a coupple places where moving noodles changes the generation.

## resources
Lora
* https://civitai.com/models/17892/cat-lingerie
* https://civitai.com/models/16687/butterfly-wings

Model
* https://civitai.com/models/8281/perfect-world

Uspcale
* PSNR https://drive.google.com/drive/folders/1ldwajXL50uC7PCS63B4Wato6Dnk-svNL
* Lollypop https://drive.google.com/u/1/uc?id=10h8YXKKOQ61ANnwLjjHqXJdn4SbBuUku&export=download
