#입력 한 두 값의 합을 출력

num1 = input("작은 값")
num2 = input("큰 값")

min = int(num1)
max = int(num2)

result = 0
for i in range(min, max+1):
    result += i
    
print("합 : ", result)