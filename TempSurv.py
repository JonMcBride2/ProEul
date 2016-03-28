fo = open("C:\Users\jon.mcbride\Desktop\TempSurv.txt","r")
fw = open("C:\Users\jon.mcbride\Desktop\TempSurvOut.txt","w")


foRead = fo.read()
lines = foRead.split("\n")

length = len(lines)
foundSurvival = False

for i in range(0,length):
	
	'''num = lines[i].rfind("]] x")
	if num > -1:
		lines[i] = "|data-sort-value="+lines[i][num+4:]+lines[i]
	'''
	if foundSurvival == True:
		if lines[i].startswith('|[[File:'):
			num = lines[i].rfind("|")
			lines[i] = '|data-sort-value='+'"'+lines[i][num+1:len(lines[i])-2]+'"'+lines[i]
	else:
		if lines[i].find("=Survival ISO-8 Shard Exchange=") > -1:
			foundSurvival = True
	
	fw.write(lines[i]+"\n")

fo.close
fw.close




