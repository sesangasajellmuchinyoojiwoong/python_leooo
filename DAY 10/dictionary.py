'''
딕셔너리(dictionary)
-python에서 사용하는 자료구조 중 하나
-keyer value 쌍으로 존재함.
-중괄호와 :를 이용해 작성
-indexing 하는 방법
1.딕셔너리[key]를 이용 (딕셔너리에서 순서는 중요하지 않음)
2.get method 사용

value를 수정하는 방법
1.indexing 이용함
2.update method 이용

-삭제하는 방법
del 딕셔너리[key]

-key를 확인하는 방법
: key in 딕셔너리
'''
리스트=[1,2,3]

튜플=(1,2,3)

딕셔너리={"축구":"손흥민","야구":"소크라테스"}
딕셔너리["야구"]="류현준"

# print(type(리스트))
# print(type(튜플))
# print(type(딕셔너리))

print(딕셔너리.get("야구"))
print(딕셔너리["야구"])

딕셔너리.update({"야구":"김혜성"})

print(딕셔너리)

딕셔너리["피겨"]="김연아"

딕셔너리.update({"배구":"김연경"})

print(딕셔너리)

del 딕셔너리["축구"]

del 딕셔너리["피겨"]

print(딕셔너리)

print ("야구" in 딕셔너리) 
print ("농구"in 딕셔너리)

fruits={"오렌지":50,"사과":100,"바나나":200}

fruit= input("어서오세요 미니스톱 입니다 단도진입 적으로 묻는다 뭐 먹을 꺼야?:")
if  fruit in fruits: 
    print(f"우리 {fruit} {fruits[fruit]}남음 1개 당 100만원이다")
else:
    print(f"안타깝지만 우린 {fruit}는 안 판다 너를 팬다")