import nmap

scanner = nmap.PortScanner()

print("Seja bem vindo ao better_scanner")
print("<------------------------------------------------------------->")

ip = input("Digite o ip a ser varrido")
print("O ip digitado foi ", ip)
type(ip)

menu = input(""""\n Escolha o tipo de varredura a ser realizada
              1 -> Varredura do tipo syn
              2 -> Varredura do tipo udp
              3 -> Varredura do tipo intensa
              Digite a opção escolhida: """)
print("A opção escolhida foi", menu)

if menu == "1":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas abertas: ", scanner[ip]['tcp'].keys())
elif menu == "2":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas abertas: ", scanner[ip]['udp'].keys())
elif menu == "3":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas abertas: ", scanner[ip]['tcp'].keys())
else:
    print("Escolha uma opção valida")
