import sys

im = [list('...##....#..........####...'),
      list('..#..#...#......####....###'),
      list('..#..#...#......#..#.......'),
      list('..##############...######..')]

HEIGHT = len(im)
WIDTH = len(im[0])

def floodFill(image, x, y, newChar, oldChar=None):
    if oldChar == None:
        oldChar = image[x][y]
    if oldChar == newChar or oldChar != image[x][y]:
        return

    image[x][y] = newChar

    if x + 1 < HEIGHT and image[x + 1][y] == oldChar:
        floodFill(image, x + 1, y, newChar, oldChar)
    if x - 1 > 0 and image[x - 1][y] == oldChar:
        floodFill(image, x - 1, y, newChar, oldChar)
    if y + 1 < WIDTH and image[x][y + 1] == oldChar:
        floodFill(image, x, y + 1, newChar, oldChar)
    if y - 1 > 0 and image[x][y - 1] == oldChar:
        floodFill(image, x, y - 1, newChar, oldChar)
    return

def printImage(image):
    for x in range(HEIGHT):
        for y in range(WIDTH):
            sys.stdout.write(image[x][y])
        sys.stdout.write('\n')
    sys.stdout.write('\n')

count = 0
printImage(im)
for x in range(HEIGHT):
    for y in range(WIDTH):
        if im[x][y] == '.':
            count += 1
            floodFill(im, x, y, 'o')
        else:
            continue
printImage(im)
print(f'The numbers of shapes is: {count}')
