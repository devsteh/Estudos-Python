frutas = ["laranja", "uva", "limão", "abacaxi", "melancia"]
frutas.sort() # ["limão", "melancia", "abacaxi", "uva", "laranja"]
frutas = ["laranja", "uva", "limão", "abacaxi", "melancia"]
frutas.sort(reverse=True) # ["laranja", "uva", "abacaxi", "melancia", "limão"]
frutas = ["laranja", "uva", "limão", "abacaxi", "melancia"]
frutas.sort(key=lambda x: len(x)) # ["limão", "uva", "abacaxi", "laranja", "melancia"]
frutas = ["laranja", "uva", "limão", "abacaxi", "melancia"]
frutas.sort(key=lambda x: len(x), reverse=True) # ["laranja", "melancia","abacaxi", "uva", "limão"]

