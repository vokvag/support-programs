import os,os.path
import sys,getopt
import time



def main(argv):
    acr = ""
    cin7 = ""
    last = ""
    try:
        opts,args = getopt.getopt(argv,"ha:c:l:",["acr=","cin7=","last="])
    except getopt.GetoptError:
        print('ACSG.py -a <ACR SOH> -c <CIN7 SOH> -l <LAST MASTER>')
        sys.exit(2)
    if(len(opts) != 3):
        print('ACSG.py -a <ACR SOH> -c <CIN7 SOH> -l <LAST MASTER>')
        sys.exit()
    for opt,arg in opts:
        if opt == '-h':
            print('ACSG.py -a <ACR SOH> -c <CIN7 SOH>-l <LAST MASTER>')
            sys.exit()
        elif opt in ("-a", "--acr"):
            acr = arg
        elif opt in ("-c", "--cin7"):
            cin7 = arg
        elif opt in ("-l", "--last"):
            last = arg
    print ('path of ACR SOH ', acr)
    print ('path of CIN7 SOH ', cin7)
    print ('path of LAST MASTER ', last)
    start_time = time.time()
    executor(acr,cin7,last)
    print("--- %s seconds ---" % (time.time() - start_time))

def executor(acr,cin7,last):
    filedir = os.getcwd()+"\\Outputs"
    if(os.path.isdir(filedir)):
        pass
    else:
        os.mkdir(filedir)
    date = time.strftime("%d%m%Y")
    acrst = "acrST_"+ date + ".txt"
    cin7st = "cin7ST_"+ date + ".txt"
    magst = "magST_"+ date + ".csv"
    dic = {}
    with open(last,'r') as f:
        for line in f:
            a = line.strip('\n').split("\t")
            if not(a[0].isnumeric()):
                continue
            dic[a[0]] = float(a[1])
        f.close()

    with open(acr,'r') as f:
        for line in f:
            a = " ".join(line.strip('\n').split()).split(" ")
            if(a[0] in dic):
                dic[a[0]] = float(a[1]) - dic[a[0]]
        f.close()

    with open(cin7,'r') as f, open(filedir + "\\" + acrst,'w') as g, open(filedir + "\\" + cin7st,'w') as h, open(filedir + "\\" + magst,"w") as i:
        g.write("PRDID\tQTY\n")
        h.write("Code\tCount\n")
        i.write("sku,qty\n")
        for line in f:
            a = line.replace('"','').strip('\n').split("\t")
            if(a[0] in dic):
                dic[a[0]] = float(a[1]) + dic[a[0]]
                if(dic[a[0]]<0):
                    dic[a[0]] = 0
                g.write(a[0]+"\t"+str(dic[a[0]])+"\n")
                h.write(a[0]+"\t"+str(dic[a[0]])+"\n")
                i.write(a[0]+","+str(dic[a[0]])+"\n")
        f.close()
        g.close()
        h.close()
        i.close()



if __name__ == "__main__":
    main(sys.argv[1:])
