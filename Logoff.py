import os
restart = input("Do you wish to logoff your computer ? (yes / no): ")
if restart == 'no':
	exit()
else:
	os.system("shutdown /l")
