def rename(Dir):
    import os
    for f in os.listdir(Dir):
        a,b = f.split("a")
        os.rename(f,a+".png")


def pppp():
    from PIL import Image
    image = Image.open("C:\\Users\\Huo\\Pictures\\Saved Pictures\\600040.png")
    image = image.resize((500, 500),Image.ANTIALIAS)
    nim = image.convert('RGB')
    nim.save("C:\\Users\\Huo\\Pictures\\Saved Pictures\\600040.jpg", optimize = True)
