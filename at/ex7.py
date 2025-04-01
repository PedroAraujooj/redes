import pcapy
import datetime

interfaces = pcapy.findalldevs()
print("Interfaces disponiveis: ")
for interface in interfaces:
    print(interface)
interface = input("Nome da Interface: ")
print("Sniffinf interface: " + interface)
cap = pcapy.open_live(interface, 65536, 1, 0)
while True:
    (header, payload) = cap.next()
    if header is not None:
        print(f"{datetime.datetime.now()}: capturado {header.getlen()} bytes")
        try:
            cap.sendpacket(payload)
            print(f" >>>> Pacote reinjetado")
        except Exception as e:
            print(f"Erro ao reinjetar pacote: {e}")

