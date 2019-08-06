from PIL import Image

file1 = open("MyFile.txt","a")

art = Image.open('encrypted.png')
art = art.convert('RGB')
width, height = art.size

# Fix ranges to fit any picture
for row in range(0, height, 10):
    for col in range(0, width, 10):
        color = art.getpixel((col, row))
        (r, g, b) = color
        file1.write(str(chr(r))+str(chr(g))+str(chr(b)))
    file1.write("\n")

file1.close()