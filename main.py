""" 			     Pythonda ajoyib modul(PyFiglet)
							   @DeCoder_uz
									   							   """

#pip install pyfiglet
from pyfiglet import Figlet

#Figlet moduli va uning parametrlari
text = Figlet(font="doh", direction='auto', justify='auto', width=140)

#Consolga chiqarish
print(text.renderText("Decoder"))