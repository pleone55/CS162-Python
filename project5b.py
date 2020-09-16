# from twilio.rest import Client

# def read_script(text_file):
#     accountSID = 'AC0c718cef2b266b5482d7262b7d8d553e'
#     authToken = '72caf7f614294b0e2aedde0dfc5942ad'

#     twilioCli = Client(accountSID, authToken)
#     myTwilioNumber = '+14087073220'
#     myCellPhone = '+19095601086'
    
#     with open('script.txt', 'rt') as f:
#         for line in f:
#             for word in line.split():
#                 message = twilioCli.messages.create(body=word, from_=myTwilioNumber, to=myCellPhone)

# read_script('script.txt')

import json

class NobelData:
    def __init__(self, filename='nobels.json'):
        self._filename = filename
        self._nobels_list = []
    
        with open(filename, 'r') as f:
            self._nobels_list = json.load(f)
    
    def get_file(self):
        return self._nobels_list
    
    def search_nobels(self, year, category):
        surnames = []
        
        for i in self._nobels_list["prizes"]:
            if i['year'] == year and i['category'] == category:
                for j in i['laureates']:
                    s = j['surname']
                    surnames.append(s)
        surnames.sort()
        return surnames

def main():
    n1 = NobelData()
    result = n1.search_nobels("1903", "physics")
    print(result)

if __name__=="__main__()": main()
main()