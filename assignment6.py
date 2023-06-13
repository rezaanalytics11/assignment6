def show_menu():
    print('1-Add product')
    print('2-Edit product')
    print('3-Delete product')
    print('4-Search product')
    print('5-Show list')
    print('6-Buy')
    print('7-Exit')

    choice1=input('Please make a choice: ')
    choice=int(choice1)

    myproduct=open(r'C:\Users\Ariya Rayaneh\Desktop\pythonProject\test2.py','r')
    data=myproduct.read()



    product_list=data.split('\n')

    #product_list.pop(3)
    #product_list.pop(3)



    k=[]

    for i in range(len(product_list)):
      product_info=product_list[i].split(',')

      mydict = {}
      mydict['id']=product_info[0]
      mydict['name'] = product_info[1]
      mydict['price'] = product_info[2]
      k.append(mydict)


    if choice==1:
        print('Inset id,name,price of added product: ')
        a=input('Insert id: ')
        b=input('name: ')
        c=input('price: ')
        k.append({'id': a, 'name': b, 'price': c})
        for i in k:
            print(i)


    if choice==2:
        print('Inset current product names: ')
        a = input('Currect name: ')
        print('Inset correct product name: ')
        b=input('Correct name: ')
        for i in k:
            if i['name']==a:
                i['name']=i['name'].replace(a,b)
                for i in k:
                     print(i)

    if choice == 3:
        print('Inset product name that should be deleted: ')
        a = input('Product name that should be deleted: ')

        for i in k:
         if i['name'] == a:
            k.remove(i)
            for j in k:
             print(j)


    if choice == 4:
        print('Inset product name: ')
        a=input('Insert name: ')
        for i in k:
            if i['name']==a:
                print('Yes we have this product')
                print(i)

            #else:
                #print('Sorry we have not this product')
                #break



    if choice == 5:
        for i in k:
            print(i)

    if choice == 6:
        a = input('Insert product name: ')
        b = input('Insert product name: ')
        c = input('Insert product name: ')

        for i in k:

            if i['name']==a:
                pricea=i['price']
                priceai=int(i['price'])

                print(a, ":", priceai)

            #else:
                #print('Please check list')
                #priceai=0

            #print(a, ":", priceai)


            if i['name']==b:
                priceb = i['price']
                pricebi= int(i['price'])
                print(b, ":", pricebi)


            #else:
                #print('Please check list')
                #pricebi=0

            if i['name'] == c:
                pricec = i['price']
                priceci=int(i['price'])
                print(c, ":", priceci)

            #else:
                #print('Please check list')
                #priceci=0



        total=priceai+pricebi+priceci
        print('Total Price:',total)



    if choice == 7:
        print('Hope to see you Again')


show_menu()
