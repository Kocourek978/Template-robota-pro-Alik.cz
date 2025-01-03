# Template robota pro web Alík.cz
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/selenium?logo=python)         ![GitHub last commit](https://img.shields.io/github/last-commit/Kocourek978/Template-robota-pro-Alik.cz?label=Posledn%C3%AD%20%C3%BAprava)      ![GitHub repo size](https://img.shields.io/github/repo-size/Kocourek978/template-robota-pro-alik.cz?label=Velikost)      ![GitHub open issues](https://img.shields.io/github/issues/Kocourek978/Template-robota-pro-Alik.cz?label=Chyby%20a%20probl%C3%A9my)



---
[English version here](#template-for-a-robot-on-the-website-alíkcz)

Kapitoly:
1. [Stručné informace](#stručné-informace )
2. [Instalace](#instalace)
3. [Příkazy](#příkazy)
4. [Další zdroje](#další-zdroje)
***

# Stručné informace

Šablona jednoduchého a funkčního robota v Pythonu pro web Alík.cz

Hodně lidí se ptá, jak si vytvořit vlastního robota na Alíkovi.
Díky tomu jsem se rozhodl, že vytvořím tento kód jako takový "startovací bod" pro všechny, kdo chtějí mít vlastního robota na Alíkovi, nebo jsou jen zvědaví, jak to funguje.

Kód je licencovaný jako public domain = každý si s ním může dělat to, co chce.

## Robot občas neposílá zprávy

To je kvůli tomu, že v klubovně je **filtr na spam**.

Když zkusíte poslat stejnou zprávu několikrát po sobě, tak se nepošle.

Jelikož odpovědi jsou většinou předdefinované, tak mohou být blokováné právě díky filtru.

Toto **není** chyba.

# Instalace
1. Stáhněte a nainstalujte [Google chrome](https://www.google.com/chrome "Google download")

2. Stáhněte a nainstalujte Python 3.11

   Kód by měl fungovat v Pythonu 3.8 - 3.12, ale byl testován na verzi 3.11.9.
   
   Lze stáhnout např:
   
   [Přes Microsoft store](https://apps.microsoft.com/detail/9nrwmjp3717k "Python 3.11.9 download")
   NEBO
   [na webu Pythonu](https://www.python.org/downloads/release/python-3119/ "Python 3.11.9 download")
   
3. Stáhněte [samotný program robota](https://github.com/Kocourek978/Template-robota-pro-Alik.cz/archive/refs/heads/main.zip "Program")

    Poté extrahujte stažený .zip soubor

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
6. Zapněte zobrazování časů

   Přihlašte se na Alíkovi za robota.

   (Jako kdybyste se přihlašovali jako normální uživatel)


   Poté si jako robot přisedněte ke stolu.

   Nakonec v "Nastavení stolů" musí být zapnutá možnost "Zobrazovat čas".

8. Spusťte program

   Instalace je hotová! Ted už jen stačí spustit program pomocí příkazu:
     ```bash
     python3 robot.py
     ```
## Co když kód nefunguje?
Ujistěte se, že jste všechno udělali správně.

Poté [nahlaste chybu tady na Githubu](https://github.com/Kocourek978/Template-robota-pro-Alik.cz/issues) a/nebo mi [napište na Alíkovskou poštu 📩](www.alik.cz/@/Kocourek978#formular)

(Lepší je ta pošta :D)

 ---

# Příkazy
Všechny verze programu mají 4 různé příkazy.
Zde si je stručně řekneme.

### Ahoj
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

# Další zdroje
Nechápete kód, chcete se dozvědět víc nebo si udělat vlastní kód?

[📩 Napište mi do Alíkovské pošty!](www.alik.cz/@/Kocourek978#formular)



A taky zde jsou nějaké další zdroje, které by mohly pomoct:

❓ - [Dotaz "Jak si můžu vytvořit svého robota?"](https://www.alik.cz/p/267231 "Odkaz na dotaz")

❓ - [Dotaz "Jakým způsobem jde Alík propojit s roboty?"](https://www.alik.cz/p/262726 "Odkaz na dotaz")

📄 - [Nástěnka "Jak by měla vypadat pravidla pro roboty?"](https://www.alik.cz/n/jak-by-mela-vypadat-pravidla-pro-roboty "Odkaz na nástěnku")

📄 - [Nástěnka "Roboti na Alíkovi"](https://www.alik.cz/n/roboti-na-alikovi "Odkaz na nástěnku")


***


# Template for a robot on the website Alík.cz
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/selenium?logo=python)         ![GitHub last commit](https://img.shields.io/github/last-commit/Kocourek978/Template-robota-pro-Alik.cz?label=Last%20Update)      ![GitHub repo size](https://img.shields.io/github/repo-size/Kocourek978/template-robota-pro-alik.cz?label=Size)      ![GitHub open issues](https://img.shields.io/github/issues/Kocourek978/Template-robota-pro-Alik.cz?label=Issues%20and%20Problems)



---
[Czech version here](#template-robota-pro-web-alíkcz)

Chapters:
1. [Overview](#overview)
2. [Installation](#installation)
3. [Commands](#commands)
4. [Additional Resources](#additional-resources)
***

# Overview

A simple and functional Python bot template for the website Alík.cz.

Many people ask how to create their own bot for Alík.cz.  
This inspired me to create this code as a "starting point" for anyone who wants their own bot for Alík.cz or is simply curious about how it works.

The code is licensed as public domain, meaning anyone can use it for anything they want.

## The Bot Sometimes Doesn’t Send Messages

This happens because the chat room has a **spam filter**.

If you try to send the same message multiple times in a row, it won’t be sent.  

Since the responses are often predefined, they can be blocked by the filter.

This is **not** a bug.

# Installation
1. Download and install [Google Chrome](https://www.google.com/chrome "Google download").

2. Download and install Python 3.11.

   The code should work on Python 3.8–3.12, but it was tested on version 3.11.9.
   
   You can download it from:
   
   [Microsoft Store](https://apps.microsoft.com/detail/9nrwmjp3717k "Python 3.11.9 download")  
   OR  
   [The Python website](https://www.python.org/downloads/release/python-3119/ "Python 3.11.9 download").
   
3. Download [the bot program itself](https://github.com/Kocourek978/Template-robota-pro-Alik.cz/archive/refs/heads/main.zip "Program").

    Then extract the downloaded `.zip` file.

4. Install the libraries.

   Using a single command:
   ```bash
   cd path\to\folder\with\program && pip install -r requirements.txt
   ```
   -OR-

   Use the command line and navigate to the program folder:
   ```bash
   cd path\to\folder\with\program
   ```
   
   Then install the libraries using **pip** and the **requirements.txt** file:
   ```bash
   pip install -r requirements.txt
   ```
5. Modify the **.env** file and add your details.

   Open the **.env** file in any text editor.
   
   The file looks like this:
   ```env
   JMENO_ROBOTA="Enter the bot account's username here"
   HESLO_ROBOTA="Enter the bot account's password here" 
   STUL="Enter the table link where the bot should sit (e.g., https://www.alik.cz/k/roboti-koutek)"
   ```
   (The .env file is in Czech so you can use one .env file in both codes)
   
   Replace the placeholders with your bot’s details.  
   The final file should look something like this:
   ```
    JMENO_ROBOTA="Zeno"
    HESLO_ROBOTA="superpassword"
    STUL="https://www.alik.cz/k/roboti-koutek"
    ```

6. Enable Time Display.

   Log in to Alík.cz as the bot (like a regular user).  
   
   Then have the bot join a table.  
   
   Finally, in "Table Settings," ensure the "Show Time" option is enabled.

7. Run the Program.

   Installation is complete! Now simply run the program using the command:
     ```bash
     python3 robot.py
     ```

## What If the Code Doesn’t Work?
Make sure you’ve followed all the steps correctly.  

Then [report the issue on GitHub](https://github.com/Kocourek978/Template-robota-pro-Alik.cz/issues) and/or [send me a message via Alík.cz mail 📩](www.alik.cz/@/Kocourek978#formular).

(Sending a message via mail is preferred :D.)

---

# Commands
All versions of the program have 4 different commands.  
Here’s a brief overview:

### Hello
Replies with "Hey! :D"

The user writes:
```Bot's name: hello``` (must be exactly and only "hello").  

The bot replies:
```Hey! :D```

### Date
Replies with the date in the format YY:MM:DD.

The user writes:
```Bot's name: date``` (can be in any case, anywhere in the text).  

The bot replies:
```YY:MM:DD```

### Repeat
Repeats the user’s text.

The user writes:
```Bot's name: repeat green grass``` (the message must start with "repeat").  

The bot replies:
```green grass```

### Leave
Leaves the table.

The user writes:
```Bot's name: leave``` (must be exactly and only "leave").  

The bot replies:
```Leaving...``` and leaves the table.

# Additional Resources
Don’t understand the code, want to learn more, or create your own code?

[📩 Send me a message via Alík.cz mail!](www.alik.cz/@/Kocourek978#formular)

Here are some additional resources that might help:

❓ - [Question: "How can I create my own bot?"](https://www.alik.cz/p/267231 "Link to question")

❓ - [Question: "How can Alík be connected to bots?"](https://www.alik.cz/p/262726 "Link to question")

📄 - [Discussion Board: "What should the rules for bots look like?"](https://www.alik.cz/n/jak-by-mela-vypadat-pravidla-pro-roboty "Link to board")

📄 - [Discussion Board: "Bots on Alík.cz"](https://www.alik.cz/n/roboti-na-alikovi "Link to board")

