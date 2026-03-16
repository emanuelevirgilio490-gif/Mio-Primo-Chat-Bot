#IMPORT FUNZIONI DELLA CALCOLATRICE:
import Operazioni as op

#IMPORT:

import time
start=time.time()
from datetime import datetime
import random
import sys
import os
from random import choice
import difflib

#Caricamenti:

prob=random.randint(1, 11)
if prob == 11:
	for i in range (101):
		print (f"\r  Nascondendo i polli: {i}%", end='', flush=True)
		time.sleep(0.02)
		
		if i == 99:
			time.sleep(4)
	print()
	print()
	for j in range (101):
		print (f"\r  Riscaldando Brodini: {j}%", end='', flush=True)
		time.sleep(0.005)
	print()
	print()
else:
	pass

#Funzioni:

#TiPewriter: effect riga per riga:

def Tp_eff_riga (testo, velocita=0.03):
	for i in testo:
		sys.stdout.write(i)
		time.sleep(velocita)
	print()

#TiPewriter: effect riga per riga

def Tp_eff (testo, velocita=0.03):
	for i in testo:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(velocita)
	print()
	
#CARICAMENTO CON PUNTINI:

def load(velocita=0.5):
	for i in range (4):
		print(f"\r  Caricamento Inutile {'.' * i}{' ' * (3 - i)}", end="", flush=True)
		time.sleep(velocita)
		
def load_cal(velocita = 0.5):
	for i in range (4):
		print (f"\r  Interruzione Calcolatrice {"." * i}{" " * (3 - i)}", end = "", flush = True)
		time.sleep(velocita)
		print (f"\r                               ", end = "")
		
#COMANDI
	
comandi = ["gioco", "nome", "cal", "exit", "pinguino", "pinguini"]

#Intro:

Tp_eff_riga ("  Brodino\n  Di\n  Pollo\n  Industries", velocita=0.05)
time.sleep(0.5)
Tp_eff ("\n  Benvenuto,\n  inserisci il tuo nome…", velocita=0.01)

#NOME

Nome=input ("\n  Nome: ").capitalize()
if Nome.strip().lower() == "bdp":
	print ("\n  Bentornato, fondatore…")
	Nome=Nome.upper()
elif Nome.strip().lower() == "nessuno":
	print ("  Allora, Addio!\n\n  Il programma è stato")
	time.sleep(1)
	print ("\r\n  INTERROTTO")
	sys.exit()
else:
	print ("\n  Ciao",Nome)
Azione_cons=["digitare <nome> per cambiarlo",
"digitare <gioco>",
"digitare <cal> (calcolatrice)\n  Beta",
"digitare <exit> per uscire"]

#CICLO WHILE:

while True:
	Scelta=random.choice(Azione_cons)
	print (f"\n  prova a…\n  {Scelta}")
	probability = random.randint (1,4)
	Risposta=input ("\n  ")
	Risposta=Risposta.strip().lower()
	print()
	end=time.time()
	second=int(end - start)
	a=0
     
#EXIT      
               
	if Risposta == 'exit':
		a+=1
		load(0.3)
		load(0.3)
		os.system('cls' if os.name == 'nt' else 'clear')
		Tp_eff (f'\n  Programma Interrotto…\n  Arrivederci {Nome}!', velocita=0.01)
		sys.exit()
            
#FAN FACT + SECONDI
	
    if probability == 3:
    	print('\r  Fan fact:\n  Sei stato nella pagina')
    	for i in range (second, second + 3):
            print (f'\r  Per {i} secondi', end="", flush=True)
            time.sleep(1)
            print()
            a+=1
            print()
    elif a >= 1:
    	pass
    else:
        a+=1
        pass
        
			
            



#Queste sono delle esclamazioni negative: mescolate ben 2 volte

    Esclamazioni_negative=["\n  Oh…","\n  Mi dispiace…","\n  Che peccato…"]
    Escl_n_A=random.choice(Esclamazioni_negative)
    Escl_n_B=random.choice(Esclamazioni_negative)
    Escl_n_C=random.choice(Esclamazioni_negative)

#PINGUINI

    pinguini=("\n (pinguino a =\n  pinguino glaciale;","\n  pinguino b = pinguino montuoso;"," pinguino c =\n  pinguino motivazionale)")
	
    scuse=['\n  Mi spiace,\n  Credo di non aver capito…',
	'\n  Potresti ripetere?',
	'\n  L`input non è una funzione\n  Ancora sviluppata…',
	'\n  Ti dispiacerebbe ripetere?',
	'\n  Non ho capito…',
	'\n  Scusami,\n  Ma non ho capito…']
    scusa=random.choice(scuse)
	


#Risposta dei comandi in base alla Risposta

#nome

    if Risposta == "nome":
	    print ("  Digita il tuo nuovo nome: ")
	    Nome=input("\n  inserisci il tuo\n  nuovo nome: ").capitalize()
	    print (f"\n  Ciao {Nome}")
	    pass

