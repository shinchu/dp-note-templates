# Reference lines for caligraphy with broad nib pens
# Source: Martina Flor. *The Golden Secrets of Lettering*.
# Code: Shin Chu
# Created: 2019-10-07
# Updated: 2020-04-13

import os, math

def mm_to_pixel(mm, dpi=300):
    inch_per_mm = 0.0393701
    return mm * inch_per_mm * dpi

# ReMarkable template size
# 1404×1872 pixels
dpi = 200
width = 1872
height = 1404

# size of the pen
pen_mm = 3.5

# constants
pen_size = mm_to_pixel(pen_mm, dpi)
line_height = pen_size * 8
gutter = mm_to_pixel(10, dpi)

width_margin = mm_to_pixel(20, dpi)
n_row = math.floor(height / (line_height + gutter))
height_margin = (height - (n_row * (line_height + gutter) - gutter)) / 2

newPage(width, height)
strokeWidth(mm_to_pixel(0.1, dpi))

translate(0, height_margin)

for i in range(n_row):
    save()
    for j in range(8):
        fill(0, 0.1)
        stroke(None)
        if j % 2 == 0:
            rect(width_margin, 0, pen_size, pen_size)
        else:
            rect(width_margin + pen_size, 0, pen_size, pen_size)
        if j == 0 or j == 2 or j == 6:
            stroke(0, 0.3)
            strokeWidth(mm_to_pixel(0.4, dpi))
        else:
            stroke(0, 0.5)
            strokeWidth(mm_to_pixel(0.1, dpi))
        line((width_margin, 0), (width - width_margin, 0))
        translate(0, pen_size)
    strokeWidth(mm_to_pixel(0.4, dpi))
    stroke(0, 0.3)
    line((width_margin, 0), (width - width_margin, 0))
    restore()
    translate(0, line_height + gutter)
    
parent_dir = os.path.dirname(os.getcwd())
filename = os.path.basename(__file__).split('.')[0]
saveImage('{}/{}.svg'.format(os.path.join(parent_dir, 'svg'),
                             filename))
saveImage('{}/{}.png'.format(os.path.join(parent_dir, 'png'),
                             filename), imageResolution=72)