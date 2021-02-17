my_dict = {1:'Apple', 2:'Oracle',3:'Advanced Programming Practice',4:'Software Project Management', 5:'Fundamentals of mathematics'}

for x in range(1,6):
    #print(my_dict[i])
    test_str = my_dict[x]
    res = {i : test_str.count(i) for i in set(test_str)}  
    print(res)

