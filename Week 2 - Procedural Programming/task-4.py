x={'1':['a','b'], '2':['c','d']}
list1 = x.get('1')
list2 = x.get('2')
for i in range(2):
    for j in range(2):          
        print(list1[i]+list2[j])