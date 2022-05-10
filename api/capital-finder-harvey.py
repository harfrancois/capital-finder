from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # /api/capital?name=
        if 'name' in dic:
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + dic['name'])
            data = r.json()
            # target data we want
            country = str(data[0]['name']['common'])
            capital = str(data[0]['capital'][0])
            # reply to request
            rep = f'The capital of {country} is {capital}.'
            message = str(rep)
        # /api/capital?capital=
        elif 'capital' in dic:
            url = 'https://restcountries.com/v3.1/capital/'
            request = requests.get(url + dic['capital'])
            data = request.json()
            # target data we want.
            country = str(data[0]['name']['common'])
            capital = str(data[0]['capital'][0])
            # reply to request
            rep = f'{capital} is the capital of {country}.'
            message = str(rep)
        else:
            message = 'Give me a name of a country or capital'

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
