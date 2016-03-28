import time
import math
# temp = 1230
# list = 10007

#def isPrime(num):
	# if num >= 2:
		# for i in range(2,num-1):
			# if num%i != 0:
				# return 0
			# return 1
	# else:
		# return 0
		
# while temp < 10001:
	# list = list + 2
	# print list + "," + temp
	# if isPrime(list) == 1:
		# temp = temp + 1
		# print str(list) + ',' + str(temp)

# print list + "," + temp

def isPrime(n): #Checks for prime via trial division
	if n >= 2:
		m = int(math.floor(math.sqrt(n)))
		for i in range(2,m+1):
			if n%i == 0: return False
		return True
	else: return False
	
# words = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred","and","thousand"]
# count = 0
# repeats = 0

# for i in range (1,1001):
	# if (i < 20): count = count + len(words[i])
	# elif (i >= 20 and i < 100):
		# count = count + len(words[20 + (i//10) - 2]) + len(words[i%10])
	
	# elif (i >= 100 and i < 1000):
		# if (i%100 == 0):
			# if (i == 100):
				# repeats = count 
				# print repeats
			# count = count + len(words[i//100]) + len(words[28]) + repeats
		
		# else: count = count + len(words[i//100]) + len(words[28]) + len(words[29])
	
	# else: count = count + len(words[1]) + len(words[30]) 

# print count

# nums = []
# nums.append([8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8])
# nums.append([49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0])
# nums.append([81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65])
# nums.append([52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91])
# nums.append([22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80])
# nums.append([24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50])
# nums.append([32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70])
# nums.append([67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21])
# nums.append([24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72])
# nums.append([21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95])
# nums.append([78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92])
# nums.append([16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57])
# nums.append([86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58])
# nums.append([19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40])
# nums.append([4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66])
# nums.append([88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69])
# nums.append([4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36])
# nums.append([20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16])
# nums.append([20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54])
# nums.append([1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48])

# prodR = 0
# prodC = 0
# prodDL = 0
# prodDR = 0
# temp = 0

# #for row in nums:
# #	print row

# for i in range(0,20): #run for row max
	# for j in range(0,17):
		# temp = nums[i][j] * nums[i][j+1] * nums[i][j+2] * nums[i][j+3]
		# prodR = max(prodR,temp)
# for i in range(0,20): #run for col max
	# for j in range(0,17):
		# temp = nums[j][i] * nums[j+1][i] * nums[j+2][i] * nums[j+3][i]
		# prodC = max(prodC,temp)
# for i in range(0,17): #run for dl max
	# for j in range(3,20):
		# temp = nums[j][i] * nums[j-1][i+1] * nums[j-2][i+2] * nums[j-3][i+3]
		# prodDL = max(prodDL,temp)
# for i in range(0,17): #run for dr max
	# for j in range(0,17):
		# temp = nums[i][j] * nums[i+1][j+1] * nums[i+2][j+2] * nums[i+3][j+3]
		# prodDR = max(prodDR,temp)
# print prodR, prodC, prodDL, prodDR
# print max(prodR,max(prodC,max(prodDL,prodDR)))

def factorial(n):
	if n <= 1: return 1
	else: return n * factorial(n-1)

# fact = factorial(100)
# sum = 0

# while fact > 0:
	# sum += fact%10
	# fact //= 10

# print sum
#count = 59
#i = 1000000000
#j = 100000001

# (16-1)/3
# #while count < 500:
# #	count = 0
# #	i+=1
# num = 0
# i = 1
# while i <= 1000:
	# num += i**i
	# i+=1
# print num%(10**10) 

# num = 0
# i = 1000000000
# i = 100000
# j = 0
# while j <= i:
	# num += j
	# j+=1
# #num = 500000000500000000
# print num
# i = 2
# #i = 5000000050000000/85000000 + 1
# j = num
# count = 2
# # count = 288
# while j > i:
	# # print i
	# if num%i == 0:
		# count+=2
		# j = num/i
		# print i
		# print j
	# i+=1
	# """if count >= 500: break
	# else: j+=1"""
# #if j==i: count-=1
# print count
# # print i
# # print j

# #100000000000000000

def getListOfPrimes(length=0):
	fo = open("C:\Users\jon.mcbride\Documents\CodingPractice\listOPrimes.txt","r")
	
	foRead = fo.read()
	primes = foRead.split("\n")
	if length == 0: length = len(primes)
	
	for i in range(0,length):
		primes[i] = int(primes[i])	
	
	fo.close()
	return primes[0:length]

