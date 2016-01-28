﻿# -*- coding: utf-8 -*-
from musicPlayer import musicPlayer
from newsStation import newsStation
from newsStation import newsparser
import socket
import subprocess

def yukkuri(str):
        return
	subprocess.check_output("/home/pi/workspace/raspi-audio/download/aquestalkpi/AquesTalkPi " + str + " | aplay -q",shell=True)

def interpreter(order,msg): # orderは認識された音声 msgはそれ以外の引数
	a = musicPlayer.audio()
	s = musicPlayer.select()
	print 0
	#c = caster()
	print 1
	if order == "再生":
		a.play()
	elif order == "停止" and a.flag == 1:
		a.stop()
	elif order == "選択":
		print 2
		s.callSelectMode()
		print 3
	elif order == "ニュース":
		return "playnews"
	elif order == "停止" and speker.flag == 1:
		#speaker.stopnews()
		return "stopnews"
	#elif order == "話題":
		#c.newsByMain()
	elif s.flag == 1:
		s.selectMusic(order) 
	return "interpreter is correctly finished."

if __name__ == "__main__":
	host = 'localhost'
	port = 10501

	#news.get()
	newsparser.parser.parse("newsStation/news.txt")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	yukkuri("ゆっくりしていってね")
	msg = ""
	newsflag = 0

	while True:
		res = s.recv(1024)
		if not res.find('WORD') == -1:	
			try:
				ary1 = res.split('WORD')
				ary2 = ary1[1].split('"')
				print ary2[1]
				msg = interpreter(ary2[1],msg)
			except:
				print("error in xml parser.")
		if msg == "playnews":
			print("newsflag is incremented.")
			newsflag += 1
		elif msg == "stopnews":
			newsflag = 0
			print("newsflag is zero")
			speaker.stopnews()
		if newsflag > 0:
			print("call speaker.playnews()")
			speaker.playnews()
