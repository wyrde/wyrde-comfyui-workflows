# Tiled Sampling Example

Uses blenderneko's [Tiled KSampler node](https://github.com/BlenderNeko/ComfyUI_TiledKSampler)

<!--
<img src="some image" align="middle">
-->

## Purpose

This workflow uses tiled sampling to sample large images in hirez fixes. The Tiled KSampler is similar to the Advanced KSampler node, so there's a couple imporant differences from the "standard" KSampler.
* denoise is handled through start and stop steps compared to total steps.
* using 30 steps, start at step 15 and end at step 30 (15 steps) is equivalent to 0.500 denoise.
* Tile Width and Height should be the maximum size the GPU can reasonably handle.
  * setting these values low can result in extra artiftacts and noise

## Versions

## Example Results

* images  
<img src="img/sampler-1A_00005_.png" width="20%" align="middle"><img src="img/sampler-1B_00005_.png" width="20%" align="middle">  
<img src="img/sampler-2A_00005_.png" width="20%" align="middle"><img src="img/sampler-2B_00005_.png" width="20%" align="middle"><img src="img/sampler-2C_00005_.png" width="20%" align="middle">  
<img src="img/sampler-3A_00005_.png" width="20%" align="middle"><img src="img/sampler-3B_00005_.png" width="20%" align="middle">

When tile size is too small:  
<img src="img/sampler-3A_00005b_.png" width="20%" align="middle">


<!-- <img src="img/" width="10%" align="middle"> -->

## resources

<!-- things people might want to duplicate results -->

Model
* https://civitai.com/models/21916/

Custom Nodes
* [blenderneko's [Tiled KSampler node](https://github.com/BlenderNeko/ComfyUI_TiledKSampler)


<!-- will likely forget to doublecheck this -->
<p align="right"><a href="..">[back]</a><a href="../../../.."> [home]</a></p>
