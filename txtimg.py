from PIL import Image
import math

def subs(pixel):
    # pixel is a array with r,g,b value
    for i,j in enumerate(pixel):
        if (j < 0):
            pixel[i] = 0
        elif (j > 256):
            pixel[i] = 256
    r = pixel[0]
    g = pixel[1]
    b = pixel[2] 
    avg =  (r+g+b) / 3
    return getChar(avg)

def getChar(color):
    chars = 'mndbso*._'
    index = round(color/(256/len(chars)))
    if index >= len(chars): index = len(chars)-1
    return chars[index]

def main(input_file, output_file, width, height):    
    with open(output_file,'w+') as f:
        t = "";
        img = Image.open(input_file)
        img = img.resize([int(width),int(height)])
        h = img.height
        w = img.width
        for i in range(h):
            for j in range(w):
                p = img.getpixel((j,i))
                print (subs(p),end='',file=f)
            print('',file=f)

if __name__ == '__main__':
    import sys
    args = sys.argv
    input_file = None
    output_file = None
    width = 0;
    height = 0;
    if '-i' in args:
        input_file = args[args.index('-i')+1]
    else:
        print('input file not specified. use -i to indicate input file')
    if '-o' in args:
        output_file = args[args.index('-o')+1]
    else:
        print('output file not specified. use -o to indicate output file')
    if '-s' in args:
        size = args[args.index('-s')+1]
        width = size.split('x')[0]
        height = size.split('x')[1]
    else:
        print('size of output file not specified. use -s to indicate size of output file and use "x" to separet width and height\n \t eg. 234x567 ')
    
    main(input_file, output_file, width, height)
