from PIL import Image

file1 = open("MyFile.txt","a")
filename = 'encrypted.png'
art = Image.open(filename)
art = art.convert('RGB')
width, height = art.size

# Fix ranges to fit any picture
for row in range(0, height, 10):
    for col in range(0, width, 10):
        color = art.getpixel((row+3, col+3))
        (r, g, b) = color
        file1.write(str(chr(r))+str(chr(g))+str(chr(b)))
    file1.write("\n")

#im.save(filename)
file1.close()