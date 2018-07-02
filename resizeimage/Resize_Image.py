def Resize_from_dir(Dir):
    import os,os.path
    count = 0
    for name in os.listdir(Dir):

        Resize_Image(Dir,name)
        count = count + 1
        print(name)
    print(count)



def Resize_Image(Dir,ImageFilePath):
    from PIL import Image
    try:
        a,b = ImageFilePath.split(".")
        image = Image.open(Dir+'\\'+ImageFilePath)
        image = image.resize((500, 500),Image.ANTIALIAS)
        nim = image.convert('RGB')

        nim.save("C:\\Users\\Huo\\Pictures\\bimages\\"+a+".jpg",optimize=True)
    except:
        print(a)
        pass
