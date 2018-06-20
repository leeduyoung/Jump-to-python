'''
[문제1] 점수의 평균
홍길동씨의 과목별 점수는 각각 다음과 같다.

과목	점수
국어	80
영어	75
수학	55
홍길동씨의 평균점수를 구하시오.
'''
scores = [80, 75, 55]

sum = 0
for score in scores:
    sum += score

print(sum/len(scores))