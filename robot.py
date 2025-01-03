from dotenv import load_dotenv # Funkce, která načte údaje ze souboru .env do environmentu (prostředí)
import selenium # Knihovna, která podporuje práci s weby
import selenium.webdriver # Podknihovna od knihovny selenium, která dovoluje použít prohlížeč Chrome
from selenium.webdriver.common.by import By # Podknihovna od knihovny selenium, která dovoluje vyhledávat HTML elementy
import datetime # Knihovna, která umožňuje práci s časem
import os # Systémová knihovna


load_dotenv() # Načte údaje ze souboru .env do environmentu (prostředí)

"""
os.environ["JMENO_ROBOTA"] - Načte hodnotu konstanty JMENO_ROBOTA z environmentu (prostředí)

Pokud je v .env definováno JMENO_ROBOTA jako:
JMENO_ROBOTA="Pepa"

tak os.environ["JMENO_ROBOTA"] vrátí string Pepa.
"""

# Deklarujeme konstanty v programu z údajů v environmentu (prostředí), které načetla předchozí funkce
JMENO_ROBOTA = os.environ["JMENO_ROBOTA"]
HESLO_ROBOTA = os.environ["HESLO_ROBOTA"]
STUL = os.environ["STUL"]

# Deklarujeme prohlížeč
while True: # Smyčka pro dialog uživatele
    odpoved = input("Spustit okno prohlížeče (1), nebo spustit pouze v konzoli (2)? (vyber čislo 1 nebo 2): ").strip() # .strip() odebere případné mezery
    if odpoved == "1": # Chceme
        prohlizec = selenium.webdriver.Chrome() # V tomto případě prohlížeč Chrome (Chromium) - nepotřebujeme nastavení, protože žádné speciální nevyužíváme.
        break
    elif odpoved == "2": # Nechceme
        nastaveni_prohlizece = selenium.webdriver.chrome.options.Options() # Inicializuje nastavení prohlížeče Chrome (Chromium)
        nastaveni_prohlizece.add_argument("--headless") # Přidá argument headless = okno prohlížeče se neotevře, poběží pouze v konzoli
        prohlizec = selenium.webdriver.Chrome(options=nastaveni_prohlizece) # V tomto případě prohlížeč Chrome (Chromium) s naším nastavením
        break
    else:
        print("Neplatná volba!")

prohlizec.set_page_load_timeout(30) # Nastaví čas, jak dlouho bude prohlížeč čekat na načtení stránky před tím, než zahlásí chybu. 30 = 30 sekund.
prohlizec.implicitly_wait(20)# Nastaví čas, jak dlouho bude prohlížeč čekat na nalezení nějakého HTML elementu před tím, než zahlásí chybu. 20 = 20 sekund.

# Nastavíme vypisovat_info na True nebo False podle toho, jestli chceme vypisovat info nebo ne.
while True: # Smyčka pro dialog uživatele
    odpoved = input("Chcete vypisovat informace do konzole? (napiš A pro ano nebo N pro ne): ").strip().upper() # .strip() odebere případné mezery a .upper() převede text do velkých písmen
    if odpoved == "A" or odpoved == "T": # Chceme
        vypisovat_info = True
        break
    elif odpoved == "N" or odpoved == "F": # Nechceme
        vypisovat_info = False
        break
    else:
        print("Neplatná volba!")

# Deklarace globálních proměnných
cas_posledni_zpravy = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), "%H:%M:%S") # Nastaví čas poslední zprávy na aktuální čas ve formátu H:M:S (Alík používá H:M:S)

def vypsat(info):
    """Funkce, která vypíše info do konzole jen pokud si to uživatel vybral"""
    global vypisovat_info # Použije globální proměnnou
    if vypisovat_info:
        print(info)

def prihlasit():
    """Funkce, ve které se robot přihlásí pomocí prohlížeče na Alík.cz za použití jména a hesla. Poté si přisedne ke stolu."""

    vypsat("Přihlašování...")
    
    prohlizec.get("https://www.alik.cz/prihlasit") # Přesměruje se na stránku přihlášení

    prihlasovaci_pole_jmeno = prohlizec.find_element(By.CSS_SELECTOR, '#login') # Najde na stránce přihlašovací pole pro zadání uživatelského jména díky CSS selectoru '#login'
    prihlasovaci_pole_jmeno.send_keys(JMENO_ROBOTA) # Napíše hodnotu uloženou v konstantě JMENO_ROBOTA do přihlašovacího pole

    prihlasovaci_pole_heslo = prohlizec.find_element(By.CSS_SELECTOR, '#heslo') # Najde přihlašovací pole pro zadání uživatelského hesla
    prihlasovaci_pole_heslo.send_keys(HESLO_ROBOTA) # Napíše hodnotu uloženou v konstantě HESLO_ROBOTA do přihlašovacího pole

    tlacitko_prihlaseni = prohlizec.find_element(By.CSS_SELECTOR, '.tlacitko') # Najde tlačítko na přihlášení
    tlacitko_prihlaseni.click() # Klikne na tlačítko

    prohlizec.get(STUL) # Přesměruje prohlížeč na URL stolu - robot je již přihlášený, takže si ke stolu přisedne.
    vypsat("Přihlášeno!")

    ahoj = "Ahoj! Úspěšně připojeno :D"
    odeslat_odpoved(ahoj)

