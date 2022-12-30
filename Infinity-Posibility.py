import time
from turtle import *
def wait(timer, repeats=0):
  for i in range(repeats):
      time.sleep(timer)
def end_script():
  print('_______________________')
  print('Made with "Ifnity-Posbility" module.')
  exit()
def draw_squares(times=10, size=30):
  for i in range(times):
        for i in range(4):
            forward(30)
            right(90)
        forward(32)
        right(45)
        forward(18)
