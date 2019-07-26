from PIL import Image, ImageDraw

pw_input = input("Enter a password: ")
pw_split = list(pw_input)
pw_numValues = []

for char in pw_split:
    pw_numValues.append(ord(char))

pw_color_vals = tuple(pw_numValues[x:x + 3]  
    for x in range(0, len(pw_numValues), 3))

print(pw_split)
print(pw_numValues)
print(pw_color_vals)

imageLength = int(100*len(pw_split)/3)
imageHeight = 500

im = Image.new('RGB', (imageLength, imageHeight), color = 'white')
im.save('output.png')
draw = ImageDraw.Draw(im)

if len(pw_numValues) % 3 == 0:
    for i in range(len(pw_color_vals)):
        draw.rectangle([(20*i, 0), (imageLength,imageHeight)], fill='rgb{}'.format(tuple(pw_color_vals[i])), outline=None, width=0)
else:
    pw_numValues = pw_numValues + pw_numValues + pw_numValues + pw_numValues + pw_numValues + pw_numValues
    pw_color_vals = tuple(pw_numValues[x:x + 3]  
    for x in range(0, len(pw_numValues), 3))

    for i in range(len(pw_color_vals)):
        draw.rectangle([(30*i, 0), (imageLength, imageHeight)], fill='rgb{}'.format(tuple(pw_color_vals[i])), outline=None, width=0)

im.save('output.png')