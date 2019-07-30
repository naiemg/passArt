from PIL import Image

file1 = open("MyFile.txt","a")

art = Image.open('output.png')
art = art.convert('RGB')

# Fix ranges to fit any picture
for row in range(0,520,1):
    file1.write("\n")
    for col in range(0,16,1):
        color = art.getpixel((col*29.125, row))
        (r, g, b) = color
        file1.write(str(chr(r))+str(chr(g))+str(chr(b)))

file1.close()