from Config.Util import *
from Config.Config import *
import os
import sys  # Ajouté pour exécuter main.py
try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except Exception as e:
   ErrorModule(e)



def return_to_main():
    """Relancer main.py quand l'utilisateur appuie sur une touche."""
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Appuyez sur une touche pour revenir au menu principal.")
    input()  # Attend que l'utilisateur appuie sur une touche
    # Exécute main.py à nouveau
    os.system(f"{sys.executable} main.py")  # Relance main.py avec Python

try:
    phone_number = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Phone Number -> {color.RESET}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            status = "Valid"
        else:
            status = "Invalid"

        if phone_number.startswith("+"):
            country_code = "+" + phone_number[1:3]
        else:
            country_code = "None"
        try:
            operator = carrier.name_for_number(parsed_number, "fr")
        except:
            operator = "None"
    
        try:
            type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
        except:
            type_number = "None"

        try: 
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else None
        except:
            timezone_info = "None"
            
        try:
            country = phonenumbers.region_code_for_number(parsed_number)
        except:
            country = "None"
            
        try:
            region = geocoder.description_for_number(parsed_number, "fr")
        except:
            region = "None"
            
        try:
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        except:
            formatted_number = "None"
            
        print(f"""
    {INFO_ADD} Phone        : {white}{phone_number}{red}
    {INFO_ADD} Formatted    : {white}{formatted_number}{red}
    {INFO_ADD} Status       : {white}{status}{red}
    {INFO_ADD} Country Code : {white}{country_code}{red}
    {INFO_ADD} Country      : {white}{country}{red}
    {INFO_ADD} Region       : {white}{region}{red}
    {INFO_ADD} Timezone     : {white}{timezone_info}{red}
    {INFO_ADD} Operator     : {white}{operator}{red}
    {INFO_ADD} Type Number  : {white}{type_number}{red}
    """)
        return_to_main()  # Relance main.py après l'affichage
    except:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Invalid Format !")
        return_to_main()  # Relance main.py en cas de mauvais format
except Exception as e:
    Error(e)