def ziskat_zpravy():
    """
    Načte nové nezpracované zprávy z chatu
    """

    global cas_posledni_zpravy # Použije globální proměnnou

    zpravy = prohlizec.find_elements(By.CSS_SELECTOR, "#chatOkno > p.c-1") # Najde všechny elementy zpráv
    pole_zprav = []
    novy_cas = None

    for zprava in zpravy:
        element_casu_zpravy = zprava.find_element(By.CSS_SELECTOR, "span.time") # Najde čas zprávy
        text_casu_zpravy = element_casu_zpravy.text.strip() # Z elementu dostane text zpravy
        cas_zpravy = datetime.datetime.strptime(text_casu_zpravy, "%H:%M:%S") # Vytvoří z textu porovnatelný datetime

        if cas_posledni_zpravy >= cas_zpravy: # Není žádná nová zpráva v chatu - pouze staré
            break
        # Jinak to samo pokračuje sem

        if zprava == zpravy[0]:
            novy_cas = cas_zpravy
            # Zpráva je první v poli Zprávy = Zpráva je nejnovější, takže se nastaví novy_cas = cas_zpravy
            # Nemůžeme rovnou nastavit cas_posledni_zpravy = cas_zpravy, protože by ignoroval starší, ještě nezpracované zprávy.
        
        formatovana_zprava = zprava.find_element("css selector", "font").text # Získá text zprávy ve formátu "Uživatel: Zpráva"
        vypsat(f"Nová zpráva! {formatovana_zprava}")
        pole_zprav.append(formatovana_zprava) # Přidáme zprávu do pole
    
    if pole_zprav != []:
        upravit_zpravy(pole_zprav)
    if novy_cas != None: # Je nějaký nový čas
        cas_posledni_zpravy = novy_cas # Už to nastavit můžeme

def upravit_zpravy(pole_zprav): 
    """
    Pro každou zprávu z pole_zprav vyextrahuje uživatele a text zprávy a zkontroluje zda je zpráva určena pro robota
    """

    vypsat("Upravuji zprávy...")

    for zprava in pole_zprav:
        uzivatelske_jmeno, _, text_zpravy = zprava.partition(": ")
        """
        Rozdělí zprávu na tři části:

        1. Uživatelské jméno -> uzivatelske_jmeno

        2. Oddělovač ": " -> Neukládá se

        3. Text zprávy -> text_zpravy
        """

        # Odebere případné mezery na začátku a na konci stringů
        uzivatelske_jmeno = uzivatelske_jmeno.strip()
        text_zpravy = text_zpravy.strip()

        if text_zpravy.lower().startswith(JMENO_ROBOTA.lower()): # Pokud zpráva začíná jménem robota (není case-sensitive - jsou jedno velká a malá písmena)
            vypsat("Zpráva je pro robota")
            if JMENO_ROBOTA.lower() + "," in text_zpravy.lower() or JMENO_ROBOTA.lower() + ":" in text_zpravy.lower(): # Pokud uživatel nenapsal POUZE jméno robota ale "jméno:" nebo "jméno,"
                text_zpravy = text_zpravy[len(JMENO_ROBOTA) + 1:] # Odstraní z textu zprávy jméno robota včetně znaku "," nebo ":"
            else:
                text_zpravy = text_zpravy[len(JMENO_ROBOTA):] # Za zprávou není žádný speciální znak - odstraní z textu zprávy pouze jméno robota

            if uzivatelske_jmeno != JMENO_ROBOTA: # Zpracujeme pouze zprávy, které nepsal sám robot
                text_zpravy = text_zpravy.strip() # Odstraníme případné mezery
                if text_zpravy != "": # Pokud zpráva není prázdná
                    zkontrolovat_zpravu(text_zpravy)

