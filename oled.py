#!/usr/bin/python

def oled_interface(dummy, state):
    from time import sleep
    from board import SCL, SDA
    import busio
    from PIL import Image, ImageDraw, ImageFont
    import adafruit_ssd1306

    i2c = busio.I2C(SCL, SDA)
    disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

    disp.fill(0)
    disp.show()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = -2
    top = padding
    bottom = height-padding
    # Move left to right keeping track of the current x position for drawing shapes.
    x = 0

    fontDefault = ImageFont.load_default()
    font2 = ImageFont.truetype('/home/pi/nintendo-ds.ttf', 16)

    draw.text((x, top+0), "CoffeePi", font=fontDefault, fill=255)

    disp.image(image)
    disp.show()

    heartbeat = 0

    def coffee_anim(x, y, frame):
        draw.rectangle((0+x, 7+y, 9+x, 13+y), outline=0, fill=255)
        draw.line(((2+x, 13+y), (7+x, 13+y)), fill=255)
        draw.line(((0+x, 15+y), (10+x, 15+y)), fill=255)
        draw.point((9+x, 9+y), fill=255)
        draw.point((10+x, 9+y), fill=255)
        draw.point((10+x, 10+y), fill=255)
        draw.point((10+x, 11+y), fill=255)
        draw.point((9+x, 11+y), fill=255)

        if frame == 0:
            draw.point((1+x, 0+y), fill=255)
            draw.point((1+x, 1+y), fill=255)
            draw.point((2+x, 2+y), fill=255)
            draw.point((2+x, 3+y), fill=255)
            draw.point((1+x, 4+y), fill=255)
            draw.point((1+x, 5+y), fill=255)

            draw.point((4+x, 0+y), fill=255)
            draw.point((4+x, 1+y), fill=255)
            draw.point((5+x, 2+y), fill=255)
            draw.point((5+x, 3+y), fill=255)
            draw.point((4+x, 4+y), fill=255)
            draw.point((4+x, 5+y), fill=255)

            draw.point((7+x, 0+y), fill=255)
            draw.point((7+x, 1+y), fill=255)
            draw.point((8+x, 2+y), fill=255)
            draw.point((8+x, 3+y), fill=255)
            draw.point((7+x, 4+y), fill=255)
            draw.point((7+x, 5+y), fill=255)

        elif frame == 1:
            draw.point((2+x, 0+y), fill=255)
            draw.point((2+x, 1+y), fill=255)
            draw.point((1+x, 2+y), fill=255)
            draw.point((1+x, 3+y), fill=255)
            draw.point((2+x, 4+y), fill=255)
            draw.point((2+x, 5+y), fill=255)

            draw.point((5+x, 0+y), fill=255)
            draw.point((5+x, 1+y), fill=255)
            draw.point((4+x, 2+y), fill=255)
            draw.point((4+x, 3+y), fill=255)
            draw.point((5+x, 4+y), fill=255)
            draw.point((5+x, 5+y), fill=255)

            draw.point((8+x, 0+y), fill=255)
            draw.point((8+x, 1+y), fill=255)
            draw.point((7+x, 2+y), fill=255)
            draw.point((7+x, 3+y), fill=255)
            draw.point((8+x, 4+y), fill=255)
            draw.point((8+x, 5+y), fill=255)


    while True:
        currentTemp = str(round(state['avgtemp'],1))
        targetTemp = str(round(state['settemp'],1))

        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top+0), "Target", font=font2, fill=255)
        draw.text((x+42, top+0), targetTemp+" C", font=font2, fill=255)
        draw.text((x, top+17), "Boiler", font=font2, fill=255)
        draw.text((x+42, top+17), currentTemp+" C", font=font2, fill=255)

        if heartbeat == 0:
            #draw.rectangle((96, 16, 104, 24), outline=0, fill=255)
            coffee_anim(96, 8, 0)
            heartbeat = 1
        else:
            #draw.rectangle((104, 16 , 112, 24), outline=0, fill=255)
            coffee_anim(96, 8, 1)
            heartbeat = 0
        disp.image(image)
        disp.show()

        sleep(0.1)