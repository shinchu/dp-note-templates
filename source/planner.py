# Project planner
# Source: Bunpei Yorifuji. *yPad*.
# Code: Shin Chu
# Created: 2020-04-13
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

# variables
start_of_a_day = 8
end_of_a_day = 24
n_days = 14
n_projects = 10
margin = mm_to_pixel(10, dpi)

# constants
n_cols = 1 + end_of_a_day - start_of_a_day + n_projects
n_rows = n_days

canvas_width = width - 2 * margin
canvas_height = height - 2 * margin

grid = canvas_width / n_cols

newPage(width, height)
fill(None)
stroke(0, 0, 0, 1)
strokeWidth(mm_to_pixel(0.2, dpi))
lineCap('round')
font("Georgia", 8 * dpi/72)

# highlight weekends
save()
translate(margin, margin)
for i in range(n_rows):
    fill(1, 0.8, 0, 0.4)
    stroke(None)
    if (n_days - i) % 7 == 6 or (n_days - i) % 7 == 0:
        rect(0, i * grid, canvas_width, grid)
restore()

# draw half
save()
translate(margin, margin)
stroke(1, 0.8, 0)
lineDash(2 * dpi/72, 2 * dpi/72)
for i in range(1, n_cols - n_projects):
    line((i * grid + grid/2, 0), (i * grid + grid/2, grid * n_rows))
for i in range(1, n_rows):
    line((grid, i * grid + grid/2), (grid * (n_cols - n_projects), i * grid + grid/2))
restore()

# draw main area
save()
translate(margin, margin)
rect(0, 0, grid * n_cols, grid * n_rows)
for i in range(1, n_cols):
    line((i * grid, 0), (i * grid, grid * n_rows))
for i in range(1, n_rows):
    line((0, i * grid), (grid * n_cols, i * grid))

# draw time
save()
fill(0, 0, 0, 1)
stroke(None)
for i in range(1, end_of_a_day - start_of_a_day + 1):
    text(str(start_of_a_day - 1 + i), (i * grid, grid * n_rows + mm_to_pixel(1.5, dpi)), 'center')
restore()

restore()

# draw project area
save()
translate(margin + grid * (n_cols - n_projects), margin + grid * n_rows)
rect(0, 0, grid * n_projects, canvas_height - grid * n_rows)
for i in range(1, n_projects):
    line((i * grid, 0), (i * grid, canvas_height - grid * n_rows))

# draw project number    
save()
fill(0, 0, 0, 1)
stroke(None)
for i in range(n_projects):
    text(chr(97 + i), (i * grid + mm_to_pixel(1.5, dpi), canvas_height - grid * n_rows - mm_to_pixel(3, dpi)), 'left')
restore()

restore()

# draw memo
save()
translate(margin + 0.25 * grid * (n_cols - n_projects - 0.5), margin + grid * n_rows + 0.8 * grid)
fill(0, 0.1)
stroke(None)
rect(0, 0, 0.75 * grid * (n_cols - n_projects - 0.5), canvas_height - grid * n_rows - 0.9 * grid)
restore()

save()
translate(margin, margin + canvas_height - 0.1 * grid)
line((0, 0), (grid * (n_cols - n_projects - 0.5), 0))
restore()

save()
translate(margin, margin + grid * n_rows + 0.8 * grid)
line((0, 0), (grid * (n_cols - n_projects - 0.5), 0))
restore()

parent_dir = os.path.dirname(os.getcwd())
filename = os.path.basename(__file__).split('.')[0]
saveImage('{}/{}.svg'.format(os.path.join(parent_dir, 'svg'),
                             filename))
saveImage('{}/{}.png'.format(os.path.join(parent_dir, 'png'),
                             filename), imageResolution=72)