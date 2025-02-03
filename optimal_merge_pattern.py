def merge(l1, l2):
    i = 0
    j = 0
    l3 = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    while i < len(l1):
        l3.append(l1[i])
        i += 1
    while j < len(l2):
        l3.append(l2[j])
        j += 1
    return l3

def optimal_merge(l1):
    cost = 0
    while len(l1) > 1:
        l1 = sorted(l1, key=len)
        cost += len(l1[0]) + len(l1[1])
        l2 = merge(l1[0], l1[1])
        l1 = [l2] + l1[2:]  
    print("Cost:", cost)
    print("Merged List:", l1[0])

l1 = []
n=int(input("Enter the no. of Lists-> "))
for i in range(n):
    size=int(input("Enter The Size of the List-> "))
    l2=[]
    for j in range(size):
        num=int(input("Enter Number-> "))
        l2.append(num)
    l2.sort()
    l1.append(l2)

optimal_merge(l1)
