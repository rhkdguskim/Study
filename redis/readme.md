# Redis 란?
- Key, Value 구조의 비정형 데이터를 저장하고 관리하기 위한 오픈 소스 기반의 비관계형 데이터베이스 시스템
- 데이터베이스, 캐시, 메세지브로커로 사용되며 **인메모리 데이터 구조**를 가진 저장소 입니다.
### Cache Server란?
- 데이터베이스가 있는데도 Redis라는 인메모리 데이터 구조 저장소를 사용하는 이유(?)
- 인메모리 데이터베이스가 아니라면 사용자가 많아 질 수록 부하가 느려집니다. ( HDD,SDD 접근 )
- 과부하를 방지하기위하여 캐시 서버(Redis)를 도입한다.
#### Look aside cache
- 클라이언트가 데이터를 요청
- 웹서버는 데이터가 존재하는지 Cache 서버에 확인
- Cache서버에 데이터가 있으면 DB데이터를 조회하지않고 Cache 서버에 있는 결과값을 클라이언트에게 바로 반환( Cache Hit)
- Cache 서버에 데이터가 없으면 DB에 데이터를 조회하여 Cache 서버에 저장하고 결과값을 클라이언트에게 반환 (Cache Miss)
#### Write Back
- 웹서버는 모든 데이터를 Cache 서버에 저장
- Cache 서버에 특정 시간동안 데이터가 저장됨
- Cache 서버에 있는 데이터를 DB에 저장
- DB에 저장된 Cache 서버의 데이터를 삭제

## Redis의 특징
- Key, Value 구조이기 때문에 쿼리를 사용할 필요 없음
- 데이터를 디스크에 쓰지않고 메모리 데이터에서 처리하기 때문에 속도가 빠름
### 사용 자료형
- String : 가장 일반적인 key-value 구조 형태
- Set : String의 집합(여러개의 값을 하나의 Value에 넣을 수 있음)
- Sorted Set : Set구조에서 정렬 Sort를 적용한 구조
- Lists : Array형식의 데이터구조
- Hash : Java에서 사용하는 HashMap 구조와 비슷
### Single Thread 구조
- **한번의 하나의 명령만 처리가능** get,set 명령어의 경우 초당 10만개 이상 데이터를 처리할 수 있음
- Race Condition 발생 가능성이 낮음.
### 사용시 주의사항
- 서버 장애 발생시 그에대한 방안모색
- 메모리 관리 중요
- 시간복잡도가 높은 명령어 사용 지향

## Redis의 주요 사용처
- Remote Data Store : 여러 서버의 Data공유를 위해 사용 할 수 있음.
- 인증 토큰 개발 : JWT ...
- Ranking Board (Sorted Set)
- 유저 API Limit
- Job Queue
- Pub/Sub 기능 : 메세지 브로커 기능
- 이 외에도 Master-Slave 형식의 데이터 이중화 구조에 대한 Redis Replication, 분산 처리를 위한 Redis cluster, 장애 복구 시스템 Redis Sentinel, Redis Topology, Redis Sharding, Redis Failover 등의 Redis를 더 효율적으로 사용하기 위한 개념들이 존재합니다.