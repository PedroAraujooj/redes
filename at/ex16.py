import nmap
import argparse


def callbackFTP(host, result):
    try:
        script = result['scan'][host]['tcp'][21]['script']
        print(f"Linha de comando: {result['nmap']['command_line']}")
        for k, v in script.items():
            print(f"{k} -----> {v}")
    except KeyError:
        pass


class NmapScannerAsyncFTP:
    def __init__(self):
        self.portScanner = nmap.PortScanner()
        self.portScannerAsync = nmap.PortScannerAsync()

    def scanning(self):
        while self.portScannerAsync.still_scanning():
            print("Escaneando >>>>>>>>>>>")
            self.portScannerAsync.wait(5)

    def nmapScanAsync(self, hostname, port):
        try:
            print(f"Checando porta {port}...............")
            self.portScanner.scan(hostname, port)
            self.state = self.portScanner[hostname]['tcp'][int(port)]['state']
            print(f" [+] {hostname} tcp/{port} {self.state}")
            if port == '21' and self.portScanner[hostname]['tcp'][int(port)]['state'] == 'open':
                print("Checando porta ftp com scripts nmap.............")
                print("Checando ftp-anon.nse.............")
                self.portScannerAsync.scan(hostname, arguments=" -A -sV -p21 --script ftp-anon.nse",
                                           callback=callbackFTP)
                self.scanning()

                print("Checando ftp-bounce.nse.............")
                self.portScannerAsync.scan(hostname, arguments=" -A -sV -p21 --script ftp-bounce.nse",
                                           callback=callbackFTP)
                self.scanning()

                print("Checando ftp-libopie.nse.............")
                self.portScannerAsync.scan(hostname, arguments=" -A -sV -p21 --script ftp-libopie.nse",
                                           callback=callbackFTP)
                self.scanning()

                print("Checando ftp-proftpd-backdoor.nse.............")
                self.portScannerAsync.scan(hostname, arguments=" -A -sV -p21 --script ftp-proftpd-backdoor.nse",
                                           callback=callbackFTP)
                self.scanning()

                print("Checando ftp-vsftpd-backdoor.nse.............")
                self.portScannerAsync.scan(hostname, arguments=" -A -sV -p21 --script ftp-vsftpd-backdoor.nse",
                                           callback=callbackFTP)
                self.scanning()

        except Exception as e:
            print(f"Erro ao conectar com {hostname}: {e}")


if __name__ == '__main__':
    scanNmap = NmapScannerAsyncFTP()
    scanNmap.nmapScanAsync("195.234.45.114", "21")
