# wyrde's basic basics of comfy workflows

## Keyboard shortcuts

```
    Ctrl + A       = select all nodes
    Ctrl + M       = mute/unmute selected nodes
    Ctrl + C       = copy selected nodes
    Ctrl + V       = paste node buffer
    Ctrl + Enter   = Adds current workflow to queue
    Delete         = delete selected nodes
    Backspace      = delete selected nodes
    Space Bar      = drag viewing area (hold space bar and move mouse pointer)

```
Notes:
* Ctrl + X does nothing.
* muted nodes don't process and block everythintg behind them 
* Ctrl+C, Ctrl+V, Ctrl+X, work normally inside a text box/field
* The text areas are like a separate layer. Space and copy/paste functions act normal inside them and use comfyUI functions outside.
* [full list of shortcuts](https://github.com/comfyanonymous/ComfyUI#shortcuts)

## Organization
* ~~Add pythongosssss _Node Templates_ [from this repo](https://github.com/pythongosssss/ComfyUI-Custom-Scripts). Download the node-templates file and put it in `ComfyUI/web/extensions/`. (Don't copy paste the editor display, save the raw file.) This repo has some other super helpful extensions as well.~~ Templates are now in ComfyUI.
  * I still recommended _image-feed_ and workflow-svg from [the repo](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
* noodles (the wires) can be organized with _reroute_ nodes. It takes extra time, but it makes figuring out a workflow a few days later much easier. Much less someone else.
* _SaveImage_ can do sub folders. The format is `folder/imageprefix`.
* The _LoadImage_ node is (at this writing) too small. Drag the bottom down to show the image preview. Glory at the terrible sketch comfy made for an example!

## Filenames
**Prefix**
Output files can be customized with substitutions
```
%date:d-M-yy%
```
all the date variables:
```
    yy -> last 2 digit of year (23)
    yyyy -> full year format (2023)
    d -> day number
    M -> month number
    h -> hour
    m -> minute
    s -> second
```
* Put in a `/` to create a folder like `%date:d-M-yyyy%/ComfyUI`
* `%width%` and `%height%` are also supported.
* Various items from nodes can also be included. Right click on a node, click on `properties` and use the contents of the _Node name for S&R_ property and the name of the _data_field_.
  * Example of putting the checkpoint in the file name:
  * _Load Checkpoint_'s API name shown in _properties_ is `CheckpointLoaderSimple` <img src="filename01.png" width="20%" align="middle" style="vertical-align:middle;">
  * The _data_field_ is `ckpt_name`<img src="filename03.png" width="20%"  align="middle" style="vertical-align:middle;">
  * combine with a `.` between: `CheckpointLoaderSimple.ckpt_name`
  * wrap the whole thing with `%` at the ends: `%CheckpointLoaderSimple.ckpt_name%`
  * and put that in the *filename_prefix* of the _Save Image_ node
	<img src="filename02.png" width="20%" align="middle"  style="vertical-align:middle;">
* each substitution gets its own %marks. Example: `%date:yyyy-M-d%/%node.data%_%node2.data2%`

**Suffix**
* ComfyUI adds the suffix of an underscore, 5-digit number, underscore, and extension at the end of the file name automatically (`_NNNNN_.png`).

<sub>Thanks to _Davemane42_ for pointing this out!</sub>

## Custom Nodes & Extensions
If comfyUI doesn't have something you expect, there's probably a custom node for it.

* Custom Nodes are placed in the custom_node directory
* It's generally a good idea to put the author's name/handle as a directory/folder, then the node(s) inside it.
  * This can cause an warning when comfy loads the folder but it is harmless.
  * an alternative is to keep the folders outside of comfy, and copy over the particular files.
* some nodes come as "suites" which will include their own directory, drop the whole thing inside custom_nodes
  * if nodes come in a folder with an `__init__.py` file, the whole thing can be put in `custom_nodes` with no errors
    * well, there might still be errors (:

Extensions are bits of javascript that extend the UI or some functions of comfyUI beyond the scope of nodes.
* Extensions are placed in the `web\extensions` folder/directory.
* Make sure to follow the author's instructions. These can break things. Easy to fix by removing the files.

## Embeddings

Otherwise known as Textual Inversons, embeddings can help create specfiic results in an image. Place embeddings in the `embeddings` folder and use them in prompts with `embedding:<filename>`. The extension isn't required. Note the lack of space after the `:`. Embeddings don't have a GUI element or node because their placement in a prompt is important. An embedding is basically a "word" with special meaning.

### Negative Embeddings

While most embeddings are put in the prompt, negative ones are placed in a negative prompt to _avoid_ a result. They can be helpful in creating better compositions. Restults can vary by model and the weight of the embedding.

* https://civitai.com/models/4629/deep-negative-v1x
* https://civitai.com/models/7808/easynegative
* https://huggingface.co/nick-x-hacker/bad-artist
* https://huggingface.co/yesyeahvh/bad-hands-5/tree/main
* https://huggingface.co/datasets/Nerfgun3/bad_prompt/
* https://civitai.com/models/23178
* https://civitai.com/models/16993
* https://civitai.com/models/15287

## Tips and Philosophy

* ComfyUI has a philosophy of keep it simple. Don't try to create a "do it all" workflow, instead focus on a specific objective.
* use the _CheckpointLoaderSimple_ node to load checkpoints. It will auto pick the right settings depending on your GPU.

##
This directory conatains some basic workflows showing beginning principles. Think of them as badly organized tutorials.

Be sure to check out the [comfy examples](https://comfyanonymous.github.io/ComfyUI_examples/) and [FAQ](https://comfyanonymous.github.io/ComfyUI_examples/faq/)

* [Cleaner Noodles Starting Workflow](https://raw.githubusercontent.com/wyrde/wyrde-comfyui-workflows/main/others/wyrde%20cleaner%20comfy%20default.json) (save the file then load/drag into comfyUI)
* [WAS Starting Workflow](./was-nodes-start/)




<p align="right"><a href="../../..">[home]</a></p>
