import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from tkinter import filedialog
from tkinter import messagebox

class Filter(object):
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
        blur_img = self.applyMasterFilter(crop_img)
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

    def applyMasterFilter(self, image, dunkel=90, hell=200):
        dunkel = dunkel
        hell = hell
        levelBlack = 285
        levelWhite = 235
        newImage = image
        for i in range(1, image.shape[0]-1):
            for j in range(1, image.shape[1]-1):
                if i % 1 == 0 and j % 1 == 0:
                    currPix = newImage[i, j]
                    if int(image[i, j]) > hell:
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


class App(object):
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.canvas = None
        self.f = Filter()

        # Button that lets the user blur the image
        self.btn_dedect=tkinter.Button(window, text="Dedecte", width=30, command=self.dedect)
        self.btn_filter_faces=tkinter.Button(window, text="Apply filter", width=30, command=self.filter_faces)
        self.btn_load_image=tkinter.Button(window, text="Load Image", width=30, command=self.load_image)

        self.btn_dedect.pack(fill=tkinter.X, expand=True)
        self.btn_load_image.pack(fill=tkinter.X, expand=True)
        self.btn_filter_faces.pack(fill=tkinter.X, expand=True)

        self.load_image()

        self.window.mainloop()

    # Callback for the "Blur" button
    def blur_image(self):
        self.cv_img = cv2.blur(self.cv_img, (3, 3))
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def load_image(self):
        if self.canvas != None:
            self.canvas.destroy()

        image_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        # Load an image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)
        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width = self.cv_img.shape
        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack(anchor=tkinter.NW)
        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def filter_faces(self):
        self.img = self.cv_img
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Detect faces
        faces = face_cascade.detectMultiScale(self.img, 1.1, 4)
        # blur defined areas in a picture
        for (x, y, w, h) in faces:
            # Method: apply() from class: Filter
            blured = self.f.applyBlur(self.img, [x, y, w, h], 1)

        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def dedect(self):
        self.img = self.cv_img
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Detect faces
        faces = face_cascade.detectMultiScale(self.img, 1.1, 4)

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(self.img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if len(faces) == 0:
            messagebox.showinfo("Face dedector", "No faces dedected - the filter is to good!")

        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)



# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")