#gioco di numeri

    if Risposta == "gioco":
        vinto=0
        perso=0
        print ("\n  Iniziamo! Se esce un numero\n  pari… Hai vinto!\n  (<e> per uscire)")
        gioco_run = bool(True)
        while gioco_run == True:
            try:
                Numero=input ("\n  Inserisci un numero\n  casuale: ")
                if Numero.strip().lower() == 'e':
                    print (f'\n  Hai vinto {vinto} volte e…\n  Hai perso {perso} volte')
                    gioco_run = bool(False)
                elif Numero.strip().lower() == 'e' and vinto == 1:
                    print (f'\n  Hai vinto {vinto} volta e…\n  Hai perso {perso} volte')
                    gioco_run = bool(False)
                elif Numero.strip().lower() == 'e' and perso == 1:
                    print (f'\n  Hai vinto {vinto} volte e…\n  Hai perso {perso} volta')
                    gioco_run = bool(False)
                elif Numero.strip().lower() == 'e' and vinto == perso == 1:
                    print (f'\n  Hai vinto {vinto} volta e…\n  Hai perso {perso} volta')
                    gioco_run = bool(False)
                Numero_2: int=random.randint(1, 2)
                Numero_a=int(Numero)
                Numero_b=int(Numero_2)
                Numero_fin= Numero_a + Numero_b
                print(f"\n  {Numero_fin}")
            except (NameError, ValueError):
                if Numero != 'e':
                    print ("\n  Inserisci un NUMERO per favore!")
                    continue
            try:
                if Numero_fin % 2==0:
                    print ("\n  Hai vinto!")
                    vinto+=1
                    pass
                else:
                    print (Esclamazione_negativa, "\n  Hai perso!")
                    perso+=1
                    pass
            except NameError:
                pass
    comandi = ["gioco", "nome", "cal", "exit", "pinguino", "pinguini"]			
    if Risposta not in comandi:
        print (scusa)
        pass
	
    if Risposta == 'pinguino' or Risposta == 'pinguini':
        print ('\n  Ecco la lista…', *pinguini)
        Pinguino=input('  Scelgo… ')
        Pinguino=Pinguino.strip().lower().replace(" ", "")
        if Pinguino == "pinguinoc" == "c":
            print('\n  Ha ispirato un`intera\n  generazione')
            Nome = 'Pinguino_Motiv💪'
		
        if Pinguino == 'pinguinob':
            pass
		
        pass
	
#CALCOLATRICE
	
    while True:
		
		
#CALCOLATRICE:	
		
        if Risposta == 'cal':
            print ('\n  Quale operazione\n  Vorresti fare?\n\n  (addizione = +);\n\n  (sottrazione = -);\n\n  (moltiplicazione = *);\n\n  (divisione = /)\n\n  (<e> per uscire)')
            Operazione=str(input('\n  Operazione: ')).strip().lower()
			
#ADDIZIONE		
			
            if Operazione == '+':
                print ('\n\n  Quanti addendi\n  Vuoi addizionare?')
				
#CONVERSIONE DEL NUMERO DEGLI ADDENDI E AVVISI DI ERRORE			
				
                try:
                    Addendi=input('\n\n  n Addendi: ')
                    if Addendi.strip().lower() == "e":
                        load_cal(0.3)
                        load_cal(0.3)
                        load_cal(0.3)
                        break
                    Addendi=int(Addendi)
                except AttributeError or ValueError or NameError:
                    print ('\n  Digita un NUMERO!')
                    continue
                if Addendi == 0:
                    print (f'\n  Non puoi fare un`addizione\n  Con {Addendi} addendi!')
                    time.sleep(2)
                    print()
                    print()
                    continue
                if Addendi == 1:
                    print (f'\n  Non puoi fare un`addizione\n  Con {Addendi} addendo!')
                    time.sleep(2)
                    print()
                    print()
                    continue
				
#ADDIZIONE TRA ADDENDO E TOTALE				
				
                print (f'\n  Scrivi i numeri\n  Dei {Addendi} addendi\n  Che vuoi addizionare')
                totale=0
                for i in range(Addendi):
                    Addendo=input("\n  Scrivi l`addendo: ").replace(",",".")
					
#CONVERSIONE DEL NUMERO				
					
                    try:
                        Addendo=int(Addendo)
                    except ValueError:
                        Addendo=float(Addendo)
                    except ValueError:
                        print ('\n  Scegli un operazione\n  Nella lista!')
                    except ValueError:
                        print (scusa)
                    print('\r                 ')
                    totale=op.add(Addendo, totale)
				
#TOTALE
				
                print ('\n   -----   ')
                print (f'\n\n  Il tuo totale è {totale}')
				
#CARICAMENTO
				
                time.sleep(2)
                print()
                load(0.1)
                load(0.1)
                load(0.1)
                load(0.1)
        print('\r                          ', end="")
        
