# wyrde's basic WAS node workflow
This is a workflow utilizing several WAS nodes.

<img src="./wyrde was node basic.png" width="80%" align="middle">

## Switching nodes
The workflow uses noodles (the lines between nodes) to switch from img2img to txt2img and baked vae to loaded vae.
* To switch from img2img to txt2img, drag a noodle from the LATENT dot on the "_EmptyLatentImage_" node to the _redirect_ node in the blue box. (The old noodle is replaced.)
* Switch back by draging from the LATENT dot on the _VAEEncode_ box to the _redirect_ node.

<img src="wyrde was basic img2img switch.png" width="80%" align="middle">
<img src="wyrde was node basic move2.png" width="80%" align="middle">
<img src="wyrde was node basic move3.png" width="80%" align="middle">

Switching from baked VAE to loaded vae is similar. (Baked VAEs are included inside the model file.)
*  Drag a noodle from the VAE dot in the _VAELoader_ node to the purple _redirect_ node below.
* To change back, drag a noodle from the VAE dot in the _CheckpointLoaderSimple_ node to the purple _redirect_ node below.
<img src="./wyrde was basic vae switch.png" width="80%" align="middle">

## In stable diffusion, size does matter

When using img2img, images should be resized to better fit the model. Most models are designed for 512x512 _initial_ generations. 768x512 and 512x768 are also common.

Large images will also suck of VRAM and time during sampling for the first generation. Instead of creating a big image in stable diffusion, it is better to go through a process called Hi-Res Fixing. That's a subject for another time, but for this basic workflow, stick to smaller initial images. (This can easily be changed for experimenting.)

Back to img2img.
* Use the _Resize Image_ node. The node is initially configured to resize images to 512x768. It is best to crop/alter your image in another program so it it fits 1:1 or 1:2 ratio for easy scaling. (Nodes can be used to alter images, but that's a more advanced topic.) Doesn't matter if the ratio isn't perfect, the image is a guide. Closer the better though.
* The _node's_ "mode" can be changed from "resize" to "rescale" to easily reduce larger images as well. <img src="./wyrde was basic img resize.png" width="80%" align="middle">


## Prompts
The workflow includes some basic propmts. Prompts are split into 2 types, positive and negative. <img src="./wyrde was basic prompts.png" align="middle">
* Positive prompts are what what you hope to see in the result.
  - (Positive prompts are often referred to simply as _prompts_, but sometimes _prompts_ means both positive and negative prompts. Confusing? Welcome to Stable Diffusion!)
* Negative prompts are items the user hopes **don't** show up in the result.
* There are all sorts of guides on making good prompts.
  - Basically, a good prompt has a subject and conditionals.
  - Subject is the main thing desired in the result, such as `adorable cat girl wearing a striped bikini`
  - conditionals are further details about the subject or the _type_ of image desired. `detailed eyes, detailed hair, pastel hair,` give further detail about the subject.
  - `absurdres, vibrant, photograph, photographic photo, photogenic, rule of thirds, anime, illustration, medium shot, Azulejo, finely detailed, realistic, masterpiece, best quality, illustration, soft focus, HDR 8K, artstation, pixv, unreal engine 5, SFW, ` is a bunch of information about the type of image desired.
    + as an aside, _Azulejo_ is a Portuguese tile which adds an interesting style to images with many models.
  - Negative prompts are much shorter. Usually. Some real doozies exist out there, generally fighting specific things showing up in results. For the basics, `bad hands, NSFW, nude` does well. A couple of those can be removed for more risqué images. (:
    + Stable Diffusion is often a contrary beast and seems to fight tooth and nail against negativet prompting.

## Click on _Queue Prompt_
The most important pat is, of course, making the images. Click on _Queue Prompt_ to start the process. If ComfyUI doesn't like how nodes are noodles, a bright red error will appear.
If it does, various nodes will glow green as it goes through the process. Eventually a picture will appear way at the end.

## Extras
What's with the _Latent Upscale by Factor (WAS)_ and second _Image Resize_ at the end? They're there to make it easy to hook in HiRez fixes. Also, I felt like it. At the moment they're not doing much. Changing the _factors_ can easily increase the final image size, but it won't look great.

### The basic of Hi-Rez Fixing:
* Move the image saving nodes further to the right. _Shift click_ or _ctrl+drag_ to select multiple nodes.
* Move them a bit further. Maybe a litle more.
* Space bar can be used to pan, even when nodes are "grabbed".
* Holding down _shift_ will snap the selected nodes to the grid.
  - Grid size can be configured in the cog wheel on the main Queue Prompt box.
* Now click on empty space to _deselect_ the nodes.
* Return to the _KSampler (WAS)_ node
* If the _Latent Upscale_ node was left next to it, great! If not, move it back.
* Change the factor to 2.
* Now select the _KSampler_ node. Ctrl+C to copy it.
* Click empty space to the right of the _Latent Uspcale_ node. Ctrl+V to paste in the sampler.
  - change _denoise_ to around `0.400`. (The decimal is Very Important™)
  - for a very basic hi-rez fix, the other settings are okay.
* Connect the LATENT dot on the _Latent Upscale to the Latent_image dot on the new _KSampler_. Connect the other noodles from the various objects to the left of the original _KSampler_.
  - bonus points using more redirects to manage the noodles. Ctrl+C and V to copy paste redirects.
  - The redirect grab spot is a little buggy. Aim for the top half.
* Connect the LATENT dot on the new _KSampler_ to the samples dot on the _VAEDecode_ node (the old noodle vanishes if it wasn't disconnected earlier).
* Click Queue Prompt to "fix" the previous image. If comfyUI wasn't restarted at some point, it'll use the old data and start on the new _KSampler_. Otherwise it'll start over from the beginning.
* The resulting image is larger, will look a little different (it was sampled), and be of decent quality.


## resources

WAS nodes
* https://github.com/WASasquatch/was-node-suite-comfyui

Model
* https://civitai.com/models/8281/perfect-world

Info about VAE
* https://rentry.org/sdvae

Places to find models and other Stable Diffusion goodies
* https://civitai.com/
* https://huggingface.co/



<p align="right">  <a href="../../../..">[home]</a> <a href="..">[back]</a></p>
     
