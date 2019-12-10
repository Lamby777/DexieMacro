#imports
from termcolor import colored
import keyboard, turtle as t, tkinter as tk
ver = "d7"

print(colored("Welcome to DxMacro, a FOSS macro customizer written in Python.", "red"))
print("DxMacro is running version " + ver + "\n")

#keyboard.press_and_release('shift+s, space')
#keyboard.write('The quick brown fox jumps over the lazy dog.')
#keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))
#keyboard.add_hotkey('page up', lambda: keyboard.write('foobar'))
#keyboard.wait('esc')
#recorded = keyboard.record(until='esc')
#keyboard.play(recorded, speed_factor=3)
#keyboard.add_abbreviation('@@', 'my.long.email@example.com')

class App(tk.Tk): 
    def __init__(self, title="Untitled", icon="python.ico", res="200x200"): 
        super().__init__()
        self.title(title)
        self.iconbitmap(icon)
        self.geometry(res)

def write_slogan():
	print("Tkinter is HARD to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

title = tk.Text(frame)
title.pack()
title.insert(tk.END, "Just a text Widget\nin two lines\n")

slogan = tk.Button(frame,
	text="Hello",
	command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()