#! python3
# bullet_point_added.py - Adds Wikipedia bullet points to the start
# of eachline of text on the clipboard.

import pyperclip
text = pyperclip.paste()

#TODO: Separate lines and add stars.

pyperclip.copy(text)