def pathproducts():
    import csv
    with open('ProductExport-7-12-2017 .csv', 'r') as f, open('bonfect.csv', 'w') as f_out:
        for line in f:
            cols = line.split(',')
            print(cols)
            if(cols[0]=="Category"):
                f_out.write("sku" +"\n")
            else:
                f_out.write(cols[4].strip() +"\n")

def ppap():
    import csv
    with open('bonfect.csv', 'w',newline='') as f:
        fieldnames = ['a','b']
        writer = csv.DictWriter(f,fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'a': 'Baked', 'b': 'Beans'})
        writer.writerow({'a': 'adf', 'b': 'asdf'})
def readf():
    import csv
    with open('catalog_product_20171207_235346.csv', 'r') as f:
        i = 0
        for line in f:
            i = i+1
            if(i<1000):
                cols = line.split(',')
                print(cols)
            else:
                break

    
def Reform_CSV():
    import csv
    with open('ProductExport-8-12-2017.csv', 'r') as f, open('bonfectCon.csv', 'w',newline='') as f_out:
        fieldnames = ['sku', 'name', 'short_description', 'description', 'price', 'weight', 'qty', '_category', '_attribute_set', '_type', '_root_category', 'status', 'tax_class_id', '_product_websites', 'image', 'small_image', 'thumbnail', 'is_in_stock', '_media_attribute_id', '_media_image']
        writer = csv.DictWriter(f_out,fieldnames=fieldnames)
        writer.writeheader()
        i = 0
        for line in f:
            i=i+1
            if(i>=0):
                cols = line.split(',')
                sku = cols[4]
                name = cols[3]
                price = cols[40]
                category = 'Confectionery/Medicated Rolls'
                img = cols[4]+'.jpg'
                if(cols[0]=='Category'):
                    pass
                else:
                    writer.writerow({'sku':sku, 'name':name, 'short_description':name, 'description':name, 'price':price, 'weight':0.3, 'qty':50, '_category':category, '_attribute_set':'Default', '_type':'simple', '_root_category':'Default Category', 'status':1, 'tax_class_id':2, '_product_websites':'base', 'image':img, 'small_image':img, 'thumbnail':img, 'is_in_stock':1, '_media_attribute_id':80, '_media_image':img})


def write_csv(Dir):
    import csv,os
    with open('bonfectNew.csv','w',newline='') as f_out:
        fieldnames = ['sku','image','small_image','thumbnail','_media_attribute_id','_media_image','_media_position','_media_is_disabled','visibility']
        writer = csv.DictWriter(f_out,fieldnames=fieldnames)
        writer.writeheader()
        pre = ""
        pos = 0
        for name in os.listdir(Dir):
            noformat = name.split(".")
            num = noformat[0].split("_")
            sku = num[0]
            if(sku != pre):
                pos = 0
                writer.writerow({'sku':sku,'image':name,'small_image':name,'thumbnail':name,'_media_attribute_id':"80",'_media_image':name,'_media_position':str(pos),'_media_is_disabled':"0",'visibility':"4"})
            else:
                pos = pos + 1
                writer.writerow({'_media_attribute_id':"80",'_media_image':name,'_media_position':str(pos),'_media_is_disabled':"0"})
            pre = sku




            
        
