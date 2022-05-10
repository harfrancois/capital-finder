from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "name" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["name"])
            data = r.json()
            country = data.data.name[0]
            capital = data.data.capital[0]
            # definitions = []
            # for word_data in data:
            #     definition = word_data["name"][0]["definitions"][0]["definition"]
            #     definitions.append(definition)
            res = f'The capital of {country} is {capital}.'
            message = str(res)

        else:
            message = "Give me a name of a country."

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return

