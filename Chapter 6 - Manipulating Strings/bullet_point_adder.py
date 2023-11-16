#! python3
# bullet_point_added.py - Adds Wikipedia bullet points to the start
# of eachline of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]      # add star to each string in "lines" list

pyperclip.copy(text)