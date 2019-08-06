from PIL import Image, ImageDraw
import random
import string

imageLength = 1000
imageHeight = 1000
filename = 'encrypted.png'

def createCanvas():
    im = Image.new('RGBA', (imageLength, imageHeight))
    im.save(filename)

def generateRandomPW(stringLength):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def encodePassword(pw_input, level):
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

    im = Image.open(filename)
    draw = ImageDraw.Draw(im)

    pw_numValues = pw_numValues *21
    pw_color_vals = tuple(pw_numValues[x:x + 3]
        for x in range(0, len(pw_numValues), 3))

    for i in range(len(pw_color_vals)):
        draw.rectangle([(10*i, level), (10*i+10,level+10)], fill='rgb{}'.format(tuple(pw_color_vals[i])), outline=None, width=0)

    im.save(filename)

pw_input = input("Enter a password: ")
createCanvas()

my_pw_position = random.randint(0,100)*10
positionDown = 0

while positionDown < imageHeight:
    if positionDown == my_pw_position:
        encodePassword(pw_input, my_pw_position)
    else:
        randomNumber = random.randint(len(pw_input),32)
        encodePassword(generateRandomPW(randomNumber), positionDown)
    positionDown += 10   # decrease this value to add more layers