from PIL import Image
img = Image.open('demo_image.jpg').convert('L')
img.resize((750,450))
img.save('greyscale.png')
