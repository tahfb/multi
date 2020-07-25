import os

def clear():
	os.system("clear")
def main():
	print('''
(-----------------------------)
| 1 - Hacking                 |
| 2 - About                   |  
(-----------------------------)
		''')
	while True:
		choix = input(">>> ")
		if choix == "1":
			clear()
			hacking()
		elif choix == "2":
			clear()
			about()
		else:
			print("\"" + choix + "\"" + " is not a valid command")
def hacking():
	print('''
(-----------------------------)
| 1 - Brute Force             |
| 2 - Nmap                    | 
| 3 - Nikto                   |
| 0 - Back                    |
(-----------------------------)
		''')
	while True:
		choix = input(">>> ")
		if choix == "1":
			os.system("bash bf/bf.sh")
			clear()
			hacking()
		elif choix == "2":
			clear()
			nmap()
		elif choix == "3":
			choix1 = input("Target : ")
			os.system("nikto -h " + choix1)
			input("Press ENTER to continue")
		elif choix == "0":
			clear()
			main()
		else:
			print("\"" + choix + "\"" + " is not a valid command")
			clear()
			hacking()
def nmap():
	print('''
(-----------------------------)
| 1 - Basic                   |
| 2 - Advanced                | 
| 3 - All                     |
| 0 - Back                    |
(-----------------------------)
		''')
	while True:
		choix = input(">>> ")
		if choix == "1":
			choix1 = input("Target : ")
			os.system("nmap " + choix1)
			input("Press ENTER to continue")
		elif choix == "2":
			choix1 = input("Target : ")
			os.system("nmap -sC -sV " + choix1)			
			input("Press ENTER to continue")
		elif choix == "3":
			choix1 = input("Target : ")
			os.system("nmap -sC -sV -A -T4 -sU -Pn " + choix1)			
			input("Press ENTER to continue")
		elif choix == "0":
			clear()
			hacking()
		else:
			print("\"" + choix + "\"" + " is not a valid command")
			clear()
			nmap()
def about():
	print("Thank to all admin & modo of Termux Android Hacking :D")
	input("Press ENTER to continue")
	clear()
	main()

main()