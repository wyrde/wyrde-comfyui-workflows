# wyrde's basic basics of comfy workflows

## Keyboard shortcuts

```
    Ctrl + A   = select all nodes
    Ctrl + M   = mute/unmute selected nodes
    Ctrl + C   = copy selected nodes
    Ctrl + V   = paste node buffer
    Delete     = delete selected nodes
    Backspace  = delete selected nodes
    Space Bar  = drag viewing area (hold space bar and move mouse pointer)

```
Notes:
* Ctrl + X does nothing.
* muted nodes don't process and block everythintg behind them 

## Organization
* Add pythongosssss _Node Templates_ [from this repo](https://github.com/pythongosssss/ComfyUI-Custom-Scripts). Download the node-templates file and put it in `ComfyUI/web/extensions/`. (Don't copy paste the editor display, save the raw file.) This repo has some other super helpful extensions as well.
  * Also recommended is _image-feed_ and workflow-svg
* noodles (the wires) can be organized with _reroute_ nodes. It takes extra time, but it makes figuring out a workflow a few days later much easier. Much less someone else.
* _SaveImage_ can do sub folders. The format is `folder/imageprefix`.
* The _LoadImage_ node is (at this writing) too small. Drag the bottom down to show the image preview. Glory at the terrible sketch comfy made for an example!

## Tips and Philosophy

* ComfyUI has a philosophy of keep it simple. Don't try to create a "do it all" workflow, instead focus on a specific objective.
* use the _CheckpointLoaderSimple_ node to load checkpoints. It will auto pick the right settings depending on your GPU.

##
This directory conatains some basic workflows showing beginning principles. Think of them as badly organized tutorials.

Be sure to check out the [comfy examples](https://comfyanonymous.github.io/ComfyUI_examples/) as well!

* [WAS Starting Workflow](./was-nodes-start/)




<p align="right"><a href="../../..">[home]</a></p>
