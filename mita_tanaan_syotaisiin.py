# Feedparser import lukemaan rss:sää ja os import tyhjentämään cmd:tä, jotta lista näkyy nätimmin
import feedparser
import os

# RSS-tilaukset ruokalistoille
url_piato = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1408&language=fi"
url_maija = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1402&language=fi"
url_tilia = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1413&language=fi"
url_lozzi = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1401&language=fi"
url_belvedere = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1404&language=fi"
url_syke = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1405&language=fi"
url_uno = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1414&language=fi"
url_ylisto = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1403&language=fi"
url_kvarkki = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=140301&language=fi"
url_rentukka = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1416&language=fi"
url_novelli = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1409&language=fi"
url_normaalikoulu = "https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1411&language=fi"
url_taide = "https://www.foodandco.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=0301&language=fi"
url_fiilu = "https://www.foodandco.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=3364&language=fi"

# Tulostaa ravintolan nimen ja ruokalistan
def tulostaRavintola(url):
    os.system('cls')
    koko_feed = feedparser.parse(url)
    ravintolan_nimi = koko_feed.feed.title
    print(ravintolan_nimi + '\n')
    ruokalista = koko_feed.entries[0].summary.replace('<br />', '')
    if len(ruokalista) == 0:
        print("Ei ruokalistaa saatavilla \n")
        return
    print(ruokalista)
    return

# Infon tulostaminen
def tulostaInfo():
    os.system('cls')
    print("Tervetuloa käyttämään ruokalistaohjelmaa! \nOhjelman tarkoituksena on kertoa käyttäjälle, mitä missäkin Jyväskylän opiskelijaravintolassa on tänään ruokana. \nRuokalistan saat esille kirjoittamalla ravintolan nimen.\nOhjelman voi lopettaa komennolla \"poistu\" ja tämän inforuudun saa näkyviin komennolla \"info\" \nMukana olevat ravintolat: \n - Maija\n - Piato\n - Tilia\n - Lozzi\n - Belvedere\n - Syke\n - Uno\n - Ylistö\n - Kvarkki\n - Rentukka\n - Novelli\n - Normaalikoulu\n - Taide\n - Fiilu" '')
    return

# Pääohjelma, joka kyselee ravintoloita ja pitää huolen käyttäjän syötteestä
def main():
    tulostaInfo()
    while (True):
        ravintola = input("Kirjoita ravintolan nimi: ")
        ravintola.lower().strip()
        match ravintola:
            case 'poistu':
                break
            case 'info':
                tulostaInfo()
            case 'piato':
                tulostaRavintola(url_piato)
            case 'maija':
                tulostaRavintola(url_maija)
            case 'tilia':
                tulostaRavintola(url_tilia)
            case 'lozzi':
                tulostaRavintola(url_lozzi)
            case 'belvedere':
                tulostaRavintola(url_belvedere)
            case 'syke':
                tulostaRavintola(url_syke)
            case 'uno':
                tulostaRavintola(url_uno)
            case 'ylistö':
                tulostaRavintola(url_ylisto)
            case 'kvarkki':
                tulostaRavintola(url_kvarkki)
            case 'rentukka':
                tulostaRavintola(url_rentukka)
            case 'novelli':
                tulostaRavintola(url_novelli)
            case 'normaalikoulu':
                tulostaRavintola(url_normaalikoulu)
            case 'taide':
                tulostaRavintola(url_taide)
            case 'fiilu':
                tulostaRavintola(url_fiilu)
            case _:
                print("tapa ittes")

        

if __name__=="__main__":
    main()