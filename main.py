from PIL import Image, ImageDraw

slop = Image.open ("images.jpeg")
bw_slop = slop.convert("L")
bw_slop.save(bw_slop.jpeg)
