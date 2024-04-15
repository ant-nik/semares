""" 
https://docs.opencv.org/4.x/d9/db7/tutorial_py_table_of_contents_calib3d.html
"""
from controller import Robot
import cv2

robot = Robot()

timestep = int(robot.getBasicTimeStep())

rcamera = robot.getDevice("right camera")
lcamera = robot.getDevice("left camera")

rcamera.enable(timestep)
lcamera.enable(timestep)

i = 0

while (robot.step(timestep) != -1):
  # Read the sensors, like:
  rcamera.saveImage(filename=f"image{i}_r.jpg", quality=50)
  lcamera.saveImage(filename=f"image{i}_l.jpg", quality=50)
  i = i + 1
  pass
  

# Enter here exit cleanup code