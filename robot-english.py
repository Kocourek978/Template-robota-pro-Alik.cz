from dotenv import load_dotenv # Function that loads data from the .env file into the environment
import selenium # A library that supports working with webs
import selenium.webdriver # A library under selenium which allows us to use the Chrome browser
from selenium.webdriver.common.by import By # A library under selenium which allows us to find HTML elements
import datetime # A library for working with time
import os # A system library


load_dotenv() # A function that loads data from the .env file into the environment

"""
os.environ["JMENO_ROBOTA"] - Loads the value of JMENO_ROBOTA from the environment

If the value of JMENO_ROBOTA is defined in the environment as:
JMENO_ROBOTA="John"

then os.environ["JMENO_ROBOTA"] will return the string "John".
"""

# We declare the constants in the code from the environment data which the previous function loaded
JMENO_ROBOTA = os.environ["JMENO_ROBOTA"]
HESLO_ROBOTA = os.environ["HESLO_ROBOTA"]
STUL = os.environ["STUL"]
# I kept the variables in Czech so you can use only one .env file

# We declare the browser
while True: # A loop for user dialogue
    response = input("Open the browser window (1) or only run in the console in headless mode (2)? (pick the number 1 or 2): ").strip() # .strip() odebere případné mezery
    if response == "1": # Option 1
        browser = selenium.webdriver.Chrome() # In this case we use the Chrome (Chromium) browser with no settings
        
        break
    elif response == "2": # Option 2
        browser_settings = selenium.webdriver.chrome.options.Options() # We initialize the settings for the Chrome (Chromium) browser
        browser_settings.add_argument("--headless") # Adds headless argument - the browser window won't open and it will then only run in the console
        browser = selenium.webdriver.Chrome(options=browser_settings) # In this case we use the Chrome (Chromium) browser with our headless settings
        break
    else:
        print("Invalid pick!")
        
browser.set_page_load_timeout(30) # Sets the time of how long the browser will wait for the page to load before throwing an error. 30 = 30 seconds.

browser.implicitly_wait(20) # Sets the time of how long the browser will wait while trying to find a HTML element before throwing an error. 20 = 20 seconds.

# We set print_info to True or False. Depending on the user's choice.
while True: # A loop for user dialogue
    response = input("Print info to console? (type Y for yes or N for no): ").strip().upper() # .strip() odebere případné mezery a .upper() převede text do velkých písmen
    if response == "Y" or response == "T": # Want
        print_info = True
        break
    elif response == "N" or response == "F": # Don't want
        print_info = False
        break
    else:
        print("Invalid pick!")

# We declare the global variables
last_msg_time = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), "%H:%M:%S") # Sets the time of last message to the current time in the H:M:S format (Alík uses H:M:S)

def writeout(info):
    """A function that will print info to the console if print_info is True"""
    global print_info # Uses the global variable
    if print_info:
        print(info)

def login():
    """A function where the robot logs in on Alík.cz using the browser and the name and password (JMENO_ROBOTA and HESLO_ROBOTA). Then joins the chat room."""

    writeout("Logging in...")
    
    browser.get("https://www.alik.cz/login") # Redirects to the login page

    login_field_name = browser.find_element(By.CSS_SELECTOR, '#login') # Finds the username login field on the web using the CSS selector '#login'
    login_field_name.send_keys(JMENO_ROBOTA) # Types out the value of JMENO_ROBOTA into the field

    login_field_password = browser.find_element(By.CSS_SELECTOR, '#heslo') # Finds the password login field 
    login_field_password.send_keys(HESLO_ROBOTA) # Types out the value of HESLO_ROBOTA into the field

    tlacitko_prihlaseni = browser.find_element(By.CSS_SELECTOR, '.tlacitko') # Finds the login button
    tlacitko_prihlaseni.click() # Presses the button

    browser.get(STUL) # Redirects the browser to the chat room URL - the robot is now logged in and will then join the chat room.
    writeout("Logged in!")

    welcome = "Hi! Successfully connected :D"
    send_message(welcome)

def load_messages():
    """
    Loads new messages from the chat
    """

    global last_msg_time # Uses the global variable

    messages = browser.find_elements(By.CSS_SELECTOR, "#chatOkno > p.c-1") # Finds all message elements
    message_array = []
    new_time = None

    for message in messages:
        time_element = message.find_element(By.CSS_SELECTOR, "span.time") # Finds the message time element
        text_time_element = time_element.text.strip() # Gets the text of the time
        message_time = datetime.datetime.strptime(text_time_element, "%H:%M:%S") # Converts time into datetime format

        if last_msg_time >= message_time: # No new message in chat
            break
        # Otherwise it continues here...

        if message == messages[0]:
            new_time = message_time
            # Message is first in the array message_array = the message is first so we set new_time = message_time
            # We can't just set last_msg_time = message_time because the code would ignore other new messages in the loop
        
        edited_message = message.find_element("css selector", "font").text # Gets the text of the message in this format "User: message"
        writeout(f"New message! {edited_message}")
        message_array.append(edited_message) # Adds the message to the array
    
    if message_array != []:
        format_messages(message_array)
    if new_time != None: # There's some now time
        last_msg_time = new_time # We can set it now

