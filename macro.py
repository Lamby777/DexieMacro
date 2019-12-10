#imports
from termcolor import colored
import keyboard, turtle as t, tkinter as tk

print(colored("Welcome to DxMacro, a FOSS macro customizer written in Python.", "red"))
print("")

#keyboard.press_and_release('shift+s, space')
#keyboard.write('The quick brown fox jumps over the lazy dog.')
#keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))
#keyboard.add_hotkey('page up', lambda: keyboard.write('foobar'))
#keyboard.wait('esc')
#recorded = keyboard.record(until='esc')
#keyboard.play(recorded, speed_factor=3)
#keyboard.add_abbreviation('@@', 'my.long.email@example.com')

input()
	

def write_slogan():
	print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
	text="QUIT", 
	fg="red",
	command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
text="Hello",
command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()