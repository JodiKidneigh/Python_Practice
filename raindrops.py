def raindrops(number):
    drops = [(3, "Pling"), (5,"Plang"), (7,"Plong")]  
    sounds = [drop for factor, drop in drops if number % factor == 0]
            
    return ''.join(sounds) or str(number)
    
   


print(raindrops(34))
print(raindrops(21))
print(raindrops(24))
print(raindrops(63))
print(raindrops(135))