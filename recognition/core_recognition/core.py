# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2

def position(x, y):
	width = max(x) - min(x)
	height = max(y) - min(y)
	if width > height:
		print('Horizontal orientation')
	elif width < height:
		print('Vertical orientation')
	else:
		print('45 deg, both methods will work')


# load the photo
image = cv2.imread("ver.jpg")

# pre-process the image by resizing it, converting it to
# graycale, blurring it, and computing an edge map
image = imutils.resize(image, height=500)
cv2.imshow('original', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)

cv2.imshow('edged_ver', edged)

cropped = edged[160:275, 140:255]
output = image[160:275, 140:255]
cv2.imshow('cropped_ver', cropped)

# find contours in the edge map, then sort them by their size in descending order
cnts = cv2.findContours(cropped.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_NONE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
displayCnt = None
#print(cnts[0])
cv2.drawContours(output, cnts[0], -1, (0, 255, 0), 3)
cv2.imshow('contours', output)

x = []
y = []
for elem in cnts[0]:
	x.append(elem[0][0])
	y.append(elem[0][1])
#print(x)
#print(y)
#print(cnts[0][0])
position(x, y)


cv2.waitKey(0)
cv2.destroyAllWindows()
