import cv2
import csv
import os

total_found_cars = 0
total_empty_park_spots = 209

total_park_spots_in_lane_1 = 25
found_cars_in_lane_1 = []

total_park_spots_in_lane_2 = 57
found_cars_in_lane_2 = []

total_park_spots_in_lane_3 = 62
found_cars_in_lane_3 = []

total_park_spots_in_lane_4 = 65
found_cars_in_lane_4 = []

image_path = "Result/58.jpg"
image_file = os.path.split(image_path)[-1]

# Import CVS results
with open("Result/Detection_Results.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row["image"] == image_file:
            # Parking lane 1
            if 425 < int(row["ymin"]) < 480 or 425 < int(row["ymax"]) < 480:
                found_cars_in_lane_1.append({"xmin": row["xmin"], "ymin": row["ymin"], "xmax": row["xmax"], "ymax": row["ymax"]})
                total_found_cars = total_found_cars + 1
            # Parking lane 2
            if 276 < int(row["ymin"]) < 360 or 276 < int(row["ymax"]) < 360:
                found_cars_in_lane_2.append({"xmin": row["xmin"], "ymin": row["ymin"], "xmax": row["xmax"], "ymax": row["ymax"]})
                total_found_cars = total_found_cars + 1
            # Parking lane 3
            if 150 < int(row["ymin"]) < 230 or 150 < int(row["ymax"]) < 230:
                found_cars_in_lane_3.append({"xmin": row["xmin"], "ymin": row["ymin"], "xmax": row["xmax"], "ymax": row["ymax"]})
                total_found_cars = total_found_cars + 1
            # Parking lane 4
            if 60 < int(row["ymin"]) < 120 or 60 < int(row["ymax"]) < 120:
                found_cars_in_lane_4.append({"xmin": row["xmin"], "ymin": row["ymin"], "xmax": row["xmax"], "ymax": row["ymax"]})
                total_found_cars = total_found_cars + 1

image = cv2.imread(image_path)

# Add parking lot numbers
cv2.putText(image, "4", (1030, 95), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "3", (1065, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "2", (1105, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "1", (1150, 465), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

# Add parking lane 1 spots
total_parking_lane_1_available_spots = str(total_park_spots_in_lane_1 - len(found_cars_in_lane_1))
cv2.putText(image, "Parking Lane 1 Available Spots:", (10, 530), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, total_parking_lane_1_available_spots, (520, 533), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "Parking Lane 1 Total Spots:", (620, 530), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, str(total_park_spots_in_lane_1), (1070, 533), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

# Add parking lane 2 spots
total_parking_lane_2_available_spots = str(total_park_spots_in_lane_2 - len(found_cars_in_lane_2))
cv2.putText(image, "Parking Lane 2 Available Spots:", (10, 570), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, total_parking_lane_2_available_spots, (520, 573), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "Parking Lane 2 Total Spots:", (620, 570), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, str(total_park_spots_in_lane_2), (1070, 573), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

# Add parking lane 3 spots
total_parking_lane_3_available_spots = str(total_park_spots_in_lane_3 - len(found_cars_in_lane_3))
cv2.putText(image, "Parking Lane 3 Available Spots:", (10, 610), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, total_parking_lane_3_available_spots, (520, 613), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "Parking Lane 3 Total Spots:", (620, 610), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, str(total_park_spots_in_lane_3), (1070, 613), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

# Add parking lane 4 spots
total_parking_lane_4_available_spots = str(total_park_spots_in_lane_4 - len(found_cars_in_lane_4))
cv2.putText(image, "Parking Lane 4 Available Spots:", (10, 650), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, total_parking_lane_4_available_spots, (520, 653), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, "Parking Lane 4 Total Spots:", (620, 650), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, str(total_park_spots_in_lane_4), (1070, 653), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

# Add total parking spots
total_available_spots = str(total_empty_park_spots - total_found_cars)
cv2.putText(image, "Total Available Spots:", (10, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(image, total_available_spots, (350, 703), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

cv2.imshow("Parking lot", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
