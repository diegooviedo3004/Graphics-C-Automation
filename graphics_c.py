from PIL import Image
 
im = Image.open(r"black_white.png")
px = im.load()
height,width = im.size

f = open("c.txt", "a")

for i in range(width):
    for j in range(height):
        value = px[i,j]
        value = int(value)
        if value == 0:
            f.write(f"circle({i},{j},1);\n")

f.close()