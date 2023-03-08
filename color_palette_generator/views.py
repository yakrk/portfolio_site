from django.shortcuts import render
import PIL
from PIL import Image
import numpy as np

def color_palette(request):
    hex_dict = {}
    if request.method=="POST":
        # Get file
        uploaded_file = request.FILES.get('image')
        if uploaded_file is not None:
            img= Image.open(uploaded_file)
            if img.mode != "RGB":
                img = img.convert("RGB")
            img_array = np.asarray(img)
            # get top 10 palettes
            color_palette = palette(img_array)[:10]
            for i, rgb_np in enumerate(color_palette):
                # get hex color code
                rgb_str = str(rgb_np)
                rgb_str_clean = rgb_str.replace("[","").replace("]","").replace("   "," ").replace("  "," ")
                r,g,b = rgb_str_clean.strip().split(" ")
                hex_color = rgb_to_hex(int(r), int(g), int(b))
                # get percentage
                percentage = round(get_percentage(img_array, hex_color),2)
                # create dict to pass to html
                hex_dict_per_index = {}
                hex_dict_per_index["hex"]= hex_color
                hex_dict_per_index["percentage"]= percentage
                hex_dict[i+1]=hex_dict_per_index
            context = {
                "hex":hex_dict,
            }
            return render(request, "color_palette_generator\color_palette_generator.html", context)
    return render(request, "color_palette_generator\color_palette_generator.html")


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def palette(img_array):
    palette, index = np.unique(asvoid(img_array).ravel(), return_inverse=True)
    palette = palette.view(img_array.dtype).reshape(-1, img_array.shape[-1])
    count = np.bincount(index)
    order = np.argsort(count)
    return palette[order[::-1]]

def asvoid(image_array):
    image_array = np.ascontiguousarray(image_array)
    return image_array.view(np.dtype((np.void, image_array.dtype.itemsize * image_array.shape[-1])))

def get_percentage(image_array, hex_color):
    # Convert the hex color value to an RGB tuple
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    # Count the number of pixels that match the desired hex color value
    color_count = np.count_nonzero(np.all(image_array == rgb_color, axis=2))
    # Calculate the percentage of the hex color used in the image
    total_pixels = image_array.shape[0] * image_array.shape[1]
    percentage = (color_count / total_pixels) * 100
    return percentage