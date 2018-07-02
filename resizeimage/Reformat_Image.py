def Reformat_from_dir(Dir):
    import os,os.path
    count = 0
    pre = ""
    for name in os.listdir(Dir):
        try:
            a,b = name.split(".")
        except:
            a = name
            print("name error "+name)
        if(a == pre):
            print("This is doubled "+name)
        pre = a;
        Reformat_Image(Dir,name)
        count = count + 1
        print(name)
    print(count)




def Reformat_Image(Dir,ImageFilePath):

    from PIL import Image
    ##f = open("log.txt","w+")
    try:
        a,b = ImageFilePath.split(".")
    ##    print(a)
    ##    print(Dir+'\\'+ImageFilePath)
        image = Image.open(Dir+'\\'+ImageFilePath, 'r')
        image_size = image.size
        width = image_size[0]
        height = image_size[1]

        if(width != height):
            bigside = width if width > height else height

            background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
            offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

            background.paste(image, offset)
            background.save("C:\\Users\\Huo\\Desktop\\a\\new images\\"+a+".png")
            ##print(a+" has been resized !")
            image.close()
            background.close()

        else:
            image.save("C:\\Users\\Huo\\Desktop\\a\\new images\\"+a+".png")
            ##print(a+" is already a square, it has not been resized !")
            image.close()
    except:
        ##f.write(ImageFilePath+"\n")
        print(ImageFilePath)

def Remove_transparent(ImageFilePath):

    from PIL import Image
    image = Image.open(ImageFilePath,'r')
    image_size = image.size
    layer = Image.new('RGBA', image_size, (255, 255, 255, 255))
    final = Image.alpha_composite(layer, image.convert('RGBA'))
    final.save("new.png")
    
