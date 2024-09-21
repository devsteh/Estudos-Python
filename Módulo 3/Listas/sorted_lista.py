frutas = ["laranja", "uva", "limão", "abacaxi", "melancia"]
print(sorted(frutas, key=lambda x: len(x))) #['uva', 'limão', 'laranja', 'abacaxi', 'melancia']

print(sorted(frutas, key=lambda x: len(x), reverse=True)) #['melancia', 'laranja', 'abacaxi', 'limão', 'uva']
