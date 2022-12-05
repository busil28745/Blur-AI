import cv2

txt = True
direc = 'test'
elseDir = 'elseDir'

i = (direc + 'labels' if txt else elseDir)
print(i)

x=28
y=309
w=158-28
h=469-309

rate = 15
blur_im = cv2.imread('C:/Users/bsbbc/project_ai/yolov5-master/data/custom_image/iu_test.jpg')
roi = blur_im[y:y+h, x:x+w]
roi = cv2.resize(roi, (w//rate, h//rate))
roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA) 
blur_im[y:y+h, x:x+w] = roi
cv2.imshow("test", blur_im)
cv2.waitKey(0)
cv2.destroyAllWindows()