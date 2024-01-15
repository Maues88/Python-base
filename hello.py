#!/usr/bin/env python3
"""
Hello world multi languages

Depending on the language configured in the  environment, the program displays
the corresponding
how to use:
    export LANG= Eng_US
exec: 
    python3 hello.py
    or
    ./hello.py


"""
#metadados
__version__ = "0.0.1"
__author__ = "Maues"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!" 
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"        

print(msg)
