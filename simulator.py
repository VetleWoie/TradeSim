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

    def purchase(self, symbol, amount, date):
        pass
    
if __name__ == "__main__":
    trade = TradeSim()