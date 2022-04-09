from math import ceil
from PIL import Image
 
im = Image.open(r"black_white.png")
px = im.load()
height,width = im.size

f = open("files/c.C", "w")
f.write("#include <stdio.h>\n#include <conio.h>\n#include<graphics.h>\n")

contador = 0

# DETERMINANDO LA CANTIDAD DE ARCHIVOS NECESARIOS A IMPORTAR

try:
    for i in range(width):
        for j in range(height):
            value = px[i,j]
            value = int(value)
            if value == 0:
                contador = contador + 1

except IndexError:
    pass

archivos = ceil(contador/800)

for i in range(0,archivos,1):
    f.write(f'#include "C:/TurboC3/BIN/files/c{i}.C"\n')

f.write('\nvoid main(){\nint gd=DETECT, gm;\ninitgraph(&gd, &gm,"C:\\TURBOC3\\bgi");\n')

for i in range(0,archivos,1):
    f.write(f"draw{i}();\n")

f.write("\ngetch();\n}")
f.close()

#CREANDO FUNCIONES
for i in range(0,archivos,1):
    f = open(f"files/c{i}.C", "w")
    f.write(f"#include <stdio.h>\n#include <conio.h>\n#include <graphics.h>\nvoid draw{i}()")
    f.write('{\n')
    f.close()

#LLENANDO ESOS ARCHIVOS
contador = 0
files = 0
try:
    for i in range(width):
        for j in range(height):
            value = px[i,j]
            value = int(value)
            if value == 0:
                if contador == 0:
                    f = open(f"files/c{files}.C","a")
                if contador % 800 == 0:
                    f.close()
                    f = open(f"files/c{files}.C","a")
                    files = files+1
                f.write(f"circle({i},{j},1);\n")
                contador = contador + 1

except IndexError:
    pass

f.close()

# AGREGANDO GETCH
for i in range(0,archivos,1):
    f = open(f"files/c{i}.C", "a")
    f.write("\ngetch();\n}")
    f.close()

