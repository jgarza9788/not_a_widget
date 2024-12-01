# !/bin/env python

import os
from PIL import Image, ImageDraw, ImageFont
from Config import Config
from utils.bar import bar
from utils import drivedata as dd
from utils import system_usage as su

DIR = os.path.dirname(os.path.realpath(__file__))
print(DIR)

def create_image_with_text(text, font_path=None, font_size=12, image_size=[500, 500], bg_color=[255, 255, 255, 255], text_color=[0, 0, 0, 255], output_path="output_image.png"):
    # Create a blank image
    image = Image.new("RGBA", tuple(image_size), tuple(bg_color))
    
    # Initialize drawing context
    draw = ImageDraw.Draw(image)
    
    # Load a font (use default font if no path is provided)
    font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()
    
    # # Calculate text size and position
    # text_width, text_height = font.getbbox(text)[2], font.getbbox(text)[3]
    # position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)

    # Define position for the upper-left corner
    position = (0, 0)  # Top-left corner of the image

    # Add text to the image
    draw.text(position, text, fill=tuple(text_color), font=font)
    
    # Save the image
    image.save(os.path.join(DIR,output_path))
    print(f"Image saved as {output_path}")




def main(theme='dark'):
    global DIR
    configData = Config().data[theme]

    font_path = None
    if configData["font_path"] != None:
        font_path = os.path.join(DIR,configData["font_path"])

    text = ""
    p_cpu = su.get_cpu_usage()
    text += f" CPU: {p_cpu:.2f}%".ljust(10) + "\n"
    text += f"{bar(p_cpu,100,length=20,fillchar="#", emptychar=" ")}\n"
    text += ""*20 + "\n"

    p_mu = su.get_memory_usage()
    text += f" RAM: {p_mu:.2f}%".ljust(10) + "\n"
    text += f"{bar(p_mu,100,length=20,fillchar="#", emptychar=" ")}\n"
    text += ""*20 + "\n"

    p_gpu = su.get_gpu_usage()
    text += f"󰢮 GPU: {p_gpu:.2f}%".ljust(10) + "\n"
    text += f"{bar(p_gpu,100,length=20,fillchar="#", emptychar=" ")}\n"
    text += ""*20 + "\n"

    d_root = dd.get_drivedata('/')
    p_root = d_root['percent']*100
    text += f" /    : {p_root:.2f}%".ljust(10) + "\n"
    text += f"{d_root['used_gb']:.2f}GB / {d_root['total_gb']:.2f}GB".ljust(20) + "\n"
    text += f"{bar(p_root,100,length=20,fillchar="#", emptychar=" ")}\n"
    text += ""*20 + "\n"

    d_ssd = dd.get_drivedata('/media/jgarza/SSD')
    p_ssd = d_ssd['percent']*100
    text += f" SSD  : {p_ssd:.2f}%".ljust(10) + "\n"
    text += f"{d_ssd['used_gb']:.2f}GB / {d_ssd['total_gb']:.2f}GB".ljust(20) + "\n"
    text += f"{bar(p_ssd,100,length=20,fillchar="#", emptychar=" ")}\n"
    text += ""*20 + "\n"

    d_h00 = dd.get_drivedata('/media/jgarza/H00')
    p_h00 = d_h00['percent']*100
    text += f" H00  : {p_h00:.2f}%".ljust(10) + "\n"
    text += f"{d_h00['used_gb']:.2f}GB / {d_h00['total_gb']:.2f}GB".ljust(20) + "\n"
    text += f"{bar(p_h00,100,length=20,fillchar="#", emptychar=" ")}\n"
    text += ""*20 + "\n"


    # text += f" CPU: {p_cpu:.2f}% {bar(p_cpu,100,length=10)}\n"
    # # text += " "*20 + "\n"
    # p_mu = su.get_memory_usage()
    # text += f" RAM: {p_mu:.2f}% {bar(p_mu,100,length=10)}\n"
    # # text += " "*20 + "\n"
    # p_gpu = su.get_gpu_usage()
    # text += f"󰢮 GPU: {p_gpu:.2f}% {bar(p_gpu,100,length=10)}\n"
    # # text += " "*20 + "\n"
    # d_root = dd.get_drivedata('/')
    # p_root = d_root['percent']*100
    # text += f" /   {p_root:.2f}% {bar(p_root,100,length=10)}\n"
    # # text += " "*20 + "\n"
    # d_ssd = dd.get_drivedata('/media/jgarza/SSD')
    # p_ssd = d_ssd['percent']*100
    # text += f" SSD {p_ssd:.2f}% {bar(p_ssd,100,length=10)}\n"
    # # text += " "*20 + "\n"
    # d_h00 = dd.get_drivedata('/media/jgarza/H00')
    # P_h00 = d_h00['percent']*100
    # text += f" H00 {P_h00:.2f}% {bar(P_h00,100,length=10)}\n"
    

    create_image_with_text(
        text=text,
        font_path=font_path,  
        font_size=configData["font_size"],
        image_size=configData["image_size"],
        bg_color=configData["bg_color"],
        text_color=configData["text_color"],
        output_path=configData["output_path"],
    )


if __name__ == '__main__':

    # import time
    # for i in range(60):
    #     main()
    #     time.sleep(1)

    main()
    pass