import cv2 as cv


def main(file_path):

    img = cv.imread(file_path)
    cv.imshow("Display window", img)
    k = cv.waitKey(0) # Wait for a keystroke in the window
    
    pass


if __name__ == "__main__":
    
    main()
