'''
반복문(while)
조건이 참인 동안 코드를 실행
조건이 거짓이면 while이 종료됨

<문법>   
while 조건:
    반복할 코드 작성
<중요>
조건을 True로 정하면 무한 반복됨
'''
# while True:
# print("지웅이 천재")

# while False:
# print("서우 ㅃㅃ")

# i = 1
# while i < 11:
#     print(i)
#     i+=1

# i = 0
# while i < 11:
# if i%2==0:
# print(i)
#     i += 1

# i = 10
# while i < 21:
#     if i % 3 != 0:
#         print(i)
#     i += 1

# i = 50
# while i < 101:
#     if i % 3 == 0:
#         if i % 4 == 0:
#             print(i)
#     i += 1

# i = 20
# e = 0
# while i < 31:
#     if i % 5 != 0:
#         e += i
#     i += 1
# print(e)

i = 0
e = 0
a = 0
while i < 101:
    if i % 2 == 0:
        a += i
    else:
        e += i
    i += 1
print(a-e)
