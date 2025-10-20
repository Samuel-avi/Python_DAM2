cont = 0
while True:
    pass1 = input("contraseña: ")
    pass2 = input("repetir contraseña: ")
    if pass1 == pass2:
        break
    else:
        print("las contraseñas no coinciden")
        cont += 1
              
print(cont)
