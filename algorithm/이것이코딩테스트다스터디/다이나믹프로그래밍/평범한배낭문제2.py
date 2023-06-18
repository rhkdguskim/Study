# https://www.acmicpc.net/problem/12865
# 가장가치있으면서 가장 가벼운 아이템을 가방에 넣는다.
# 가방의 무게보다 작은 결과로 순열을 만든다.

N, W = map(int, input().split())

itemlist = []
for _ in range(N):
    itemlist.append(list(map(int, input().split()))) # 물건의 무게, 물건의 가치

bag = []
def makelist(itemlist, idx):
    totalweight = 0
    totalvalue = 0
    for data in bag:
        totalweight += data[0]
        if totalweight <= W:
            totalvalue += data[1]
        else:
            return totalvalue
    
    itemlists = itemlist
    for i in len(itemlists):
        bag.append(itemlists.pop(i)) 
        makelist(itemlists, i)
        bag.pop()
    

valuelist = []
def checkBagWeight(bag):
    weight = 0
    value = 0
    for i in range(len(bag)):
        weight += i[1]
        value += i[0]
    if(weight > W):
        return
    else:
        return valuelist.append(value)
    
bag = []
def addItem(bag):
    weight = 0
    value = 0
    for i in range(len(bag)):
        weight += bag[i][0]
        if(weight > W):
            return valuelist.append(value)
        else :
            value += bag[i][1]
        
    
    for i in range(len(itemlist)):
        data1 = itemlist.pop()
        #print("PUSH ", data1)
        bag.append(data1)
        addItem(bag)
        data = bag.pop()
        #print("POP ", data)
        itemlist.insert(0, data)
        
addItem(bag)
print(max(valuelist))