import cv2
import numpy as np


class Filter:
    # Flask:
    # Methoden
    # cv.filte2D(RGB_img, -1, kernel_2)
    def __init__(self):
        # Constructior
        self.name = "Beat Furrer"

    def applyBlur(self, image, coordinates, boost):
        '''
        Applies a blur filter to the specified image areas
        :param image: complet image
        :param coordinates: areas to be blurred
        :param boost: intensity of the blurdness
        :return: new image with the blured areas
        '''
        new_image = image
        x = coordinates[0]
        y = coordinates[1]
        w = coordinates[2]
        h = coordinates[3]
        crop_img = image[y:y + h, x:x + w]
        blur_img = self.applyInvert(crop_img, 0)
        # blur_img = self.shiftPixels(crop_img)
        # blur_img = cv2.blur(crop_img, (15, 15))
        new_image[y:y + h, x:x + w] = blur_img
        return new_image

    def applyInvert(self, image, coordinates):
        dunkel = 100
        hell = 180
        newImage = image
        for i in range(1, image.shape[0]-1):
            for j in range(1, image.shape[1]-1):
                if i % 1 == 0 and j % 1 == 0:
                    if int(image[i, j][0]) > hell and int(image[i, j][1]) > hell and \
                            int(image[i, j][2]) > hell:
                        newImage[i, j][2] = 141
                        newImage[i, j][1] = 101
                        newImage[i, j][0] = 101
                    if int(image[i, j][0]) < dunkel and int(image[i, j][1]) < dunkel and \
                            int(image[i, j][2]) < dunkel:
                        newImage[i, j, 2] = 255
                        newImage[i, j, 1] = 193
                        newImage[i, j, 0] = 148
                        # nur einen channel: newImage[i, j, ] = 148 (der Channel am schluss 0, 1, 2 einfach leer lassen)
                j += 1
            i += 1
        return image

    def kim_Filter(self):
        pass

    def applyPreventFD(self, image, coordinates, intensity):
        pass

    def shiftPixels(self, crop_img):
        diagonale = 0
        for i in range(1, crop_img.shape[0]):
            for j in range(1, crop_img.shape[1]):
                if j % 2 == 0 and i % 2 == 0:       # diagonale < j für Dreiecke
                    crop_img[i, j][0] = 0
                    crop_img[i, j][1] = 0
                    crop_img[i, j][2] = 0
                j += 1
            i += 1
            diagonale += 1
        return crop_img

