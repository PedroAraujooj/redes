import re
import requests
import sys
import os
import argparse
import time
import optparse


def fuzz(url, custonWordlist):
    results = []
    if custonWordlist:
        words = [w.strip() for w in open(str(custonWordlist), "rb").readlines()]
    else:
        words = [w.strip() for w in open(wordlist["dict"], "rb").readlines()]
    try:
        if not url.startswith("http://"):
            url = "http://" + url
        for paths in words:
            paths = paths.decode()
            if not paths.startswith("/"):
                paths = "/" + paths
            fullPath = url + paths
            print(fullPath)
            response = requests.get(fullPath)
            code = response.status_code
            print(f"[+] [{time.strftime('%H:%M:%S')}] - [{code}] - {paths} -> {fullPath}")

            if code == 200:
                results.append(fullPath)
        ok_results(results)
    except Exception as e:
        print(f"ERRO ==> {e}")


def ok_results(results):
    print('200 OK results')
    print('---------------')
    for result in results:
        print(f"[+] - [200] - {result}")


def main():
    pars = optparse.OptionParser(description="[+] Descobrindo arquivos e diretorios ocultos")
    pars.add_option('-u', '--url', action="store", dest="url", type="string", help='URL do target', default=None)
    pars.add_option('-w', '--word', action="store", dest="wordlist", type="string", help='Wordlist customizada',
                    default=None)

    opts, args = pars.parse_args()
    if not opts.url:
        pars.print_help()
    if not opts.wordlist:
        if not os.path.isfile(opts.wordlist):
            print("[!] Confira sua wordlist")
    fuzz(opts.url, opts.wordlist)


if __name__ == '__main__':
    main()
