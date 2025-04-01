import argparse
import nmap


def callbackResult(host, scan_result):
    port_state = scan_result['scan'][host]['tcp']
    print(f"Linha de comando: {scan_result['nmap']['command_line']}")
    for k, v in port_state.items():
        print(f'Porta {k} ----> {v}')


class NmapScannerAsync:
    def __init__(self):
        self.portScannerAsync = nmap.PortScannerAsync()

    def scanning(self):
        while self.portScannerAsync.still_scanning():
            print("Escaneando >>>>>")
            self.portScannerAsync.wait(5)

    def nmapScanAsync(self, hostname, port):
        try:
            print(f"Checando porta {port} (assíncrono) ..........................")
            self.portScannerAsync.scan(hostname, arguments="-A -sV -p " + str(port), callback=callbackResult)
            self.scanning()
        except Exception as e:
            print(f"Erro ao conectar com {hostname}: {e}")


class NmapScanner:
    def __init__(self):
        self.portScanner = nmap.PortScanner()

    def nmapScan(self, ip_address, port):
        self.portScanner.scan(ip_address, port)
        if ip_address not in self.portScanner.all_hosts():
            print(f'[-] Host {ip_address} não está acessível ou não foi encontrado pelo nmap.')
            return
        if 'tcp' not in self.portScanner[ip_address]:
            print(f'[-] Nenhuma informação TCP para {ip_address}.')
            return

        port_state = self.portScanner[ip_address]['tcp'].get(int(port), {})
        state = port_state.get('state', 'desconhecido')
        print(f'[+] Executando comando: {self.portScanner.command_line()}')
        print(f'[+] Scanning: {ip_address} tcp/{port} {state}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scanner Nmap síncrono e assíncrono')

    parser.add_argument('--ip_address',
                        help='Endereço de IP para o scanner síncrono (opcional, só se quiser rodar modo síncrono).')
    parser.add_argument('--ports',
                        help='Portas separadas por vírgula para scanner síncrono. Ex: 21,22,25,80 (opcional).')

    parser.add_argument('--host',
                        help='IP/domínio para o scanner assíncrono (opcional, só se quiser rodar modo assíncrono).')
    parser.add_argument('--async_ports', default='80,8080',
                        help='Portas separadas por vírgula para scanner assíncrono. Ex: 21,22,25,80. Default=80,8080.')

    args = parser.parse_args()

    if args.ip_address and args.ports:
        print("PART SINCRONA =====================================>>>>")
        sync_ports = args.ports.split(',')
        for p in sync_ports:
            NmapScanner().nmapScan(args.ip_address, p)
    else:
        print("[!] Modo síncrono não executado (faltando --ip_address ou --ports).")

    if args.host:
        print("PART ASSINCRONA =====================================>>>>")
        async_ports = args.async_ports.split(',')
        for p in async_ports:
            NmapScannerAsync().nmapScanAsync(args.host, p)
    else:
        print("[!] Modo assíncrono não executado (faltando --host).")
