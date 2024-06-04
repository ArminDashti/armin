from PIL import Image, ImageDraw


def draw_line(img, start_point=(50, 50), end_point=(400, 400), color='black', width=2):
  draw = ImageDraw.Draw(img)
  draw.line([start_point, end_point], fill=color, width=width)
  return img
