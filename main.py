import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

df=pd.read_excel("participants.xlsx")

template_path = "certificate.png"
output_dir = "certificates"
os.makedirs(output_dir, exist_ok=True)

font_path = "arial.ttf"
font_size = 90
font_color = (0, 0, 0)

names=df["name"]
for name in names:
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    w = draw.textlength(name, font=font)
    x = (image.width - w) / 2
    y = 700 #This varies for different templates
    
    draw.text((x, y), name, fill=font_color, font=font)
    
    # Save personalized certificate
    output_path = os.path.join(output_dir, f"{name}.png")
    image.save(output_path)