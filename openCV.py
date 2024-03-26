import cv2
#顯示出彩色照片
image = cv2.imread('image.jpg')
if image is not None:
  cv2.imshow('Image',image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
else:
  print("無法讀取影像")
