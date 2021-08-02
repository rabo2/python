#1부터 100까지 2의 배수합
result = 0
for i in range(1,100+1):
    if i%2 == 0:
        result += i
        
print("합 : ", result)