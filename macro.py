#importspi
from termcolor import colored
import keyboard
ver = "d7"

def printHelp():
	return [print(
		x + ": \n\t" + cmds[x]["desc"] + "\n"
	) for x in cmds]

def recordMacro():
	print("Type starting key combo. (ex. ctrl+shift+x or alt+q)")
	print("Macros can always be deleted, so if you mess up, use command " + colored("del", "red") + "!")
	mkey = input()
	print("Great! Now, press the keys that the macro should automate.")
	print("End the list with Ctrl + Esc")
	print("When you are ready to record them, press enter to start.")
	recorded = keyboard.record(until='esc')
	
	#keyboard.play(recorded, speed_factor=3)

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
#keyboard.add_hotkey('page up', lambda: keyboard.write('foobar'))
#keyboard.add_hotkey('esc', print, args=("stuff"))
#keyboard.wait('esc')
#keyboard.play(recorded, speed_factor=3)
#keyboard.add_abbreviation('@@', 'my.long.email@example.com')
