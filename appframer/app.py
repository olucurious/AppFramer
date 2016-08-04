#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'olucurious'

import PIL
from PIL import ImageFont
from PIL import Image, ImageFilter
from PIL import ImageDraw
import textwrap
import os
import json
import string
import sys
import argparse
from time import strftime
import six
import inspect

"""
The following resolutions are acceptable to iTunes connect:

iPhone 3+4 (3.5 Inch)
640 x 960

iPhone 5 (4 Inch)
640 x 1136

iPhone 6 (4.7 Inch)
750 x 1334

iPhone 6 Plus (5.5 Inch)
1242 x 2208

You need the screenshot in this resolution, the phone scales them down to 1080 x 1920
iPad (Air and Mini Retina)
1536 x 2048

Apple Watch
312 x 390 pixels

(only one orientation)
iPad Pro
2048 x 2732
"""

OUTPUT_DIR = os.getcwd() + '/FramedAppScreens - %s/' % strftime("%d-%m-%Y AT %H.%M")


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):  # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


class FrameScreenshots:
    def __init__(self, screenshot_location, title_text, desc_text, title_color=None, desc_color=None):
        self.screenshot_location = screenshot_location
        self.title_text = title_text
        self.desc_text = desc_text
        # Opening the screen shot image file
        self.screenshot_image = Image.open(self.screenshot_location)
        self.title_color = (title_color if title_color else (255, 255, 255))
        self.desc_color = (desc_color if desc_color else (255, 255, 255))
        # Loading Fonts...
        self.title_font = ImageFont.truetype(get_script_dir() + "/fonts/Champagne & Limousines Bold.ttf", 120)
        self.desc_font = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 70)

    def generate(self):
        screen_sizes = dict()
        screen_sizes[3.5] = (640, 960)
        screen_sizes[4] = (640, 1136)
        screen_sizes[4.7] = (750, 1334)
        screen_sizes[5.5] = (1242, 2208)
        for iphone in screen_sizes:
            print("Now processing '%s' screen for %s inches" % (self.title_text, iphone))
            self.process_iphone(iphone, screen_sizes[iphone][0], screen_sizes[iphone][1])
        print("Done with '%s' screen" % self.title_text)
        print("------------------------------------------")

    def process_iphone(self, dim, width, height):
        scrshot2 = self.screenshot_image.resize((1536, 2726), PIL.Image.ANTIALIAS)
        final_version = scrshot2.filter(ImageFilter.GaussianBlur(radius=8))
        self.set_text(final_version, self.desc_text, self.desc_font, 'desc')
        self.set_text(final_version, self.title_text, self.title_font, 'title')
        # ------------------
        iphone_type = ('iphone6plus' if dim > 4 else 'iphone5')
        iphone_device = Image.open("%s/devices/%s.png" % (get_script_dir(), iphone_type))
        final_version.paste(iphone_device, (0, 0), iphone_device)
        if dim <= 4:
            img2 = self.screenshot_image.resize((1135, 1800), PIL.Image.ANTIALIAS)
            final_version.paste(img2, (200, 920))
        else:
            img2 = self.screenshot_image.resize((1147, 1906), PIL.Image.ANTIALIAS)
            final_version.paste(img2, (190, 820))
        if not os.path.isdir(OUTPUT_DIR):
            os.mkdir(OUTPUT_DIR)
        destination_dir = OUTPUT_DIR + '/%s' % dim
        if not os.path.isdir(destination_dir):
            os.mkdir(destination_dir)
        final_version = final_version.resize((width, height), PIL.Image.ANTIALIAS)
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        file_name = ''.join(c for c in self.title_text if c in valid_chars)
        final_version.convert('RGB').save("%s/%s.jpg" % (destination_dir, file_name))

    def set_text(self, blurred_image, text, font, text_type):
        MAX_W, MAX_H = blurred_image.size
        para = textwrap.wrap(text, width=40)
        draw = ImageDraw.Draw(blurred_image)
        current_h, pad = (300 if text_type == 'desc' else 100), 10
        text_color = (self.desc_color if text_type == 'desc' else self.title_color)
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill=text_color)
            current_h += h + pad


def main():
    desc = 'AppFramer helps to reduce the pain of putting your app screenshots in the various device frames'
    parser = argparse.ArgumentParser(prog='appframer', description=desc)
    parser.add_argument('-i', '--input', type=str, help='Pass the input screens.json file location', required=True)
    # TODO - allow the user to specify output directory
    # parser.add_argument('-o', '--output', help='Directory to write the generated files', required=True)
    args = vars(parser.parse_args())
    data = json.load(open(args['input']))
    print("------------------------------------------")
    if 'screens' in data and isinstance(data['screens'], list):
        for screen in data['screens']:
            framedshot = FrameScreenshots(screen['file_path'], screen['title'], screen['description'],
                                          screen['title_color'], screen['description_color'])
            framedshot.generate()
        print("------------------------------------------")
        print("Screenshots device frame processing complete...")
        print("Get the output at %s" % OUTPUT_DIR)
    else:
        print("Invalid input format in %s json file" % args['input'])
    sys.exit()
