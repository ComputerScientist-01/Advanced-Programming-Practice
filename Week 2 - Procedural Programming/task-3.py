def sum_tuple_in_list(lst):
    print([sum(i) for i in lst])

lst=[(1, 2), (1, 3), (2, 3)]
lst2 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

sum_tuple_in_list(lst)
sum_tuple_in_list(lst2)
