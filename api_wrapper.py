import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

class nordnet_wrapper:
    def __init__(self):
        print("Setting up connection to Nordnet")
        self.s = requests.Session() 
        res = self.s.post('https://www.nordnet.se/api/2/login/anonymous',
            headers = {
                'Content-Type': 'application/json',
            })   
        print(res.content)
    
    def login(self):
        res = self.s.post('https://www.nordnet.se/api/2/authentication/basic/login',
            json = {
                'username': os.environ["nn_user"],
                'password': os.environ["nn_pass"]
            })
        print("Login server response: ", res.content)

        res = self.s.get('https://www.nordnet.se/oversikt')               
        print("Status code login server: ", res.status_code)
        #print("Login server response: ", res.content)
        
    def fetch_tickers_stocks(self):
        res = self.s.get('https://www.nordnet.se/api/2/instrument_search/query/stocklist?limit=100&offset=100',
            headers = {
                    'accept':	'application/json',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7',
                    'client-id': 'NEXT',
                    'content-type': 'application/x-www-form-urlencoded',
                    'DNT': '1',
                    'Origin': 'https://www.nordnet.se',
                    'Referer': 'https://www.nordnet.se/',
                    'sec-ch-ua':	'" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': 'macOS',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode':	'cors',
                    'Sec-Fetch-Site':	'same-origin',
                    'User-Agent':	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
            })
        #data = json.loads(res.content)
        print("Status code fetch tickets: ",  res.status_code)

    def fetch_tickers_etf(self):
        res = self.s.post('https://www.nordnet.se/api/2/instrument_search/query/stocklist?sort_order=asc&sort_attribute=name&limit=100&offset=0',
            headers = {
                    'accept':	'application/json',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7',
                    'client-id': 'NEXT',
                    'content-type': 'application/x-www-form-urlencoded',
                    'DNT': '1',
                    'Origin': 'https://www.nordnet.se',
                    'Referer': 'https://www.nordnet.se/',
                    'sec-ch-ua':	'" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': 'macOS',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode':	'cors',
                    'Sec-Fetch-Site':	'same-origin',
                    'User-Agent':	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
            })
        data = json.loads(res.content)
        print(data)

    def fetch_positions(self):
        res = self.s.post('https://www.nordnet.se/api/2/batch',
            headers = {
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7',
                    'DNT': '1',
                    'Origin': 'https://www.nordnet.se',
                    'Referer': 'https://www.nordnet.se/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                    'client-id': 'NEXT',
                    'content-type': 'application/json',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"macOS"'                    
            },
            json = {"batch":"[{\"relative_url\":\"accounts/2/fees_and_refunds_summary\",\"method\":\"GET\"},{\"relative_url\":\"accounts/2/positions?include_instrument_loans=true\",\"method\":\"GET\"},{\"relative_url\":\"user/settings/myEconomySelectorDiscovered\",\"method\":\"GET\"}]"}
            )
        print("Status code fetch positions: ", res.status_code)
        data = json.loads(res.content)
        print(data)

    
def main():
    nn = nordnet_wrapper()
    nn.login()
    nn.fetch_positions()

if __name__ == '__main__':
    main()

#    Accept-Encoding: 'gzip, deflate, br'
#    Accept-Language: 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7'
#    Connection: 'keep-alive'
#    #Cookie: NEXT=d1816a24938d7023094748af5462bf16656229a4; lang=sv; _csrf=q8cd7SpvQwWoBQ7WYtoP3uYM; nntheme=%7B%22a11y%22%3Afalse%2C%22dark%22%3A%22AUTO%22%2C%22osPref%22%3A%22LIGHT%22%7D; cookie_consent=analytics%2Cfunctional%2Cmarketing%2Cnecessary; _ga=GA1.2.1735222681.1653588487; _gid=GA1.2.137864750.1653588487; nn_notifications_read=6083_1653462469408; _gat_UA-58430789-7=1; NN-JWT=eyJraWQiOiJiTm1FeUFhYXgyYTg0eVRBMy0xLUZlRFdDSE5xSnBPMXhVbTBTWFhzQTVJIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJseDJzdGhsbSIsImF1ZCI6InByb2QiLCJhbXIiOiJiYXNpYyIsImF1eiI6IntcImNub1wiOjkwMDYxMTM0MyxcImNpZFwiOlwiMWQxNmI3YTgtZDM5ZS00ODI4LTk3ZjYtNDA1ODJiNTcyYmYxXCIsXCJhY2NcIjpbe1wiYW5vXCI6MTMxOTQ2MzQsXCJhaWRcIjoxfSx7XCJhbm9cIjoxNjY5MDU1NCxcImFpZFwiOjJ9LHtcImFub1wiOjIxMzU5NzczLFwiYWlkXCI6M31dfSIsImlzcyI6Imh0dHBzOlwvXC93d3cubm9yZG5ldC5zZSIsInJlZnJlc2giOiJkMTgxNmEyNDkzOGQ3MDIzMDk0NzQ4YWY1NDYyYmYxNjY1NjIyOWE0IiwiY3NyZiI6IjNiNDFiMzQ1LWUxMzktNDUwOS1iMDZmLWVkYmU2OTcxNmNiZiIsImV4cCI6MTY1MzU5MDAxOCwibGFuZyI6InN2IiwiY29yZyI6IlNFIn0.N61SvyxEXeAlIUNQbqOFOhq0eAyVi5poyIu3bVJqHiK1AcL6LTZjJq5vNpZBdlFdqvf9scbDRd1C4FN0eeuROw5oTv2REyX3biNnke4cERmanMF84U1xpmvEEeTie8V838nczFX2vCNLuyRRHrJhQvFzHflkqkORbEeYpo3L8v14E5Ti4r-gjBa6mRH18VYjiWr60SvG9X5ht7u5eBteLk_OBjHXpdFK-m5_BD8nlAppeyhLvhHNzxG-KkAxvKkF6k5HJDzourXwwATljssFK12nYZTNt4SACNr8-8itvJWzD-dHpU5qVZBX2OYvgBckRtqCeGXiYMSVmqQqAQv3uA
#    Cookie: next_token
#    DNT: 1
#    Host: www.nordnet.se
#    Referer: https://www.nordnet.se/
#    Sec-Fetch-Dest: empty
#    Sec-Fetch-Mode: cors
#    Sec-Fetch-Site: same-origin
#    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36
#    accept: application/json
#    client-id: NEXT
#    ntag: 3b41b345-e139-4509-b06f-edbe69716cbf
#    sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
#    sec-ch-ua-mobile: ?0
#    sec-ch-ua-platform: "macOS"
#    x-nn-href: https://www.nordnet.se/marknaden/aktiekurser/16100594-lundin-energy?accid=2


