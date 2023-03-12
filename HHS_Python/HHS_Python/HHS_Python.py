# 수박수박수박수박수박수? 2023/03/12 프로그래머스

def solution(n):
    answer = ''
    for i in range(0,n):
        if i % 2 == 1:
            answer = answer + '박'
        else:
            answer = answer + '수'
    
    return answer

# 