def format_messages(message_array): 
    """
    Formats the message - extracts the user and the text and checks if the message is meant for the robot
    """

    writeout("Formatting messages...")

    for message in message_array:
        username, _, message_text = message.partition(": ") # Splits the message into three parts
        

        # Removes blank characters at the front and end of the string (if any)
        username = username.strip()
        message_text = message_text.strip()

        if message_text.lower().startswith(JMENO_ROBOTA.lower()): # If message starts with the robot's name (isn't case-sensitive)
            writeout("Message is for robot")
            if JMENO_ROBOTA.lower() + "," in message_text.lower() or JMENO_ROBOTA.lower() + ":" in message_text.lower(): # If the user didn't write JUST the name but wrote "name:" or "name,"
                message_text = message_text[len(JMENO_ROBOTA) + 1:] # Removes the robot's name from the message including the "," or ":"
            else:
                message_text = message_text[len(JMENO_ROBOTA):] # There isn't any additional character - removes just the robot's name

            if username != JMENO_ROBOTA: # If the robot didn't write the message
                message_text = message_text.strip() # Removes blank characters at the front and end of the string (if any)
                if message_text != "": # If message isn't empty 
                    process_message(message_text)

def process_message(message):
    """
    Processes the message and sends the desired response
    """

    writeout("Processing message...")

    if message == "hello": # If the message is "hello" (IS case-sensitive. Use .lower() if you don't want it to be.)
        writeout("Hello command")
        response = "Hey! :D"
        send_message(response) # Function sends the response to the chat
    elif message == "quit" or message == "leave":
        writeout("Quit command")
        response = "Leaving..."
        send_message(response) # Function sends the response to the chat
        quit() # Robot odejde od stolu a program se vypne
    elif "date" in message.lower(): # If "date" is anywhere in the message (ISN'T case-sensitive)
        writeout("Date command")
        response = datetime.date.today() # Returns today's date as a datetime object
        response = str(response) # Converts datetime object into a string
        send_message(response) # Function sends the response to the chat
    elif message.lower().startswith("repeat"): # If message starts with "repeat" (ISN'T case-sensitive)
        writeout("Repeat command")
        message = message[len("repeat"):] # Removes the "repeat" from the front of the message so it doesn't say the "repeat" part.
        message = message.strip() # Removes blank characters at the front and end of the string (if any)
        # Example - if the message was "repeat hello" then the program would remove "repeat" and the blank after it - leaves only the part to repeat
        send_message(message) # Function sends the response to the chat
    else:
        writeout("Unknown command")
        response = "I don't know this command :("
        send_message(response) # Function sends the response to the chat


def send_message(response):
    """
    Sends a message to the chat
    """

    # If the same message gets sent more times in a row - like if "hello" got sent 4 times, then the chat room anti spam filter can block it - making it send only 1 time

    writeout("Sending message...")

    message_field = browser.find_element(By.CSS_SELECTOR, '#say') # Finds the field to enter the message
    browser.execute_script("arguments[0].value = arguments[1];", message_field, response) # Pastes the message
    
    """
    You can also change this 
    browser.execute_script("arguments[0].value = arguments[1];", message_field, response)

    to
    message_field.send_keys(response)

    It will function mostly the same.
    Only problem is that the characters like emojis send_keys() sometimes doesn't support.

    send_keys(response) Works like a keyboard - types out the message - can't use most of the emojis.

    execute_script("arguments[0].value = arguments[1];", message_field, response) Works like pasting - pastes any text (with emojis) into message_field.
    It's also faster - pastes the message, doesn't type it out.
    """

    tlacitko_odeslat = browser.find_element(By.CSS_SELECTOR, '#send-text') # Finds the send button
    tlacitko_odeslat.click() # Sends the message

def quit():
    """
    Leaves the chat room and closes the program
    """

    writeout("Quitting...")

    tlacitko_quit = browser.find_element(By.CSS_SELECTOR, 'li.quit a') # Finds the button to leave the chat room
    tlacitko_quit.click() # Presses it

    browser.quit() # Closes the browser

    os._exit(0) # Instantly closes the program

if __name__ == "__main__": # If the program is ran as main and not as an import
    login() # First it logs in (once)
    while True:
        try:
            load_messages() # Then calls load_messages() until it quits.
        except selenium.common.exceptions.StaleElementReferenceException: # An error that sometimes happens when it's trying to find an element that isn't yet loaded on the page
            continue # We don't need to do anything as it will fix itself when the page fully loads