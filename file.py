from PIL import Image

#   Turns ref image into an ascii art 
#   Max width (For fitting on command line) is 83

#   Prepares the image and data
#   REPLACE WITH LOCATION YOU KEEP THE PROGRAM VVVV
im = Image.open(r"C:\Users\Tobes\Desktop\Image downsize\ref.png")


w,h = im.size
px = im.load()
data = ([(sum(list(l))/3)/2.55 for l in list(im.getdata())])

data_grid = [[] for i in range(h)]
cur = 0

for i in range(h):
    for ii in range(w):
        data_grid[i].append(round(data[cur]))
        cur += 1

#   Converts the numbers to ASCII
for i in range(len(data_grid)):
    for ii in range(len(data_grid[i])):
        cur = data_grid[i][ii]
        if cur < 11 : data_grid[i][ii] = '  '
        elif cur < 22 : data_grid[i][ii] = '..'
        elif cur < 33 : data_grid[i][ii] = '::'
        elif cur < 44 : data_grid[i][ii] = '--'
        elif cur < 55 : data_grid[i][ii] = '=='
        elif cur < 66 : data_grid[i][ii] = '++'
        elif cur < 77 : data_grid[i][ii] = '**'
        elif cur < 88 : data_grid[i][ii] = '##'
        elif cur < 99 : data_grid[i][ii] = '%%'
        else : data_grid[i][ii] = '@@'

#   Prints the output
for i in data_grid:   print(''.join(map(str,i)))
