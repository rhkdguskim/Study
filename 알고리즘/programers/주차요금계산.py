# 프로그래머스 주차요금계산 문제
# 주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을때, 차량별로 주차 요금을 계산하려고합니다.
import math

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", 
           "06:00 0000 IN", 
           "06:34 0000 OUT", 
           "07:59 5961 OUT", 
           "07:59 0148 IN", 
           "18:59 0000 IN", 
           "19:09 0148 OUT", 
           "22:59 5961 IN", 
           "23:00 5961 OUT"]


def solution(fees, records):
    answer = []
    newrecords = [record.split() for record in records]
    newrecords = sorted(newrecords, key=lambda x:x[1])
    carnumber = ""
    cardata = dict()
    # cardata dictionary에 데이터를 정리한다.
    for data in newrecords :
        data[0] = data[0].split(':')
        if(carnumber != data[1]):
            carnumber = data[1]
            cardata[carnumber] = list()
        
        # 시간과 출입여부 데이터를 넣는다.
        cardata[carnumber].append([data[0],data[2]])
    
    # OUT이 없는 경우를 추가해준다 
    for data in cardata:
        if len(cardata[data]) % 2 == 1 :
            cardata[data].append([["23","59"], 'OUT'])
    
    # 분으로 통일하여 계산한다.
    for data in cardata:
        min=0
        for timestamp in cardata[data]:
            if(timestamp[1] == 'OUT'):
                min += 60*int(timestamp[0][0]) # 시
                min += int(timestamp[0][1]) # 분
            else:
                min -= 60*int(timestamp[0][0]) # 시
                min -= int(timestamp[0][1]) # 분
            
        if(min >= fees[0]) :
            answer.append(fees[1] + math.ceil((min-fees[0])/fees[2])*fees[3])
            print("당신은 추가요금", data, fees[1] + math.ceil((min-fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])
            print("당신은 기본요금", data, fees[1])
    
    
    return answer


solution(fees, records)