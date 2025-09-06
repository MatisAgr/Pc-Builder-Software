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

#--------------Importation des modules----------------------------------------

import subprocess as sp

cmdName = {"os":"wmic path Win32_OperatingSystem get Name /value","cpu" : "wmic path Win32_Processor get Name /value","motherboard":"wmic path Win32_BaseBoard get Manufacturer,Product /value","gpu":"wmic path Win32_VideoController get Name /value","ram":"wmic path Win32_PhysicalMemory get PartNumber /value","diskdrive":"wmic path Win32_DiskDrive get Model /value"}

def getName(composant:str)->str or list:
    """
    Parameters
    ----------
    composant : str
        Parametre correspondant au composant.

    Returns
    -------
    str or list
        Fonction permettant à partir d'un dictionnaire de commandes, le nom du composant dans l'ordinateur de l'utilisateur.

    """
    if composant in cmdName.keys():
        prompt = sp.Popen(cmdName[composant], stdout=sp.PIPE) #On execute la commande dans un invité de commande ouvert par python
        res,err = prompt.communicate()
        reslines = res.decode("cp1252", "ignore") .split('\n')#On décode le résultat de la commande afin de pouvoir la lire
        out = []
        for elt in reslines:
            if elt !="\r\r": #On supprime les caractères indésirables
                char =" ".join(elt.split()) #On sépare les mots afin de les rattacher correctement avec des espaces 
                out.append(char[:(len(elt)-2)])
        del(out[-1])
        return supprChar(composant,out)
    else:
        return(str(composant) + " -> Nom de Composant invalide")

def supprChar(composant:str,txt:list)->str or list:
    """    
    Parameters
    ----------
    composant : str
        Parametre correspondant au composant.
    txt : list
        Correspond a une liste de str avec des caractères qu'il faut supprimer

    Returns
    -------
    str or list
        Fonction permettant de supprimer les caractères indésirables au cas par cas
        
    """
    nTxt = ""
    if composant == "os":
        nTxt = txt[0][5:25]
    elif composant == "cpu":
        nTxt = txt[0][5:]
    elif composant == "gpu":
        nTxt = txt[0][5:] 
    elif composant == "motherboard":
        nTxt = txt[0][13:] +" "+ txt[1][8:]

    elif composant == "ram":
        nTxt=""
        index = 0
        for i in range(len(txt)):
            if "." in txt[i]:
                for j in range(len(txt[i])):
                    if txt[i][j]==".":
                        index = j
                nTxt += txt[i][11:index] + "   "
            else:
                nTxt += txt[i][11:] + "   "

    elif composant == "diskdrive":
        nTxt=[]
        index = 0
        if len(txt)<=2:
            for i in range(len(txt)):
                if "-" in txt[i]:
                    for j in range(len(txt[i])):
                        if txt[i][j]=="-":
                            index = j
                    nTxt.append(txt[i][6:index])
                else:
                    nTxt.append(txt[i][6:])
        else:
            for i in range(1,len(txt)):
                if "-" in txt[i]:
                    for j in range(len(txt[i])):
                        if txt[i][j]=="-":
                            index = j
                    nTxt.append(txt[i][6:index])
                else:
                    nTxt.append(txt[i][6:])
                    
    return nTxt