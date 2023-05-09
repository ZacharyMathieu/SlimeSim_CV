import cv2
import numpy as np

image: np.matrix = np.zeros((200, 200), dtype=np.uint8)

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
