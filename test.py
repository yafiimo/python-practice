

l = [4,5,6,7,8]

l2 = next((i for i,x in enumerate(l) if x > 100), -1)

print(l2)