import cv2
import sys
import filter_Task5 as filter       #File mit allen Methoden zum Filter


class Main(object):

    def __init__(self, pos, boost):
        self.boost = boost
        self.filter = filter.Filter()
        self.position = pos

    def load(self):
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Read the input image
        #img_name = sys.argv[1]
        img_name = "test2.jpg"
        img = cv2.imread(img_name)
        # blur defined areas in a picture
        for p in self.position:
            # Method: apply() from class: Filter
            blured = self.filter.apply(img, [p[0], p[1], p[2], p[3]], [self.boost, self.boost])
        # Convert into grayscale
        gray = cv2.cvtColor(blured, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display the output
        cv2.imwrite('edited_'+img_name, img)
        cv2.imshow('img', img)
        cv2.waitKey()

    # Zusätzliche Methoden
    def moreMethods(self):
        print("Name der Methode muss geändert werden")


if __name__ == '__main__':
    # Hauptprogramm startet mit diesen Zeilen
    # Beispiel mit Filterstufe 1
    m = Main([[817, 73, 177, 177], [600, 144, 154, 154], [365, 166, 156, 156], [68,  184, 163, 163]], 1)
    m.load()

    # Beispiel mit Filterstufe 10
    m2 = Main([[817, 73, 177, 177], [600, 144, 154, 154], [365, 166, 156, 156], [68, 184, 163, 163]], 10)
    m2.load()

    # Beispiel mit Filterstufe 43
    m2 = Main([[817, 73, 177, 177], [600, 144, 154, 154], [365, 166, 156, 156], [68, 184, 163, 163]], 43)
    m2.load()
