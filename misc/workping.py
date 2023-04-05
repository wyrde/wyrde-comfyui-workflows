import argparse
import os
from PIL import Image, PngImagePlugin

def make_workflow_png(image, workflow):
    if not os.path.exists(image):
        ValueError(f"Invalid image path `{image}`")
    if not os.path.exists(workflow):
        ValueError(f"Invalid workflow path `{workflow}`")
    path = os.path.dirname(image)
    filename = os.path.basename(image).rsplit('.', 1)[0]
    try:
        with open(workflow, "r") as file:
            data = file.read()
    except OSError as e:
        Exception("There was an error reading the workflow JSON:", e)
    image = Image.open(image)
    info = PngImagePlugin.PngInfo()
    info.add_text("workflow", data)
    new_path = os.path.join(path, filename+'.png')
    image.save(new_path, "PNG", pnginfo=info)
    return new_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add workflow metadata to a PNG image")
    parser.add_argument("--image", type=str, help="Path to the PNG image")
    parser.add_argument("--workflow", type=str, help="Path to the workflow JSON file")
    args = parser.parse_args()
    new_image_path = make_workflow_png(args.image, args.workflow)

    print(f"Workflow added to `{new_image_path}`")
