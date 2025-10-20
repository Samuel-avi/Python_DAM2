texto = input("Escribe un texto: ")

texto_hacker = (texto
                .replace("a", "4").replace("A", "4")
                .replace("e", "3").replace("E", "3")
                .replace("i", "1").replace("I", "1")
                .replace("o", "0").replace("O", "0"))

print("Texto en estilo hacker:", texto_hacker)