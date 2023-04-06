def raindrops(number):
    rain_sound = ""
    drops = [(3, "Pling"), (5,"Plang"), (7,"Plong")]
    
    for factor, drop in drops:
        if number % factor == 0:
            rain_sound += drop
            
    return rain_sound or str(number)
    
   


print(raindrops(34))
print(raindrops(21))
print(raindrops(24))
print(raindrops(63))
print(raindrops(135))