import cv2

image = cv2.imread("Result/first_result.jpg")
cv2.putText(image, "1", (1150, 465), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "2", (1105, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "3", (1065, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "4", (1030, 95), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

cv2.imshow("Parking lot", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
