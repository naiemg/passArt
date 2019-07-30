from PIL import Image

file1 = open("MyFile.txt","a")

art = Image.open('output.png')
art = art.convert('RGB')

# Fix ranges to fit any picture
for row in range(0,1536,1):
    file1.write("\n")
    for col in range(0,30,1):
        color = art.getpixel((col*68.2666666667, row))
        (r, g, b) = color
        file1.write(str(chr(r))+str(chr(g))+str(chr(b)))

file1.close()