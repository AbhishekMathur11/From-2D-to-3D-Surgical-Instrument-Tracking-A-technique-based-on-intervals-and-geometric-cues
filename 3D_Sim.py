import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

def main():
    imdir = r"path_to_images"
    ext = ['jpg']  # Add image formats here

    with open("action_7.txt", "a") as f:
        files = [file for e in ext for file in glob.glob(f"{imdir}.{e}")]
        i = 0

        for file in files:
            image = cv2.imread(file)
            process_image(image, f, i)
            i += 1

def process_image(image, f, i):
    boundaries = [
        ([720, 0, 0], [720, 0, 0]),
        ([0, 560, 0], [0, 560, 0])
    ]

    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 50, 75, cv2.THRESH_BINARY)[1]
        result = output.copy()
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cntr in contours:
            x, y, w, h = cv2.boundingRect(cntr)
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
            rect = cv2.minAreaRect(cntr)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(result, [box], 0, (0, 191, 255), 2)
            print([box])
            print(f"image {i}, box[0]: {box[0]}, box[1]: {box[1]}, box[2]: {box[2]}, box[3]: {box[3]}, rect[2]: {rect[2]}", file=f)

        cv2.imshow("images", np.hstack([image, result]))
        cv2.waitKey(0)

if __name__ == "__main":
    main()
