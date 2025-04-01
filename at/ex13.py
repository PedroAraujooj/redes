import dns.resolver
import subprocess


def run_dnsrecon(domain):
    cmd = ["dnsrecon", "-d", domain, "-t", "std"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Saída do dnsrecon para o host {domain}:")
    print(result.stdout)


if __name__ == '__main__':
    host = 'example.com'
    records = ['A', 'AAAA', 'MX', 'NS', 'SOA', 'TXT']
    for record in records:
        try:
            responses = dns.resolver.resolve(host, record)
            print('\n Registros', record)
            for response in responses:
                print(f'       {response}')
        except Exception as e:
            print("Canot resolve query for record ", record)
            print('Error obtaining information: ', e)
    run_dnsrecon(host)
