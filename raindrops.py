def raindrops(number):
    rain_sound = ""
    if number % 3 == 0:
        rain_sound += "Pling"

    if number % 5 == 0:
        rain_sound += "Plang"
       
    if number % 7 == 0:
        rain_sound += "Plong"
            
    if rain_sound == "":
        rain_sound += str(number)
    
    print(rain_sound)


raindrops(34)
raindrops(21)
raindrops(24)
raindrops(63)
raindrops(35)