from config import *
from input import wait_to_start
from screenshot import get_screenshot
from tile_detection import detect_and_click_on_tiles


def main():
  end = [False]

  wait_to_start(end)
  _detect_tiles([START_TILE], 0)

  while not end[0]:
    _detect_tiles([REGULAR_TILE, BONUS_TILE], VERTICAL_EXTRA)

  print('Finished.')

def _detect_tiles(tiles, vertical_extra):
  (top, left, height, width) = SCREENSHOT_DIMENSIONS
  image = get_screenshot(top, left, height, width)
  detect_and_click_on_tiles(image, VERTICAL_PIXELS, tiles, top + vertical_extra, left)

if __name__ == '__main__':
  main()
