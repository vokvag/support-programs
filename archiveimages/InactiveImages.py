import os,os.path
import sys,getopt
import time
import shutil

def main(argv):
    file = ""
    source = ""
    dest = ""
    try:
        opts,args = getopt.getopt(argv,"hf:s:d:",["file=","source=","dest="])
    except getopt.GetoptError:
        print('InactiveImages.py -f <Inactive list> -s <Archive Source> -d <Archive Destination>')
        sys.exit(2)
    if(len(opts) != 3):
        print('InactiveImages.py -f <Inactive list> -s <Archive Source> -d <Archive Destination>')
        sys.exit()
    for opt,arg in opts:
        if opt == '-h':
            print('InactiveImages.py -f <Inactive list> -s <Archive Source> -d <Archive Destination>')
            sys.exit()
        elif opt in ("-f", "--file"):
            file = arg
        elif opt in ("-s", "--source"):
            source = arg
        elif opt in ("-d", "--dest"):
            dest = arg
    if not (file == ""):
        print('Moving from', source, 'to' ,dest)
    start_time = time.time()
    executor(file,source,dest)
    print("--- %s seconds ---" % (time.time() - start_time))

def executor(file,source,dest):
    if not (os.path.isdir(dest)):
        os.mkdir(dest)
    with open(file,'r') as f, open(dest+"\\"+"noimageinactives.txt",'a') as w:
        for line in f:
            code = line.strip('\n')
            if not(code.isnumeric()):
                continue
            ###find the path
            if(os.path.isdir(source+"\\"+code)):
                ##move to new dir
                shutil.move(source+"\\"+code,dest)
            else:
                w.write(code+"\n")
        f.close()
        w.close()


if __name__ == "__main__":
    main(sys.argv[1:])
