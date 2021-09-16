#! /usr/bin/env python3

import cv2
import numpy as np

def main():
    img = cv2.imread('dori.jpg')
    cv2.imwrite('dori_cp.jpg', img)
    img2 = cv2.imread('dori_cp.jpg')

    print(np.array_equal(img, img2))


    print(type(img))
    print(type(img2))
    print(img.shape)
    print(img2.shape)
    print(img.dtype)
    print(img2.dtype)


    # cv2.imshow('dori', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
