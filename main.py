import tkinter as tk
import util
import face_recognition


class APP:
    def __init__(self):
        # Create Main window - WebCam
        self.main_window = tk.Tk()
        self.main_window.geometry('1200x520+350+100')

        # Login Button
        self.login_button_main_window = util.get_button(self.main_window, 'Login', 'green', self.login)
        # Placement of button
        self.login_button_main_window.place(x=750, y=300)

        # Register New User Button
        self.register_new_user_button_main_window = util.get_button(self.main_window, 'Register New User', 'gray',
                                                                    self.register_new_user, fg='black')
        # Placement of button
        self.register_new_user_button_main_window.place(x=750, y=400)

    # Command Function - Login
    def login(self):
        pass

    # Command Function - Register New User
    def register_new_user(self):
        pass

    def start(self):
        # Calls Main Window when we start the application
        self.main_window.mainloop()


if __name__ == '__main__':
    app = APP()
    app.start()
