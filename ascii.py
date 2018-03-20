import cv2 #Get a wider ascii shade range and allow choosing high resolutions etc also gif viewer XD
import os
from sys import argv,exit,stdout #change this and put argparse for -r reverse shade scheme and -color etc
from math import floor#Make a better shade wheel for the 255 possible values
#import socket
#from threading import Thread
import time

########################FUTURE ADDITIONS#####################
#1 need to stich the asciiSelf block to the main frame
#2 adjust bash settings to reduce font size by the code and not by the user
#3 centralize the server

size=0

def ascii(img):
	ratio = img.shape[0]/float(img.shape[1])
	rows, columns = os.popen('stty size', 'r').read().split()
	columns = int(columns)/2
	img = cv2.cvtColor(cv2.resize(img,(columns,int(floor(columns*ratio)))), cv2.COLOR_BGR2GRAY)
	gap = (int(rows)-img.shape[0])/2
	def asciiMapping(val):
		shades = ' .:-=+*#@'#[::-1]
		segments = 255/(len(shades)-1)
		return shades[(val/segments)]
	transformedAscii = []
	for i in img:
		temp = []
		for j in i:
			temp.append(asciiMapping(j))
		transformedAscii.append(temp)
	ascii = ''
	for i in transformedAscii:
		ascii += ' '.join(i)
		ascii += '\n'
	return '\n'*gap+ascii

"""def asciiSelf(img):
	ratio = img.shape[0]/float(img.shape[1])
	rows=30
	columns = 30
	img = cv2.cvtColor(cv2.resize(img,(columns,int(floor(columns*ratio)))), cv2.COLOR_BGR2GRAY)
	gap = (int(rows)-img.shape[0])/2
	def asciiMapping(val):
		shades = ' .:-=+*#@'#[::-1]
		segments = 255/(len(shades)-1)
		return shades[(val/segments)]
	transformedAscii = []
	for i in img:
		temp = []
		for j in i:
			temp.append(asciiMapping(j))
		transformedAscii.append(temp)
	ascii = ''
	for i in transformedAscii:
		ascii += ' '.join(i)
		ascii += '\n'
	return '\n'*gap+ascii
"""

cap = cv2.VideoCapture(0)
#client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#client.connect(('10.180.30.77',8000))
#client.send("anand is awesome")

ret, frame = cap.read()
#client.send(str(len(ascii(frame))))
#size=int(client.recv(6))

"""def recieve():
	global size
	while True:
		data=client.recv(size)
		if not data:
			sys.exit(0)
		print(data)
"""
#Thread(target=recieve).start()

while(cap.isOpened()):
	ret, frame = cap.read()
#	client.send(ascii(frame))
	#os.system('cls' if os.name == 'nt' else 'clear')
	stdout.write(ascii(frame))#+asciiSelf(frame)+'\n')
	#stdout.flush()
	#time.sleep(0.001)
	#client.send("ihbisuvebbvseibgoisibhilis")
	#recvd=client.recv(10000)
	#print(recvd)
#client.close()
