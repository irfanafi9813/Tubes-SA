import time

def sort(itemset):
	data = list()
	for name, amount, value in itemset:
		data.append((value/amount, value, amount, name))
	density = sorted(data, reverse=True, key=lambda tup: tup[0])
	profit = sorted(data, reverse=True, key=lambda tup: tup[1])
	weight = sorted(data, key=lambda tup: tup[2])
	return (density, profit, weight)

def pilih(itemset, duit):
	i = 0
	bag = []
	tot = profit = 0
	kategori= ""
	totVal = []
	item = [itemset[0], itemset[1], itemset[2]]
	while i < 3:
		for unit_value, value, amount, name in item[i]:
			if tot+amount<=duit:
				tot += amount
				profit += value
				if i==0:
					kategori="M. Kering"
				elif i==1:
					kategori="M. Basah"
				elif i==2:
					kategori="Susu"
				bag += [(kategori, name, amount, value)]
				totVal = [tot, profit]
				break
		i+=1
	return bag, totVal

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
byDensity = list()
byProfit = list()
byWeight = list()
for x in item:
	byDensity.append(sort(x)[0])
	byProfit.append(sort(x)[1])
	byWeight.append(sort(x)[2])

item = [byDensity, byProfit, byWeight]
pilihan = list()
totVal = list()
for y in item:
	pilihan.append(pilih(y, duit)[0])
	totVal.append(pilih(y, duit)[1])

print("------- BERDASARKAN DENSITY -------")
print("{:10}{:10}{:10}{:10}".format("Kategori", "Brand", "Harga", "Protein"))
print("\n".join("{:10}{:10}{:5}{:10}".format(*item) for item in pilihan[0]))
print("Total Biaya: {}, Total Protein: {}".format(totVal[0][-2], totVal[0][-1]))
print("-"*35)
print("\n")

print("------- BERDASARKAN PROFIT -------")
print("{:10}{:10}{:10}{:10}".format("Kategori", "Brand", "Harga", "Protein"))
print("\n".join("{:10}{:10}{:5}{:10}".format(*item) for item in pilihan[1]))
print("Total Biaya: {}, Total Protein: {}".format(totVal[1][-2], totVal[1][-1]))
print("-"*35)
print("\n")

print("------- BERDASARKAN HARGA -------")
print("{:10}{:10}{:10}{:10}".format("Kategori", "Brand", "Harga", "Protein"))
print("\n".join("{:10}{:10}{:5}{:10}".format(*item) for item in pilihan[2]))
print("-"*35)
print("Total Biaya: {}, Total Protein: {}".format(totVal[2][-2], totVal[2][-1]))
print("\n")
end = time.time()
print("The time of execution of above program is :", end-start)