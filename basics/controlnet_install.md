When installing controlnet_preprocesors, make sure to run the install.py included in the distribution. It requires a number of files to run properly. If the install.py isn't run, the dreaded `ModuleNotFoundError` error appears!

```
(base) PS D:\sd\comfyui\portable> cd .\ComfyUI\custom_nodes\
(base) PS D:\sd\comfyui\portable\ComfyUI\custom_nodes> git clone https://github.com/Fannovel16/comfy_controlnet_preprocessors.git
Cloning into 'comfy_controlnet_preprocessors'...
remote: Enumerating objects: 841, done.
remote: Counting objects: 100% (69/69), done.
remote: Compressing objects: 100% (40/40), done.
Receiving objects:  97% (816/841)sed 39 (delta 29), pack-reused 772
Receiving objects: 100% (841/841), 607.29 KiB | 5.23 MiB/s, done.
Resolving deltas: 100% (327/327), done.
(base) PS D:\sd\comfyui\portable\ComfyUI\custom_nodes> cd ..\..
(base) PS D:\sd\comfyui\portable> .\run_nvidia_gpu.bat

D:\sd\comfyui\portable>.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --port 9199
Set vram state to: NORMAL_VRAM
Using xformers cross attention
Traceback (most recent call last):
  File "D:\sd\comfyui\portable\ComfyUI\nodes.py", line 1119, in load_custom_node
    module_spec.loader.exec_module(module)
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\__init__.py", line 1, in <module>
    from . import canny, hed, midas, mlsd, openpose, uniformer, leres, mp_pose_hand, color, binary, pidinet, mp_face_mesh
  File "D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\canny\__init__.py", line 1, in <module>
    import cv2
ModuleNotFoundError: No module named 'cv2'

Cannot import D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors module for custom nodes: No module named 'cv2'
WAS Node Suite Running At: D:\sd\comfyui\portable\ComfyUI\custom_nodes\was-node-suite-comfyui\WAS_Node_Suite.py
WAS Node Suite Running From: D:\sd\comfyui\portable\ComfyUI\custom_nodes\was-node-suite-comfyui
WAS Node Suite: Loaded
Adding extra search path checkpoints d:/sd/models
Adding extra search path vae d:/sd/vae
Adding extra search path loras d:/sd/Lora
Adding extra search path upscale_models d:\sd\upscale
Adding extra search path embeddings d:\sd\embeddings
Starting server

To see the GUI go to: http://127.0.0.1:9199
```

* cd into the controlnet folder
cd .\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\
* run install py
(base) PS D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors> ..\..\..\python_embeded\python.exe .\install.py
* wait a while
* leave to make some tea
* drink tea

