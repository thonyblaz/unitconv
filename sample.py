import unitconv as uc
valor = uc.conversion(4, "mm", "cm", "leng",4)
print(valor)


lista = [2,3,4,5,6,98]
for i in range(0,len(lista)):
    valor = uc.conversion(lista[i], "m2", "plg2", "area",4)
    print(valor)

print(uc.open_json("leng").keys())