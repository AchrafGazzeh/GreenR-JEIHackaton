# GreenR

This repository contains code developed by the GreenR team for the JEI Hackaton. The code utilizes computer vision based on `cv2` and `yolov5`, as well as `Qt` code for the dashboard.

## Dependencies

- PyQt5
- serial
- torch
- cv2
- numpy
- pandas

## Description

The code includes a class `Ui_MainWindow` which sets up the user interface for the dashboard. The dashboard displays information about the **type of waste detected** and the **user's name and total points**. The code also includes functions for connecting to a serial device and processing video frames with computer vision.

## Usage

1. Install the dependencies listed above.
2. Run the code to start the dashboard.
3. Connect to a serial device and begin processing video frames to detect and classify waste.
4. View the detected waste type and user information on the dashboard.
