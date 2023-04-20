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
list1 = []
def get_random_number(min=0, max=10):
    return random.randint(min,max)
def log(log="Hello world!", print: Optional[bool] = None, list: Optional[bool] = None, returner: Optional[bool] = None):
  if print is not None:
    print(log)
  elif list is not None:
    global list1
    list2 = []
    list1.append(log)
    list1.purpose = "logged-list"
    list2.append(log)
    list2.purpose = "logged-list"
    return list2
  else:
    return log

# Default code if ran as a program:
if __name__ == '__main__':
  log(log="Reminder: The code is supposed to be used as a module!", print=True)
  draw_squares(True,15)

class Maped:
    def __init__(self, value):
        self.value = value
        self.splitt = None
        
    def split(self, char=';', get=True):
        char = str(char)
        to_return = []
        join = ''
        value = self.value
        for c in value:
            if c != char:
                join += c
            else:
                to_return.append(join)
                join = ''
        to_return.append(join)
        self.splitt = to_return
        if get:
            return to_return
        
    def unsplit(self, char=';', split=None):
        if split is None:
            split = self.splitt
        value = char.join(split)
        self.value = value
        return value
        
    def __str__(self):
        return f"<{self.__class__.__name__} Class: {self.__class__}, data: <value: <{self.value}>, split: <{self.splitt}>>>"
    def __repr__(self):
        return f"{self.__class__.__name__} Class: {self.__class__}, data: <value: <{self.value}>, split: <{self.splitt}>>"
def get_logs_list():
  global list1
  return list1
def clear_logs_list():
  global list1
  list1 = []