```
(base) PS D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors> ..\..\..\python_embeded\python.exe .\install.py
Installing requirements...
Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cu117
Collecting opencv-contrib-python
  Using cached opencv_contrib_python-4.7.0.72-cp37-abi3-win_amd64.whl (44.9 MB)
Collecting opencv-python
  Using cached opencv_python-4.7.0.72-cp37-abi3-win_amd64.whl (38.2 MB)
Collecting timm==0.6.7
  Using cached timm-0.6.7-py3-none-any.whl (509 kB)
Requirement already satisfied: torchvision in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from -r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 4)) (0.15.1+cu118)
Requirement already satisfied: scipy in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from -r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 5)) (1.10.1)
Collecting matplotlib
  Using cached matplotlib-3.7.1-cp310-cp310-win_amd64.whl (7.6 MB)
Collecting scikit-image
  Using cached scikit_image-0.20.0-cp310-cp310-win_amd64.whl (23.7 MB)
Collecting prettytable==3.6.0
  Using cached prettytable-3.6.0-py3-none-any.whl (27 kB)
Collecting svglib
  Using cached svglib-1.5.1-py3-none-any.whl
Collecting reportlab
  Using cached reportlab-3.6.12-cp310-cp310-win_amd64.whl (2.3 MB)
Collecting addict
  Using cached addict-2.4.0-py3-none-any.whl (3.8 kB)
Collecting yapf
  Using cached yapf-0.32.0-py2.py3-none-any.whl (190 kB)
Collecting mediapipe==0.9.1.0
  Using cached mediapipe-0.9.1.0-cp310-cp310-win_amd64.whl (49.8 MB)
Requirement already satisfied: torch>=1.4 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from timm==0.6.7->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 3)) (2.0.0+cu118)
Requirement already satisfied: wcwidth in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from prettytable==3.6.0->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 8)) (0.2.6)
Requirement already satisfied: numpy in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from mediapipe==0.9.1.0->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 13)) (1.24.2)
Collecting flatbuffers>=2.0
  Using cached flatbuffers-23.3.3-py2.py3-none-any.whl (26 kB)
Collecting absl-py
  Using cached absl_py-1.4.0-py3-none-any.whl (126 kB)
Requirement already satisfied: protobuf<4,>=3.11 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from mediapipe==0.9.1.0->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 13)) (3.20.3)
Requirement already satisfied: attrs>=19.1.0 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from mediapipe==0.9.1.0->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 13)) (22.2.0)
Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from torchvision->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 4)) (9.4.0)
Requirement already satisfied: requests in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from torchvision->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 4)) (2.28.2)
Requirement already satisfied: filelock in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from torch>=1.4->timm==0.6.7->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 3)) (3.10.0)
Requirement already satisfied: jinja2 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from torch>=1.4->timm==0.6.7->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 3)) (3.1.2)
Requirement already satisfied: typing-extensions in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from torch>=1.4->timm==0.6.7->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 3)) (4.5.0)
Requirement already satisfied: networkx in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from torch>=1.4->timm==0.6.7->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 3)) (3.0)
Requirement already satisfied: sympy in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from torch>=1.4->timm==0.6.7->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 3)) (1.11.1)
Collecting fonttools>=4.22.0
  Using cached fonttools-4.39.3-py3-none-any.whl (1.0 MB)
Collecting contourpy>=1.0.1
  Using cached contourpy-1.0.7-cp310-cp310-win_amd64.whl (162 kB)
Requirement already satisfied: packaging>=20.0 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from matplotlib->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 6)) (23.0)
Collecting kiwisolver>=1.0.1
  Using cached kiwisolver-1.4.4-cp310-cp310-win_amd64.whl (55 kB)
Collecting pyparsing>=2.3.1
  Using cached pyparsing-3.0.9-py3-none-any.whl (98 kB)
Collecting cycler>=0.10
  Using cached cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting python-dateutil>=2.7
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting lazy_loader>=0.1
  Using cached lazy_loader-0.2-py3-none-any.whl (8.6 kB)
Collecting tifffile>=2019.7.26
  Downloading tifffile-2023.4.12-py3-none-any.whl (219 kB)
     -------------------------------------- 219.4/219.4 kB 1.9 MB/s eta 0:00:00
Collecting PyWavelets>=1.1.1
  Using cached PyWavelets-1.4.1-cp310-cp310-win_amd64.whl (4.2 MB)
Collecting imageio>=2.4.1
  Using cached imageio-2.27.0-py3-none-any.whl (3.4 MB)
Collecting lxml
  Using cached lxml-4.9.2-cp310-cp310-win_amd64.whl (3.8 MB)
Collecting cssselect2>=0.2.0
  Using cached cssselect2-0.7.0-py3-none-any.whl (15 kB)
Collecting tinycss2>=0.6.0
  Using cached tinycss2-1.2.1-py3-none-any.whl (21 kB)
Collecting webencodings
  Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Collecting six>=1.5
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: charset-normalizer<4,>=2 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from requests->torchvision->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 4)) (3.1.0)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from requests->torchvision->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 4)) (1.26.15)
Requirement already satisfied: idna<4,>=2.5 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from requests->torchvision->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 4)) (3.4)
Requirement already satisfied: certifi>=2017.4.17 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from requests->torchvision->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 4)) (2022.12.7)
Requirement already satisfied: MarkupSafe>=2.0 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from jinja2->torch>=1.4->timm==0.6.7->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 3)) (2.1.2)
Requirement already satisfied: mpmath>=0.19 in d:\sd\comfyui\portable\python_embeded\lib\site-packages (from sympy->torch>=1.4->timm==0.6.7->-r D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors/requirements.txt (line 3)) (1.3.0)
Installing collected packages: yapf, webencodings, flatbuffers, addict, tinycss2, tifffile, six, reportlab, PyWavelets, pyparsing, prettytable, opencv-python, opencv-contrib-python, lxml, lazy_loader, kiwisolver, imageio, fonttools, cycler, contourpy, absl-py, scikit-image, python-dateutil, cssselect2, svglib, matplotlib, timm, mediapipe
  Attempting uninstall: timm
    Found existing installation: timm 0.6.12
    Uninstalling timm-0.6.12:
      Successfully uninstalled timm-0.6.12
Successfully installed PyWavelets-1.4.1 absl-py-1.4.0 addict-2.4.0 contourpy-1.0.7 cssselect2-0.7.0 cycler-0.11.0 flatbuffers-23.3.3 fonttools-4.39.3 imageio-2.27.0 kiwisolver-1.4.4 lazy_loader-0.2 lxml-4.9.2 matplotlib-3.7.1 mediapipe-0.9.
[notice] A new release of pip is available: 23.0.1 -> 23.1
[notice] To update, run: D:\sd\comfyui\portable\python_embeded\python.exe -m pip install --upgrade pip
A matching Triton is not available, some optimizations will not be enabled.
Error caught was: No module named 'triton'
Set vram state to: NORMAL_VRAM
Download models...
Downloading: "https://huggingface.co/lllyasviel/ControlNet/resolve/main/annotator/ckpts/network-bsds500.pth" to D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\ckpts\network-bsds500.pth

100%|█████████████████████████████████████████████████████████████████████████████| 56.1M/56.1M [00:03<00:00, 16.2MB/s]
Downloading: "https://huggingface.co/lllyasviel/ControlNet/resolve/main/annotator/ckpts/dpt_hybrid-midas-501f0c75.pt" to D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\ckpts\dpt_hybrid-midas-501f0c75.pt

100%|███████████████████████████████████████████████████████████████████████████████| 470M/470M [00:53<00:00, 9.28MB/s]
Downloading: "https://huggingface.co/lllyasviel/ControlNet/resolve/main/annotator/ckpts/mlsd_large_512_fp32.pth" to D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\ckpts\mlsd_large_512_fp32.pth

100%|█████████████████████████████████████████████████████████████████████████████| 6.05M/6.05M [00:00<00:00, 12.3MB/s]
Downloading: "https://huggingface.co/lllyasviel/ControlNet/resolve/main/annotator/ckpts/body_pose_model.pth" to D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\ckpts\body_pose_model.pth

100%|███████████████████████████████████████████████████████████████████████████████| 200M/200M [00:17<00:00, 11.8MB/s]
Downloading: "https://huggingface.co/lllyasviel/ControlNet/resolve/main/annotator/ckpts/hand_pose_model.pth" to D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\ckpts\hand_pose_model.pth

100%|███████████████████████████████████████████████████████████████████████████████| 141M/141M [00:12<00:00, 11.9MB/s]
cuda
Downloading: "https://huggingface.co/lllyasviel/ControlNet/resolve/main/annotator/ckpts/upernet_global_small.pth" to D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\ckpts\upernet_global_small.pth

100%|███████████████████████████████████████████████████████████████████████████████| 197M/197M [00:20<00:00, 10.1MB/s]
Use Checkpoint: False
Checkpoint Number: [0, 0, 0, 0]
Use global window for all blocks in stage3
load checkpoint from local path: D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\ckpts\upernet_global_small.pth
Downloading: "https://cloudstor.aarnet.edu.au/plus/s/lTIJF4vrvHCAI31/download" to D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\ckpts\download

100%|███████████████████████████████████████████████████████████████████████████████| 506M/506M [00:19<00:00, 26.8MB/s]
Downloading: "https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/third-party-models/table5_pidinet.pth" to D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors\ckpts\pidinet\table5_pidinet.pth

100%|█████████████████████████████████████████████████████████████████████████████| 2.74M/2.74M [00:00<00:00, 7.36MB/s]
Done!
```

now move up a few dirs and run comfy

```
(base) PS D:\sd\comfyui\portable\ComfyUI\custom_nodes\comfy_controlnet_preprocessors> cd ..\..\..\..
(base) PS D:\sd\comfyui> cd .\portable\
(base) PS D:\sd\comfyui\portable> .\run_nvidia_gpu.bat

D:\sd\comfyui\portable>.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --port 9199
Set vram state to: NORMAL_VRAM
Using xformers cross attention
WAS Node Suite Running At: D:\sd\comfyui\portable\ComfyUI\custom_nodes\was-node-suite-comfyui\WAS_Node_Suite.py
WAS Node Suite Running From: D:\sd\comfyui\portable\ComfyUI\custom_nodes\was-node-suite-comfyui
WAS Node Suite: Loaded
Adding extra search path checkpoints d:/sd/models
Adding extra search path vae d:/sd/vae
Adding extra search path loras d:/sd/Lora
Adding extra search path upscale_models d:\sd\upscale
Adding extra search path embeddings d:\sd\embeddings
Starting server

To see the GUI go to: http://127.0.0.1:9199
```
