import os,os.path
from PIL import Image
from pathlib import Path
import sys
def Image_Modifier(Dir):
    for name in os.listdir(Dir):
        print(name)
        code = Name_Checking(name)
        
        if(code==""):
            continue
        
        image = Image.open(Dir+'\\'+name,'r')
        image = Resize_Image(Square_Image(Remove_Transparence(image)))
        final = image.convert('RGB')
        DestPath = "C:\\Users\\Hao\\Desktop\\processed"
        file = DestPath + "\\" +code + ".jpg"
        num = 0
        while(Path(file).exists()):
            num = num + 1
            file = DestPath + "\\" + code + "_" + (str)(num) + ".jpg"
        
        final.save(file,optimize=True)

        image.close()
        final.close()

def Name_Checking(name):
    a= name.split("-")
    name = a[0]
    if(name.isdigit()):
        return name
    else:
        final = ""
        m = 0
        temp = ""
        l = 0
        for letter in name:
            if(letter.isdigit()):
                temp = temp+letter
                l = l+1
            else:
                if(l>m):
                    m = l   
                    final = temp
                temp = ""
                l = 0
        if(l>m):
            final = temp
        return final

            
    



def Remove_Transparence(image):
    layer = Image.new('RGBA', image.size, (255, 255, 255, 255))
    final = Image.alpha_composite(layer, image.convert('RGBA'))
    layer.close()
    image.close()
    return final

def Square_Image(image):
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    if(width != height):
        bigside = width if width > height else height
        background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))
        background.paste(image, offset)
        image.close()
        return background
    else:
        return image

def Resize_Image(image):
    image = image.resize((500, 500),Image.ANTIALIAS)
    return image

Image_Modifier(sys.argv[1])