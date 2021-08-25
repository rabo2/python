import cv2

image = cv2.imread("Image/omok.png", cv2.COLOR_BGR2GRAY)

crop_image = []
imgArr= []

for i in range(0,19):
    colorArr=[]
    for j in range(0,19): 
        crop_image = image[i*40:(i*40)+40, j*40:(j*40)+40]

        color = -1

        if crop_image[20][20][1] < 20:
            color = 2
        elif crop_image[20][20][1] > 200:
            color = 1
        else :
            color = 0

        colorArr.insert(j, color)
        
    imgArr.insert(i, colorArr)
    
    
for i in range(0,19) :     
    print(imgArr[i])

