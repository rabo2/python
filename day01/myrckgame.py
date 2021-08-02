import random
from _ast import Or
mine = ""
com = ""
result = ""


mine = input("가위 바위 보 입력")
arr = ["가위","바위","보"]
index = random.randint(1, 3)
com = arr[index]


if mine == com :
    print("비김")
elif (mine == "가위" and com =="보") or (mine == "바위" and com == "가위")or (mine == "보" and com == "바위") :
    result = "승리"
else :
    result = "패배"

print(mine)
print(com)
print(result)
