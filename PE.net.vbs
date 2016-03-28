REM Const total = 600851475143
REM Dim list : list = 10007
REM Dim pre : pre = 600851475142
REM Dim temp : temp = 1230

REM REM for i = 30 to 20719016384 Step 2
	REM REM if total mod i = 0 Then
		REM REM list = list + i + ","
		REM REM msgbox i
	REM REM end if
REM REM next

REM REM msgbox list

REM REM function findTopPrime(num)
	REM REM if num mod 2 = 0 Then
		REM REM 'msgbox num
		REM REM num = findTopPrime(num/2)
	REM REM Else
		REM REM temp = num/2
		REM REM for i = 3 to temp-1 Step 2
			REM REM if isPrime(i) and num mod i = 0 Then
		REM REM '		msgbox num
				REM REM num = findTopPrime(num/i)
			REM REM End If
		REM REM Next
	REM REM End If
	REM REM findTopPrime = num
REM REM End Function

REM REM 'msgbox isPrime(31623761849)
REM REM msgbox findTopPrime(total)

REM function isPrime(num)
	REM if num >= 2 Then
		REM for i = 2 to num-1
			REM if (num mod i) <> 0 Then
				REM isPrime = 0
			REM End if
		REM Next
		REM isPrime = 1
	REM else
		REM isPrime = 0
	REM End if
REM end function



REM REM sub diffSNS()
	REM REM dim sum : sum = 0
	REM REM dim sq : sq = 0
		REM REM for i = 1 to 100
			REM REM sum = sum + i
			REM REM sq = sq + i*i
		REM REM next
	REM REM sum = sum*sum
	REM REM msgbox sum - sq
REM REM end sub

REM while temp < 10001
	REM list = list + 2
	REM if isPrime(list) = 1 Then
		REM temp = temp + 1
		REM msgbox list,,temp
	REM End If
REM Wend
REM msgbox list,,temp
REM Dim numS : numS = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
REM Dim temp(1000)
REM Dim Prod : Prod = 0
REM for i = 1 to 1000
	REM temp(i) = CInt(mid(numS,i,1))
REM Next
REM for i = 0 to 995
	REM Prod = mx(Prod, (temp(i) * temp(i+1) * temp(i+2) * temp(i+3) * temp(i+4)))
REM Next
REM msgbox Prod

REM Function mx(num1,num2)
	REM if num1 > num2 Then
		REM mx = num1
	REM else
		REM mx = num2
	REM end if
REM end function

Function findPrime(target) 'Finds {target}th prime. Extends list of primes if target is beyond.
	dim filesys, primeTxt, num, aPrime, primes
	dim targetCS: targetCS = target-1
	Const ForReading = 1, ForWriting = 2, ForAppending = 8
	Const TristateFalse = 0, TristateTrue = -1, TristateUseDefault = -2
	Set filesys = CreateObject("Scripting.FileSystemObject")
	
	primes = getListOfPrimes
	x = uBound(primes)
	
	Set primeTxt = filesys.OpenTextFile("C:\Users\jon.mcbride\Documents\CodingPractice\listOPrimes.txt", ForAppending, False, TristateFalse)
	
	num = primes(x) + 2
	
	If x < targetCS Then
		redim preserve primes(targetCS)
	End If
	
	'primeTxt.WriteLine ""
	Do While x < target 'Extends list of primes
		aPrime = True
		For each prime in primes
			If prime = 0 Then
				Exit For 'Exits when the list is complete
			ElseIf num mod prime = 0 Then
				aPrime = False
				Exit For 'Exits if not Prime
			End If
		Next
		If aPrime = True Then 'Only runs if Prime
			primeTxt.WriteLine ""
			primes(x) = num
			primeTxt.Write primes(x)
			x = x+1
		End If
		num = num+2
	Loop
	primeTxt.Close()
	Set primeTxt = nothing
	Set filesys = nothing
	
	findPrime = primes(targetCS)
End Function

