from PIL import Image, ImageDraw
import random
import string

imageLength = 1000
imageHeight = 1000
filename = 'encrypted.png'
random_shift = random.randint(1, 254)
random_mod = random.randint(1, 100)

def createCanvas():
    im = Image.new('RGB', (imageLength, imageHeight))
    im.save(filename)

def generateRandomPW(stringLength):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def encodePassword(pw_input, level):    # hello
    #print("original: " + pw_input)
    pw_split = list(pw_input)           # ['h','e','l','l','o']
    pw_numValues = []

    for char in pw_split:
        pw_numValues.append(ord(char))  # [104, 101, 108, 108, 111]

    pw_numValues_encrypted = []
    for char in pw_split:               # [106, 103, 110, 110, 113]
        pw_numValues_encrypted.append(ord(char)+random_shift%random_mod)

    pw_encoded = ''
    for val in range(len(pw_numValues_encrypted)):
        pw_encoded += chr(pw_numValues_encrypted[val])
    #print("encoded: " + pw_encoded)

    im = Image.open(filename)
    draw = ImageDraw.Draw(im)

    pw_numValues_encrypted = pw_numValues_encrypted *21     # [106, 103, 110, 110, 113 ... ... ... ...]
    pw_color_vals = tuple(pw_numValues_encrypted[x:x + 3]   # [(106, 103, 110),(110, 113 ...) ... ... ...]
        for x in range(0, len(pw_numValues_encrypted), 3))

    for i in range(len(pw_color_vals)):
        draw.rectangle([(level, 10*i), (level+10, 10*i+10)], fill='rgb{}'.format(tuple(pw_color_vals[i])), outline='white', width=1)

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

print(random_shift)
print(random_mod)