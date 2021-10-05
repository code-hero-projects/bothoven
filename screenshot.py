import numpy
from mss import mss


def get_screenshot(top, left, height, width) -> numpy.ndarray:
  with mss() as sct:
    monitor = { "top": top, "left": left, "height": height, "width": width }
    screenshot_image = sct.grab(monitor)

    return numpy.array(screenshot_image)
