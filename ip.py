import sys
import os 

def iplist():
#IP

	a = input("\tIP: \tOCTET 1:")
	b = input("\t\tOCTET 2:")
	c = input("\t\tOCTET 3:")
	d = int(input("\t\tOCTET 4:"))

	e = input("\tIP:\tOCTET 1:")
	f = input("\t\tOCTET 2:")
	g = input("\t\tOCTET 3:")
	h = int(input("\t\tOCTET 4:"))

	ip = [0, 0, 0, 0]
	ip[0] = int(a)
	ip[1] = int(b)
	ip[2] = int(c)
	ip[3] = int(d)

	ip2 = [0, 0, 0, 0]
	ip2[0] = int(e)
	ip2[1] = int(f)
	ip2[2] = int(g)
	ip2[3] = int(h)
	h=h+1

	for i in range (d,h):

		print (a+'.'+b+'.'+c+'.'+str(i))


	orig_stdout = sys.stdout
	f = open('output.txt', 'w')
	sys.stdout = f

	for i in range (d,h):
				print (a+'.'+b+'.'+c+'.'+str(i))
	sys.stdout = orig_stdout
	
	f.close()


iplist()
print("----------------------")
os.system('python3 blacklist.py -f output.txt')