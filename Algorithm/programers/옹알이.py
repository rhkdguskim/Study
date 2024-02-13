# 머쓱이는 태어난지 6개월 된 조카를 보고 돌보고 있습니다.
# 조카는 "aya", "ye", "woo" , "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한 발음밖에 하지 못합니다.
# 문자열 배열 babbling이 매개변수로 주어질때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return 하도록 solution 함수를 완성해주세요.


babbling = ["aya", "yee", "u", "maa", "wyeoo"]
babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
def solution(babbling):
    answer = 0
    for data in babbling:
        if(data.replace("aya"," ").replace("ye", " ").replace("woo"," ").replace("ma"," ").strip() == ""):
            answer += 1
    
    return answer
    
solution(babbling)