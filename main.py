import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("test.jpg")

# several steps need to do
# turn it into grayscale -> why? -> because the algorithm that we are going to use is works better with single channel color, like grayscale. i think the founder of the algorithm is suzuki abe, so we can call it suzuki abe algorithm ahahaha.
# so the second step we have to apply thresholding, to convert the grayscale, to black and white. kinda weird right, black and white after grayscale, maybe i just dont understand. buy we can also use canny to find edges instead of thresholding.
# and the third step, just apply the algorithm.

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
find_edges = cv.Canny(img, 30, 200)
contour, hirearchy = cv.findContours(find_edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(img, contour, -1, (0, 255, 0), 3)
cv.imwrite("img_contoured.jpg", img)
cv.destroyAllWindows()
