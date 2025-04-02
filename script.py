from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
import os

if not os.path.exists('./Tickets'):
   os.makedirs('./Tickets')

# Shuffling it twice and making an appended list to satisfy our needs for 3 pages of 4 tickets each.
def shuffleArray(nums):
    shuffledOnce = nums.copy()
    random.shuffle(shuffledOnce)
    shuffledTwice = nums.copy()
    random.shuffle(shuffledTwice)
    return shuffledOnce + shuffledTwice

NUMBER_OF_TICKETS = 20
myFont = ImageFont.truetype('font.ttf', 60)

# Coordinates of the first ticket where numbers need to be printed. 
# Note - my code will automatically fill the rest of the 3 tickets 
# based on locations on the first ticket of the image that has 4 tickets in one
drawDestQuarter = [
        (669,262),
        (847,358),
        (1039,247),
        (145,592),
        (345,705),
        (565,632),
        (849,829),
        (798,1016),
        (1048,958),
        (497,1346),
        (96,1602),
        (464,1598),
        (895,1290),
        (778,1431),
        (1054,1550)
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

    for j in range(15):
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
    for i in range(180):
        if i < 60:
            j = i
        elif i < 120:
            j = i - 60
        elif i < 180:
            j = i - 120
        if i == 60:
            img.save("Tickets/image" + str(1 + (3 * k)) + ".png")
            img.close()
            img = Image.open("sample.png")
        if i == 120:
            img.save("Tickets/image" + str(2 + (3 * k)) + ".png")
            img.close()
            img = Image.open("sample.png")

        I1 = ImageDraw.Draw(img)
        I1.text(drawDestList[j], str(meganums[i]), font = myFont, align = "center", anchor="mm", fill = (0,0,0))

    img.save("Tickets/image" + str(3 + (3 * k)) + ".png")
    img.close()