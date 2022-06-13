from itertools import product, chain, combinations
import time

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def get_combi(item):
    combi = []
    for x in range(len(item)):
        comb = []
        for combo in powerset(item[x]):
            comb.append(combo)
        combi.append(comb)
    return combi

def pilih(comb, duit):
    totHarga=0
    total = []
    for item in comb:
        tot = []
        for y in item:
            nama = y
            harga = sum([pair[1] for pair in y])
            prot = sum([pair[2] for pair in y])
            if harga<=duit and harga!=0:
                tot.append([nama, harga, prot])
        tot = max(tot, key=lambda tup: tup[2])
        tot1 = max(tot[0], key=lambda tup: tup[2])
        total.append(tot1)
    return total
                
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
item = [itemset_1, itemset_2, itemset_3]
combi = get_combi(item)
bagged = pilih(combi, duit)

print("{:17}{:10}{:12}".format("Brand", "Harga", "Protein"))
totalBiaya = totalProtein = 0
for x in bagged:
    print("{:17}{:5}{:12}".format(*x))
    totalBiaya+=x[1]
    totalProtein+=x[2]
print("Total Biaya: {}, Total protein: {}".format(totalBiaya, totalProtein))
end = time.time()
print("The time of execution of above program is :", end-start)
