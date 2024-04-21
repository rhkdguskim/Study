def solution(phone_book):
    # 정렬을 한뒤에
    # i과 i+1을 순차적으로 비교한다.
    phone_book.sort()
    for i in range(len(phone_book)-1):
        length = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:length]:
            return False
        
    return True