import os
import datetime
import subprocess
import tkinter as tk
import cv2
from PIL import Image, ImageTk
from utils import util


class FaceRecognitionApp:
    def __init__(self):
        # Initialize the main application window
        self.setup_main_window()

        # Setup the buttons for login and user registration
        self.setup_buttons()

        # Setup the webcam feed to display in the main window
        self.setup_webcam_feed()

        # Directory to store registered user images
        self.db_dir = '../db'
        os.makedirs(self.db_dir, exist_ok=True)  # Create directory if it doesn't exist

        # Path to the log file for recording attendance
        self.log_path = '../log.txt'

    def setup_main_window(self):
        """Initializes the main application window."""
        self.main_window = tk.Tk()
        self.main_window.geometry('1200x520+350+100')  # Set the window size and position

    def setup_buttons(self):
        """Sets up the login and registration buttons in the main window."""
        # Button for logging in
        self.login_button = util.get_button(self.main_window, 'Login', 'gray', self.login, fg='black')
        self.login_button.place(x=750, y=300)  # Position the login button

        # Button for registering a new user
        self.register_button = util.get_button(self.main_window, 'Register New User', 'gray', self.register_new_user,
                                               fg='black')
        self.register_button.place(x=750, y=400)  # Position the registration button

    def setup_webcam_feed(self):
        """Initializes and displays the webcam feed in the main window."""
        # Label to display the webcam feed
        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)  # Set the position and size of the webcam label

        # Start the webcam and display the feed
        self.add_webcam(self.webcam_label)

    def add_webcam(self, label):
        """Adds the webcam feed to a label in the GUI."""
        self.cap = cv2.VideoCapture(0)  # Open the default webcam (device index 0)
        self._label = label
        self.process_webcam()  # Start processing the webcam feed

    def process_webcam(self):
        """Processes and updates the webcam feed in real-time."""
        ret, frame = self.cap.read()  # Capture a frame from the webcam

        # Convert the frame from BGR (OpenCV default) to RGB (for PIL)
        self.most_recent_capture_arr = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Update the label with the processed frame
        self.update_webcam_feed()

    def update_webcam_feed(self):
        """Updates the GUI with the latest webcam frame."""
        pil_img = Image.fromarray(self.most_recent_capture_arr)  # Convert the frame to a PIL image
        imgtk = ImageTk.PhotoImage(image=pil_img)  # Convert the PIL image to a format that Tkinter can display
        self._label.imgtk = imgtk  # Prevent the image from being garbage collected
        self._label.configure(image=imgtk)  # Update the label with the new image

        # Schedule the function to be called again after 20 milliseconds for continuous updates
        self._label.after(20, self.process_webcam)

    def login(self):
        """Handles the user login by capturing a frame and checking it against the database."""
        unknown_img_path = './.tmp.jpg'

        # Save the most recent frame as a temporary image
        cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)

        # Run face recognition to identify the person in the image
        output = subprocess.check_output(['face_recognition', self.db_dir, unknown_img_path])
        name = output.decode('utf-8').split(',')[1].strip()  # Extract the name from the output
        print(name)  # Print the recognized name for debugging

        # Check if the face was recognized and handle accordingly
        if name in ['unknown_person', 'no_persons_found']:
            util.msg_box('Unknown person found', "Unknown User, Please register new user or try again.")
        else:
            util.msg_box('Welcome Back!', f"Welcome Back {name}!")

            # Log the attendance with the current timestamp
            with open(self.log_path, 'a') as f:
                f.write(f'{name},{datetime.datetime.now()}\n')

        os.remove(unknown_img_path)  # Remove the temporary image

    def register_new_user(self):
        """Opens a new window for registering a new user."""
        self.register_window = tk.Toplevel(self.main_window)
        self.register_window.geometry('1200x520+370+120')  # Set the window size and position

        # Setup the registration window with relevant buttons and input fields
        self.setup_register_window()

    def setup_register_window(self):
        """Sets up the components of the user registration window."""
        # Button to accept and save the new user's registration
        self.accept_button = util.get_button(self.register_window, 'Accept', 'gray', self.accept_new_user, fg='black')
        self.accept_button.place(x=750, y=300)  # Position the accept button

        # Button to try capturing the image again
        self.try_again_button = util.get_button(self.register_window, 'Try Again', 'gray', self.try_again, fg='black')
        self.try_again_button.place(x=750, y=400)  # Position the try again button

        # Label to display the captured image
        self.capture_label = util.get_img_label(self.register_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)  # Position the capture label

        # Display the captured image in the label
        self.add_img_to_label(self.capture_label)

        # Text entry for the new user's username
        self.username_entry = util.get_entry_text(self.register_window)
        self.username_entry.place(x=750, y=150)  # Position the username entry field

        # Label to prompt the user to enter their username
        self.text_label = util.get_text_label(self.register_window, 'Please, \ninput username:')
        self.text_label.place(x=750, y=70)  # Position the prompt label

    def try_again(self):
        """Closes the registration window to allow the user to try capturing the image again."""
        self.register_window.destroy()  # Close the registration window

    def add_img_to_label(self, label):
        """Displays the most recent webcam capture in the specified label."""
        imgtk = ImageTk.PhotoImage(
            image=Image.fromarray(self.most_recent_capture_arr))  # Convert to Tkinter image format
        label.imgtk = imgtk  # Prevent the image from being garbage collected
        label.configure(image=imgtk)  # Update the label with the new image

        # Store the captured image for later use during registration
        self.register_capture = self.most_recent_capture_arr.copy()

    def accept_new_user(self):
        """Saves the new user's information and image to the database."""
        name = self.username_entry.get(1.0, "end-1c").strip()  # Get and clean the username input
        cv2.imwrite(os.path.join(self.db_dir, f'{name}.jpg'), self.register_capture)  # Save the image in the database

        util.msg_box('Success!', "User Was Registered Successfully!")  # Show a success message
        self.register_window.destroy()  # Close the registration window

    def start(self):
        """Starts the main event loop of the application."""
        self.main_window.mainloop()


# Entry point of the program
if __name__ == '__main__':
    app = FaceRecognitionApp()  # Create an instance of the app
    app.start()  # Start the application