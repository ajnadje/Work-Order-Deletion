#12/5/2019
#This script will automate X work order deletion

import pyautogui
import time
from win10toast import ToastNotifier

print('This script will automate Onservice work order deletion. Press Ctrl-C to quit at anytime')
input('\nPlease log into X, make sure this window does not obstruct Onservice\'s top menu bar, \nthen hit anything to continue')
#click Work Orders
pyautogui.click(360,206)
#wait for 2 seconds
time.sleep(4)
#click Search/Filter
pyautogui.click(1735,278)
#check Include closed work orders
pyautogui.click(74,557)
#click Status drop down
pyautogui.click(1180,411)
#check Closed
pyautogui.click(1256,494)
#click Search
pyautogui.click(1760,600)

console = input('\nIs the Status for all work orders set to Closed? (y to continue or anything else to end script)')

if console.lower() == 'y':
	input('\nNavigate to the work orders you would like to delete, then press any key to continue')
	#add command to scroll to the top
	try:
		while True:	
			#take an input here to ask the user how many work orders they would like to delete.
			number=int(input('How many work orders would you like to delete?'))
			for i in range(number): #use user input to determine how many time to iterate.
				#scroll to the top
				pyautogui.scroll(100)
				time.sleep(2)
				#click the work order
				pyautogui.click(264,718)
				time.sleep(3)
				#click Delete
				pyautogui.click(1825,284)
				time.sleep(1)
				#click OK on the dialog box that opens
				pyautogui.click(1054,186)
				time.sleep(3)
			console=input('\nPlease go to the next page and press y to continue, otherwise press anything else to end the script')
			if console.lower() == 'y':
				continue
			else:
				break

	except KeyboardInterrupt:
		print('\n You stopped the script early') 
else:
	input('\n Please close this window and try again.')
input('Done')

