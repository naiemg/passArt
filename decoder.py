from PIL import Image

file1 = open("MyFile.txt","w", encoding="ascii")
filename = 'encrypted.png'
art = Image.open(filename)
art = art.convert('RGB')
width, height = art.size

# First Scan
for row in range(0, height, 10):
    for col in range(0, width, 10):
        color = art.getpixel((row+0.55, col+0.55))
        (r, g, b) = color
        if r != 0 and b != 0:
            first_code = int(r)
            second_code = int(b)
            break

# Second Scan
for row in range(0, height, 10):
    for col in range(0, width, 10):
        color = art.getpixel((row+3, col+3))
        (r, g, b) = color
        file1.write(str(chr((r-first_code%second_code)))+str(chr((g-first_code%second_code)))+str(chr((b-first_code%second_code))))
    file1.write("\n")

file1.close()