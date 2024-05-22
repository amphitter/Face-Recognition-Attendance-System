# Face Recognition Attendance System

This project is a face recognition attendance system using Python, OpenCV, face_recognition, and Firebase. It captures images of students, encodes their faces, stores the encodings and student information in Firebase, and updates attendance records based on real-time face recognition.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
  - [EncodeGernator.py](#encodegernatorpy)
  - [AddDatatoDatabase.py](#adddatatodatabasepy)
  - [main.py](#mainpy)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload student images and encode faces.
- Store face encodings and student information in Firebase.
- Capture real-time webcam feed and recognize faces.
- Retrieve student information and update attendance records in Firebase.
- Display real-time attendance information on screen.

## Prerequisites

- Python 3.7+
- Anaconda
- Firebase account with Realtime Database and Storage enabled
- OpenCV
- face_recognition library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/amphitter/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. Create a new Anaconda environment and activate it:

   ```bash
   conda create -n face_recognition python=3.8
   conda activate face_recognition
   ```

3. Install the required packages:

   ```bash
   pip install opencv-python
   pip install face-recognition
   pip install firebase-admin
   pip install numpy
   pip install cvzone
   ```

4. Set up Firebase:
   - Download your serviceAccountKey.json from Firebase Console and place it in the project directory.
   - Ensure your Firebase project has a Realtime Database and Storage bucket enabled.

## Usage

1. **Encode Student Images**:
   - Place student images in the Images folder. The images should be named with the student ID (e.g., 123456.png).
   - Run EncodeGernator.py to upload images to Firebase Storage and create face encodings:

     ```bash
     python EncodeGernator.py
     ```

2. **Add Student Data to Database**:
   - Modify AddDatatoDatabase.py to include your student data.
   - Run AddDatatoDatabase.py to upload data to Firebase Realtime Database:

     ```bash
     python AddDatatoDatabase.py
     ```

3. **Run the Face Recognition System**:
   - Ensure your webcam is connected.
   - Run main.py to start the face recognition system and update attendance records in real-time:

     ```bash
     python main.py
     ```

## Code Overview

### EncodeGernator.py

This script uploads student images to Firebase Storage and encodes faces.

- Initializes Firebase app with credentials.
- Reads images from the Images folder.
- Encodes the faces and saves the encodings to EncodeFile.p using pickle.

### AddDatatoDatabase.py

This script adds student data to Firebase Realtime Database.

- Initializes Firebase app with credentials.
- Defines student data in a dictionary.
- Uploads the data to the Realtime Database.

### main.py

This script captures real-time webcam feed and performs face recognition.

- Initializes Firebase app with credentials.
- Loads face encodings from EncodeFile.p.
- Captures frames from the webcam.
- Recognizes faces and retrieves student information from the Realtime Database.
- Updates attendance records and displays student information on the screen.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.
```
This should maintain the formatting when you copy it into your README file. Let me know if you need any further adjustments!
