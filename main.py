import cv2
import sys
import filter_Task5 as filter       #File mit allen Methoden zum Filter
import calc_diff


class Main(object):
    def __init__(self, imgName, boost):
        self.boost = boost
        self.filter = filter.Filter()
        self.img_name = imgName

    def load(self):
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Read the input image
        #img_name = sys.argv[1]
        img = cv2.imread(self.img_name)
        # Detect faces
        faces = face_cascade.detectMultiScale(img, 1.1, 4)
        # blur defined areas in a picture
        for (x, y, w, h) in faces:
            # Method: apply() from class: Filter
            blured = self.filter.apply(img, [x, y, w, h], [self.boost, self.boost])
        # Convert into grayscale
        gray = cv2.cvtColor(blured, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display the output
        cv2.imwrite('edited_'+self.img_name, img)
        cv2.imshow('img', img)

        # Print error
        print(calc_diff.rms(cv2.imread(self.img_name), img, "image"))
        print(calc_diff.rms(cv2.imread(self.img_name), img, "histogram"))
        cv2.waitKey()

    # Zusätzliche Methoden
    def moreMethods(self):
        print("Name der Methode muss geändert werden")


if __name__ == '__main__':
    # Hauptprogramm startet mit diesen Zeilen
    # Beispiel mit Filterstufe 1
    add = 50
    m = Main("test2.jpg", 1)
    m.load()

    m = Main("test.jpg", 1)
    m.load()