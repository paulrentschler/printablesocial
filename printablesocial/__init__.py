from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os, qrcode


class PrintableSocial:

    def __init__(self):
        self.platforms = {
            'facebook': {
                'url': 'https://www.facebook.com/',
                'color': (59,89,152),
                },
            'twitter': {
                'url': 'https://twitter.com/',
                'color': (85,172,238),
                },
            'youtube': {
                'url': 'https://www.youtube.com/',
                'color': (229,45,39),
                },
            }


    def _colorize(self, img, color):
        """
        Change the black pixels in the specified img to the color specified
        by the color tuple (r,b,g) and return the colored image
        """
        # Get the size of the image
        width, height = img.size
        # Process every pixel
        if color != (0,0,0):
            for x in range(0, width):
               for y in range(0, height):
                    if img.getpixel( (x,y) ) == (0,0,0):
                        img.putpixel( (x,y), color )
        return img


    def create(self, platform, account=''):
        """
        Platform indicates which social media platform to create the QR Code
        icon for and account is appended to the standard url for that platform
        """
        parent = os.path.dirname(os.path.realpath(__file__))
        if platform in self.platforms:
            url = self.platforms[platform]['url']
            if account != '':
                url += account
            mask = Image.open("%s/%s.png" % (parent, platform))
            return self._social_qr(
                url,
                self.platforms[platform]['color'],
                mask
                )
        return None


    def _qrcode(self, url):
        """
        Generate a QR Code for the url provided using the predetermined size
        and the highest possible error correction options
        """
        qr = qrcode.QRCode(
            version=7,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        return qr.make_image()


    def _social_qr(self, url, color, logo_mask):
        """
        Returns a QR Code image that looks like a social media icon
        """
        logo_mask = logo_mask.convert("RGBA")
        img = self._qrcode(url)
        social_img = self._colorize(img.convert("RGB"), color)
        social_img.paste(logo_mask, (0,0), logo_mask)
        return social_img
