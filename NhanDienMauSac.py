# Nguyễn Xuân Bảo
# Mssv: 17552520201600013
import numpy as np
import cv2
# Xuất Video từ webcam
webcam = cv2.VideoCapture(0)
# Sử dụng vòng lặp
while (1):
    #Đọc video từ wedcam vào biến imageFrame
    _, imageFrame = webcam.read()
    # Đảo màu imageFrame thành BGR(RGB color space) to HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    # Đặt khoảng màu để nhận dạng
    # Định nghĩa các mặt nạ màu
    red_lower = np.array([150, 30, 80], np.uint8)  #lower_red = np.array([160,20,70])
    red_upper = np.array([180,255,255], np.uint8) #upper_red = np.array([180,255,255])
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    yellow_lower = np.array([22, 93, 0], dtype="uint8")
    yellow_upper = np.array([45, 255, 255], dtype="uint8")
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

    # Sử dụng 1 Kernal 5x5 để xử lý từng màu giữa imageFrame và Mask để xác định và phát hiện màu cụ thể
    kernal = np.ones((5, 5), "uint8")
    # Màu đỏ
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame,mask=red_mask)
    # Màu xanh lá
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(imageFrame, imageFrame,mask=green_mask)
    # Màu xanh dương
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,mask=blue_mask)
    # Màu vàng
    yellow_mask = cv2.dilate(yellow_mask, kernal)
    res_yellow = cv2.bitwise_and(imageFrame, imageFrame,mask=yellow_mask)


    # Tạo 1 cái Contour để follow theo màu đỏ
    contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),(x + w, y + h),(0, 0, 255), 2)
            cv2.putText(imageFrame, "RED", (x, y),cv2.FONT_HERSHEY_SIMPLEX, 1.0,(0, 0, 255))

        # Tạo 1 cái Contour để follow theo màu xanh lá
    contours, hierarchy = cv2.findContours(green_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),(x + w, y + h),(0, 255, 0), 2)
            cv2.putText(imageFrame, "GREEN", (x, y),cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 0))

        # Tạo 1 cái Contour để follow theo màu xanh dương
    contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),(x + w, y + h),(255, 0, 0), 2)
            cv2.putText(imageFrame, "BLUE", (x, y),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255, 0, 0))

        #   Tạo 1 cái Contour để follow theo màu vàng
    contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),(x + w, y + h),(0, 255, 255), 2)
            cv2.putText(imageFrame, "YELLOW", (x, y),cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 255))

        # Xuất Frame với tên Nguyễn Xuân Bảo và ấn phím q để thoát Frame
    cv2.imshow("NGUYEN XUAN BAO", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break