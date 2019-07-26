from PIL import Image, ImageDraw
import random
import string

def createCanvas():
    imageLength = int(100*len(pw_split)/3)
    imageHeight = 500

    im = Image.new('RGB', (imageLength, imageHeight), color = 'white')
    im.save('output.png')

def randomStringwithDigitsAndSymbols(stringLength=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def encodePassword (pw_input, level):
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

    im = Image.open("output.png")
    draw = ImageDraw.Draw(im)

    if len(pw_numValues) % 3 == 0:
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

# Will Clean up Later
encodePassword(pw_input, 0)
encodePassword(randomStringwithDigitsAndSymbols(), 40)
encodePassword(randomStringwithDigitsAndSymbols(), 80)
encodePassword(randomStringwithDigitsAndSymbols(), 120)
encodePassword(randomStringwithDigitsAndSymbols(), 160)
encodePassword(randomStringwithDigitsAndSymbols(), 200)
encodePassword(randomStringwithDigitsAndSymbols(), 240)
encodePassword(randomStringwithDigitsAndSymbols(), 280)
encodePassword(randomStringwithDigitsAndSymbols(), 320)
encodePassword(randomStringwithDigitsAndSymbols(), 360)
encodePassword(randomStringwithDigitsAndSymbols(), 400)
encodePassword(randomStringwithDigitsAndSymbols(), 440)
encodePassword(randomStringwithDigitsAndSymbols(), 480)