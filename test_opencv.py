#! /usr/bin/env python3

import cv2
import numpy as np

def main():
    img = cv2.imread('dori.jpg')
    # cv2.imwrite('dori_cp.jpg', img)
    # img2 = cv2.imread('dori_cp.jpg')

    # print(np.array_equal(img, img2))

    # print(type(img))
    # print(type(img2))
    # print(img.shape)
    # print(img2.shape)
    # print(img.dtype)
    # print(img2.dtype)

    # cv2.imshow('dori', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # img_diff = img.astype(int) - img2.astype(int)
    # print(img_diff.max())
    # print(img_diff.min())

    # img_diff_abs = np.abs(img_diff)
    # print(img_diff_abs.max())
    # print(img_diff_abs.min())
    # cv2.imwrite('dori_diff_abs.jpg', img_diff_abs)

    # img_diff_abs_norm = img_diff_abs / img_diff_abs.max() * 255
    # print(img_diff_abs_norm.max())
    # print(img_diff_abs_norm.min())
    # cv2.imwrite('dori_diff_abs_norm.jpg', img_diff_abs_norm)

    # img_diff_bin = (img_diff_abs > 1) * 255
    # cv2.imwrite('dori_diff_bin.jpg', img_diff_bin)

    # img[:, :, (0,1)] = 0
    # img[:, :, (0, 2)] = 0
    # cv2.imwrite('dori_g.jpg', img)
    img[:, :, (1, 2)] = 0
    cv2.imwrite('dori_b.jpg', img)

if __name__ == '__main__':
    main()
