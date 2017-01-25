Title: How to use OLED display with Banana Pi
Date: 2016-07-25 08:00
Modified: 2016-07-25 08:00
Category: Readings
Tags: Books
Slug: oled-display-i2c-with-bananapi
Cover: '/images/dodgest_logo3.jpg'

Today we're going to connect an OLED display on Banana Pi/Banana Pro throught I²C. These displays are very small, but very readable due to the high contrast.

In this example I will use a 128x64 OLED display based on SSD1306 controller. You can find models that use [I²C](https://en.wikipedia.org/wiki/I%C2%B2C) or [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) as communication interface. SPI is generally faster than I2C but uses more pins.

## Connecting the module

The table bellow shows how to connect a display that uses I²C interface.

| OLED Pin | BananaPi/Pro Pin |
|:--------:|:----------------:|
| VCC           | 1 (3V3)       |
| GND           | 6 (GND)       |
| SCL (or CLK)  | 5 (SCL)       |
| SDA (or Data) | 3 (SDA)       |
| RST           | 24 (GPIO8)    |
