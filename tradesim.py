import json
import requests

APIURL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey="

class TradeSim():
    def __init__(self):
        self.readApikey()

    def readApikey(self):
        """
        Description:
            Reads the alpha vantage API key from a text file named APIkey.txt
        """
        keyfile = open('APIkey.txt')
        self.key = keyfile.readline()
        print(self.key)
        keyfile.close()
    
    def createTestfile(self):
        """
        Description:
            Creates a test file using the IBM stock for debugging
        """
        data = requests.get(APIURL + self.key)
        ibm = open('IBM.day', 'w')
        ibm.write(data.text)
        print(data.text)

    def getTestPrice(self, date):
        """
        Description:
            Gets the avarage stockprice for IBM on the given date.
        Paramaters:
            date: String giving the date to check given as 'yyyy-mm-dd'
        Return value:
            float: Avarage stockprice for IBM on the given date 
        """
        avarage = 0
        with open('IBM.day') as json_file:
            data = json.load(json_file)
            for price in sorted(data['Time Series (Daily)'][date])[:4]:
                avarage += float(data['Time Series (Daily)'][date][price])
            avarage /= 4
            return avarage
    
if __name__ == "__main__":
    trade = TradeSim()
    print(trade.getTestPrice("2000-04-10"))