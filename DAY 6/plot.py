"""
import matplotlib.pyplot as plt
fruits = ["apple", "orange", "watermelon", "banananana"]
counts = [5, 2, 10, 7]
창, 내용 = plt.subplots(2, 1)
내용[0].bar(fruits, counts)
내용[1].barh(fruits, counts)
plt.show()

import matplotlib.pyplot as plt
fruits = ["apple", "orange", "watermelon", "banananana"]
counts = [5, 2, 10, 7]
창, 내용 = plt.subplots(1, 2)
내용[0].bar(fruits, counts)
내용[1].barh(fruits, counts)
plt.show()
"""
# import matplotlib.pyplot as plt
# fruits = ["apple", "orange", "banananana", "watermelon","water"]
# barcolor=["red","orange","yellow","green","blue"]
# counts = [5, 2, 10, 7,9]
# 창, 내용 = plt.subplots(2, 1)
# 내용[0].bar(fruits, counts,color=barcolor)
# 내용[1].barh(fruits, counts,color=barcolor)
# plt.show()

import matplotlib.pyplot as plt
hight = ["130cm", "140cm", "150cm", "160cm","170cm"]
barcolor=["darkred","red","yellow","greenyellow","green"]
counts = [3, 10, 7, 3,2]
창, 내용 = plt.subplots(1,1)
내용.bar(hight, counts,color=barcolor)
plt.show()