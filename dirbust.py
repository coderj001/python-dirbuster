import requests 
import os 
from sys import argv 


def main():
	if len(argv) == 1 :
		print('''
			Please use the command given below...
			python dirbust.py url wordlist
			example:
			python dirbust.py http://example.com/ wordlist.txt/
			''')
	elif len(argv) == 2:
		if argv[1][len(argv[1])-4:len(argv[1])] == '.txt':
			print('\t\t\tPlease give url of a site before wordlist.')
		else:
			print('\t\t\tPlease enter link of the wordlist after url.')
	elif len(argv) == 3:
		dirb(str(argv[1]),"/"+str(argv[2]))
	else:
		print('''
			You have entered command in wrong format.
			Please use the command given below...
			python dirbust.py url wordlist
			example:
			python dirbust.py http://example.com/ wordlist.txt/
			''')


def dirb(urls,wordlist):
	arr=[]
	url=urls
	try:
		if url[:7] != 'http://':
			url="http://"+url
		r=requests.get(url)
		if r.status_code == 200:
			print('Host is up.')
		else:
			print('Host is down.')
			return
		if os.path.exists(os.getcwd()+wordlist):
			fs=open(os.getcwd()+wordlist,"r")
			for i in fs:
				print(url+"/"+i)
				rq=requests.get(url+"/"+i)
				if rq.status_code == 200:
					print(">OK".rjust(len(url+"/"+i)+5,'-'))
					arr.append(str(url+"/"+i))
				else:
					print(">404".rjust(len(url+"/"+i)+5,'-'))
			fs.close()
			print("output".center(100,'-'))
			l=1
			for i in arr:
				print(l, "> ", i)
				l+=1
		else:
			print(wordlist+" don't exists in the directory.")
	except Exception as e:
		print(e)



if __name__ == '__main__':
	main()