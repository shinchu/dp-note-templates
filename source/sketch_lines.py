# Reference lines for type sketches
# Source: https://github.com/guidoferreyra/Drawbot/baseDrawer.py
# Code: Shin Chu
# Created: 2020-04-25
# Updated: 2020-04-30

import os, math

def mm_to_pixel(mm, dpi=300):
    inch_per_mm = 0.0393701
    return mm * inch_per_mm * dpi

def pixel_to_mm(pixel, dpi=300):
    mm_per_inch = 25.4
    return pixel * mm_per_inch / dpi

class SketchLines:
    def __init__(self, scale, length, xheight=500, ascender=750, descender=-250,
                 cap_height=720, baseline_overshoot=15, xheight_overshoot=15,
                 glyph_width=None):

        self.margin = length * 0.05
        self.length = length - self.margin
        self.xheight = xheight * scale
        self.ascender = ascender * scale
        self.descender = descender * scale
        self.cap_height = cap_height * scale
        self.baseline_overshoot = baseline_overshoot * scale
        self.xheight_overshoot = xheight_overshoot * scale

        if glyph_width:
            self.glyph_width = glyph_width * scale
        else:
            self.glyph_width = None

    def draw_line(self, y_position, name):
        text(name, (self.margin * 0.05, y_position))
        line((self.margin, y_position), (self.margin + self.length, y_position))

    def draw_descender(self):
        self.draw_line(self.descender, "desc")

    def draw_baseline(self):
        self.draw_line(0, "base")

    def draw_xheight(self):
        self.draw_line(self.xheight, "x")

    def draw_cap_height(self):
        self.draw_line(self.cap_height, "cap")

    def draw_ascender(self):
        self.draw_line(self.ascender, "asc")

    def draw_baseline_overshoot(self):
        rect(self.margin, -self.baseline_overshoot, self.length, self.baseline_overshoot)

    def draw_xheight_overshoot(self):
        rect(self.margin, self.xheight, self.length, self.xheight_overshoot)

    def draw_glyph_width(self):
        if self.glyph_width:
            advance = 0
            while advance < self.length:
                line((self.margin + advance + self.glyph_width, self.descender),
                     (self.margin + advance + self.glyph_width, self.ascender))
                advance += self.glyph_width
        else:
            return

    def draw(self):
        font("Input Mono Condensed", 36 * scale)
        cmykStroke(None)
        cmykFill(0, 0, 1, 0, 0.5)
        self.draw_baseline_overshoot()
        self.draw_xheight_overshoot()
        cmykStroke(0, 0, 0, 1)
        cmykFill(0, 0, 0, 1)
        self.draw_descender()
        self.draw_baseline()
        self.draw_xheight()
        self.draw_cap_height()
        self.draw_ascender()
        cmykStroke(0, 0, 0, 1, 0.3)
        cmykFill(None)
        self.draw_glyph_width()

if __name__ == "__main__":

    # A4 paper
    dpi = 72
    width = mm_to_pixel(297, dpi)
    height = mm_to_pixel(210, dpi)

    # variables
    xheight = 500
    ascender = 750
    descender = -250
    cap_height = 720
    baseline_overshoot = 15
    xheight_overshoot = 15
    glyph_width = 500

    upm = ascender - descender
    scale = 100 / pixel_to_mm(upm, dpi) # make 1000px = 10cm

    h_margin = mm_to_pixel(5, dpi)
    v_margin = mm_to_pixel(2, dpi)
    body_width = width - 2 * h_margin
    body_height = height - 2 * v_margin

    size(width, height)
    lines = SketchLines(scale, body_width, glyph_width=500)

    advance = 0
    while advance + upm * scale < body_height:
        save()
        translate(h_margin, advance + v_margin - descender * scale)
        lines.draw()
        restore()
        advance += upm * scale + 2 * v_margin


    parent_dir = os.path.dirname(os.getcwd())
    filename = os.path.basename(__file__).split('.')[0]
    saveImage('{}/{}.pdf'.format(os.path.join(parent_dir, 'pdf'),
                                 filename))
