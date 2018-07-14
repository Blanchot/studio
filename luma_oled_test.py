#luma_oled_test

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

with canvas(device) as draw:
  draw.rectangle(device.bounding_box, outline="white", fill="black")
  draw.text((30, 40), "Hello World", fill="white")

