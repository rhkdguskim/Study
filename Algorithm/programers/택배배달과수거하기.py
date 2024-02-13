# 당신은 일렬로 나열된 n개의 집에 배달을 하려 합니다. 배달할 물건은 모두 크기가 같은 재활용 택배 상자에 담아 배열하여
# 배달을 다니면서 빈 재활용 택배 상자를 수거하려고 한다. 

cap = 4
n = 5
deliveries = [1,0,3,1,2]
pickups = [0,3,0,4,0]

def solution(cap, n, deliveries, pickups):
    # 배달 전략
    car = 0
    seek = n
    delivery = list()
    for i in deliveries:
        car += i
        if(car >= cap) :
            if(car != cap) :
                car = car - cap
            else :
                car = 0
                
            delivery.append(seek)
            seek -= 1
    
    print(delivery)
        

def Move(dis):
    distance += dis
    

solution(cap,n,deliveries,pickups)
