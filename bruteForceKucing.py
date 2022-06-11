# https://stackoverflow.com/questions/31497021/knapsack-with-requirement-to-select-one-item-each-from-many-sets
# heuristik: tikda bisa dijelaskan secara matematis, 
# karena menggunakan terkaan, intuisi, dan common sense

from itertools import product
import time

def anycomb(item1, item2, item3):
    comb = []
    for combi in product(item1, item2, item3):
        comb.append(combi)
    return (comb)

def totalvalue(comb):
    global duit
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    if totwt <= duit:
        return (totval, -totwt)
    else:
        return (0,0)

itemset_1 = (
    ("RC", 120000, 36), 
    ("maxi", 27000, 32), 
    ("healthy pet", 60000, 30),
    ("excel", 21000, 30),
    ("ori cat", 20000, 27))
itemset_2 = (
    ("me-o", 18000, 11), 
    ("life cat", 15000, 10), 
    ("kit cat", 18000, 6),
    ("snappy tom tuna", 16000, 6), 
    ("whiskas", 20000, 9))
itemset_3 = (
    ("growsy", 4000, 34), 
    ("long life", 3800, 33),
    ("tridaya", 750, 13))

duit = int(input("Masukkan anggaran: "))
start = time.time()
comb = anycomb(itemset_1, itemset_2, itemset_3)
bagged = max(comb, key=totalvalue)
for x in range(3):
    bag = list(bagged[x])
    if x==0:
        bag.insert(0,"M. Kering")
        bag1 = tuple(bag)
    elif x==1:
        bag.insert(0,"M. Basah")
        bag2 = tuple(bag)
    elif x==2:
        bag.insert(0,"Susu")
        bag3 = tuple(bag)
bagged1 = (bag1,)+(bag2,)+(bag3,)

val, wt = totalvalue(bagged)
if val==0 and wt==0:
    print("Anggaran tidak cukup")
else:
    print("{:10}{:10}{:10}{:10}".format("Kategori", "Brand", "Harga", "Protein"))
    print("\n".join("{:10}{:10}{:5}{:10}".format(*item) for item in bagged1))
print("Total Biaya: %i, Total protein: %i" % (-wt, val))
print("\n")
end = time.time()
print("The time of execution of above program is :", end-start)