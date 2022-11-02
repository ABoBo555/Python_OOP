# if unmutable obj is passed into a fun it will create a new address point for update obj
# but for mutable obj it will direct to the same address point whatever
def change(L):
    print(id(L))
    if type(L) == list:
        L.append(5)
    elif type(L) == tuple:
        L = L + (5, 6)
    print(L)
    print(
        "For tuple case here address is changed: ", id(L)
    )  # this is bcz tuplel is unmutable


alist = [1, 2, 3, 4]
atuple = (1, 2, 3, 4)
print("This is list case:")
print(id(alist))
print(alist)
change(alist)

print(alist)

print("This is tuple case:")
print(id(atuple))
print(atuple)
change(atuple)

print(atuple)
