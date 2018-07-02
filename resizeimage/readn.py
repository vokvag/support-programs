def readnames(Dir):
    import os,os.path
    try:
        os.makedirs(Dir+'\\new')
    except FileExistsError:
        print("folderExist")
    for name in os.listdir(Dir):
        print(name)

def walkp(Dir):
    from os import walk
    f = []
    for(dp,dn,fn)in walk(Dir):
        print(dp)
        print(dn)
        print(fn)

def compare_md5(p1,p2):
    import hashlib
    m1 = hashlib.md5()
    m1.update(open(p1,"rb").read())
    c1 = m1.hexdigest()
    m2 = hashlib.md5()
    m2.update(open(p2,"rb").read())
    c2 = m2.hexdigest()
    if(c1==c2):
        return True
    else:
        return False

def compare_modified_date(p1,p2):
    import os.path
    return os.path.getmtime(p1) >= os.path.getmtime(p2)
    

def compare_two_folders(p,f1,f2):
    import os
    fn1 = "both"
    try:
        os.makedirs(p+'\\'+fn1)
    except FileExistsError:
        print("Folder "+fn1+" Exist")
    fn2 = "dff"
    try:
        os.makedirs(p+'\\'+fn2)
    except FileExistsError:
        print("Folder "+fn2+" Exist")
    fn3 = "dff.new"
    try:
        os.makedirs(p+'\\'+fn3)
    except FileExistsError:
        print("Folder "+fn3+" Exist")
    p1 = p+"\\"+f1
    p2 = p+"\\"+f2
    files1 = os.listdir(p1)
    files2 = os.listdir(p2)
    for name in files1:
        if(name in files2):
            if(compare_md5(p1+"\\"+name,p2+"\\"+name)):
                os.rename(p1+"\\"+name,p+'\\'+fn1+"\\"+name)
                os.remove(p2+"\\"+name)
            else:
                os.rename(p1+"\\"+name,p+'\\'+fn2+"\\"+name)
                os.rename(p2+"\\"+name,p+'\\'+fn3+"\\"+name)
##        else:
##            print(name)
    print("DONE!")
    
