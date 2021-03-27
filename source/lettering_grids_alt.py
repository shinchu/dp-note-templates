# Alternate grids for Japanese lettering
# Source: Graphic-sha. *Typography 01*.
# Code: Shin Chu
# Created: 2019-09-28
# Updated: 2020-04-13

import os, math

def mm_to_pixel(mm, dpi=300):
    inch_per_mm = 0.0393701
    return mm * inch_per_mm * dpi

def draw_box(box_size, box_mm, outer_mm, inner_mm, corner_mm, dpi, show_cross=True, show_bi=True, show_corner=True, show_inner=True, show_unit=True, show_side=True, show_dots=True):

    rect(0, 0, box_size, box_size)

    if show_inner:
        save()
        translate(mm_to_pixel(inner_mm, dpi), mm_to_pixel(inner_mm, dpi))
        rect(0, 0, box_size - 2 * mm_to_pixel(inner_mm, dpi), box_size - 2 * mm_to_pixel(inner_mm, dpi))
        restore()

    if show_corner:
        save()
        translate(-mm_to_pixel(corner_mm, dpi), -mm_to_pixel(corner_mm, dpi))
        line((0, 0), (0, 3 * mm_to_pixel(corner_mm, dpi)))
        line((0, 0), (3 * mm_to_pixel(corner_mm, dpi), 0))
        translate(0, box_size + 2 * mm_to_pixel(corner_mm, dpi))
        line((0, 0), (0, -3 * mm_to_pixel(corner_mm, dpi)))
        line((0, 0), (3 * mm_to_pixel(corner_mm, dpi), 0))
        translate(box_size + 2 * mm_to_pixel(corner_mm, dpi), 0)
        line((0, 0), (0, -3 * mm_to_pixel(corner_mm, dpi)))
        line((0, 0), (-3 * mm_to_pixel(corner_mm, dpi), 0))
        translate(0, -(box_size + 2 * mm_to_pixel(corner_mm, dpi)))
        line((0, 0), (0, 3 * mm_to_pixel(corner_mm, dpi)))
        line((0, 0), (-3 * mm_to_pixel(corner_mm, dpi), 0))
        restore()

    if show_cross:
        save()
        translate(0, box_size/2)
        line((-mm_to_pixel(outer_mm, dpi), 0), (box_size + mm_to_pixel(outer_mm, dpi), 0))
        restore()
        save()
        translate(box_size/2, 0)
        line((0, -mm_to_pixel(outer_mm, dpi)), (0, box_size + mm_to_pixel(outer_mm, dpi)))
        restore()

    if show_bi:
        save()
        for i in range(int(box_mm / 2)):
            translate(0, 2 * box_size / box_mm)
            line((0, 0), (box_size, 0))
        restore()
        save()
        for i in range(int(box_mm / 2)):
            translate(2 * box_size / box_mm, 0)
            line((0, 0), (0, box_size))
        restore()

    if show_unit:
        save()
        translate(box_size / box_mm, 0)
        for i in range(int(box_mm / 2) - 2):
            translate(2 * box_size / box_mm, 0)
            if i % 2 == 0:
                line((0, 0), (0, mm_to_pixel(inner_mm, dpi)))
                line((0, box_size), (0, box_size - mm_to_pixel(inner_mm, dpi)))
            else:
                line((0, 0), (0, 2 * box_size / box_mm))
                line((0, box_size), (0, box_size - 2 * box_size / box_mm))
        restore()
        save()
        translate(0, box_size / box_mm)
        for i in range(int(box_mm / 2) - 2):
            translate(0, 2 * box_size / box_mm)
            if i % 2 == 0:
                line((0, 0), (mm_to_pixel(inner_mm, dpi), 0))
                line((box_size, 0), (box_size - mm_to_pixel(inner_mm, dpi), 0))
            else:
                line((0, 0), (2 * box_size / box_mm, 0))
                line((box_size, 0), (box_size - 2 * box_size / box_mm, 0))
        restore()

    if show_side:
        save()
        translate(box_size + (box_size/box_mm)/2, 0)
        for i in range(15):
            translate(0, box_size / 16)
            line((0, 0), (box_size / box_mm, 0))
        restore()

    if show_dots:
        dot_size = corner_mm / 15
        rect(box_size / box_mm, box_size / box_mm, mm_to_pixel(dot_size, dpi), mm_to_pixel(dot_size, dpi))
        rect(box_size / box_mm, box_size - box_size / box_mm, mm_to_pixel(dot_size, dpi), mm_to_pixel(dot_size, dpi))
        rect(box_size - box_size / box_mm, box_size / box_mm, mm_to_pixel(dot_size, dpi), mm_to_pixel(dot_size, dpi))
        rect(box_size - box_size / box_mm, box_size - box_size / box_mm, mm_to_pixel(dot_size, dpi), mm_to_pixel(dot_size, dpi))


dpi = 72
# A4 paper
width = mm_to_pixel(297, dpi)
height = mm_to_pixel(210, dpi)
# A5 paper
# width = mm_to_pixel(210, dpi)
# height = mm_to_pixel(148, dpi)

# box size
box_mm = 60

# constants
outer_mm = box_mm / 12
inner_mm = box_mm / 40
corner_mm = 1
box_size = mm_to_pixel(box_mm, dpi)
outer_box = mm_to_pixel(box_mm + 2 * outer_mm, dpi)
gutter = mm_to_pixel(10, dpi)

n_col = math.floor(width / (outer_box + gutter))
n_row = math.floor(height / (outer_box + gutter))

width_margin = (width - ((outer_box + gutter) * n_col - gutter)) / 2
height_margin = (height - ((outer_box + gutter) * n_row - gutter)) / 2

newPage(width, height)
fill(None)
cmykStroke(1, 0, 0, 0, 0.5)
strokeWidth(mm_to_pixel(0.1, dpi))

translate(width_margin + mm_to_pixel(outer_mm, dpi), height_margin + mm_to_pixel(outer_mm, dpi))

for i in range(n_row):
    save()
    for j in range(n_col):
        draw_box(box_size, box_mm, outer_mm, inner_mm, corner_mm, dpi)
        translate(outer_box + gutter, 0)
    restore()
    translate(0, outer_box + gutter)

parent_dir = os.path.dirname(os.getcwd())
filename = os.path.basename(__file__).split('.')[0]
saveImage('{}/{}.pdf'.format(os.path.join(parent_dir, 'pdf'),
                             filename))