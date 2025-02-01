from urllib import request, parse

cabecalho = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0",
             "Cookie": "PHPSESSID=1k49mtbee0d1hnd8uhsrjj8iq1"}

dados ={"user":"admin", "password": "senhafoda"} #aqui posso por uma wordlist para ficar fazendo um bruteforce
dados = parse.urlencode(dados).encode()

req = request.Request("http://www.bancocn.com/admin/index.php",  headers=cabecalho, data=dados)
resposta = request.urlopen(req)
html = resposta.read()
print(html)