import keyboard
import pyautogui


def mouse_click(x, y):
  pyautogui.click(x, y)

def wait_to_start(end_flag):
  print('Press S to start.')
  keyboard.wait('s')

  print('Started.')
  print('Press F to finish.')

  keyboard.add_hotkey('f', lambda: _set_end_flag(end_flag))

def _set_end_flag(end_flag):
  end_flag[0] = True
