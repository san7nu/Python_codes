## Create each of numbers(0-9) in 5*3 pixel image file

from PIL import Image, ImageColor

def fillpixel(RC,name):
    img = Image.new('RGB', (3, 5),(255,255,255))
    pixels = img.load()
    for r in range(1,6):
        for c in range(1,4):
            if c in RC[r-1]:
                continue
            pixels[c-1,r-1] = (0,0,0)
    img.save(name)
    return

num = []
num.append([[0],[2],[2],[2],[0]])
num.append([[1,2],[1,2],[1,2],[1,2],[1,2]])
num.append([[0],[1,2],[0],[2,3],[0]])
num.append([[0],[1,2],[1],[1,2],[0]])
num.append([[2],[2],[0],[1,2],[1,2]])
num.append([[0],[2,3],[0],[1,2],[0]])
num.append([[0],[2,3],[0],[2],[0]])
num.append([[0],[1,2],[1,2],[1,2],[1,2]])
num.append([[0],[2],[0],[2],[0]])
num.append([[0],[2],[0],[1,2],[0]])

for i in range(0,len(num)):
    fillpixel(num[i],str(i)+'.png')