def properSum(n):
	sum = 0
	for i in range(1,n):
		if n%i == 0: sum+=i
	return sum
def amicableNumbers():	
	psl = [-1,-1];
	anl = [0,0];
	sum = 0

	for i in range(2,10000):
		psl.append(properSum(i))
		anl.append(0)

	for a in range(2,10000):
		if anl[a] == 0:
			b = psl[a]
			if b < 10000 and psl[b] == a and a != b:
				anl[a] = 1
				anl[b] = 1

	for num in range(2,10000):
		if anl[num] == 1: sum += psl[num]

	print sum
def decPattern():
	nums = []
	for i in range(2,100):
		print i
		print 1.0/i
		nums.append(1.0/i)
	
def abundantSum():
	abNums = []
	for i in range(2,28124):
		if properSum(i) > i: abNums.append(i)
	abSums = []
	for x in range(0,len(abNums)):
		for y in range(x,len(abNums)): abSums.append(abNums[x]+abNums[y])
	abSums.sort()
	sum = 0
	abS = 0
	#while abSums[abS] < 28124:
	for i in range(1,28124):
		while i > abSums[abS]: abS += 1
		if i < abSums[abS]: sum += i
		else: 
			while i == abSums[abS]: abS += 1
	print sum

def distinctPowers():
	nums = []
	for i in range(2,101):
		for j in range(2,101):
			nums.append(i**j)
	nums.sort()
	
	count = 0
	temp = 0
	for x in nums:
		if x != temp: count+=1
		temp = x
	print count
#distinctPowers()

def digitFifthPowers():
	nums = [0**5,1**5,2**5,3**5,4**5,5**5,6**5,7**5,8**5,9**5];
	sums = []
	
	for x in nums:
		sums.append(x*5)
"""1-1
11,21,12-3
111,112,121,211,122,212,221-7
1111,1112,1121,1211,2111,1122,1212,1221,2121,2211,1222,2122,2212,2221-14
11111,11112,11121,11211,12111,21111,11122,11212,12112,21112,11221,12121,21121,12211,21211,22111"""
def tph():
	t = []
	p = []
	h = []
	a = 0
	b = 0
	c = 0
	
	for n in range (143,500):
		t.append(n*(n+1)/2)
		if n > 165:	p.append(n*(3*n-1)/2)
		if n > 285: h.append(n*(2*n-1))
	
	
	
	while t[a] != p[b] and  p[b] != h[c]:
		while t[a] > 0:
			break
		break
		
def milDigFib():
	a = 1
	b = 1
	f = 0
	count = 2
	
	while f < 10**999:
		count+=1
		f = a+b
		a = b
		b = f
	print count
#milDigFib()

def lexPerms(nObjs,rATime):
	x = factorial(nObjs)/factorial(nObjs-rATime)
	print x
	#print x * 3

"""print factorial(0)
print factorial(1)
print factorial(2)
print factorial(3)
print factorial(4)
print factorial(5)
print factorial(6)
print factorial(7)
print factorial(8)
print factorial(9)"""

def digFactos(nObjs):
	x = 0
	for i in range(1,nOjs+1):
		x += nObjs**i
	return x

	
def inPrimeList(num):
	primes = getListOfPrimes()
	aPrime = False
	
	for prime in primes:
		if num == prime:
			aPrime = True
			break
		elif num < prime: break
	
	return aPrime
		
def primePerms():
	primes = getListOfPrimes()
	x = []
	for prime in primes:
		if prime >= 1000 and prime < 10000-6660:
			if inPrimeList(prime + 3330) == True and inPrimeList(prime + 6660) == True:
				x.append(prime)
				x.append(prime + 3330)
				x.append(prime + 6660)
		
	print x

#primePerms()

def circularPrimes():
	primes = getListOfPrimes()
	count = 0
	mc = []
	
	for prime in primes:
		if prime >= 1000000: break
		circular = True
		length = len(str(prime))
		num = prime
		print num
		for n in range(1,length):
			x = (num/10 + (num%10)*(10**(length-1)))
			if inPrimeList(x) == False:
				circular = False
				break
		if circular == True:
			count += 1
			mc.append(prime)
	mc.sort()
	print mc
	print count
	print len(mc)

