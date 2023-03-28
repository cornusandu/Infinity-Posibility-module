import time
from typing import Optional, Callable
from asyncio.windows_events import NULL
from turtle import *
import random
def wait(timer=1, repeats=1):
  for i in range(repeats):
      time.sleep(timer)
def end_script():
  print('_______________________')
  print('Made with "Infinity-Posbility" module.')
  exit()
def draw_squares(Pattern=False,times=10, size=30):
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
def log(log="Hello world!", print: Optional[bool] = None, list: Optional[bool] = None, returner: Optional[bool] = None):
  if print is not None:
    print(log)
  elif list is not None:
    list1 = []
    list1.append(log)
    list1.purpose = "logged-list"
    return list1
  else:
    return log

# Default code if ran as a program:
if __name__ == '__main__':
  print("Reminder: The code is supposed to be used as a module!")
  draw_squares(True,15)