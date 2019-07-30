from PIL import Image, ImageDraw
import random
import string

def createCanvas(length):
    imageLength = int(100*length/3)
    imageHeight = 520
    im = Image.new('RGB', (imageLength, imageHeight), color = 'white')
    im.save('output.png')

def generateRandomPW(stringLength):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def encodePassword (pw_input, level):
    pw_split = list(pw_input)
    pw_numValues = []

    for char in pw_split:
        pw_numValues.append(ord(char))

    pw_color_vals = tuple(pw_numValues[x:x + 3]
        for x in range(0, len(pw_numValues), 3))

    # For debugging purposes/ delete later
    print(pw_split)
    print(pw_numValues)
    print(pw_color_vals)

    imageLength = int(100*len(pw_split))
    imageHeight = 520

    im = Image.open("output.png")
    draw = ImageDraw.Draw(im)

    if len(pw_numValues) % 3 == 0:
        pw_color_vals = pw_color_vals + pw_color_vals + pw_color_vals + pw_color_vals + pw_color_vals + pw_color_vals
        for i in range(len(pw_color_vals)):
            draw.rectangle([(30*i, level), (imageLength,imageHeight)], fill='rgb{}'.format(tuple(pw_color_vals[i])), outline=None, width=0)
    else:
        pw_numValues = pw_numValues + pw_numValues + pw_numValues + pw_numValues + pw_numValues + pw_numValues
        pw_color_vals = tuple(pw_numValues[x:x + 3]  
        for x in range(0, len(pw_numValues), 3))

        for i in range(len(pw_color_vals)):
            draw.rectangle([(30*i, level), (imageLength, imageHeight)], fill='rgb{}'.format(tuple(pw_color_vals[i])), outline=None, width=0)

    im.save('output.png')

pw_input = input("Enter a password: ")
pw_len = len(list(pw_input))
createCanvas(pw_len)

my_pw_position = random.randint(0,520)
positionDown = 0

while positionDown < 520:
    if positionDown == my_pw_position:
        encodePassword(pw_input, my_pw_position)
    else:
        randomNumber = random.randint(len(pw_input),32)
        encodePassword(generateRandomPW(randomNumber), positionDown)
    positionDown += 1   # decrease this value to add more layers