def zkontrolovat_zpravu(zprava):
    """
    Zkontroluje text zprávy a odešle požadovanou odpověď
    """

    vypsat("Kontroluji zprávu...")

    if zprava == "ahoj": # Pokud je zprava "ahoj" (Při porovnání BERE v potaz velká a malá písmena - je case-sensitive. Možno použít .lower(), aby se nerozlišovala velká a malá písmena.)
        vypsat("Příkaz ahoj")
        odpoved = "Ahojky! :D"
        odeslat_odpoved(odpoved) # Funkce odešle zprávu do chatu
    elif zprava == "odejit" or zprava == "odejít":
        vypsat("Příkaz odejít")
        odpoved = "Odcházím..."
        odeslat_odpoved(odpoved) # Funkce odešle zprávu do chatu
        odejit() # Robot odejde od stolu a program se vypne
    elif "datum" in zprava.lower(): # Pokud je "datum" kdekoli ve zprávě (NEBERE v potaz velká a malá písmena - není case-sensitive.)
        vypsat("Příkaz datum")
        odpoved = datetime.date.today() # Vrátí dnešní datum JAKO typ DATETIME
        odpoved = str(odpoved) # Převede z typu datetime do stringu
        odeslat_odpoved(odpoved) # Funkce odešle zprávu do chatu
    elif zprava.lower().startswith("zopakuj"): # Pokud zpráva začíná na "zopakuj" (NEBERE v potaz velká a malá písmena - není case-sensitive.)
        vypsat("Příkaz zopakuj")
        zprava = zprava[len("zopakuj"):] # Odebere řetězec "zopakuj" ze začátku zprávy, ať neopakuje slovo "zopakuj".
        zprava = zprava.strip() # Odebere případné mezery
        # Pŕíklad - Zpráva je "Zopakuj ahoj jak se máš" - odebere se slovo "zopakuj" a následující mezery. Výsledná zpráva je v tomto případě "ahoj jak se máš"
        odeslat_odpoved(zprava) # Funkce odešle zprávu do chatu
    else:
        vypsat("Neznámý příkaz")
        odpoved = "Neznám tento příkaz :("
        odeslat_odpoved(odpoved) # Funkce odešle zprávu do chatu


def odeslat_odpoved(odpoved):
    """
    Odešle odpověd do chatu
    """

    # Pokud se stejná zpráva pošle rychle po sobě, tak ji Alíkův filtr nemusí odeslat např. by se zpráva "Ahojky! :D" měla poslat 2x hned po sobě, ale Alík jednu zablokuje, takže se pošle pouze 1x

    vypsat("Odesílám zprávu...")

    pole_zpravy = prohlizec.find_element(By.CSS_SELECTOR, '#say') # Najde pole, kam se zadává zpráva
    pole_zpravy.send_keys(odpoved) # Napíše odpověď
    
    """
    Případně lze zaměnit 
    pole_zpravy.send_keys(odpoved)

    za
    prohlizec.execute_script("arguments[0].value = arguments[1];", pole_zpravy, odpoved)

    Funguje stejně, jen druhá možnost je rychlejší a podporuje znaky jako emoji, které send_keys() nemusí umět.

    send_keys(odpoved) funguje způsobem jako klávesnice - umí text a píše ho jako na klávesnici, ale neumí hodně emoji.

    execute_script("arguments[0].value = arguments[1];", pole_zpravy, odpoved) funguje způsobem vložení - vloží text (s emoji a čímkoliv jiným) do pole_zpravy.
    Také je rychlejší - pouze to vloží, nepíše.
    """

    tlacitko_odeslat = prohlizec.find_element(By.CSS_SELECTOR, '#send-text') # Najde tlačítko na odeslání
    tlacitko_odeslat.click() # Odešle zprávu

def odejit():
    """
    Odejde od stolu v klubovně a vypne program
    """

    vypsat("Odcházení...")

    tlacitko_odejit = prohlizec.find_element(By.CSS_SELECTOR, 'li.quit a') # Najde tlačítko odejít od stolu
    tlacitko_odejit.click() # Zmáčkne tlačítko

    prohlizec.quit() # Vypne prohlížeč

    os._exit(0) # Okamžitě vypne program

if __name__ == "__main__": # Pokud je program spuštěn samostatně a ne jako modul pomocí import
    prihlasit() # První se jedenkrát přihlásí
    while True:
        try:
            ziskat_zpravy() # Poté se provádí ziskat_zpravy() dokud se program nevypne.
        except selenium.common.exceptions.StaleElementReferenceException: # Chyba která občas nastane, když se stránka ještě načítá a program se už snaží najít element na stránce
            continue # Nemusíme řešit, až se stránka načte úplně, chyba už nenastane.