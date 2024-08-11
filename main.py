import os.path
import datetime
import pickle

import tkinter as tk  # Import Tkinter for creating the graphical user interface
import cv2  # Import OpenCV for webcam access and image processing
from PIL import Image, ImageTk  # Import PIL for handling and displaying images in Tkinter
import face_recognition  # Import face_recognition for handling face detection and recognition
import util  # Import custom utility functions (assuming you have a util module)


class APP:
    def __init__(self):
        # Initialize the main window
        self.main_window = tk.Tk()
        self.main_window.geometry('1200x520+350+100')  # Set the size and position of the window

        # Create a "Login" button using a custom utility function
        self.login_button_main_window = util.get_button(self.main_window, 'Login', 'gray', self.login, fg='black')
        self.login_button_main_window.place(x=750, y=300)  # Position the "Login" button on the window

        # Create a "Register New User" button using a custom utility function
        self.register_new_user_button_main_window = util.get_button(self.main_window, 'Register New User', 'gray',
                                                                    self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)  # Position the "Register New User" button

        # Create a label to display the webcam feed
        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)  # Position the webcam display label

        # Add the webcam feed to the label
        self.add_webcam(self.webcam_label)

    def add_webcam(self, label):
        # Initialize webcam capture if not already done
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)  # Open webcam (device index 0)

        # Store the label where the webcam feed will be displayed
        self._label = label
        self.process_webcam()  # Start processing the webcam feed

    def process_webcam(self):
        # Capture a frame from the webcam
        ret, frame = self.cap.read()

        # Convert the frame from BGR (OpenCV's default) to RGB (PIL's default)
        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)

        # Convert the frame to a PIL image
        self.most_recent_capture_pil = Image.fromarray(img_)

        # Convert the PIL image to a format that Tkinter can display
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk  # Store the image in the label to prevent it from being garbage collected
        self._label.configure(image=imgtk)  # Update the label with the new image

        # Schedule the function to be called again after 20 milliseconds to refresh the frame
        self._label.after(20, self.process_webcam)



    def login(self):
        pass

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window .geometry('1200x520+370+120')

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Accept', 'gray', self.accept_register_new_user, fg='black')
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Try Again', 'gray', self.try_again_register_new_user, fg='black',)
        self.try_again_button_register_new_user_window.place(x=750, y=400)


        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window,
                                                                'Please, \ninput username:')
        self.text_label_register_new_user.place(x=750, y=70)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()


    def start(self):
        # Start the main event loop of the application, keeping the window open and interactive
        self.main_window.mainloop()



    def accept_register_new_user(self):
        pass


# Entry point of the program
if __name__ == '__main__':
    app = APP()  # Create an instance of the APP class
    app.start()  # Start the application