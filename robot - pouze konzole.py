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
Nastaveni_prohlizece = selenium.webdriver.chrome.options.Options() # Inicializuje nastavení prohlížeče Chrome (Chromium)
Nastaveni_prohlizece.add_argument("--headless") # Přidá argument headless = okno prohlížeče se neotevře, poběží pouze v konzoli
Prohlizec = selenium.webdriver.Chrome(options=Nastaveni_prohlizece) # V tomto případě prohlížeč Chrome (Chromium) s naším nastavením
Prohlizec.set_page_load_timeout(30) # Nastaví čas, jak dlouho bude prohlížeč čekat na načtení stránky před tím, než zahlásí chybu. 30 = 30 sekund.
Prohlizec.implicitly_wait(20)# Nastaví čas, jak dlouho bude prohlížeč čekat na nalezení nějakého HTML elementu před tím, než zahlásí chybu. 20 = 20 sekund.

# Deklarace globálních proměnných
Cas_posledni_zpravy = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), "%H:%M:%S") # Nastaví čas poslední zprávy na aktuální čas ve formátu H:M:S (Alík používá H:M:S)

def Prihlasit():
    """Funkce, ve které se robot přihlásí pomocí prohlížeče na Alík.cz za použití jména a hesla. Poté si přisedne ke stolu."""

    print("Přihlašování...")
    
    Prohlizec.get("https://www.alik.cz/prihlasit") # Přesměruje se na stránku přihlášení

    Prihlasovaci_pole_jmeno = Prohlizec.find_element(By.CSS_SELECTOR, '#login') # Najde na stránce přihlašovací pole pro zadání uživatelského jména díky CSS selectoru '#login'
    Prihlasovaci_pole_jmeno.send_keys(JMENO_ROBOTA) # Napíše hodnotu uloženou v konstantě JMENO_ROBOTA do přihlašovacího pole

    Prihlasovaci_pole_heslo = Prohlizec.find_element(By.CSS_SELECTOR, '#heslo') # Najde přihlašovací pole pro zadání uživatelského hesla
    Prihlasovaci_pole_heslo.send_keys(HESLO_ROBOTA) # Napíše hodnotu uloženou v konstantě HESLO_ROBOTA do přihlašovacího pole

    Tlacitko_prihlaseni = Prohlizec.find_element(By.CSS_SELECTOR, '.tlacitko') # Najde tlačítko na přihlášení
    Tlacitko_prihlaseni.click() # Klikne na tlačítko

    Prohlizec.get(STUL) # Přesměruje prohlížeč na URL stolu - robot je již přihlášený, takže si ke stolu přisedne.
    print("Přihlášeno!")

    Ahoj = "Ahoj! Úspěšně připojeno :D"
    Odeslat_odpoved(Ahoj)

def Ziskat_zpravy():
    """
    Načte nové nezpracované zprávy z chatu
    """

    global Cas_posledni_zpravy # Použije globální proměnnou

    Zpravy = Prohlizec.find_elements(By.CSS_SELECTOR, "#chatOkno > p.c-1") # Najde všechny elementy zpráv
    Pole_zprav = []
    Novy_cas = None

    for Zprava in Zpravy:
        Element_casu_zpravy = Zprava.find_element(By.CSS_SELECTOR, "span.time") # Najde čas zprávy
        Text_casu_zpravy = Element_casu_zpravy.text.strip() # Z elementu dostane text zpravy
        Cas_zpravy = datetime.datetime.strptime(Text_casu_zpravy, "%H:%M:%S") # Vytvoří z textu porovnatelný datetime

        if Cas_posledni_zpravy >= Cas_zpravy: # Není žádná nová zpráva v chatu - pouze staré
            break
        # Jinak to samo pokračuje sem

        if Zprava == Zpravy[0]:
            Novy_cas = Cas_zpravy
            # Zpráva je první v poli Zprávy = Zpráva je nejnovější, takže se nastaví Novy_cas = Cas_zpravy
            # Nemůžeme rovnou nastavit Cas_posledni_zpravy = Cas_zpravy, protože by ignoroval starší, ještě nezpracované zprávy.
        
        Formatovana_zprava = Zprava.find_element("css selector", "font").text # Získá text zprávy ve formátu "Uživatel: Zpráva"
        print(f"Nová zpráva! {Formatovana_zprava}")
        Pole_zprav.append(Formatovana_zprava) # Přidáme zprávu do pole
    
    if Pole_zprav != []:
        Upravit_zpravy(Pole_zprav)
    if Novy_cas != None: # Je nějaký nový čas
        Cas_posledni_zpravy = Novy_cas # Už to nastavit můžeme

def Upravit_zpravy(Pole_zprav): 
    """
    Pro každou zprávu z Pole_zprav vyextrahuje uživatele a text zprávy a zkontroluje zda je zpráva určena pro robota
    """

    print("Upravuji zprávy...")

    for Zprava in Pole_zprav:
        Uzivatelske_jmeno, _, Text_zpravy = Zprava.partition(": ")
        """
        Rozdělí zprávu na tři části:

        1. Uživatelské jméno -> Uzivatelske_jmeno

        2. Oddělovač ": " -> Neukládá se

        3. Text zprávy -> Text_zpravy
        """

        # Odebere případné mezery na začátku a na konci stringů
        Uzivatelske_jmeno = Uzivatelske_jmeno.strip()
        Text_zpravy = Text_zpravy.strip()

        if Text_zpravy.lower().startswith(JMENO_ROBOTA.lower()): # Pokud zpráva začíná jménem robota (není case-sensitive - jsou jedno velká a malá písmena)
            print("Zpráva je pro robota")
            if JMENO_ROBOTA.lower() + "," in Text_zpravy.lower() or JMENO_ROBOTA.lower() + ":" in Text_zpravy.lower(): # Pokud uživatel nenapsal POUZE jméno robota ale "jméno:" nebo "jméno,"
                Text_zpravy = Text_zpravy[len(JMENO_ROBOTA) + 1:] # Odstraní z textu zprávy jméno robota včetně znaku "," nebo ":"
            else:
                Text_zpravy = Text_zpravy[len(JMENO_ROBOTA):] # Za zprávou není žádný speciální znak - odstraní z textu zprávy pouze jméno robota

            if Uzivatelske_jmeno != JMENO_ROBOTA: # Zpracujeme pouze zprávy, které nepsal sám robot
                Text_zpravy = Text_zpravy.strip() # Odstraníme případné mezery
                if Text_zpravy != "": # Pokud zpráva není prázdná
                    Zkontrolovat_zpravu(Text_zpravy)

