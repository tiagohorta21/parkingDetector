import cv2

image = cv2.imread("Result/first_result.jpg")

# Add parking lot numbers
cv2.putText(image, "1", (1150, 465), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "2", (1105, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "3", (1065, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "4", (1030, 95), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

# Add total parking spots
total_available_spots = "20"
cv2.putText(image, "Total Available Spots:", (10, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, total_available_spots, (350, 703), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

# Add parking lane 2 spots
parking_lane_2_spots = "20"
cv2.putText(image, "Parking Lane 2 Spots:", (10, 650), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, parking_lane_2_spots, (368, 653), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

cv2.imshow("Parking lot", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
