import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread(r"C:\Users\Abhishek Raman\Desktop\Abhishek\Recordings\Img_File4\frame0.jpg")
# DISPLAYg
cv2.imshow("Test_Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
[x,y,z]=img.shape


count=0
for i in range(1,x-1):
    for j in range(1,y-1):
        print(img[i,j]) 
        count=count+1
        print(count)