# Plain grids for Japanese lettering
# Code: Shin Chu
# Created: 2019-09-28
# Updated: 2020-04-13

import os, math

def mm_to_pixel(mm, dpi=300):
    inch_per_mm = 0.0393701
    return mm * inch_per_mm * dpi

def draw_box(box_size, box_mm, dpi, show_cross=True, show_tenth=True, show_unit=True):

    rect(0, 0, box_size, box_size)
    if show_cross:
        save()
        translate(0, box_size/2)
        line((0, 0), (box_size, 0))
        restore()
        save()
        translate(box_size/2, 0)
        line((0, 0), (0, box_size))
        restore()

    if show_tenth:
        save()
        for i in range(10):
            strokeWidth(mm_to_pixel(0.1, dpi))
            translate(0, box_size/10)
            line((0, 0), (box_size, 0))
        restore()
        save()
        for i in range(10):
            strokeWidth(mm_to_pixel(0.1, dpi))
            translate(box_size/10, 0)
            line((0, 0), (0, box_size))
        restore()

    if show_unit:
        save()
        for i in range(box_mm):
            strokeWidth(mm_to_pixel(0.05, dpi))
            translate(0, box_size/box_mm)
            line((0, 0), (box_size, 0))
        restore()
        save()
        for i in range(box_mm):
            strokeWidth(mm_to_pixel(0.05, dpi))
            translate(box_size/box_mm, 0)
            line((0, 0), (0, box_size))
        restore()


# A4 paper
dpi = 72
width = mm_to_pixel(297, dpi)
height = mm_to_pixel(210, dpi)

# box size
box_mm = 50

# constants
box_size = mm_to_pixel(box_mm, dpi)
gutter = mm_to_pixel(6, dpi)

n_col = math.floor(width / (box_size + gutter))
n_row = math.floor(height / (box_size + gutter))

width_margin = (width - ((box_size + gutter) * n_col - gutter)) / 2
height_margin = (height - ((box_size + gutter) * n_row - gutter)) / 2

newPage(width, height)
fill(None)
cmykStroke(1, 0, 0, 0)
strokeWidth(mm_to_pixel(0.25, dpi))

translate(width_margin, height_margin)

for i in range(n_row):
    save()
    for j in range(n_col):
        draw_box(box_size, box_mm, dpi)
        translate(box_size + gutter, 0)
    restore()
    translate(0, box_size + gutter)

parent_dir = os.path.dirname(os.getcwd())
filename = os.path.basename(__file__).split('.')[0]
saveImage('{}/{}.pdf'.format(os.path.join(parent_dir, 'pdf'),
                             filename))