from PIL import Image

img = Image.open("assets/icon_click.png")
img.save("assets/icon_click.ico", format="ICO")
