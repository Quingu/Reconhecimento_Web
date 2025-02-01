import sys
import requests

from threading import Thread

def brute(url, wordlist_part):
    for word in wordlist_part:
        try:
            url_final = "{}/{}".format(url, word.strip())
            resposta = requests.get(url_final)
            code = resposta.status_code
            if code != 404:
                print("{} -- {}".format(url_final, code))
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print(e)
            pass

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        url = sys.argv[1]
        wordlist_file = sys.argv[2]

        with open(wordlist_file, "r") as file:
            wordlist = file.readlines()

        # Configuração das threads
        num_threads = 5  # Número de threads
        chunk_size = len(wordlist) // num_threads  # Divisão da wordlist em partes iguais
        threads = []

        for i in range(num_threads):
            # Divisão da wordlist para cada thread
            start = i * chunk_size
            if i == num_threads - 1:  # Última thread pega o restante
                end = len(wordlist)
            else:
                end = start + chunk_size

            wordlist_part = wordlist[start:end]

            thread = Thread(target=brute, args=(url, wordlist_part))
            threads.append(thread)

        # Inicia as threads
        for thread in threads:
            thread.start()

        # Aguarda todas as threads finalizarem
        for thread in threads:
            thread.join()

        print("Todas as threads foram finalizadas.")
    else:
        print("Usage: python dirbrute.py http://www.exemplo.com wordlist")