def truncatable(num,direction):
	length = len(str(num))
	if direction == "lr":
		for i in range(0,length):
			num = num%(10**(length-i))
			if inPrimeList(num) == False or len(str(num)) < (length-i): return False
	elif direction == "rl":
		for i in range(0,length):
			if inPrimeList(num) == False: return False
			num = num/10
	return True

def truncatablePrimes():
	primes = getListOfPrimes()
	sum = 0
	count = 0
	mList = []
	for prime in primes:
		if prime > 19 and truncatable(prime,"lr") == True and truncatable(prime,"rl") == True:
			sum += prime
			count += 1
			mList.append(prime)
			print mList
		if count == 11: break
	print mList
	return sum
	
#print truncatablePrimes()
#circularPrimes()

			
def reciprocalCycles():
	fo = open("C:\Users\jon.mcbride\Documents\CodingPractice\ReciprocalCycles.txt","w")
	
	for i in range(1,1000):
		fo.write(str(i)+"\n")
		fo.write(str(1.000000000000000/i)+"\n")
	fo.close()
	
#reciprocalCycles()

def champConstant():
	sn = ""
	x = 1
	y = 1
	while len(sn) < 1000000:
		sn += str(x)
		x += 1 
	x = 1
	while x <= 1000000:
		z = int(sn[x-1])
		print z
		y *= z
		x*=10
	print y
	

#champConstant()

def combinatoricSelectionsM(num):
	count = 0
	for i in range (1,num+1):
		if factorial(num)/(factorial(i)*factorial(num-i)) > 1000000: count += 1
	return count

def combinatoricSelections():
	count = 0
	for i in range(23,101):
		count += combinatoricSelectionsM(i)
	print count

def hdtNums(cap):
	tNum = 1
	current = 2
	while numOfDivs(tNum) < cap:
		tNum += current
		current += 1
	return tNum
	
def numOfDivs(n):
	if n > 1:
		count = 0
		m = int(math.floor(math.sqrt(n)))
		for i in range(1,m+1):
			if n%i == 0: count += 2
		return count
	else: return 1
	
def longCollatzSeq(x):
	i = 1
	res = 0
	current = 0
	count = 0
	while i < x:
		count = longCollatzSeqCount(i)
		if count == max(current,count):
			current = count
			res = i
		i+=1
	return res
	
def longCollatzSeqCount(n):
	if n == 1: return 1
	elif n%2 == 0: return 1 + longCollatzSeqCount(n/2)
	else: return 1 + longCollatzSeqCount(3*n+1)
		
