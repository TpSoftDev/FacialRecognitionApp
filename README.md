# FaceRecognitionAPP

## Overview

This project is a **Face Recognition Attendance System** implemented in Python. The system captures real-time video from a webcam, processes the video feed to detect faces, and allows users to log in or register as new users using facial recognition. The application is built using various technologies such as OpenCV, face_recognition, and Tkinter, making it both a powerful and user-friendly tool for managing attendance based on facial recognition.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Future Improvements](#future-improvements)
7. [Contributing](#contributing)
8. [License](#license)

## Features

- **Real-Time Face Recognition**: Captures video feed from a webcam and recognizes faces in real-time.
- **User Registration**: Allows new users to register their face in the system for future recognition.
- **Login System**: Existing users can log in using facial recognition.
- **Attendance Logging**: Automatically logs the attendance of recognized users with timestamps.
- **Graphical User Interface (GUI)**: User-friendly interface created using Tkinter.
- **Temporary Image Handling**: Captures and processes images temporarily for login and registration.

## Technologies Used

- **Python**: Core programming language used for the application.
- **OpenCV**: Used for capturing video feed from the webcam and processing images.
- **face_recognition**: A Python library built on dlib’s state-of-the-art face recognition to recognize and compare faces.
- **Tkinter**: Used for creating the graphical user interface (GUI) for the application.
- **PIL (Pillow)**: Python Imaging Library used to handle and display images in the GUI.
- **Subprocess**: Python module used to interact with command-line tools like `face_recognition`.

## Installation

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**: Download and install Python from [python.org](https://www.python.org/downloads/).

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance-system.git
   cd face-recognition-attendance-system
   ```

2. **Install Required Python Packages**

   Create a `requirements.txt` file with the following content:

   ```
   opencv-python
   face_recognition
   pillow
   ```

   Install the dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Face Recognition Command-Line Tool**

   Follow the instructions provided in the [face_recognition GitHub repository](https://github.com/ageitgey/face_recognition#installation) to set up the command-line tool necessary for face recognition.

4. **Create Necessary Directories**

   The application expects a directory for storing user images. Create this directory if it does not exist:

   ```bash
   mkdir db
   ```

## Usage

1. **Run the Application**

   Execute the main script to start the application:

   ```bash
   python app.py
   ```

2. **Application Features**

   - **Login**: Click the "Login" button to perform facial recognition and log in.
   - **Register New User**: Click the "Register New User" button to capture and save new user facial data.

## Project Structure

- `app.py`: Main script that contains the application logic and user interface.
- `util.py`: Custom utility functions used across the application.
- `requirements.txt`: List of required Python packages.
- `db/`: Directory where registered user images are stored.
- `log.txt`: Log file where attendance records are stored.

## Future Improvements

- **Accuracy Enhancement**: Improve the accuracy of face recognition algorithms.
- **User Management**: Add features for updating or deleting user data.
- **Security**: Implement additional security measures for storing facial data.
- **Performance Optimization**: Enhance real-time processing performance.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Replace `https://github.com/yourusername/face-recognition-attendance-system.git` with your actual GitHub repository URL. Make sure to include a `requirements.txt` file and a `LICENSE` file in your project directory.
