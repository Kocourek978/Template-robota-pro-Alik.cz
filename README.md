# Template robota pro web Alík.cz
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/selenium?logo=python)

---
Kapitoly:
1. [Stručné informace](#stručné-informace )
2. [Instalace](#instalace)
3. [Příkazy](#příkazy)
***

# Stručné informace

Šablona jednoduchého a funkčního robota v Pythonu pro web Alík.cz

Hodně lidí se ptá, jak si vytvořit vlastního robota na Alíkovi.
Díky tomu jsem se rozhodl, že vytvořím tento kód jako takový "startovací bod" pro všechny, kdo chtějí mít vlastního robota na Alíkovi, nebo jsou jen zvědaví, jak to funguje.

Kód je licencovaný jako public domain = každý si s ním může dělat to, co chce.

## Verze kódu
Zatím jsou tři verze programu.

Zde jsou jejich rozdíly:

| Název        | Funkce           |
| ------------- |:-------------:|
| robot.py      | Standartní program, vypisuje do konzole info. |
| robot - zadne printy.py      | Stejný jako robot.py, ale do konzole nic nepíše      |
| robot - pouze konzole.py | Stejný jako robot.py, ale neotevře okno prohlížeče - prohlížeč běží skrytě v headless módu.      |

# Instalace
1. Stáhněte a nainstalujte [Google chrome](https://www.google.com/chrome "Google download")

2. Stáhněte a nainstalujte Python 3.11

   Kód by měl fungovat v Pythonu 3.8 - 3.12, ale byl testován na verzi 3.11.9.
   
   Lze stáhnout např:
   
   [Přes Microsoft store](https://apps.microsoft.com/detail/9nrwmjp3717k "Python 3.11.9 download")
   NEBO
   [na webu Pythonu](https://www.python.org/downloads/release/python-3119/ "Python 3.11.9 download")
   
3. Stáhněte [samotný program robota](https://github.com/Kocourek978/Template-robota-pro-Alik.cz/archive/refs/heads/main.zip "Program")

    Poté extrahovat stažený .zip soubor

4. Nainstalujte knihovny

   Pomocí jednoho příkazu
   ```bash
   cd cesta\do\složky\s\programem && pip install -r requirements.txt
   ```

    -NEBO-
  
     Použijte příkazový řádek a přesuňte se přesuňte do složky programu:
     ```bash
     cd cesta\do\složky\s\programem
     ```
  
     poté pomocí příkazu **pip** a souboru **requirements.txt** jednoduše nainstalujete knihovny:
     ```bash
     pip install -r requirements.txt
     ```
5. Modifikujte soubor **.env** a přidejte vaše údaje

   Otevřete soubor **.env** v jakémkoli textovém editoru

   Soubor vypadá takto:

    ```env
    JMENO_ROBOTA="Zde napiš přihlašovací jméno účtu robota"
    HESLO_ROBOTA="Zde napiš přihlašovací heslo účtu robota" 
    STUL="Zde napiš odkaz ke stolu, kam by si měl robot přisednout (např. https://www.alik.cz/k/roboti-koutek)"
    ```

    Vyměňte placeholdery za údaje robota.
    Konečný soubor by měl vypadat nějak takto:

   ```env
    JMENO_ROBOTA="Zeno"
    HESLO_ROBOTA="superheslo"
    STUL="https://www.alik.cz/k/roboti-koutek"
    ```
6. Spusťte program

   Instalace je hotová! Ted už jen stačí spustit program pomocí příkazu
     ```bash
     python3 robot.py
     ```

# Příkazy
Všechny verze programu mají 4 různé příkazy.
Zde si je stručně řekneme.

#### Ahoj
Napíše "Ahojky! :D"

Uživatel napíše
```Jméno robota: ahoj``` (musí být přesně a pouze "ahoj")

Robot odpoví
```Ahojky! :D```

### Datum
Napíše datum ve formátku YY:MM:DD

Uživatel napíše
```Jméno robota: datum``` (může být jakákoliv varianta, velká a malá písmena, kdekoliv v textu)

Robot odpoví
```YY:MM:DD```

### Zopakuj
Zopakuje text uživatele

Uživatel napíše
```Jméno robota: zopakuj travička zelená``` (zpráva musí začínat na "zopakuj")

Robot odpoví
```travička zelená```

### Odejít
Odejde od stolu

Uživatel napíše
```Jméno robota: odejít``` (musí být přesně a pouze "odejít")

Robot odpoví
```Odcházím...``` a odejde od stolu.
