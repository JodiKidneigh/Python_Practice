def raindrops(number):
    rain_sound = ""
    drops = ["Pling", "Plang", "Plong"]
    factors = [3, 5, 7]
    for (index, factor) in enumerate(factors):
        if number % factor == 0:
            rain_sound += drops[index]
            
    return rain_sound if rain_sound else str(number)
    
   


print(raindrops(34))
print(raindrops(21))
print(raindrops(24))
print(raindrops(63))
print(raindrops(135))