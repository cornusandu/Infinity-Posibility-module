import time
from turtle import *
import random
def wait(timer=1, repeats=1):
  for i in range(repeats):
      time.sleep(timer)
def end_script():
  print('_______________________')
  print('Made with "Infinity-Posbility" module.')
  exit()
def draw_squares(NoPattern=True,times=10, size=30):
  for i in range(times):
        for i in range(4):
            forward(30)
            right(90)
        if Pattern:
          forward(32)
          right(45)
          forward(18)
        else:
          forward(random.randint(20, 45))
          right(random.randint(2, 182))
          forward(random.randint(4, 25))
def get_random_number(min=0, max=10):
    return random.randint(min,max)
