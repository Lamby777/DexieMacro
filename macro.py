#importspi
from termcolor import colored
import keyboard
ver = "d7"

def printHelp():
	return [print(
		x + ": \n\t" + cmds[x]["desc"] + "\n"
	) for x in cmds]

def recordMacro():
    print("Type starting key. (You can always delete macros)")
    keyboard.read_key()

cmds = {
	"help": {"fn": printHelp, "desc": "Shows help for commands"},
	"exit": {"fn": quit, "desc": "Quits the CLI, stops all macros"},
    "new": {"fn": recordMacro, "desc": "Adds a new macro"}
}

print(colored("Welcome to DxMacro, a FOSS CLI Macro tool written in Python3.", "red"))
print("DxMacro is running version " + ver)
print("Type command \"help\" for help")

while True:
	print("> ", end="")
	cmd = input()
	if cmd in cmds.keys():
		cmds[cmd]["fn"]()
	else:
		print(colored("Command does not exist, try \"help\"", "red"))

#keyboard.press_and_release('shift+s, space')
#keyboard.write('The quick brown fox jumps over the lazy dog.')
#keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))
#keyboard.add_hotkey('page up', lambda: keyboard.write('foobar'))
#keyboard.wait('esc')
#recorded = keyboard.record(until='esc')
#keyboard.play(recorded, speed_factor=3)
#keyboard.add_abbreviation('@@', 'my.long.email@example.com')
