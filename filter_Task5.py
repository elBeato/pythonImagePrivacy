import cv2

'''
'''
class Filter:
    '''
    Filter Klasse
    '''
    def __init__(self):
        # Constructior
        self.name = "Beat Furrer"

    def apply(self, image, coordinates, boost):
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
        blur_img = cv2.blur(crop_img, (boost[0], boost[1]))
        new_image[y:y + h, x:x + w] = blur_img
        return new_image

    def apply2_0(self):
        return "tut noch nichts"