def Zkontrolovat_zpravu(Zprava):
    """
    Zkontroluje text zprávy a odešle požadovanou odpověď

    
    Argumenty:

    Zprava (string): Text zprávy
    """

    print("Kontroluji zprávu...")

    if Zprava == "ahoj": # Pokud je Zprava "ahoj" (Při porovnání BERE v potaz velká a malá písmena - je case-sensitive. Možno použít .lower(), aby se nerozlišovala velká a malá písmena.)
        print("Příkaz ahoj")
        Odpoved = "Ahojky! :D"
        Odeslat_odpoved(Odpoved) # Funkce odešle zprávu do chatu
    elif Zprava == "odejit" or Zprava == "odejít":
        print("Příkaz odejít")
        Odpoved = "Odcházím..."
        Odeslat_odpoved(Odpoved) # Funkce odešle zprávu do chatu
        Odejit() # Robot odejde od stolu a program se vypne
    elif "datum" in Zprava.lower(): # Pokud je "datum" kdekoli ve zprávě (NEBERE v potaz velká a malá písmena - není case-sensitive.)
        print("Příkaz datum")
        Odpoved = datetime.date.today() # Vrátí dnešní datum JAKO typ DATETIME
        Odpoved = str(Odpoved) # Převede z typu datetime do stringu
        Odeslat_odpoved(Odpoved) # Funkce odešle zprávu do chatu
    elif Zprava.lower().startswith("zopakuj"): # Pokud zpráva začíná na "zopakuj" (NEBERE v potaz velká a malá písmena - není case-sensitive.)
        print("Příkaz zopakuj")
        Zprava = Zprava[len("zopakuj"):] # Odebere řetězec "zopakuj" ze začátku zprávy, ať neopakuje slovo "zopakuj".
        Zprava = Zprava.strip() # Odebere případné mezery
        # Pŕíklad - Zpráva je "Zopakuj ahoj jak se máš" - odebere se slovo "zopakuj" a následující mezery. Výsledná zpráva je v tomto případě "ahoj jak se máš"
        Odeslat_odpoved(Zprava) # Funkce odešle zprávu do chatu
    else:
        print("Neznámý příkaz")
        Odpoved = "Neznám tento příkaz :("
        Odeslat_odpoved(Odpoved) # Funkce odešle zprávu do chatu


def Odeslat_odpoved(Odpoved):
    """
    Odešle odpověd do chatu


    Argumenty:

    Odpoved (string): Text odpovědi 
    """

    print("Odesílám zprávu...")

    Pole_zpravy = Prohlizec.find_element(By.CSS_SELECTOR, '#say') # Najde pole, kam se zadává zpráva
    Pole_zpravy.send_keys(Odpoved) # Napíše odpověď
    
    """
    Případně lze zaměnit 
    Pole_zpravy.send_keys(Odpoved)

    za
    Prohlizec.execute_script("arguments[0].value = arguments[1];", Pole_zpravy, Odpoved)

    Funguje stejně, jen druhá možnost je rychlejší a podporuje znaky jako emoji, které send_keys() nemusí umět.

    send_keys(Odpoved) funguje způsobem jako klávesnice - umí text a píše ho jako na klávesnici, ale neumí hodně emoji.

    execute_script("arguments[0].value = arguments[1];", Pole_zpravy, Odpoved) funguje způsobem vložení - vloží text (s emoji a čímkoliv jiným) do Pole_zpravy.
    Také je rychlejší - pouze to vloží, nepíše.
    """

    Tlacitko_odeslat = Prohlizec.find_element(By.CSS_SELECTOR, '#send-text') # Najde tlačítko na odeslání
    Tlacitko_odeslat.click() # Odešle zprávu

def Odejit():
    """
    Odejde od stolu v klubovně a vypne program
    """

    print("Odcházení...")

    Tlacitko_odejit = Prohlizec.find_element(By.CSS_SELECTOR, 'li.quit a') # Najde tlačítko odejít od stolu
    Tlacitko_odejit.click() # Zmáčkne tlačítko

    Prohlizec.quit() # Vypne prohlížeč

    os._exit(0) # Okamžitě vypne program

if __name__ == "__main__": # Pokud je program spuštěn samostatně a ne jako modul pomocí import
    Prihlasit() # První se jedenkrát přihlásí
    while True:
        try:
            Ziskat_zpravy() # Poté se provádí Ziskat_zpravy() dokud se program nevypne.
        except selenium.common.exceptions.StaleElementReferenceException: # Chyba která občas nastane, když se stránka ještě načítá a program se už snaží najít element na stránce
            continue # Nemusíme řešit, až se stránka načte úplně, chyba už nenastane.