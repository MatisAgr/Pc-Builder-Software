# -*- coding: utf-8 -*-
# =============================================================================
#                                                                             #
#                       GRAND PROJET NSI TERMINALE                            #
#                                                                             #
#                       - Pierre-Louis                                        #
#                       - Julien                                              #
#                       - Marius                                              #
#                       - Matis                                               #
#                                                                             #
# =============================================================================

#--------------Importation du module------------------------------------------
import csv

def recupCsv()->list:
    """
    Fonction qui permet de récupérer les informations des csvs

    Returns
    -------
    list
        liste de liste avec chaque ligne de chaque csv.

    """
    cpu = []
    with open("csv/CPU.csv",'r',encoding='ansi') as fichier:#On ouvre le fichier
        for ligne in (csv.reader(fichier,delimiter=',',)):#Pour chaque ligne
            cpu.append(ligne)#on ajoute la ligne dans une luste
    del cpu[0] #On supprime la premiere ligne de la liste
    
    gpu= []
    with open("csv/GPU.csv",'r',encoding='ansi') as fichier:
        for ligne in csv.reader(fichier):
            gpu.append(ligne)
    del gpu[0]
    
    hdd = []
    with open("csv/HDD.csv",'r',encoding='ansi') as fichier:
        for ligne in csv.reader(fichier):
            hdd.append(ligne)
    del hdd[0]
    
    ssd = []
    with open("csv/SSD.csv",'r',encoding='ansi') as fichier:
        for ligne in csv.reader(fichier):
            ssd.append(ligne)
    del ssd[0]
    
    ram = []
    with open("csv/RAM.csv",'r',encoding='ansi') as fichier:
        for ligne in csv.reader(fichier):
            ram.append(ligne)
    del ram[0]
    
    mb=[]
    with open("csv/MOTHERBOARD.csv",'r',encoding='ansi') as fichier:
        for ligne in csv.reader(fichier):
            mb.append(ligne)
    del mb[0]
    
    os =  []
    with open("csv/OS.csv",'r',encoding='ansi') as fichier:
        for ligne in csv.reader(fichier):
            os.append(ligne)
    del os[0]
    
    return [cpu,gpu,ram,hdd,ssd,mb,os]