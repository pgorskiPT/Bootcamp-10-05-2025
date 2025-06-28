import time
import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"


def multiple_requests():
    start_time = time.time()
    for _ in range(100):  # 0..99
        r = requests.get(url)
        # print(r.json())

    elapsed_time = time.time() - start_time
    print(f"Requests time: {elapsed_time}")


multiple_requests()
# Requests time: 6.27962589263916
# dla 1 -> Requests time: 0.06939220428466797

# Biblioteka	Asynchroniczność	Wydajność (przy wielu zapytaniach)	Łatwość użycia	HTTP/2
# requests	    Nie             	Średnia	                            Bardzo łatwa	Nie
# httpx	        Tak             	Wysoka	                            Łatwa	        Tak
# aiohttp	    Tak	                Wysoka	                            Średnia	        Tak
# urllib3	    Nie             	Wysok (w synchronicznym środowisku)	Łatwa	        Tak
# grequests	    Nie                 (ale równoległe)  Wysoka	        Łatwa	        Nie