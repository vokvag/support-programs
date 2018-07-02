def searchterms(fdir):
    with open(fdir,'r') as f, open("output1.txt","w") as o1, open("output2.txt","w") as o2:
        for line in f:
            a = line.strip('\n').lower()
            result = []
            result.append(a)
            result = removeSpace(result)
            result = removeHi(result)
            result = removePer(result)          
            result = removeAnd(result)
            result = removeQuo(result)
            result = removeS(result)
            result = replaceNum(result)
            ##print(list(set(result)))
            s = a
            for i in set(result):
                if not i == a:
                    s = s + "\t" + i
                    o2.write(i+"\t"+a+"\n")

            o1.write(s+"\n")

            
            
        f.close()
        o1.close()
        o2.close()

def replaceNum(l):
    result = []
    for a in l:
        if "1" in a:
            result.append(a.replace("1","one"))
        if "2" in a:
            result.append(a.replace("2","two"))
        if "3" in a:
            result.append(a.replace("3","three"))
        if "4" in a:
            result.append(a.replace("4","four"))
        if "5" in a:
            result.append(a.replace("5","five"))
        if "6" in a:
            result.append(a.replace("6","six"))
        if "7" in a:
            result.append(a.replace("7","seven"))
        if "8" in a:
            result.append(a.replace("8","eight"))
        if "9" in a:
            result.append(a.replace("9","nine"))
        if "0" in a:
            result.append(a.replace("0","zero"))
    return l + result



def removeS(l):
    result = []
    for a in l:
        if a.endswith("'s"):
            result.append(a[:-2])
        elif a.endswith("s"):
            result.append(a[:-1])
    return l + result


def removeAnd(l):
    result = []
    for a in l:
        if " & " in a:
            result.append(a.replace(" & "," and "))
            result.append(a.replace(" & "," n "))
            result.append(a.replace(" & ",""))
        elif "&" in a:
            result.append(a.replace("&"," and "))
            result.append(a.replace("&"," n "))
            result.append(a.replace("&",""))
            result.append(a.replace("&"," & "))
    return l + result

def removeSpace(l):
    result = []
    for a in l:
        if " " in a:
            result.append(a.replace(" ",""))
    return l + result

def removeHi(l):
    result = []
    for a in l:
        if "-" in a:
            result.append(a.replace("-",""))
            result.append(a.replace("-"," "))
    return l + result

def removeQuo(l):
    result = []
    for a in l:
        if "'" in a:
            result.append(a.replace("'",""))
    return l + result

def removePer(l):
    result = []
    for a in l:
        if "%" in a:
            result.append(a.replace("%",""))
    return l + result
