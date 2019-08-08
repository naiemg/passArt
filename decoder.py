from PIL import Image

file1 = open("MyFile.txt","w", encoding="ascii")
filename = 'encrypted.png'
art = Image.open(filename)
art = art.convert('RGB')
width, height = art.size
first_code = 126
second_code = 55

# Fix ranges to fit any picture
for row in range(0, height, 10):
    for col in range(0, width, 10):
        color = art.getpixel((row+3, col+3))
        (r, g, b) = color
        file1.write(str(chr((r-first_code%second_code)))+str(chr((g-first_code%second_code)))+str(chr((b-first_code%second_code))))
    file1.write("\n")

file1.close()