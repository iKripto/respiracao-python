import time

def respirar():
    while True:
        for i in range(4, 0, -1):  
            print(f"\nInspire pelo nariz por {i} segundos.")
            time.sleep(1)

        for i in range(7, 0, -1):  
            print(f"Segure a respiração por {i} segundos.")
            time.sleep(1)

        for i in range(8, 0, -1):  
            print(f"Expire lentamente pela boca por {i} segundos.")
            time.sleep(1)

        opcao = input("\nRepetir? (s/n): ").strip().lower()
        if opcao != 's':
            print("Programa encerrado!")
            break
respirar()
