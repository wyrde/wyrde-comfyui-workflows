# wyrde img2img-hr-fix-sharpen-x2-x2
Uses WAS nodes. https://github.com/WASasquatch/was-node-suite-comfyui

Takes an image and
* resizes it to 512x768
* uses bicubic to scale it x2
* samples it for a hi-rez fix
* upscales with a model by x4 (now x8 original size) then scales it down again for a final result of 2048x3072

Values can be changes easily.