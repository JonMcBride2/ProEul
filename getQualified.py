def getQualified(length=0):

"""qualify=8574
include=52073"""
	#These are the locations of the files can be sifted through. 
	cm = open("C:\Users\jon.mcbride\Desktop\clickmotive.csv","r")
	#cmQ = open("C:\Users\jon.mcbride\Desktop\clickmotiveQualified.csv","w")
	cmS = open("C:\Users\jon.mcbride\Desktop\clickmotiveSpecial.csv","w")
	
	cmRead = cm.read()
	primes = foRead.split("\n")
	
	for i in range(0,len(primes)):
		"""includeCount=0
		qualifyCount=0
		if primes[i].find("include=") > -1 or primes[i].find("qualify=") > -1:
			includeCount=primes[i].count("include=")
			qualifyCount=primes[i].count("qualify=")
			cmQ.write(primes[i] + ", includeCount:" + str(includeCount) + ", qualifyCount:" + str(qualifyCount) + "\n")"""
		if primes[i].find("1C6RR7LT0ES300782") > -1 or  primes[i].find("1FTFW1ET0EKD30153") > -1 or primes[i].find("3FA6P0K98ER224941") > -1:
			ar = primes[i].split("<SpecialNew")
			for i in ar: cmS.write(i + "\n")
			cmS.write("\n\n")
	cm.close()
	#cmQ.close()
	cmS.close()
	
getQualified()