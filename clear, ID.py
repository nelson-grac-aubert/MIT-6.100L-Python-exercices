L = [1,2,3,4]
print(id(L))
L.append(8)
print(L)
print(id(L))
L.clear()
print(L)
print(id(L))

print("-------------------------")

L = []
print(L)
print(id(L))