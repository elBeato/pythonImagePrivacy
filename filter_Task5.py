import cv2
import numpy as np


class Filter:
    # Flask:
    # Methoden
    # cv.filte2D(RGB_img, -1, kernel_2)
    def __init__(self):
        # Constructior
        self.name = "Beat Furrer"

    def optimum(self, image):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        optimal_values = []
        for d in range(80):
            for h in range(230, 256):
                test = self.beat_Filter(image, h, d)
                faces = face_cascade.detectMultiScale(test, 1.1, 4)
                if len(faces) == 0:
                    optimal_values.append((h, d))
        print(min(sorted(optimal_values)))


    def applyBlur(self, image, coordinates, boost):
        '''
        Applies a blur filter to the specified image areas
        :param image: complet image
        :param coordinates: areas to be blurred
        :param boost: intensity of the blurdness
        :return: new image with the blured areas
        '''
        # self.optimum(image)
        new_image = image
        x = coordinates[0]
        y = coordinates[1]
        w = coordinates[2]
        h = coordinates[3]
        crop_img = image[y:y + h, x:x + w]
        # blur_img = self.applyInvert(crop_img, 0)
        # blur_img = self.shiftPixels(crop_img)
        # blur_img = cv2.blur(crop_img, (15, 15))
        # blur_img = self.applyPreventFD(crop_img)
        blur_img = self.beat_Filter(crop_img)
        new_image[y:y + h, x:x + w] = blur_img
        return new_image

    def applyInvert(self, image):
        dunkel = 100
        hell = 180
        newImage = image
        for i in range(1, image.shape[0]):
            for j in range(1, image.shape[1]):
                if i % 1 == 0 and j % 1 == 0:
                    if int(image[i, j]) > hell and int(image[i, j]) > hell and \
                            int(image[i, j]) > hell:
                        newImage[i, j] = 141
                    if int(image[i, j]) < dunkel and int(image[i, j]) < dunkel and \
                            int(image[i, j]) < dunkel:
                        newImage[i, j] = 255
                j += 1
            i += 1
        return image

    def beat_Filter(self, image, dunkel=90, hell=200):
        dunkel = dunkel
        hell = hell
        levelBlack = 285
        levelWhite = 235
        newImage = image
        for i in range(1, image.shape[0]-1):
            for j in range(1, image.shape[1]-1):
                if i % 1 == 0 and j % 1 == 0:
                    currPix = newImage[i, j]
                    if currPix > hell:
                        newImage[i, j] = levelBlack - currPix
                        continue
                    if int(image[i, j]) < dunkel:
                        newImage[i, j] = levelWhite - currPix
                j += 1
            i += 1
        return image

    def applyPreventFD(self, bild, grundwert=30, abweichung=50):
        try:
            row, col, ch = bild.shape
        except:
            row, col = bild.shape
        ch = 1
        noisy = np.zeros((row, col, ch), np.uint8)
        gauss = np.random.normal(grundwert, abweichung, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        gauss = cv2.convertScaleAbs(gauss)
        noisy = cv2.add(bild, gauss)
        noisy = bild + gauss
        return noisy

    def shiftPixels(self, crop_img):
        diagonale = 0
        for i in range(1, crop_img.shape[0]):
            for j in range(1, crop_img.shape[1]):
                if j % 2 == 0 and i % 2 == 0:       # diagonale < j für Dreiecke
                    crop_img[i, j] = 0
                j += 1
            i += 1
            diagonale += 1
        return crop_img

