import shutil
import os,os.path
import sys,getopt
import time


def main(argv):
    src = ""
    dst = ""
    try:
        opts,args = getopt.getopt(argv,"hs:d:",["src=","dst="])
    except getopt.GetoptError:
        print('ArchiveImages.py -s <source> -d <destination>')
        sys.exit(2)
    if(len(opts) != 2):
        print('ArchiveImages.py -s <source> -d <destination>')
        sys.exit()
    for opt,arg in opts:
        if opt == '-h':
            print('ArchiveImages.py -s <source> -d <destination>')
            sys.exit()
        elif opt in ("-s", "--src"):
            src = arg
        elif opt in ("-d", "--dst"):
            dst = arg
    print ('path of src ', src)
    print ('path of dst ', dst)
    start_time = time.time()
    executor(src,dst)
    print("--- %s seconds ---" % (time.time() - start_time))

def executor(src,dst):
    for (dp,dn,fn) in os.walk(src):
        print("Now Scanning: "+dp)
        for name in fn:
            gnn = getnewname(dp,name)
            if(gnn=="Invalid"):
                continue
            style_code = gnn[0]
            new_name = gnn[1]
            makenewdir(dst,style_code)
            if not (os.access(dp+"\\"+name,os.W_OK)):
                os.chmod(dp+"\\"+name, 0o666)
            try:
                shutil.copy2(dp+"\\"+name,dst+"\\"+style_code+"\\"+new_name)
            except (OSError,IOError) as e:
                print(e)
                print("Source: "+dp+"\\"+name)
                print("Destination: "+dst+"\\"+style_code+"\\"+new_name)


def makenewdir(dst,style_code):
    if(os.path.isdir(dst+"\\"+style_code)):
        return
    else:
        os.mkdir(dst+"\\"+style_code)
        

    



def getnewname(path,name):
    n = name.split(".")
    if(len(n)<=1):
        ##TODO
        print("Unknown Format: "+path+"\\"+name)
        pass
    else:
        s = n[0]
        fileformat = n[len(n)-1]
        style_code = genstylecode(s)
        if(style_code=="Invalid"):
            ##print(style_code)
            return style_code
        md5 = getmd5(path+"\\"+name)
        new_name= style_code+"-"+md5+"."+fileformat
        return (style_code,new_name)




def genstylecode(name):
    style_code = ""
    m = 0
    temp = ""
    l = 0
    for letter in name:
        if(letter.isdigit()):
            temp = temp+letter
            l = l+1
        else:
            if(l>m):
                m = 1
                style_code = temp
            temp = ""
            l = 0
    if(l>m):
        style_code = temp

    if(len(style_code)<=5 or style_code[0]!='6'):
        return "Invalid"    
    return style_code

def getmd5(filepath):
    import hashlib
    m = hashlib.md5()
    m.update(open(filepath,"rb").read())
    c = m.hexdigest()
    return c



if __name__ == "__main__":
    main(sys.argv[1:])

