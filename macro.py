#imports
from termcolor import colored
import keyboard
ver = "d7"

cmds = {
	"exit": "haha"
}

print(colored("Welcome to DxMacro, a FOSS CLI Macro tool written in Python3.", "red"))
print("DxMacro is running version " + ver)
print("Type command \"help\" for help")

while True:
	print("> ", end="")
	cmd = input()
	if cmd in cmds.keys():
		quit()
#keyboard.press_and_release('shift+s, space')
#keyboard.write('The quick brown fox jumps over the lazy dog.')
#keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))
#keyboard.add_hotkey('page up', lambda: keyboard.write('foobar'))
#keyboard.wait('esc')
#recorded = keyboard.record(until='esc')
#keyboard.play(recorded, speed_factor=3)
#keyboard.add_abbreviation('@@', 'my.long.email@example.com')
