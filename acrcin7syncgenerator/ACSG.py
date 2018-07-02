import os,os.path
import sys,getopt
import time



def main(argv):
    acr = ""
    cin7 = ""
    last = ""
    new = ""
    try:
        opts,args = getopt.getopt(argv,"ha:c:l:n:",["acr=","cin7=","last=","new="])
    except getopt.GetoptError:
        print('ACSG.py -a <ACR SOH> -c <CIN7 SOH> -l <LAST MASTER> -n <DIR FOR NEW>')
        sys.exit(2)
    if(len(opts) < 3):
        print('ACSG.py -a <ACR SOH> -c <CIN7 SOH> -l <LAST MASTER> -n <DIR FOR NEW>')
        sys.exit()
    if(len(opts) > 4):
        print('ACSG.py -a <ACR SOH> -c <CIN7 SOH> -l <LAST MASTER> -n <DIR FOR NEW>')
        sys.exit()
    for opt,arg in opts:
        if opt == '-h':
            print('ACSG.py -a <ACR SOH> -c <CIN7 SOH>-l <LAST MASTER> -n <DIR FOR NEW>')
            sys.exit()
        elif opt in ("-a", "--acr"):
            acr = arg
        elif opt in ("-c", "--cin7"):
            cin7 = arg
        elif opt in ("-l", "--last"):
            last = arg
        elif opt in ("-n", "--new"):
            new = arg
    print ('path of ACR SOH ', acr)
    print ('path of CIN7 SOH ', cin7)
    print ('path of LAST MASTER ', last)
    if not (new == ""):
        print ('path of NEW ADD ', new)
    start_time = time.time()
    executor(acr,cin7,last,new)
    print("--- %s seconds ---" % (time.time() - start_time))

def executor(acr,cin7,last,new):
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

    with open(cin7,'r') as f:
        for line in f:
            a = line.replace('"','').strip('\n').split("\t")
            if(a[0] in dic):
                dic[a[0]] = float(a[1]) + dic[a[0]]
                if(dic[a[0]]<0):
                    dic[a[0]] = 0
        f.close()

    if not (new == ""):
        for newpath in os.listdir(new):
            dic = newadd(new+"\\"+newpath,dic)

    with open(filedir + "\\" + acrst,'w') as g, open(filedir + "\\" + cin7st,'w') as h, open(filedir + "\\" + magst,"w") as i:
        g.write("PRDID\tQTY\n")
        h.write("Code\tCount\n")
        i.write("sku,qty,is_in_stock\n")
        for item in dic:
            g.write(item+"\t"+str(dic[item])+"\n")
            h.write(item+"\t"+str(dic[item])+"\n")
            i.write(item+","+str(dic[item])+","+("1" if dic[item]>0 else "0")+"\n")
        g.close()
        h.close()
        i.close()

def newadd(path,dic):
    with open(path,'r') as f:
        for line in f:
            a = line.strip('\n').split(",")
            if not (a[0].isnumeric()):
                continue
            if (a[0] in dic):
                dic[a[0]] = dic[a[0]] + float(a[1])
            else:
                dic[a[0]] = float(a[1])
    return dic



if __name__ == "__main__":
    main(sys.argv[1:])
