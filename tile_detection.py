import threading

from input import mouse_click


def detect_and_click_on_tiles(image, vertical_pixels, tiles_to_search, top, left):
  for vertical_pixel in vertical_pixels:
    thread = threading.Thread(target=_detect_tile_in_row, args=(image, vertical_pixel, tiles_to_search, top, left), daemon=True)
    thread.start()

def _detect_tile_in_row(image, vertical_pixel, tiles_to_search, top, left):
  for line in image:
    current_pixel = line[vertical_pixel]
    if _has_tile(current_pixel, tiles_to_search):
      (screen_x, scrren_y) = left + vertical_pixel, top
      mouse_click(screen_x, scrren_y)
      return

def _has_tile(current_pixel, tiles_to_search):
  current_red, current_green, current_blue, current_alpha = current_pixel
  for tile in tiles_to_search:
    expected_red, expected_green, expected_blue = tile
    if (current_red == expected_red and current_green == expected_green and current_blue == expected_blue):
      return True

  return False
