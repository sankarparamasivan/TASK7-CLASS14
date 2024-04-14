import requests


class Users:
    def __init__(self, url):        
        self.url = url
        self.response = requests.get(url)
   
    def isConnected(self):
        if self.response.status_code == 200:
            return True
        return False


    def fetchData(self):
        try:
            if self.isConnected():
                return self.response.json()
            raise Exception()
        except:
            print("It is not connected")
            return None
            
            
    def getBreweries(self):
        BreweriesList = []
        if not self.fetchData() is None:
            for userDict in self.fetchData():
                 if (userDict.get("Breweries",None)) is not None:
                     for user in userDict.get("Breweries").values():
                         print(user.get("name"))
            return BreweriesList
        else:
            print("It is not connected")
       


url = "https://www.openbrewerydb.org/breweries/United%20States/New%20York"
userObj = Users(url)
print(userObj.getBreweries())
