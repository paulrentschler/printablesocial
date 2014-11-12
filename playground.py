#!/Users/paulrentschler/Documents/projects/printablesocial/bin/python

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import qrcode


def various_boxes_borders(box_size, border):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data('http://www.google.com')
    qr.make(fit=True)
    img = qr.make_image()
    img.save("images/testh-%s-%s.png" % (box_size, border))


def various_versions(size):
    qr = qrcode.QRCode(
        version=size,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data('http://www.google.com')
    img = qr.make_image()
    img.save("images/version-%s.png" % (size))


def make_one(box_size, border, size, error, version):
    qr = qrcode.QRCode(
        version=size,
        error_correction=error,
        box_size=box_size,
        border=border,
    )
    qr.add_data('http://www.google.com')
    img = qr.make_image()
    img.save("image-%s-%s-%s-%s.png" % (version, size, box_size, border))


def make_bunch():
    for bs in range(10, 100, 10):
        for b in range(4, 10):
            various_boxes_borders(bs, b)
    for s in range(1, 40):
        various_versions(s)


def make_qr(url):
    qr = qrcode.QRCode(
        version=7,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    return qr.make_image()


def change_color(img, new_color):
    # Get the size of the image
    width, height = img.size

    # Process every pixel
    for x in range(0, width):
       for y in range(0, height):
            if img.getpixel( (x,y) ) == (0,0,0):
                img.putpixel( (x,y), new_color )
    return img


def make_facebook(url):
    img = make_qr(url)
    fb = change_color(img.convert("RGB"), (59,89,152))
    draw = ImageDraw.Draw(fb)
    font = ImageFont.truetype('LucidaGrandeBold.ttf', 475)
    draw.text((200, 150), "f", (255,255,255), font=font)
    img.save("fb-original.png")
    fb.save("facebook.png")


def make_twitter(url):
    img = make_qr(url)
    twitter = change_color(img.convert("RGB"), (85,172,238))
    logo = Image.open('twitter-logo.png')
    twitter.paste(logo, (0,0), logo)
    img.save('tw-original.png')
    twitter.save('twitter.png')


def make_youtube(url):
    img = make_qr(url)
    yt = change_color(img.convert("RGB"), (229,45,39))
    #yt = change_color(img.convert("RGB"), (51,51,51))
    logo = Image.open('youtube-logo.png')
    yt.paste(logo, (0,0), logo)
    img.save('yt-original.png')
    yt.save('youtube.png')


if __name__ == '__main__':
    make_facebook('https://www.facebook.com/paul.rentschler')
    make_twitter('https://twitter.com/paulrentschler')
    make_youtube('http://www.youtube.com')


