from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
import os

if not os.path.exists('./Tickets'):
   os.makedirs('./Tickets')

# Shuffling it 4 times and making an appended list to satisfy our needs for 3 pages of 4 tickets each.
def shuffleArray(nums):
    shuffledOnce = nums.copy()
    random.shuffle(shuffledOnce)
    shuffledTwice = nums.copy()
    random.shuffle(shuffledTwice)
    shuffledThrice = nums.copy()
    random.shuffle(shuffledThrice)
    shuffledForce = nums.copy()
    random.shuffle(shuffledForce)
    return shuffledOnce + shuffledTwice + shuffledThrice + shuffledForce

NUMBER_OF_TICKETS = 50
myFont = ImageFont.truetype('font.ttf', 60)

# Coordinates of the first ticket where numbers need to be printed. 
# Note - my code will automatically fill the rest of the 3 tickets 
# based on locations on the first ticket of the image that has 4 tickets in one
drawDestQuarter = [
        (330,200),
        (335,325),
        (330,450),
        (500,200),
        (615,200),
        (745,200),
        (1170,180),
        (1170,280),
        (1170,375),
        (1170,475),
        (330,615),
        (330,730),
        (330,840),
        (750,590),
        (750,685),
        (750,790),
        (750,885),
        (905,610),
        (905,740),
        (905,860),
        (70,1010),
        (70,1110),
        (70,1200),
        (70,1300),
        (750,1030),
        (750,1150),
        (750,1275),
        (900,1050),
        (900,1150),
        (900,1275)
    ]

drawDestList = []

# I am writing these values as I have a A4 Sheet (2480 x 3508) split into 4 quaters for 4 tickets each page
for i in range(4):
    if i == 0:
        tempx = 0
        tempy = 0
    if i == 1:
        tempx = 1240
        tempy = 0
    if i == 2:
        tempx = 0
        tempy = 1754
    if i == 3:
        tempx = 1240
        tempy = 1754

    for j in range(30):
        x = tempx + drawDestQuarter[j][0]
        y = tempy + drawDestQuarter[j][1]
        drawDestList.append((x,y))

# Code to calculate how many iterations to run the loop for 
# to get the desired number of tickets
ITERATIONS = NUMBER_OF_TICKETS / 12
ITERATIONS += 1
ITERATIONS = int(ITERATIONS)

# Creating the initial array of 90 numbers
nums = []
for i in range(90):
    nums.append(i + 1)

for k in range(ITERATIONS):
    meganums = shuffleArray(nums)
    img = Image.open("sample.png")
    for i in range(360):
        if i < 120:
            j = i
        elif i < 240:
            j = i - 120
        elif i < 360:
            j = i - 240
        if i == 120:
            img.save("Tickets/image" + str(1 + (3 * k)) + ".png")
            img.close()
            img = Image.open("sample.png")
        if i == 240:
            img.save("Tickets/image" + str(2 + (3 * k)) + ".png")
            img.close()
            img = Image.open("sample.png")

        I1 = ImageDraw.Draw(img)
        I1.text(drawDestList[j], str(meganums[i]), font = myFont, align = "center", anchor="mm", fill = (0,0,0))

    img.save("Tickets/image" + str(3 + (3 * k)) + ".png")
    img.close()
