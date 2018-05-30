
#http://freesugar.tistory.com/50?category=757582
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 이미지를 읽어옴
img = cv2.imread('mypic.jpg', 0)

# 푸리에 변환 하고 이런저런 맞춤
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

# 작은 마스크를 만들어서 푸리에 변환한 영역의 가운데를 지워 버림(하이패스 필터)
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
f_ishift = np.fft.ifftshift(fshift)

# 다시 이미지로 역변환
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# 그림으로 보여줌.
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back, cmap='gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])

plt.show()

print("ok")