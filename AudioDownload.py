def Download():
	import pafy,bitmath
	url=input("Enter URL: \n")
	video = pafy.new(url)
	print("Track Name: " + video.title)
	print("Duration: " + video.duration)
	count=0
	print("Available formats:")
	audiostreams = video.audiostreams 
	for i in audiostreams: 
	    print(count,i.extension, i.get_filesize(), bitmath.Byte(bytes=i.get_filesize()).best_prefix())
	    count+=1
	tno=int(input("Select track to Download: "))
	audiostreams[tno].download(filepath="F:/Python Songs")
def Repeat():
	import os
	import sys
	w=int(input("Press '0' to exit or '1' to download another track: "))
	if w==1:
		AD()
	elif w==0:
		sys.exit()
	else:
		w=int(input("Incorrect input entered, try again! :"))

def AD():
	Download()
	Repeat()
	
if __name__=="__main__":
	AD()
