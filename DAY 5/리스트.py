"""
리스트(list)
열거혈 변수를 나타내는 자료구조 중 하나
<문법>
대괄호로 묶어주고, 요소들은 쉼표로 구분
비어있는 리스트는"[]"표현
요소들의 값은 indexing으로 가져올수 있음
-왼쪽에서 오른쪽으로 indexing 할 때는 0,1,2번째 순서로 정해짐
-왼쪽에서 왼쪽으로 indexing할 때는
-1,-2,-3번째로 순서로 정해짐

<특징1>
요소를 추가할때 append메소드를 사용
*오른쪽에 요소가 추가됨

<특징2>
요소를 삭제할때 pop매소드를 사용
*오른쪽에 요소가 사라짐

<특징3>
리스트 초기화 할 때 clear 메소드 사용

<특징4>
오른차순 정렬할 때 sort 메소드 사용

<특징5>
거꾸로 정렬할 때 reverse 메소드 사용

q.sort()아레에 q.reverse()를 쓰면 내림차순이 된다

sort는 적은 것 부터 큰 것까지 나오게 한다

<특징6>
index
값으로 자리를 찾을때 사용하는 메소드

<특징7>
indexing
자리로 값을 찾는 문법

<문법>
indexing 할때 댜괄호와 숫자를 사용

<특징8>
count
값이 몇개있는지 알아보는 메소드

<특징9>
내가 원하는 위치에 값을 끼워놓을 때
insert 메소드 사용

<특징10>
내가 원하는 값을 지울 때
remove 메소드 사용

<특징11>
리스트와 리스트를 결합할 때 extend 메소드 사용

<특징12>
리스트와 리스트르 결합할 때
(+)연산자 사용

<특징13>
리스트에 길이를 구하는 함수는 len함수 사용

<특징14>
for와리스트를 결합한 문법
"""
# a = [1, 2, 3]
# print(a)
# #print(a[-2] % a[2])
# # print(a[0]*a[2])
# # print(a[0])
# b = ["사과", "바나나", "귤"]
# print(b)
# c = [13, "헨섬하고 멋지고 아름다운 지웅", 2011, "오누"]
# print(c)
# d = []
# print(d)
# a = []
# a.append(10)
# print(a)
# a.append(20)
# print(a)
# a.append(30)
# print(a)
# 결과 = []
# for i in range(1, 11):
#     결과.append(i)
# print(결과)

# b = [1, 2, 3, 4]
# b.pop()
# print(b)
# b.pop()
# print(b)

# c = ["사과", "바나나", "귤"]
# c.clear()
# print(c)

# ㅇ = [2, 4, 1, 3]
# ㅇ. sort()
# print(ㅇ)
# e = ["banana", "cherry", "apple"]
# e.sort()
# print(e)

# f = [2, 4, 1, 3]
# f.reverse()
# print(f)
# g = ["banana", "cherry", "apple"]
# g.reverse()
# print(g)

# q = [2, 4, 1, 3]
# q.sort()
# q.reverse()
# print(q)

# a = ["banana", "cherry", "apple"]
# a.sort()
# a.reverse()
# print(a)

# a = [10, 20, 30]
# print(a[-1]*a[-2])

# a = [10, 20, 30]
# print(a[-2] % a[1])
# c = [1, 2, 3, 4, 1]
# print(c.count(1))

# c = [1, 2, 3, 4, 1]
# print(c.count(5))

# e = [1, 2, 3]
# e.insert(1, 100)
# print(e)

# i = [1, 2, 3]
# i.insert(1, 100)
# i.insert(2, 200)
# print(i)

# f = [100, 200, 10, 300]
# f.remove(10)
# f.remove(200)
# print(f)

# g = [1, 2]
# h = [3, 4, 5]
# g.extend(g)
# print(g)

# h.extend(h)
# print(h)

# i = [100, 200]
# j = [300, 400, 500]
# print(i+j)
# print(j+i)

# k = [10, 20, 30]
# print(len(k))
# k.append(40)
# print(len(k))

# k.clear()
# print(len(k))

fruits = ["cherry", "apple", "banana"]
for i in range(len(fruits)):
    print(fruits[i])

for fruits in fruits:
    print(fruits)
