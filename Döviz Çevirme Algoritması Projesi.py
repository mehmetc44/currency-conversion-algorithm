import requests
from bs4 import BeautifulSoup

HTML = requests.get("https://canlidoviz.com/").content
soup = BeautifulSoup(HTML, "html.parser")
class Currency:
    def GetInput(self):
        print('''
Turkish Lira : TL
Dolar : USD 
Strerlin : GBP
Euro : EUR
Swiss Frang : CHF
        ''')
        self.birimler = (input('Çevrilecek Para Birimi: '),input('Neye çevrilcek: '))


    def Result(self):

        (ilk, ikinci) = self.birimler

        degerler = soup.find_all("td",{"class":"canli text-mobile-value"})
        dolar =    float(str(degerler[0]).split(">")[1].split("<")[0])
        euro =     float(str(degerler[1]).split(">")[1].split("<")[0])
        sterlin =  float(str(degerler[4]).split(">")[1].split("<")[0])
        frang =    float(str(degerler[14]).split(">")[1].split("<")[0])

        a = int(input(f'Kaç {ilk}\'i {ikinci}\'ye çevirmek istersiniz?: '))
        if ilk == 'USD':

            if ikinci == 'TL':
                print(dolar * a)
            elif ikinci == 'EUR':
                print (dolar / euro * a)
            elif ikinci == 'GBP':
                print(dolar / sterlin * a)
            elif ikinci == 'CHF':
                print(dolar / frang * a)
        elif ilk == 'EUR' :
            if ikinci == 'TL':
                print(euro * a)
            elif ikinci == 'USD':
                print (euro / dolar * a)
            elif ikinci == 'GBP':
                print( euro / sterlin * a)
            elif ikinci == 'CHF':
                print(euro / frang * a)
        elif ilk == 'GBP':
            if ikinci == 'TL':
                print(sterlin * a)
            elif ikinci == 'USD':
                print (sterlin/ dolar * a)
            elif ikinci == 'EUR':
                print( sterlin / euro * a)
            elif ikinci == 'CHF':
                print(sterlin / frang * a)
        elif ilk == 'CHF':
            if ikinci == 'TL':
                print(frang * a)
            elif ikinci == 'USD':
                print (frang / dolar * a)
            elif ikinci == 'GBP':
                print( frang / sterlin * a)
            elif ikinci == 'EUR':
                print( frang / euro * a)
        elif ilk == 'TL':
            if ikinci == 'EUR':
                print(1 / euro)
            elif ikinci == 'USD':
                print (1 / dolar * a)
            elif ikinci == 'GBP':
                print( 1 / sterlin * a)
            elif ikinci == 'CHF':
                print( 1 / frang * a)
x = Currency()
x.GetInput()
x.Result()