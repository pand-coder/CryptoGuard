import requests
import base64
import phonenumbers
from phonenumbers import geocoder, timezone

def display_header():
    print("               , _.-~~-.__            __.,----.                   ")
    print("      (';    __( )         ~~~'--..--~~         '.               ")
    print("(    . \"..-'  ')|                     .       \\  '.            ")
    print(" \\\\ |\.'                    ;       .  ;       ;   ;           ")
    print("  \\ \\'   /9)                 '       .  ;           ;         ")
    print("   ; )           )    (        '       .  ;     '    .        ")
    print("    )    _  __.-'-._   ;       '       . ,     /\\    ;        ")
    print("    '-'\"'--'      ; \"-. '.    '            _.-(  \".  (        ")
    print("                  ;    \\,)    )--,..----';'    >  ;   .       ")
    print("                   \\   ( |   /           (    /   .   ;       ")
    print("     ,   ,          )  | ; .(      .    , )  /     \\  ;       ")
    print(",;'-PjP;.';.-.;._,;/;,;)/;.;.);.;,,;,;,,;/;;,),;.,/,;.).,;,    ")
    print("           =============================================================   ")                                       
    print("                                   RHINOEYE                               ") 
    print("           =============================================================   ")
    print("                                   VERSION 0.0.1                               ") 
    print("           =============================================================   ")
    print("                                   OSINTBOT                             ")
    print("                             ======================                        ")
    print("                        Author:  PAVAN SHANMUKHA MADHAV GUNDA                        ")
    print("                             ======================                        ")  
    print("")

def ip2location_api():
    ip2location_url = 'https://api.ip2location.io/'
    print("Please replace 'your_api_key' with your actual IP2Location API key.")
    ip2location_api_key = 'your_api_key'

    ip_address = input("Enter an IP address: ")

    try:
        response = requests.get(f'{ip2location_url}?key={ip2location_api_key}&ip={ip_address}', timeout=10)
        response.raise_for_status()
        print('IP2Location Response:')
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error accessing IP2Location API: {e}")

def picarta_ai_api():
    print("EXIF DATA OF IMAGE (KEEP THE IMAGE LOCAL ON MACHINE)")
    picarta_url = "https://picarta.ai/classify"
    print("Please replace 'your_api_token' with your actual Picarta API token.")
    api_token = "your_api_token"
    headers = {"Content-Type": "application/json"}

    # Prompt the user for the image path
    image_path = input("Enter the path to the image file: ")

    try:
        with open(image_path, "rb") as image_file:
            img_path = base64.b64encode(image_file.read()).decode('utf-8')

        payload = {
            "TOKEN": api_token,
            "IMAGE": img_path
        }

        response = requests.post(picarta_url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        print(result)
    except FileNotFoundError:
        print("Error: Image file not found. Ensure the path is correct.")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing Picarta API: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def ip2whois_api():
    ip2whois_url = 'https://api.ip2whois.com/v2'
    print("Please replace 'your_api_key' with your actual IP2Whois API key.")
    ip2whois_api_key = 'your_api_key'

    domain = input("Enter a domain name: ")

    try:
        response = requests.get(f'{ip2whois_url}?key={ip2whois_api_key}&domain={domain}', timeout=10)
        response.raise_for_status()
        print('\nIP2Whois Response:')
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error accessing IP2Whois API: {e}")

def get_phone_number_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        region = geocoder.description_for_number(parsed_number, "en")
        tz = timezone.time_zones_for_number(parsed_number)

        print(f"Phone Number: {phone_number}")
        print(f"Region: {region}")
        print(f"Timezone: {tz}")
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error: {e}")

def menu():
    display_header()
    
    while True:
        print("\n===== MENU =====")
        print("1. IP address info")
        print("2. Exif data")
        print("3. Domain Name")
        print("4. Phone number info")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            ip2location_api()
        elif choice == '2':
            picarta_ai_api()
        elif choice == '3':
            ip2whois_api()
        elif choice == '4':
            phone_number = input("Enter the phone number: ")
            get_phone_number_info(phone_number)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
