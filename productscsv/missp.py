def No_pictures():
    import csv
    with open('catalog_product_20171220_221431.csv','r') as f, open('MissingImages.csv', 'w',newline='') as f_out:
        fieldnames = ['sku', 'name','_category','image']
        writer = csv.DictWriter(f_out,fieldnames=fieldnames)
        writer.writeheader()
        i = 0
        for line in f:
            i = i+1
            if(i>=0):
                cols = line.split(',')
                sku = cols[0]
                name = cols[34]
                category = cols[4]
                img = cols[22]
                visibility = cols[54]
                is_in_stock = cols[66]
                if(sku !='' and category!='' and category[1:9]!="Seasonal" and visibility == '4' and is_in_stock != '0' and (img == '' or img == 'no_selection')):
                    writer.writerow({'sku':sku,'name':name,'_category':category,'image':img})
                ##print(cols)
            