REM Sub extendPrimeList(target)
	REM dim filesys, primeTxt, num, aPrime, primes REM(10000)
	REM REM dim  x: x = 0
	REM Const ForReading = 1, ForWriting = 2, ForAppending = 8, targetCS = target-1
	REM Set filesys = CreateObject("Scripting.FileSystemObject") 
	REM REM Set primeTxt = filesys.OpenTextFile("C:\Users\jon.mcbride\Documents\CodingPractice\listOPrimes.txt", ForReading)
	
	REM REM Do Until primeTxt.AtEndOfStream
		REM REM num = primeTxt.ReadLine
		REM REM If num <> "" Then
			REM REM primes(x) = num
			REM REM x = x + 1
		REM REM End If
	REM REM Loop
	REM REM primeTxt.close()
	REM REM Set primeTxt = nothing
	
	REM primes = getListOfPrimes
	REM x = uBound(primes)
	
	REM num = primes(x)
	REM If num < target Then
	
		REM Set primeTxt = filesys.OpenTextFile("C:\Users\jon.mcbride\Documents\CodingPractice\listOPrimes.txt", ForAppending, False, True)
		
		REM primeTxt.WriteLine ""
		REM REM primeTxt.WriteLine ""
		REM num = num + 2
		REM If x < targetCS Then
			REM redim preserve primes(targetCS)
		REM End If
		
		REM Do While x < target REM 10001
			REM aPrime = True
			REM For each prime in primes
				REM If prime = 0 Then
					REM Exit For 'Exits when the list is complete
				REM ElseIf num mod prime = 0 Then
					REM aPrime = False
					REM Exit For 'Exits if not Prime
				REM End If
			REM Next
			REM If aPrime = True Then 'Only runs if Prime
				REM primes(x) = num
				REM primeTxt.WriteLine primes(x)
				REM x = x+1
			REM End If
			REM num = num+2
		REM Loop
		REM primeTxt.Close()
		REM Set primeTxt = nothing
		REM Set filesys = nothing
	REM End If
	
	REM findPrime = primes(targetCS)
	REM REM msgbox primes(10000)
REM End Sub

msgbox findPrime(112119)

function getListOfPrimes() 'returns my external list of prime numbers
	dim filesys, primeTxt, primes
	Const ForReading = 1, ForWriting = 2, ForAppending = 8
	Set filesys = CreateObject("Scripting.FileSystemObject") 
	Set primeTxt = filesys.OpenTextFile("C:\Users\jon.mcbride\Documents\CodingPractice\listOPrimes.txt", ForReading)
	
	primes = split(primeTxt.ReadAll,vbCrLf)
	primeTxt.close()
	Set primeTxt = nothing
	Set filesys = nothing
	
	getListOfPrimes = primes
End function

function pokerHands()
	Const ForReading = 1, ForWriting = 2, ForAppending = 8
	dim filesys, handsTxt, hands, p1hand(4), p2hand(4),winner
	dim p1: p1 = 0
	dim p2: p2 = 0
	Set filesys = CreateObject("Scripting.FileSystemObject") 
	Set handsTxt = filesys.OpenTextFile("C:\Users\jon.mcbride\Documents\CodingPractice\poker.txt", ForReading)
	
	Do Until handsTxt.EndOfFile
		hands = split(handsTxt.ReadLine," ")
		for i = 0 to 9
			if i < 5 Then
				p1hand(i) = hands(i)
			else
				p2hand(i-5) = hands(i)
			end if
		next
			
		if checkHand(p1hand) > checkHand(p2hand) Then
			p1 = p1 + 1
		else
			p2 = p2 + 1
		end if
	Loop
	
	hands.close()
	Set hands = nothing
	Set filesys = nothing
	
	pokerHands = p1
end function

REM function checkHand(hand)
	REM dim cards(4,1), flush, values(14), score = 0
	REM flush = true
	REM straight = -1
	REM count = 5
	
	REM for i = 0 to 4
		REM cards(i,0) = left(hand(i),len(hand(i))-1)
		REM cards(i,1) = right(hand(i),1)
		REM if i > 0 && !cards(i,1).equals(cards(0,1)) Then
			REM flush = false
		REM end if
		REM value = cards(i,0)
		REM select value
			REM case "2","3","4","5","6","7","8","9","10"
				REM values(CInt(value)) = values(CInt(value)) + 1
			REM case "J"
				REM values(11) = values(11) + 1
			REM case "Q"
				REM values(12) = values(12) + 1
			REM case "K"
				REM values(13) = values(13) + 1
			REM case "A"
				REM values(14) = values(14) + 1
		REM end select	
	REM next
	
	REM for n = 2 to 14
		
		REM count = count - values(n)
	REM if flush then
		REM score = score * 1000
REM end function


sub reciprocalCycles():
	Const ForReading = 1, ForWriting = 2, ForAppending = 8
	dim filesys, fo
	Set filesys = CreateObject("Scripting.FileSystemObject") 
	Set fo = filesys.OpenTextFile("C:\Users\jon.mcbride\Documents\CodingPractice\ReciprocalCycles.txt",ForWriting, False, True)
	
	for i = 1 to 1000
		fo.writeLine(i)
		fo.writeLine(1.000000000000000/i)
	next
	fo.close()
	set fo = nothing
	set filesys = nothing
end sub
	
reciprocalCycles()

