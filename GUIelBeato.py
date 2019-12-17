import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np
from tkinter import filedialog
from tkinter import messagebox


class Filter(object):
    ''' Filter class to change or transform faces in an image so the opencv face dedector can't not dedect anymore'''
    # Autor: Beat Furrer
    # Date: November / December 2019
    def __init__(self):
        # Constructor
        self.name = "Beat Furrer"

    def optimum(self, image):
        ''' Not in use - work in procress'''
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        optimal_values = []
        for d in range(80):
            for h in range(230, 256):
                test = self.beat_Filter(image, h, d)
                faces = face_cascade.detectMultiScale(test, 1.1, 4)
                if len(faces) == 0:
                    optimal_values.append((h, d))
        print(min(sorted(optimal_values)))

    def applyBlur(self, faces, coordinates, boost, filterOption):
        '''
        Applies a blur filter to the specified image areas
        :param image: complet image
        :param coordinates: areas to be blurred
        :param filterOption: which filter is choose by the user
        :return: new image with the blured areas
        '''
        # self.optimum(image)
        new_face = faces
        x, y, w, h = coordinates
        crop_face = faces[y:y + h, x:x + w]

        if filterOption == 1:
            blur_face = cv2.blur(crop_face, (15, 15))
        elif filterOption == 2:
            blur_face = self.shiftPixels(crop_face)
        elif filterOption == 3:
            blur_face = self.applyGuissian(crop_face, 5, 20)
        elif filterOption == 4:
            blur_face = self.applyMasterFilter(crop_face)
        # blur_face = self.applyInvert(crop_face, 0)
        new_face[y:y + h, x:x + w] = blur_face
        return new_face

    def applyInvert(self, faces):
        ''' Not in Use
        :param faces:
        :return: inverted faces
        '''
        dark = 100
        bright = 180
        newfaces = faces
        for i in range(1, faces.shape[0]):
            for j in range(1, faces.shape[1]):
                if i % 1 == 0 and j % 1 == 0:
                    if int(faces[i, j]) > bright and int(faces[i, j]) > bright and \
                            int(faces[i, j]) > bright:
                        newfaces[i, j] = 141
                    if int(faces[i, j]) < dark and int(faces[i, j]) < dark and \
                            int(faces[i, j]) < dark:
                        newfaces[i, j] = 255
                j += 1
            i += 1
        return newfaces

    def applyMasterFilter(self, faces, dark=90, bright=200):
        '''
        Mirror the darkerparts to brighter parts and do the same for the brighter pixels.
        :param faces: image from a face on the picture
        :param dark: all pixel darker then this treshold mirror on 255/2. 
        :param bright: all pixel brighter then this treshold mirror on 255/2. 
        :return: face image with the opposit of brighter and darker parts
        '''
        dark = dark
        bright = bright
        levelBlack = 285
        levelWhite = 235
        newImage = faces
        for i in range(1, faces.shape[0]-1):
            for j in range(1, faces.shape[1]-1):
                # possiblity to change the ratio of the used pixels, every one by 1
                if i % 1 == 0 and j % 1 == 0:
                    currPix = newImage[i, j]
                    if int(currPix) > bright:
                        newImage[i, j] = levelBlack - currPix
                        continue
                    if int(currPix) < dark:
                        newImage[i, j] = levelWhite - currPix
                j += 1
            i += 1
        return newImage

    def applyGuissian(self, faces, mean, deviation):
        '''
        Gauissian filter for coloured pictures
        :param faces: image from a face on the picture
        :param mean: mean value of the Gaussian distribuation
        :param deviation: dev value of the Gaussian distribution
        :return: image with pixel with normal distribuation
        '''
        try:
            row, col, ch = faces.shape
        except:
            row, col = faces.shape
        ch = 3
        noisy = np.zeros((row, col, ch), np.uint8)
        gauss = np.random.normal(mean, deviation, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        gauss = cv2.convertScaleAbs(gauss)
        noisy = cv2.add(faces, gauss)
        noisy = faces + gauss
        return noisy

    def shiftPixels(self, crop_face):
        '''
        Simple changing of pixel, every second pixel will be black
        :param crop_face: image from a face on the picture
        :return: image of face black doted
        '''
        diagonale = 0
        for i in range(1, crop_face.shape[0]):
            for j in range(1, crop_face.shape[1]):
                if j % 2 == 0 and i % 2 == 0:       # diagonale < j für Dreiecke
                    for ch in range(0,3):
                        crop_face[i, j][ch] = 255
                j += 1
            i += 1
            diagonale += 1
        return crop_face


class GUI(object):
    ''' User Interface with tkinter for load, dedect and blur or filter faces '''
    # Autor: Beat Furrer
    # Autor: 13.12.19
    def __init__(self, window, window_title):
        '''
        Constructor method for the GUI
        :param window: tkinker object
        :param window_title: Name of the window
        '''
        self.window = window
        self.window.title(window_title)
        self.canvas = None
        self.f = Filter()

        self.v = tkinter.IntVar()
        self.v.set(4)  # initializing the choice, i.e. Master Filter
        self.intense = 10

        # Frames for buttons, radiobuttons and menu
        frame_btn = tkinter.Frame(self.window)
        frame_rb = tkinter.Frame(self.window)
        frame_menu = tkinter.Frame(self.window)

        # Button that lets the user blur/transform/change the faces
        btn_dedect=tkinter.Button(frame_btn, text="Dedecte", width=30, command=self.dedect)
        btn_applyOnFaces=tkinter.Button(frame_btn, text="Apply filter", width=30, command=self.applyOnFaces)
        btn_load_image=tkinter.Button(frame_menu, text="Load Image", width=30, command=self.load_image)
        btn_clear=tkinter.Button(frame_menu, text="Clear filter & dedectors", width=30, command=self.clearFilterAndDedection)

        # Packing buttons
        btn_dedect.pack(fill=tkinter.X, expand=True)
        btn_load_image.pack(side=tkinter.RIGHT, expand=True)
        btn_applyOnFaces.pack(fill=tkinter.X, expand=True)
        btn_clear.pack(side=tkinter.RIGHT, expand=True)

        # Radiobuttons for choose some filter method
        rb1 = tkinter.Radiobutton(frame_rb, text="Bluring", padx=20, variable=self.v, value=1)
        rb2 = tkinter.Radiobutton(frame_rb, text="Shift Pixel", padx=20, variable=self.v, value=2)
        rb3 = tkinter.Radiobutton(frame_rb, text="Guissan Filter", padx=20, variable=self.v, value=3)
        rb4 = tkinter.Radiobutton(frame_rb, text="Master Filter", padx=20, variable=self.v, value=4)

        # Packing radiobuttenx
        rb1.pack(side=tkinter.RIGHT)
        rb2.pack(side=tkinter.RIGHT)
        rb3.pack(side=tkinter.RIGHT)
        rb4.pack(side=tkinter.RIGHT)

        # Packing frames
        frame_btn.pack(anchor=tkinter.N, fill=tkinter.X)
        frame_menu.pack(anchor=tkinter.N, fill=tkinter.X)
        frame_rb.pack(anchor=tkinter.N)

        self.load_image()

        self.window.mainloop()

    def load_image(self):
        ''' Load any image out of the directory '''
        if self.canvas != None:
            self.canvas.destroy()

        self.image_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.origin = self.reload_origin_image(cv2.imread(self.image_path))
        # Resize image if it's too big
        if self.origin[1].shape[0] > 560:
            self.origin = (self.resize_image(self.origin[0]), self.resize_image(self.origin[1]))
            self.cv_face = self.origin[1]
        else:
            # Load an image using OpenCV
            self.cv_face = cv2.cvtColor(cv2.imread(self.image_path), cv2.COLOR_BGR2RGB)
        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, channel = self.cv_face.shape
        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack(anchor=tkinter.NW)
        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_face))
        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def clearFilterAndDedection(self):
        ''' Delete any changes on the picture and load the origin '''
        self.origin = self.reload_origin_image(cv2.imread(self.image_path))
        # Load an image using OpenCV
        self.cv_face = cv2.cvtColor(cv2.imread(self.image_path), cv2.COLOR_BGR2RGB)
        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_face))
        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def reload_origin_image(self, origin):
        ''' Reload the orignal image'''
        in_gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
        in_color = cv2.cvtColor(origin, cv2.COLOR_BGR2RGB)
        return in_gray, in_color

    def applyOnFaces(self):
        ''' Use filter on the image '''
        self.face = self.origin[0]
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Detect faces
        faces = face_cascade.detectMultiScale(self.face, 1.1, 4)
        # Feedback to the user if a picture without any face
        self.feedback_user("No faces dedected - Maybe a image without any face, or already blured!", faces)
        # blur defined areas in a picture
        for (x, y, w, h) in faces:
            # Method: apply() from class: Filter
            if self.v.get() == 3 or 2:
                self.cv_face = self.f.applyBlur(self.origin[1], [x, y, w, h], 1, self.v.get())
            else:
                self.cv_face = self.f.applyBlur(self.origin[0], [x, y, w, h], 1, self.v.get())

        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_face))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def dedect(self):
        ''' Dedection of faces on the image, if there are any, otherwise create a message box information '''
        self.face = self.cv_face
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Detect faces
        faces = face_cascade.detectMultiScale(self.face, 1.1, 4)

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(self.face, (x, y), (x + w, y + h), (255, 0, 0), 2)

        self.feedback_user("No faces dedected - the filter is to good!", faces)

        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.face))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def feedback_user(self, error_Msg, faces):
        ''' if the facededector dedect no faces, get the system a feedback to the user '''
        if len(faces) == 0:
            messagebox.showinfo("Face dedector 2.0 - MATH101", error_Msg)

    def resize_image(self, image):
        img = image
        ratio = 600 / image.shape[0]
        return cv2.resize(img, None, fx = ratio, fy=ratio, interpolation = cv2.INTER_LINEAR)

# Create a window and pass it to the Application object
GUI(tkinter.Tk(), "Face dedection with Tkinter and OpenCV - by Beat Furrer")