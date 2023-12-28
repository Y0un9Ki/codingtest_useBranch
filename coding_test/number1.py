# 정수 배열 numbers가 주어집니다. 
# numbers에서 서로 다른 인덱스에 있는 
# 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 
# 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = []
    num_list=[]
    result=[]
    n=1
    for i in numbers:
        for j in numbers[n:]:
            num_list.append(i+j)
        n+=1
    while 1<=len(num_list):
        answer.append(min(num_list))
        num_list.remove(min(num_list))
    set_list=set(answer)
    result=list(set_list)
    
    
    return result

#하지만 반례가 존재해서 풀리지 않았다.