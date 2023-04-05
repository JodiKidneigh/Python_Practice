def raindrops(number):
    factors = False
    if number % 3 == 0:
        print("Pling")
        factors = True

    if number % 5 == 0:
        print("Plang")
        factors = True
        
    if number % 7 == 0:
        print("Plong")
        factors = True
    
    if factors == False:
        print(str(number))


raindrops(34)
raindrops(21)
raindrops(24)
raindrops(63)
raindrops(35)