def countingSummations(n):
	if n < 2: return 0
	elif n == 2: return 1
	elif n == 3: return 2
	elif n%2 == 0: return countingSummations(n//2)*2
	else: return countingSummations(n//2) + countingSummations(n//2 + 1)
	
def lychrelNumbers():
	x = 1
	nums = []
	while x < 10000:
		arr = []
		arr.append(x)
		for i in range (0,50):
			arr.append
			
			
"""def consecPrimeSum():
	primes = getListOfPrimes(79000)
	current = 0
	temp = 0
	length = 0
	
	for prime in primes:
		temp += prime
		if temp < 1000000:
			if isPrime(temp): length += 1
			else:
				current = temp
				
		else: break
	return current"""			

def consecPrimeSum(num=79000):
	primes = getListOfPrimes(num)
	maxPrime = 0
	maxTerms = 0
	
	for x in range(0,len(primes)):
		current = 0
		length = 0
		temp = 0
		tempTerms = 0
		for y in range(x,len(primes)):
			temp += primes[y]
			tempTerms += 1
			if temp < 1000000:
				if isPrime(temp):
					current = temp
					length = tempTerms
			else: break
		if length >= maxTerms:
			maxTerms = length
			maxPrime = current
			#print maxPrime," ",maxTerms," ",x
	return maxPrime,maxTerms
	
def latticePaths(a,b):
	n = a+b
	k = a
	return factorial(n)/(factorial(n-k)*factorial(k))

def digitFactorials(stop=10000000):
	total = 0
	num = 3
	while num < stop:
		temp = num
		sum = 0
		while temp > 0:
			sum += factorial(temp%10)
			temp /= 10
		if sum == num:
			total += sum
			print num
		num += 1
	return total
		
def poker():
	fo = open("C:\Users\jon.mcbride\Documents\CodingPractice\poker.txt","r")
	fow = open("C:\Users\jon.mcbride\Documents\CodingPractice\pokerRes.txt","w")
		
	foRead = fo.read()
	hands = foRead.split("\n")
		
	p1Wins = 0
	p2Wins = 0
	otherWins = 0
	for x in range(0,len(hands)):
		currentHands = hands[x].split(" ")
		
		p1Hand = []
		p1HandRes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		p2Hand = []
		p2HandRes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		#0=flush, 1-13=cards, 14=pairs, 15=3kind, 16=4kind, 17=straight
		for i in range(0,10):
			if i < 5: p1Hand.append(currentHands[i])
			else: p2Hand.append(currentHands[i])
		
		p1HandRes[0] = pokerHandFlush(p1Hand)
		p2HandRes[0] = pokerHandFlush(p2Hand)
		
		pokerHandCount(p1Hand,p1HandRes)
		pokerHandCount(p2Hand,p2HandRes)
		
		p1HandRes[14] = pokerCheckPairs(p1HandRes)
		p2HandRes[14] = pokerCheckPairs(p2HandRes)
		p1HandRes[15] = pokerCheck3OfAKind(p1HandRes)
		p2HandRes[15] = pokerCheck3OfAKind(p2HandRes)
		p1HandRes[16] = pokerCheck4OfAKind(p1HandRes)
		p2HandRes[16] = pokerCheck4OfAKind(p2HandRes)
		p1HandRes[17] = pokerCheckStraight(p1HandRes)
		p2HandRes[17] = pokerCheckStraight(p2HandRes)
		
		winner = pokerHandWinner(p1HandRes,p2HandRes)

		fow.write(hands[x])
		fow.write("\t")
		fow.write("\t" + str(winner) + "\n")
		
		if winner == 1: p1Wins += 1
		elif winner == 2: p2Wins += 1
		else: otherWins += 1

	fo.close()
	fow.close()
	return 'p1Wins: ',p1Wins,'; p2Wins: ',p2Wins,'; otherWins:',otherWins
	#return p1Wins
	
def pokerHandFlush(hand):
	if hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and hand[3][1] == hand[4][1]: return 1
	return 0

def pokerHandCount(hand,arr):
	for i in range(0,5):
		if hand[i][0] == '2': arr[1] += 1
		elif hand[i][0] == '3': arr[2] += 1
		elif hand[i][0] == '4': arr[3] += 1
		elif hand[i][0] == '5': arr[4] += 1
		elif hand[i][0] == '6': arr[5] += 1
		elif hand[i][0] == '7': arr[6] += 1
		elif hand[i][0] == '8': arr[7] += 1
		elif hand[i][0] == '9': arr[8] += 1
		elif hand[i][0] == 'T': arr[9] += 1
		elif hand[i][0] == 'J': arr[10] += 1
		elif hand[i][0] == 'Q': arr[11] += 1
		elif hand[i][0] == 'K': arr[12] += 1
		else: arr[13] += 1
	
def pokerHandWinner(p1HandRes,p2HandRes):
		#0=flush, 1-13=cards, 14=pairs, 15=3kind, 16=4kind, 17=straight
	#RF/SF
	if (p1HandRes[0] == 1 and p1HandRes[17] == 1) or (p2HandRes[0] == 1 and p2HandRes[17] == 1):
		if p1HandRes[0] == 1 and p2HandRes[0] == 1:
			if p1HandRes[17] > p2HandRes[17]: return 1
			else: return 2
		elif p1HandRes[0] == 1: return 1
		else: return 2
	#4K
	elif p1HandRes[16] + p2HandRes[16] > 0:
		if p1HandRes[16] > p2HandRes[16]: return 1
		else: return 2
	#FH
	elif (p1HandRes[15] > 0 and p1HandRes[14][0] > 0) or (p2HandRes[15] > 0 and p2HandRes[14][0] > 0):
		if p1HandRes[15] > p2HandRes[15]: return 1
		else: return 2
	#F
	elif p1HandRes[0] + p2HandRes[0] > 0:
		if p1HandRes[0] > p2HandRes[0]: return 1
		elif p1HandRes[0] < p2HandRes[0]: return 2
		else: pokerCheckHigh(p1HandRes[1:14],p2HandRes[1:14]) #HighCard
	#S
	elif p1HandRes[17] + p2HandRes[17] > 0:
		if p1HandRes[17] > p2HandRes[17]: return 1
		elif p1HandRes[17] < p2HandRes[17]: return 2
		else: return 0 #Same numbers in the straight, which shouldn't happen in this case.
	#3K
	elif p1HandRes[15] + p2HandRes[15] > 0:
		if p1HandRes[15] > p2HandRes[15]: return 1
		else: return 2
	#2P/P
	elif p1HandRes[14][0] > 0 or p2HandRes[14][0] > 0:
		if p1HandRes[14][1] <> 0 and p2HandRes[14][1] == 0: return 1
		elif p1HandRes[14][1] == 0 and p2HandRes[14][1] <> 0: return 2
		elif max(p1HandRes[14]) > max(p2HandRes[14]): return 1
		elif max(p1HandRes[14]) < max(p2HandRes[14]): return 2
		elif min(p1HandRes[14]) > min(p2HandRes[14]): return 1
		elif min(p1HandRes[14]) < min(p2HandRes[14]): return 2
		else: return pokerCheckHigh(p1HandRes[1:14],p2HandRes[1:14]) #HighCard			
	#H
	return pokerCheckHigh(p1HandRes[1:14],p2HandRes[1:14]) #HighCard
	#UhOh
	return 0
		
def pokerCheckStraight(arr):
	for i in range(1,9):
		if arr[i] == 1:
			straight = i+4
			for j in range(1,5):
				if arr[i+j] <> 1: return 0
			else: return straight
		elif arr[i] > 1: return 0
	return 0
	
def pokerCheck4OfAKind(arr):
	for i in range(1,14):
		if arr[i] == 4: return i
	return 0
	
def pokerCheck3OfAKind(arr):
	for i in range(1,14):
		if arr[i] == 3: return i
	return 0
	
def pokerCheckPairs(arr):
	pairs = [0,0]
	for i in range(1,14):
		if arr[i] == 2:
			if pairs[0] == 0: pairs[0] = i
			else:
				pairs[1] = i
				break
	return pairs
	
def pokerCheckHigh(arr1,arr2):
	p1Count = 0
	p2Count = 0
	for i in range(0,13):
		p1Count += arr1[i]
		p2Count += arr2[i]
		if p1Count == 5 and p2Count == 5: return 0
		elif p1Count == 5: return 2
		elif p2Count == 5: return 1
	else: return 0
	

def recCycles(i=1000):
	y = 1
	m = 0
	z = 0
	#for x in range(2,i):
	x = 2
	while x < i:
		count = 1
		n = y
		n *= 10
		n %= x
		while n <> y and n > 0 and count < i:
			count += 1
			n *= 10
			n %= x
		if count > m and count < i and n <> 0:
			m = count
			z = x
			print z,m
		x += 1
	return z
			
def goldbachOC():
	x = 33
	primes = getListOfPrimes()
	while x >= 33:
		if not inPrimeList(x):
			for prime in primes:
				if prime > x: break
				else:
					y = Math.Sqrt((x-prime)/2)
					if Math.Sqrt(y) <> ((int)Math.Sqrt(y)): return x
		"""if not inPrimeList(x):
			print x
			works = 0
			for i in range(0,x):
				y = i**2
				if y > x: break
				if inPrimeList(x-(2*(y))):
					works = 1
					break
			if works == 0: return x"""
		"""if not inPrimeList(x):
			works = 0
			z = int(math.floor(x**.5))
			for i in range(0,z):
				if inPrimeList(x-(2*(i**2))):
					works = 1
					break
			if works == 0: return x"""
		x += 2
	return x

def convOfe(x,run=1):
	if run = x: return 0
	elif run%3 = 0: return 1/((2*(run/3)
		else: 1
		
		return convOfe(x,run+1)
	
	
#print latticePaths(20,20)	
# tStart = time.time()
# #print math.sqrt(25)
# print inPrimeList(1299722)
# print str(time.time() - tStart)
tStart = time.time()
#print math.sqrt(25)
"""print hdtNums(500)
#print countingSummations(55) #hdtNums(501)"""
#print consecPrimeSum()
#print digitFactorials()
#print poker()
#print recCycles()
print goldbachOC()
print str(time.time() - tStart)
#print lexPerms(3,5)