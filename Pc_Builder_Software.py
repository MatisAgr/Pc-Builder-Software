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

#===========================================================================#
#------------------------Importations des modules---------------------------#
#===========================================================================#

from tkinter import *
from tkinter import ttk, filedialog
import tkinter.messagebox as messagebox
import infos_pc as iPC
import infos_csv
import json
from random import choice

class App:
    
    def __init__(self):
        """Création de l'application"""
        self.root = Tk() #Création de la fenêtre Tkinter
        self.rootAssistant = None #Initialisation de la fenêtre de l'assistant
        self.root.geometry("840x600") #Dimension de notre fenêtre
        self.root.title("PBS") #Titre la fenêtre, de notre application
        self.root.iconbitmap('logo.ico') #Logo de la fenêtre
        self.Can = Canvas(self.root,width=840,height=600,bg='grey') #Création d'un Canvas dans la fenêtre avec une taille(840x600) et une couleur de fond défini.
        
        # ===============================================================================================#
        #-------------------------Importations des images------------------------------------------------#
        # ===============================================================================================#
        
        self.img_modifi_pc1 = PhotoImage(file="images/modifie_pc.png")
        self.img_modifi_pc2 = PhotoImage(file="images/modifie_pc2.png")
        
        self.img_nouveau_pc1 = PhotoImage(file="images/nouveau_pc.png")
        self.img_nouveau_pc2 = PhotoImage(file="images/nouveau_pc2.png")
        
        self.img_config_auto1 = PhotoImage(file="images/config_auto.png")
        self.img_config_auto2 = PhotoImage(file="images/config_auto2.png")
        
        self.img_retour1 = PhotoImage(file="images/retour.png")
        self.img_retour2 = PhotoImage(file="images/retour2.png")
        self.img_valider1 = PhotoImage(file="images/valider.png")
        self.img_valider2 = PhotoImage(file="images/valider2.png")
        
        self.img_fond_compo1 = PhotoImage(file="images/fond_compo.png")            #|
        self.img_fond_compo2 = PhotoImage(file="images/fond_compo2.png")           #|
        self.img_fond_compo3 = PhotoImage(file="images/fond_compo3.png")           #| Images de fond 
        self.img_fond_compo4 = PhotoImage(file="images/fond_compo4.png")           #|
        self.img_fond_compo5 = PhotoImage(file="images/fond_modif_pc_droite.png")  #|
        
        self.img_logo_in1 = PhotoImage(file="images/logo_in.png")
        self.img_logo_in2 = PhotoImage(file="images/logo_in2.png")
        
        self.img_telecharger1 = PhotoImage(file="images/telecharger.png")
        self.img_telecharger2 = PhotoImage(file="images/telecharger2.png")
    
        self.img_menu1 = PhotoImage(file="images/menu.png")
        self.img_menu2 = PhotoImage(file="images/menu2.png")
        
        self.img_enregistrer1 = PhotoImage(file="images/enregistrer.png")
        self.img_enregistrer2 = PhotoImage(file="images/enregistrer2.png")
        
        self.img_assistant1 = PhotoImage(file="images/assist.png")
        self.img_assistant2 = PhotoImage(file="images/assist2.png")
        
        self.img_rechercher1 = PhotoImage(file="images/rechercher3.png")
        self.img_rechercher2 = PhotoImage(file="images/rechercher4.png")
        
        self.img_modif_compo_auto1 = PhotoImage(file="images/modif_compo_auto.png")
        self.img_modif_compo_auto2 = PhotoImage(file="images/modif_compo_auto2.png")
        
        self.img_info1 = PhotoImage(file="images/info.png")
        self.img_info2 = PhotoImage(file="images/info2.png")
        

        # Création du dictionnaire pour créer un mode ON/OFF dur les boutons à l'aide d'autre fonction---#

            
        self.dico = {"bouton_modif":[self.img_modifi_pc1,self.img_modifi_pc2],
                     "bouton_nouveau_pc":[self.img_nouveau_pc1,self.img_nouveau_pc2],
                     "bouton_auto":[self.img_config_auto1,self.img_config_auto2],
                     "bouton_retour":[self.img_retour1,self.img_retour2],
                     "bouton_valider":[self.img_valider1,self.img_valider2],
                     "bouton_menu":[self.img_menu1,self.img_menu2],
                     "bouton_telecharger":[self.img_telecharger1,self.img_telecharger2],
                     "bouton_assistant":[self.img_assistant1,self.img_assistant2],
                     "bouton_rechercher":[self.img_rechercher1,self.img_rechercher2],
                     "bouton_info":[self.img_info1,self.img_info2],
                     "bouton_modif_compo_auto":[self.img_modif_compo_auto1,self.img_modif_compo_auto2]}

        #======================================================================================================#
        
        self.dico_page = {"new_pc":self.new_pc,"modif_pc":self.modifie_pc,"auto_pc":self.auto_pc} #Dictionnaire pour connaitre notre page précédente et pouvoir y revenir.


        # ==========================================================================================
        # Création de liste pour chaque composant comportant toutes les infos liées au composant---#
        # ==========================================================================================

        self.listeCpu = infos_csv.recupCsv()[0]
        self.listeGpu = infos_csv.recupCsv()[1]
        self.listeRam = infos_csv.recupCsv()[2]
        self.listeHdd = infos_csv.recupCsv()[3]
        self.listeSsd = infos_csv.recupCsv()[4]
        self.listeMb = infos_csv.recupCsv()[5]
        self.listeOs = infos_csv.recupCsv()[6]
        
        # ============================================================================#
        # Traitement des données sous forme de liste                                  #
        # ============================================================================#
        
        diskdriveTemp = iPC.getName("diskdrive")
        self.hdd = ""
        self.ssd = ""
        self.ram = iPC.getName("ram")        

        for elt in self.listeRam:
            if elt[1]==self.ram:
                self.ram += str(elt[2] + " " + elt[3])
        if self.ram == iPC.getName("ram"):
            self.ram = "RAM Introuvable"

        ssdFound = False
        hddFound = False
        for i in range(len(diskdriveTemp)):
            for elt in self.listeHdd:
                if elt[1] == diskdriveTemp[i]:
                    self.hdd +=str (elt[2] + " " + elt[3])
                    hddFound = True
            for elt in self.listeSsd:
                if elt[1] == diskdriveTemp[i]:
                    self.ssd+=str(elt[2] + " " + elt[3])
                    ssdFound = True
                elif str(elt[2] + " " + elt[3]) == str(diskdriveTemp[i]):
                    self.ssd+=str(elt[2] + " " + elt[3])
                    ssdFound = True
        
        for j in range(len(diskdriveTemp)):
            if ssdFound == False:
                self.ssd = "SSD introuvable"
            if hddFound == False:
                self.hdd = "HDD introuvable"
        
        # ============================================================================#
        # Stockage des infos dans différents dictionnaires                            #
        # ============================================================================#
        
        self.info = {"cpu":iPC.getName("cpu"),
                     "os":iPC.getName("os"),
                     "gpu":iPC.getName("gpu"),
                     "motherboard":iPC.getName("motherboard"),
                     "ram":self.ram,
                     "diskdrive":self.hdd+" et "+self.ssd}

        self.puissance = 0
        self.prix = 0
        self.dico_os = {"liste":self.recup_info(self.listeOs),"nom":iPC.getName("os"),"titre1":"Ton système d'exploitation :","titre2":"Systèmes d'exploitation","x_y_h1_h2":(40,45,30,30),"largeur_max":195,"modif":"Choisissez un composant"} #x y h1 h2
        self.dico_cpu = {"liste":self.recup_info(self.listeCpu),"nom":iPC.getName("cpu"),"titre1":"Ton processeur :","titre2":"Processeurs","x_y_h1_h2":(40,100,30,30),"largeur_max":180,"modif":"Choisissez un composant"}
        self.dico_gpu = {"liste":self.recup_info(self.listeGpu),"nom":iPC.getName("gpu"),"titre1":"Ta carte graphique :","titre2":"Cartes graphiques","x_y_h1_h2":(40,155,30,30),"largeur_max":286,"modif":"Choisissez un composant"}
        self.dico_mb = {"liste":self.recup_info(self.listeMb),"nom":iPC.getName("motherboard"),"titre1":"Ta carte mere :","titre2":"Cartes mère","x_y_h1_h2":(40,210,30,30),"largeur_max":364,"modif":"Choisissez un composant"}
        self.dico_ram = {"liste":self.recup_info(self.listeRam),"nom":self.ram,"titre1":"Tes RAMs :","titre2":"Mémoire vive","x_y_h1_h2":(40,265,30,30),"largeur_max":279,"modif":"Choisissez un composant"}
        self.dico_ssd = {"liste":self.recup_info(self.listeSsd),"nom":self.ssd,"titre1":"Tes disques durs SSD :","titre2":"Disques dur (ssd)","x_y_h1_h2":(40,375,30,30),"largeur_max":260,"modif":"Choisissez un composant"}
        self.dico_hdd = {"liste":self.recup_info(self.listeHdd),"nom":self.hdd,"titre1":"Tes disques durs HDD :","titre2":"Disques dur (hdd)","x_y_h1_h2":(40,320,30,30),"largeur_max":238,"modif":"Choisissez un composant"}
        
        self.dico_composant = {"os":self.dico_os,"cpu":self.dico_cpu,"gpu":self.dico_gpu,"mb":self.dico_mb,"ram":self.dico_ram,"ssd":self.dico_ssd,"hdd":self.dico_hdd}
        
        
        # =============================================================================#
        # Variables des permettant des ce situés sur les différentes pages             #
        # =============================================================================#
        self.repertoire = {}
        self.statut = False
        self.statut_auto = False
        self.botOnline = False
        
        self.root.protocol("WM_DELETE_WINDOW",self.fermeture)#protocole de fermeture des fenêtres

    def jeffAssistant(self):
        """Création de la fenêtre de l'assistant"""
        if self.botOnline == False:
            self.botOnline = True
            self.rootAssistant = Tk() #Création de la fenêtre Tkinter de l'assistant 
            self.Interface = InterfaceBot(self.rootAssistant,self) #Création de la fenêtre de l'assistant
            self.rootAssistant.configure(bg="#19232d") #Couleur de fond de la fenêtre
            self.rootAssistant.geometry('400x400') #Dimension de la fenêtre de l'assistant
            self.rootAssistant.title("Jeff Assistant") #Titre la fenêtre de l'assistant
            self.rootAssistant.iconbitmap("logo.ico") #Logo de la fenêtre
            self.rootAssistant.mainloop()
        

        
 
    def main(self):
        """Création de la première fenetre de notre application avec 
        L'affichage de nos composants
        Les boutons pour modifier son pc, en faire un nouveau, en faire un automatique"""
        
        self.statut,self.statut_auto=False,False #On initialise les variables statut et statut_auto
        self.repertoire = {}
        
        for elt in self.dico_composant.values():
            elt["modif"]="Choisissez un composant"
        
        # =============================================================================#
        # On unbind les enter / leave / les clics de boutton / le Entrée               #
        # =============================================================================#
 
        self.root.unbind("<Return>")
        self.Can.unbind("<Enter>")
        self.Can.unbind("<Leave>")
        self.Can.unbind("<Button-1>")
        
        self.Can.destroy() #Détruit le Canvas précédent pour laisser place à un nouveau
        self.Can = Canvas(self.root, width=840, height=600, bg='#19232d') #Création d'un Canvas avec sa taille et sa couleur de fond
        self.Can.pack() #On place ce Canvas
        
        # ==========================================================================================
        # Fonction main pour placer toutes les informations du menu et l'accès aux autres pages----#
        # ==========================================================================================         
        bouton_modif = Button(self.Can,image=self.img_modifi_pc1, cursor="hand2", command= lambda : self.modifie_pc(), borderwidth=0, highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_modif.place(x=525, y=40)
        
        bouton_modif.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_modif,"bouton_modif"))
        bouton_modif.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_modif,"bouton_modif"))
    
        bouton_nouveau_pc = Button(self.Can,image=self.img_nouveau_pc1,cursor="hand2", command= lambda : self.new_pc(), borderwidth=0, highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_nouveau_pc.place(x=525, y=180)
        
        bouton_nouveau_pc.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_nouveau_pc,"bouton_nouveau_pc"))
        bouton_nouveau_pc.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_nouveau_pc,"bouton_nouveau_pc"))   
     
    
        bouton_auto = Button(self.Can,image=self.img_config_auto1, cursor="hand2",  command= lambda : self.auto_pc(), borderwidth=0, highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_auto.place(x=525, y=320)

        bouton_auto.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_auto,"bouton_auto"))
        bouton_auto.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_auto,"bouton_auto"))    
        
        fond1 = Label(self.Can,image = self.img_fond_compo1)
        fond1.place(x=25, y=20)
        
        logo = Label(self.Can,image=self.img_logo_in1,borderwidth=0, highlightthickness = 0, bd = 0)
        logo.place(x=570, y=425)
        
        bouton_assistant = Button(self.Can,image=self.img_assistant1, cursor="hand2",  command= lambda : self.jeffAssistant(), borderwidth=0, highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_assistant.place(x=770, y=538)  
        bouton_assistant.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_assistant,"bouton_assistant"))
        bouton_assistant.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_assistant,"bouton_assistant"))    
        
        
        #Création de zones de texte----------------------------------------------------
    
        for elt in self.dico_composant.values():
            elt["label"] = Label(self.root, text=elt["titre1"], font=("Raleway",13), anchor="w", bg='#2f3136', fg='#6699ff' )
            elt["label"].place(x=elt["x_y_h1_h2"][0], y=elt["x_y_h1_h2"][1]+30, height=elt["x_y_h1_h2"][2], width=411)
            elt["label2"] = Label(self.root, text=elt["nom"], font=("Amaranth",12), anchor="w", bg='#2f3136', fg='cyan')
            elt["label2"].place(x=elt["x_y_h1_h2"][0], y=elt["x_y_h1_h2"][1]+55, height=elt["x_y_h1_h2"][3], width=411)
        
        bienvenue = Label(self.root, text="Bienvenue sur PBS !", font=("Amaranth",34), anchor="w",bg='#2f3136', fg='#6699ff')
        bienvenue.place(x=50, y=490, height=40, width=381)
        
        ton_pc = Label(self.root, text="TON PC : ", font=("Amaranth",24), anchor="w",bg='#2f3136', fg='#6699ff')
        ton_pc.place(x=180, y=40, height=40, width=211)
        

        
    def modifie_pc(self):
        """Fonction permettant de modifier son pc avec la création d'un nouveau Canvas"""
        self.Can.destroy()
        self.Can = Canvas(self.root, width=840, height=600, bg='#19232d')
        self.Can.pack()
        
        # =============================================================================#
        # On unbind les enter / leave / les clics de boutton / le Entrée               #
        # =============================================================================#
        self.root.unbind("<Return>")
        self.Can.unbind("<Enter>")
        self.Can.unbind("<Leave>")
        self.Can.unbind("<Button-1>")
        
        self.content = "Modification du PC : \n"
        
        # ==========================================================================================
        # Création de la page modifier_pc et placement des informations nécessaires----------------#
        # ==========================================================================================
        
        bouton_retour = Button(self.Can,image=self.img_retour1, cursor="hand2", command = lambda : self.main(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_retour.place(x=180, y=500)
        
        bouton_valider = Button(self.Can,image=self.img_valider1, cursor="hand2", command= lambda : self.validation("modif_pc"), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_valider.place(x=510, y=500)    
    
        bouton_retour.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_retour,"bouton_retour"))
        bouton_retour.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_retour,"bouton_retour")) 
        
        bouton_valider.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_valider,"bouton_valider"))
        bouton_valider.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_valider,"bouton_valider")) 
        
        fond_gauche = Label(self.Can,image = self.img_fond_compo5, borderwidth=0)
        fond_gauche.place(x=20, y=25)
        
        fond_droite = Label(self.Can,image = self.img_fond_compo3, borderwidth=0)
        fond_droite.place(x=470, y=25)
        
        bouton_logo=Button(self.Can,image=self.img_logo_in2, cursor="hand2", command= lambda : self.main(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')        
        bouton_logo.place(x=367, y=480)
        
        bouton_assistant = Button(self.Can,image=self.img_assistant1, cursor="hand2",  command= lambda : self.jeffAssistant(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_assistant.place(x=770, y=538)  
        bouton_assistant.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_assistant,"bouton_assistant"))
        bouton_assistant.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_assistant,"bouton_assistant"))  
       
        #Création de zones de texte à l'aide d'un dictionnaire préalablement construit---        
       
        for elt in self.dico_composant.values():
            elt["label"] = Label(self.root, text=elt["titre1"], font=("Raleway",13), anchor="w",cursor='hand2', bg='#2f3136', fg='#6699ff' )
            elt["label"].place(x=elt["x_y_h1_h2"][0], y=elt["x_y_h1_h2"][1], height=elt["x_y_h1_h2"][2], width=400)
            elt["label"].bind("<Enter>", self.survol_on_2)
            elt["label"].bind("<Leave>", self.survol_off_2)
            elt["label"].bind("<Button-1>", self.changer_compo)
            if self.statut == False:
                elt["label2"] = Label(self.root, text=elt["nom"], font=("Amaranth",12), anchor="w",cursor='hand2' , bg='#2f3136', fg='cyan')
            else:
                elt["label2"] = Label(self.root, text=elt["modif"], font=("Amaranth",12), anchor="w",cursor='hand2' , bg='#2f3136', fg='cyan')
            elt["label2"].place(x=elt["x_y_h1_h2"][0], y=elt["x_y_h1_h2"][1]+25, height=elt["x_y_h1_h2"][3], width=400)
            elt["label2"].bind("<Enter>", self.survol_on_2)
            elt["label2"].bind("<Leave>", self.survol_off_2)
            elt["label2"].bind("<Button-1>", self.changer_compo)
            
        #-------------------Barre de recherche-----------------------
        
        self.search_bar = Entry(fond_droite, width = 28, insertontime = 400, insertofftime = 400, font = ("TkDefaultFont",13))
        self.search_bar.place(x = 27, y = 70, height = 25)
        
        self.search_btn = Button(fond_droite,image=self.img_rechercher1,command=lambda : self.rechercher(None),cursor = "hand2", borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        self.search_btn.place(x = 293, y = 70, height = 25)

        self.search_btn.bind("<Enter>", lambda i : self.survol_on(i,self.dico,self.search_btn,"bouton_rechercher"))
        self.search_btn.bind("<Leave>", lambda i : self.survol_off(i,self.dico,self.search_btn,"bouton_rechercher"))
        
        self.root.bind("<Return>", self.rechercher)
        
       
        #-----------------Variables pour scrollbar-------------------
              
        self.frame1 = Frame(fond_droite,relief=GROOVE, height= 410, width = 330,highlightthickness=1,highlightbackground='cyan')
        self.Can2 = Canvas(self.frame1,bg='#19232d',highlightthickness=0)
        self.frame2 = Frame(self.Can2,bg='#19232d')        
        self.scrollbar = Scrollbar(self.frame1, orient="vertical", command=self.Can2.yview)
        
        #-------------Configuration de la scrollbar------------------
        
        self.frame1.place( x = 15, y = 110)       
        self.Can2.configure(yscrollcommand=self.scrollbar.set)      
        self.scrollbar.pack(fill="y", side="right")
        self.Can2.pack(side="left")        
        self.Can2.create_window((0,0),window=self.frame2,anchor='nw')
        self.frame2.bind("<Configure>",self.scrollbar_configure)
        
        self.frame2.configure(width=300,height=310)  

        self.Can2.bind_all("<MouseWheel>", self.on_mousewheel)
        
        #------------------------------------------------------------
        
        titre = Label(self.root, text="", font=("Raleway",25), anchor="center", bg='#2f3136', fg='#6699ff' )
        titre.place(x=490, y=45, height=40,width=fond_droite.winfo_width()-40) 
        
        # ==========================================================================================
        # Création de la page nouveau_pc et placement des informations nécessaires-----------------#
        # ==========================================================================================
        
    def new_pc(self):
        """Fonction permettant de créer un nouveau pc avec la création d'un nouveau Canvas"""
        self.Can.destroy()
        self.Can = Canvas(self.root, width=840, height=600, bg='#19232d')
        self.Can.pack()

        # =============================================================================#
        # On unbind les enter / leave / les clics de boutton / le Entrée               #
        # =============================================================================#
        self.root.unbind("<Return>")
        self.Can.unbind("<Enter>")
        self.Can.unbind("<Leave>")
        self.Can.unbind("<Button-1>")
        
        self.content = "Nouveau PC : \n"
        
        self.repertoire = {}
        if self.statut_auto==False:
            bouton_retour = Button(self.Can,image=self.img_retour1, cursor="hand2", command = lambda : self.main(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        else:
            bouton_retour = Button(self.Can,image=self.img_retour1, cursor="hand2", command = lambda : self.auto_valider(None), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_retour.place(x=180, y=500)
        
        bouton_valider = Button(self.Can,image=self.img_valider1, cursor="hand2", command= lambda : self.validation("new_pc"), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_valider.place(x=510, y=500)    
    
        bouton_retour.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_retour,"bouton_retour"))
        bouton_retour.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_retour,"bouton_retour")) 
        
        bouton_valider.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_valider,"bouton_valider"))
        bouton_valider.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_valider,"bouton_valider")) 
        
        fond_gauche = Label(self.Can,image = self.img_fond_compo5, borderwidth=0)
        fond_gauche.place(x=20, y=25)
        
        fond_droite = Label(self.Can,image = self.img_fond_compo3, borderwidth=0)
        fond_droite.place(x=470, y=25) 
        
        bouton_logo=Button(self.Can,image=self.img_logo_in2, cursor="hand2", command= lambda : self.main(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')        
        bouton_logo.place(x=367, y=480)
        
        bouton_assistant = Button(self.Can,image=self.img_assistant1, cursor="hand2",  command= lambda : self.jeffAssistant(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_assistant.place(x=770, y=538)  
        bouton_assistant.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_assistant,"bouton_assistant"))
        bouton_assistant.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_assistant,"bouton_assistant"))  
       
        for elt in self.dico_composant.values():
            elt["label"] = Label(self.root, text=elt["titre1"], font=("Raleway",13), anchor="w",cursor='hand2', bg='#2f3136', fg='#6699ff' )
            elt["label"].place(x=elt["x_y_h1_h2"][0], y=elt["x_y_h1_h2"][1], height=elt["x_y_h1_h2"][2], width=371)
            elt["label"].bind("<Enter>", self.survol_on_2)
            elt["label"].bind("<Leave>", self.survol_off_2)
            elt["label"].bind("<Button-1>", self.changer_compo)  
            elt["label2"] = Label(self.root, text=elt["modif"], font=("Amaranth",12), anchor="w",cursor='hand2' , bg='#2f3136', fg='cyan')
            elt["label2"].place(x=elt["x_y_h1_h2"][0], y=elt["x_y_h1_h2"][1]+25, height=elt["x_y_h1_h2"][3], width=371)
            elt["label2"].bind("<Enter>", self.survol_on_2)
            elt["label2"].bind("<Leave>", self.survol_off_2)
            elt["label2"].bind("<Button-1>", self.changer_compo)
        
        #-------------------Barre de recherche----------------------
        
        self.search_bar = Entry(fond_droite, width = 25, insertontime = 400, insertofftime = 400, font = ("Raleway",13),bg = "#BDD0EE")
        self.search_bar.place(x = 27, y = 70, height = 25)
        
        self.search_btn = Button(fond_droite,image=self.img_rechercher1,command=lambda : self.rechercher(None),cursor = "hand2", borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        self.search_btn.place(x = 293, y = 70, height = 25)
              
        self.search_btn.bind("<Enter>", lambda i : self.survol_on(i,self.dico,self.search_btn,"bouton_rechercher"))
        self.search_btn.bind("<Leave>", lambda i : self.survol_off(i,self.dico,self.search_btn,"bouton_rechercher"))     
            
       #-----------------Variables pour scrollbar-------------------
       
        self.fg = "#000000"
        self.font = "Verdana 10"
         
        self.frame1 = Frame(fond_droite, relief=GROOVE, height= 410, width = 330, highlightthickness=1, highlightbackground='cyan')
        self.Can2 = Canvas(self.frame1,bg='#19232d',highlightthickness=0)
        self.frame2 = Frame(self.Can2,bg='#19232d')
        
        self.scrollbar = Scrollbar(self.frame1, orient="vertical", command=self.Can2.yview)
        
        self.root.bind("<Return>", self.rechercher)
        
        #-------------Configuration de la scrollbar------------------
        
        self.frame1.place( x = 15, y = 110)
        
        self.Can2.configure(yscrollcommand=self.scrollbar.set)
      
        self.scrollbar.pack(fill="y", side="right")
        self.Can2.pack(side="left")
        
        self.Can2.create_window((0,0),window=self.frame2,anchor='nw')
        self.frame2.bind("<Configure>",self.scrollbar_configure)
        self.frame2.configure(width=300,height=310) 
        
        #-------------------------
        
        # ==========================================================================================
        # Création de la page auto_pc et placement des informations nécessaires--------------------#
        # ==========================================================================================       
        
    def auto_pc(self):
        """Fonction permettant de créer un nouveau pc avec un prix ou une puissance choisi"""
        self.statut=False
        self.statut_auto=False
        
        
        # =============================================================================#
        # On unbind les enter / leave / les clics de boutton / le Entrée               #
        # =============================================================================#        
        self.root.unbind("<Return>")
        self.Can.unbind("<Enter>")
        self.Can.unbind("<Leave>")
        self.Can.unbind("<Button-1>")
        
        self.Can.destroy()
        self.Can = Canvas(self.root, width=840, height=600, bg='#19232d')
        self.Can.pack()
        
        self.var = True
        
        
        # ==========================================================================================
        # Création de la page auto_pc et placement des informations nécessaires--------------------#
        # ==========================================================================================    
        
        bouton_retour = Button(self.Can,image=self.img_retour1, cursor="hand2", command= lambda : self.main(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_retour.place(x=180, y=500)
        
        bouton_valider=Button(self.Can,image=self.img_valider1, cursor="hand2", command= lambda : self.auto_valider(None), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_valider.place(x=510, y=500)
        
        self.root.bind("<Return>", self.auto_valider)
    
        bouton_retour.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_retour,"bouton_retour"))
        bouton_retour.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_retour,"bouton_retour")) 
    
        bouton_valider.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_valider,"bouton_valider"))
        bouton_valider.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_valider,"bouton_valider"))       

        logo_compo3 = Label(self.Can,image = self.img_fond_compo3, borderwidth=0)
        logo_compo3.place(x=20, y=25)
        logo_compo4 = Label(self.Can,image = self.img_fond_compo3, borderwidth=0)
        logo_compo4.place(x=470, y=25) 
        
        bouton_logo=Button(self.Can,image=self.img_logo_in2, cursor="hand2", command= lambda : self.main(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')        
        bouton_logo.place(x=367, y=480)
                
        self.fct_prix = Entry(self.Can, width=14, bg='#19232d', justify='center', fg='cyan',font=('Samsung Sharp Sans-Bold',30))        
        command = self.fct_prix.register(self.verif_int_entry)
        self.fct_prix.configure(validatecommand=(command, '%P'), validate='key') 
        self.fct_prix.insert(0,"0")
        self.fct_prix.place(x=95, y=180, width=200, height=80)
        fct_prix_l = Label(self.Can, text="Le prix souhaité :",fg='cyan',bg='#2f3136',justify='center', font=('Samsung Sharp Sans-Bold',20))
        fct_prix_l.place(x=90, y=105)
    
        self.fct_puissance = Entry(self.Can, width=14, bg='#19232d', justify='center', fg='cyan',font=('Samsung Sharp Sans-Bold',30))
        command2 = self.fct_puissance.register(self.verif_int_entry)
        self.fct_puissance.configure(validatecommand=(command2, '%P'), validate='key')
        self.fct_puissance.insert(0,"0")
        self.fct_puissance.place(x=550, y=180, width=200, height=80)
        fct_puissance_l = Label(self.Can, text="La puissance souhaité :",fg='cyan',bg='#2f3136',justify='center', font=('Samsung Sharp Sans-Bold',20))
        fct_puissance_l.place(x=500, y=105)
                
        bouton_info=Button(self.Can,image=self.img_info1, cursor="hand2", command= lambda : self.info_bench(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_info.place(x=725, y=400)
    
        bouton_info.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_info,"bouton_info"))
        bouton_info.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_info,"bouton_info")) 
        
        self.texte_info1 = Label(self.root, text=" ", font=("Raleway",9), anchor="w", bg='#2f3136', fg='#6699ff')
        self.texte_info1.place(x=500, y=320, height=80, width=300)
        
        bouton_assistant = Button(self.Can,image=self.img_assistant1, cursor="hand2",  command= lambda : self.jeffAssistant(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_assistant.place(x=770, y=538)  
        bouton_assistant.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_assistant,"bouton_assistant"))
        bouton_assistant.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_assistant,"bouton_assistant"))  


        
    def validation(self,prev_page):
        """Fonction de validation pour -Modif_pc- et New_pc-"""
        self.statut=True
        
        # =============================================================================#
        # On unbind les enter / leave / les clics de boutton / le Entrée               #
        # =============================================================================#
        self.root.unbind("<Return>")
        self.Can.unbind("<Enter>")
        self.Can.unbind("<Leave>")
        self.Can.unbind("<Button-1>")
        
        for elt in self.dico_composant.values():
            elt["modif"]=elt["label2"].cget("text")
        self.prix_final = 0
        
        for dico in self.dico_composant.values():
            for elt in dico["liste"]:
                if dico["modif"]==self.hdd or dico["modif"]==self.ssd:
                    pass
                elif dico["liste"][elt]["nom"]==dico["modif"]:
                    self.content += dico["modif"] +" -> "+str(dico["liste"][elt]["prix"])+"€" + " | Lien : "+dico["liste"][elt]["lien"]+ "\n"
                    self.prix_final+=int(dico["liste"][elt]["prix"])
            
        self.content += "Prix Total : " + str(self.prix_final) + "€"
        
        self.Can.destroy()
        self.Can = Canvas(self.root, width=840, height=600, bg='#19232d')
        self.Can.pack()
        
        
        # ==========================================================================================
        # Création de la page de validation de modif_pc et nouveau_pc-----------------------------#
        # ==========================================================================================
        
        self.bouton_retour = Button(self.Can,image=self.img_retour1, cursor="hand2", command = lambda : self.dico_page[prev_page](), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        self.bouton_retour.place(x=180, y=500)
        
        self.bouton_telecharger=Button(self.Can,image=self.img_telecharger1, cursor="hand2", command= lambda : self.telecharger_recap(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        self.bouton_telecharger.place(x=510, y=500)    
    
        self.bouton_retour.bind("<Enter>", lambda i : self.survol_on(i,self.dico,self.bouton_retour,"bouton_retour"))
        self.bouton_retour.bind("<Leave>", lambda i : self.survol_off(i,self.dico,self.bouton_retour,"bouton_retour")) 
        
        self.bouton_telecharger.bind("<Enter>", lambda i : self.survol_on(i,self.dico,self.bouton_telecharger,"bouton_telecharger"))
        self.bouton_telecharger.bind("<Leave>", lambda i : self.survol_off(i,self.dico,self.bouton_telecharger,"bouton_telecharger"))    
        
        self.fond = Label(self.Can,image = self.img_fond_compo4, borderwidth=0)
        self.fond.place(x=20, y=25)
        
        self.bouton_logo=Button(self.Can,image=self.img_logo_in2, cursor="hand2", command= lambda : self.main(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')        
        self.bouton_logo.place(x=367, y=480)
        
        self.bouton_assistant = Button(self.Can,image=self.img_assistant1, cursor="hand2",  command= lambda : self.jeffAssistant(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        self.bouton_assistant.place(x=770, y=538)  
        self.bouton_assistant.bind("<Enter>", lambda i : self.survol_on(i,self.dico,self.bouton_assistant,"bouton_assistant"))
        self.bouton_assistant.bind("<Leave>", lambda i : self.survol_off(i,self.dico,self.bouton_assistant,"bouton_assistant"))  
        
        #Création de zones de texte----------------------------------------------------
        
        titre_recap = Label(self.root, text="Voici ta liste d'achats : ", font=("Raleway",17), anchor="w", bg='#2f3136', fg='#008AF5')
        titre_recap.place(x=340, y=45, height=30, width=251)
    
        systeme_os = Label(self.root, text="Le système d'exploitation : ", font=("Raleway",15), anchor="w", bg='#2f3136', fg='#6699ff')
        systeme_os.place(x=50, y=70, height=30, width=251)
        systeme_os_info = Label(self.root, text=self.dico_os["modif"], font=("Amaranth",14), anchor="w", bg='#2f3136', fg='cyan')
        systeme_os_info.place(x=50, y=100, height=30, width=411)
        
        processeur = Label(self.root, text="Le processeur : ", font=("Raleway",15), anchor="w", bg='#2f3136', fg='#6699ff')
        processeur.place(x=50, y=130, height=30, width=411)
        processeur_info = Label(self.Can, text=self.dico_cpu["modif"], font=("Amaranth",14), anchor="w", bg='#2f3136', fg='cyan')
        processeur_info.place(x=50, y=160, height=30, width=411)
        
        carte_graphique = Label(self.root, text="La carte graphique : ", font=("Raleway",15), anchor="w", bg='#2f3136', fg='#6699ff')
        carte_graphique.place(x=50, y=190, height=30, width=411)
        carte_graphique_info = Label(self.root, text=self.dico_gpu["modif"], font=("Amaranth",14), anchor="w", bg='#2f3136', fg='cyan')
        carte_graphique_info.place(x=50, y=220, height=30, width=411)
        
        carte_mere = Label(self.root, text="La carte mère : ", font=("Raleway",15), anchor="w", bg='#2f3136', fg='#6699ff')
        carte_mere.place(x=50, y=250, height=30, width=411)
        carte_mere_info = Label(self.Can, text=self.dico_mb["modif"], font=("Amaranth",14), anchor="w", bg='#2f3136', fg='cyan')
        carte_mere_info.place(x=50, y=280, height=30, width=611)
        
        memoire_vive = Label(self.root, text="La mémoire vive : ", font=("Raleway",15), bg='#2f3136', anchor="w", fg='#6699ff')
        memoire_vive.place(x=50, y=310, height=30, width=411)
        memoire_vive_info = Label(self.root, text=self.dico_ram["modif"], font=("Amaranth",14), bg='#2f3136', anchor="w", fg='cyan')
        memoire_vive_info.place(x=50, y=340, height=30, width=411)
    
        disque_dur = Label(self.root, text="Le disque dur :", font=("Raleway",15), anchor="w",bg='#2f3136', fg='#6699ff')
        disque_dur.place(x=50, y=370, height=30, width=411)
        disque_dur_info = Label(self.root, text=(self.dico_hdd["modif"]+"\n"+self.dico_ssd["modif"]), font=("Amaranth",14), anchor="w", bg='#2f3136', fg='cyan')
        disque_dur_info.place(x=50, y=400, height=50, width=411)

        recap_prix = Label(self.root, text="Le prix :", font=("Raleway",21), anchor="w",bg='#2f3136', fg='#6699ff')
        recap_prix.place(x=650, y=250, height=40, width=111)
        recap_prix_info = Label(self.root, text=str(self.prix_final)+"€", font=("Amaranth",20), anchor="w", bg='#2f3136', fg='cyan')
        recap_prix_info.place(x=650, y=300, height=40, width=111) 


        
    def auto_valider(self,event):
        """Fonction de validation une fois que l'on a choisi un prix ou une puissance"""

        # =============================================================================#
        # On unbind les enter / leave / les clics de boutton / le Entrée               #
        # =============================================================================#        
        self.root.unbind("<Return>")
        self.Can.unbind("<Enter>")
        self.Can.unbind("<Leave>")
        self.Can.unbind("<Button-1>")

        if self.statut_auto==False:    
            self.prix = int(self.fct_prix.get())
            self.puissance = float(self.fct_puissance.get())
        
        # ===========================================================================================#
        #  On récupere les composants permettant une config au plus proche du prix/puissance demandé #
        # ===========================================================================================#
        if self.prix == 0 and self.puissance==0:
            messagebox.showerror(title="ERREUR", message="Tu dois choisir au moins un prix ou une puissance.")
            return(self.auto_pc())
        elif self.prix != 0 and self.puissance==0:
            os = self.recherchePlusProche("prix",self.prix*(10/100),"os")
            cpu = self.recherchePlusProche("prix",self.prix*(30/100),"cpu")
            gpu = self.recherchePlusProche("prix",self.prix*(30/100),"gpu")
            mb = self.recherchePlusProche("prix",self.prix*(9/100),"mb")
            ram = self.recherchePlusProche("prix",self.prix*(18/100),"ram")
            ssd = self.recherchePlusProche("prix",self.prix*(7/100),"ssd")
            hdd = self.recherchePlusProche("prix",self.prix*(6/100),"hdd")
        elif self.prix==0 and self.puissance!=0:
            self.symb = ""
            os = ["Un OS n'a pas de Puissance, à vous de voir ;)",0,0] #Un os n'a pas de puissance
            cpu = self.recherchePlusProche("puissance",self.puissance*(30/100),"cpu")
            gpu = self.recherchePlusProche("puissance",self.puissance*(30/100),"gpu")
            mb = ["Une Carte Mere n'a pas de Puissance, à vous de voir ;)",0,0] #Une carte mère n'a pas de puissannce
            ram = self.recherchePlusProche("puissance",self.puissance*(18/100),"ram")
            ssd = self.recherchePlusProche("puissance",self.puissance*(15/100),"ssd")
            hdd = self.recherchePlusProche("puissance",self.puissance*(8/100),"hdd")
        elif self.prix !=0 and self.puissance!=0:
            messagebox.showerror(title="ERREUR", message="Tu dois choisir SOIT un prix SOIT une puissance.")
            return(self.auto_pc())
        
        self.statut=True
        self.statut_auto=True
        # ============================================================================#
        # On ajoute les composants au dictionnaire global                             #
        # ============================================================================#
        self.dico_composant["os"]["modif"]=os[0]
        self.dico_composant["cpu"]["modif"]=cpu[0]
        self.dico_composant["gpu"]["modif"]=gpu[0]
        self.dico_composant["mb"]["modif"]=mb[0]
        self.dico_composant["ram"]["modif"]=ram[0]
        self.dico_composant["ssd"]["modif"]=ssd[0]
        self.dico_composant["hdd"]["modif"]=hdd[0]

        prix_final = 0 #Initialisation de la variable du prix total final
        
        # ============================================================================#
        # On créé le contenu du txt que l'on va mettre à disposition                  #
        # ============================================================================#        

        self.content = "Configuration Automatique : \n"
        for dico in self.dico_composant.values():
            for elt in dico["liste"]:
                if dico["liste"][elt]["nom"]==dico["modif"]:
                    self.content += dico["modif"] +" -> "+str(dico["liste"][elt]["prix"])+"€" + " | Lien : "+dico["liste"][elt]["lien"]+ "\n"
                    prix_final+=int(dico["liste"][elt]["prix"])
            
        self.content += "Prix Total : " + str(prix_final) + "€"


        self.Can.destroy()
        self.Can = Canvas(self.root, width=840, height=600, bg='#19232d')
        self.Can.pack()
        
        # ==========================================================================================
        # Création de la page de validation de auto_pc---------------------------------------------#
        # ==========================================================================================
        
        bouton_retour = Button(self.Can,image=self.img_retour1, cursor="hand2", command = lambda : self.auto_pc(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_retour.place(x=180, y=500)
        
        self.verif_auto_valider = True

        bouton_telecharger=Button(self.Can,image=self.img_telecharger1, cursor="hand2", command= lambda : self.telecharger_recap(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_telecharger.place(x=510, y=500)    
 
        bouton_retour.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_retour,"bouton_retour"))
        bouton_retour.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_retour,"bouton_retour")) 

        bouton_logo=Button(self.Can,image=self.img_logo_in2, cursor="hand2", command= lambda : self.main(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')        
        bouton_logo.place(x=367, y=480)
        
        bouton_telecharger.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_telecharger,"bouton_telecharger"))
        bouton_telecharger.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_telecharger,"bouton_telecharger"))    
        
        fond = Label(self.Can,image = self.img_fond_compo4, borderwidth=0)
        
        fond.place(x=20, y=25)
        
        #Création de zones de texte----------------------------------------------------
         
        titre_recap = Label(self.Can, text="Ce pc te convient-il ? ", font=("Raleway",20), anchor="w", bg='#2f3136', fg='#008AF5')
        titre_recap.place(x=505, y=45, height=40, width=271)
    
        systeme_os = Label(self.Can, text="Le systeme d'exploitation : ", font=("Raleway",13), anchor="w", bg='#2f3136', fg='#6699ff')
        systeme_os.place(x=50, y=50, height=30, width=251)
        systeme_os_info = Label(self.Can, text=os[0]+" ---> "+str(os[1])+"€", font=("Amaranth",12), anchor="w", bg='#2f3136', fg='cyan')
        systeme_os_info.place(x=50, y=80, height=30, width=411)
        
        processeur = Label(self.Can, text="Le processeur : ", font=("Raleway",13), anchor="w", bg='#2f3136', fg='#6699ff')
        processeur.place(x=50, y=110, height=30, width=511)
        processeur_info = Label(self.Can, text=cpu[0]+" ---> "+str(cpu[1])+"€", font=("Amaranth",12), anchor="w", bg='#2f3136', fg='cyan')
        processeur_info.place(x=50, y=140, height=30, width=511)
        
        carte_graphique = Label(self.Can, text="La carte graphique : ", font=("Raleway",13), anchor="w", bg='#2f3136', fg='#6699ff')
        carte_graphique.place(x=50, y=170, height=30, width=511)
        carte_graphique_info = Label(self.Can, text=gpu[0]+" ---> "+str(gpu[1])+"€", font=("Amaranth",12), anchor="w", bg='#2f3136', fg='cyan')
        carte_graphique_info.place(x=50, y=200, height=30, width=511)
        
        carte_mere = Label(self.Can, text="La carte mère : ", font=("Raleway",13), anchor="w", bg='#2f3136', fg='#6699ff')
        carte_mere.place(x=50, y=230, height=30, width=511)
        carte_mere_info = Label(self.Can, text=mb[0]+" ---> "+str(mb[1])+"€", font=("Amaranth",12), anchor="w", bg='#2f3136', fg='cyan')
        carte_mere_info.place(x=50, y=260, height=30, width=511)
        
        memoire_vive = Label(self.Can, text="La mémoire vive : ", font=("Raleway",13), bg='#2f3136', anchor="w", fg='#6699ff')
        memoire_vive.place(x=50, y=290, height=30, width=511)
        memoire_vive_info = Label(self.Can, text=ram[0]+" ---> "+str(ram[1])+"€", font=("Amaranth",12), bg='#2f3136', anchor="w", fg='cyan')
        memoire_vive_info.place(x=50, y=320, height=30, width=511)
    
        disque_dur = Label(self.Can, text="Tes disques dur :", font=("Raleway",13), anchor="w",bg='#2f3136', fg='#6699ff')
        disque_dur.place(x=50, y=350, height=30, width=511)
        
        disque_dur_info = Label(self.Can, text="HDD : "+hdd[0]+" ---> "+str(hdd[1])+"€", font=("Amaranth",12), anchor="w", bg='#2f3136', fg='cyan')
        disque_dur_info.place(x=50, y=410, height=30, width=511)
        disque_dur2_info = Label(self.Can, text="SSD : "+ssd[0]+" ---> "+str(ssd[1])+"€", font=("Amaranth",12), anchor="w", bg='#2f3136', fg='cyan')
        disque_dur2_info.place(x=50, y=380, height=30, width=511)


        prix_total = str(os[1]+cpu[1]+gpu[1]+mb[1]+ram[1]+ssd[1]+hdd[1])
        puissance_total = str(os[2]+cpu[2]+gpu[2]+mb[2]+ram[2]+ssd[2]+hdd[2])[:6]

        prix_fin = Label(self.Can, text="Prix total :", font=("Raleway",22), bg='#2f3136', anchor="w", fg='#6699ff')
        prix_fin.place(x=570, y=250, height=30, width=221)
        prix_fin_i = Label(self.Can, text=prix_total+"€", font=("Amaranth",20), bg='#2f3136', anchor="w", fg='cyan')
        prix_fin_i.place(x=600, y=280, height=40, width=191)
        
        puissance_fin = Label(self.Can, text="Puissance totale :", font=("Raleway",22), bg='#2f3136', anchor="w", fg='#6699ff')
        puissance_fin.place(x=570, y=350, height=30, width=221)
        puissance_fin_i = Label(self.Can, text=puissance_total, font=("Amaranth",20), bg='#2f3136', anchor="w", fg='cyan')
        puissance_fin_i.place(x=600, y=380, height=40, width=191)
        
        bouton_modifier=Button(self.Can,image=self.img_modif_compo_auto1, cursor="hand2", command= lambda : self.new_pc(), borderwidth=0,highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_modifier.place(x=565, y=150)       
        bouton_modifier.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_modifier,"bouton_modif_compo_auto"))
        bouton_modifier.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_modifier,"bouton_modif_compo_auto"))
        
        bouton_assistant = Button(self.Can,image=self.img_assistant1, cursor="hand2",  command= lambda : self.jeffAssistant(), borderwidth=0, highlightthickness = 0, bd = 0, activebackground='#2f3136')
        bouton_assistant.place(x=770, y=538)  
        bouton_assistant.bind("<Enter>", lambda i : self.survol_on(i,self.dico,bouton_assistant,"bouton_assistant"))
        bouton_assistant.bind("<Leave>", lambda i : self.survol_off(i,self.dico,bouton_assistant,"bouton_assistant"))    
        
    def recup_info(self,liste:list)->dict:
        """
        Parameters
        ----------
        liste : LIST
            Liste correspondante aux lignes des csv

        Returns
        -------
        dico : DICT
            Renvoie un dictionnaire de dictionnaire nous permettant de récupérer toutes les infos que l'on utilise.
        """
        dico = {}
        if liste != self.listeMb and liste != self.listeOs: #On cherche les csvs qui n'ont pas le meme patern
            for elt in liste:
                dico[str(elt[2])+" "+str(elt[3])] = {"nom":str(elt[2])+" "+str(elt[3]),"prix":int(elt[-1]),"puissance":float(elt[5]),"lien":elt[-2]}
        elif liste == self.listeMb:            
            for elt in liste:
                dico[str(elt[0]+" "+elt[1])]={"nom":str(elt[0]+" "+elt[1]),"prix":int(elt[-1]),"puissance":0,"lien":"Pas de lien disponible"}
        elif liste == self.listeOs:
            for elt in liste:
                dico[str(elt[1])+" "+str(elt[2])] = {"nom":str(elt[1])+" "+str(elt[2]),"prix":int(elt[-1]),"puissance":0,"lien":elt[-2]}
        return dico
    
    def changement_modif_pc(self,event,dico:dict,rep:dict):
        """Fonction permettant de changer le nom du composant utilisé par celui sur lequel on vient de cliquer (fonctionne avec un bind)""" 
        rep["label2"].configure(text=dico[event.widget]) #on change le text du label par celui sur lequel on vient de cliquer
        rep["modif"]=dico[event.widget] #on enregistre cette modif dans le dico pour pouvoir la retrouver quand on fera retour sur la page validation 

    def changer_compo(self,event):
        """Fonction permettant l'affichage de la liste de composant voulue dans la scrollbar 
        cette liste de composant va s'afficher comme une une liste de labels, qu'on placera avec .grid(), 
        afin de pouvoir capter les evenement fais dessus avec .bind() """
      
        self.Can2.yview_scroll(-1000, "units") #pour qu'à chaque changement d'affichage la scrollabr se retrouve en haut
        self.search_bar.delete(0,END) #supprime ce qu'il y a écrit dans la searchbar
        if type(event)==str:
            for dico in self.dico_composant:
                if self.dico_composant[dico]["label"].cget("text") == event:
                    self.repertoire = dico #on récupère le dictionnaire du composant dont on veut afficher la liste
        else:
            for dico in self.dico_composant:
                if self.dico_composant[dico]["label"] == event.widget or self.dico_composant[dico]["label2"] == event.widget :
                    self.repertoire = dico #on récupère le dictionnaire du composant dont on veut afficher la liste
        x=0
        self.dico_label = {} #initialisation du dict qui va stocker tout les labels créés plus bas 
        for widget in self.frame2.winfo_children(): #detruit les widget deja present sur la frame 
            widget.destroy()
        for elt in self.dico_composant[self.repertoire]["liste"]:               
            label = Label(self.frame2,text=self.dico_composant[self.repertoire]["liste"][elt]["nom"],bg='#19232d',fg='cyan',cursor='hand2')#| création du label associé au nom du composant de la liste 
            self.dico_label[label] = self.dico_composant[self.repertoire]["liste"][elt]["nom"] #                                            | enregistrement du label dans le dict
            label.grid(row=x,column=0,sticky="ew") #on place le label 
            label.bind("<Button-1>", lambda i : self.changement_modif_pc(i,self.dico_label,self.dico_composant[self.repertoire])) #|
            label.bind("<Enter>", self.survol_on_3)                                                                               #| on bind les evenement tels que le survol de la souris et le clic 
            label.bind("<Leave>", self.survol_off_3)                                                                              #|
            x+=1 #on augmente de 1 pour placer le prochain labels une case plus bas dans le grid 
        
        Label(self.frame2,text="",bg='#19232d',width=42).grid(row=x+1,column=0,sticky="ew") #on créer un label qui prend la taille de la frame en largeur pour que tout les élément du grid soit ajustés par rapport à lui(grace au sticky="ew")
        self.titre = Label(self.root, text=self.dico_composant[self.repertoire]["titre2"], font=("Raleway",20), anchor="center", bg='#2f3136', fg='#6699ff' )# on affiche le bon titre au dessus de la searchbar 
        self.titre.place(x=490, y=45, height=40, width=300)      
        
    def rechercher(self,event):
        """Fonction permettant l'affichage de la liste de composant voulue dans la scrollbar suite à une recherche avec la searchbar
        cette liste de composant va s'afficher comme une une liste de labels, qu'on placera avec .grid(), 
        afin de pouvoir capter les evenement fais dessus avec .bind() """
        
        self.Can2.yview_scroll(-1000, "units") #pour qu'à chaque changement d'affichage la scrollabr se retrouve en haut
        
        if self.repertoire!={}: #on verifie qu'un composant a bien été choisis (programation défensive)      
            x=0
            self.dico_label = {}
            for widget in self.frame2.winfo_children(): #detruit les widget deja present sur la frame 
                widget.destroy()
                
            entry = self.search_bar.get().lower() # on récupere l'entry de la search bar 
            entrySplit = entry.split() # on utilise .split() pour créer une liste les différent mot du entry            
                
            for elt in self.dico_composant[self.repertoire]["liste"]:
                cpt = 0
                for mot in entrySplit:
                    if self.dico_composant[self.repertoire]["liste"][elt]["nom"].lower().find(mot.lower()) != -1:
                        cpt+=1
                if cpt==len(entrySplit):
                    label = Label(self.frame2,text=self.dico_composant[self.repertoire]["liste"][elt]["nom"],bg='#19232d',fg='cyan',cursor='hand2')#| création du label associé au nom du composant de la liste 
                    self.dico_label[label] = self.dico_composant[self.repertoire]["liste"][elt]["nom"] #                                            | enregistrement du label dans le dict
                    label.grid(row=x,column=0,sticky="ew") #on place le label 
                    label.bind("<Button-1>", lambda i : self.changement_modif_pc(i,self.dico_label,self.dico_composant[self.repertoire])) #|
                    label.bind("<Enter>", self.survol_on_3)                                                                               #| on bind les evenement tels que le survol de la souris et le clic 
                    label.bind("<Leave>", self.survol_off_3)                                                                              #|
                    x+=1 #on augmente de 1 pour placer le prochain labels une case plus bas dans le grid 
                    
            if self.dico_label == {} :
                Label(self.frame2, text="Aucun résultat", anchor="center", bg='#19232d', fg='cyan').grid(row=0,column=0,sticky="ew") #on affiche 'Aucun résulat si la recherche n'a rien donné
                
            Label(self.frame2,text="", anchor="center",bg='#19232d',width=42).grid(row=x+1,column=0,sticky="ew") #on créer un label qui prend la taille de la frame en largeur pour que tout les élément du grid soit ajustés par rapport à lui(grace au sticky="ew")    
            titre = Label(self.root, text=self.dico_composant[self.repertoire]["titre2"], font=("Raleway",20), anchor="center", bg='#2f3136', fg='#6699ff' )# on affiche le bon titre au dessus de la searchbar 
            titre.place(x=490, y=45, height=40, width=310)  
        else : #si aucun composant n'est choisis
            Label(self.frame2, text="Veuillez sélectionner une catégorie", anchor="center", bg='#19232d', fg='cyan').grid(row=0,column=0,sticky="ew")
            Label(self.frame2,text="", anchor="center",bg='#19232d',width=42).grid(row=1,column=0,sticky="ew") 
            
    def on_mousewheel(self, event):
        """Fonction permettant le fonctionnemnt de la scrollbar avec la molette de la souris  pour les page modifie_pc et new_pc"""
        v = int(-1*(event.delta/120))
        self.Can2.yview_scroll(v, "units")
                
    def scrollbar_configure(self,event):
        """Fonction permettant le fonctionnement se la scrollbar pour les page modifie_pc et new_pc"""
        self.Can2.configure(scrollregion=self.Can2.bbox("all"),width=300,height=310)
    
    def telecharger_recap(self):
        """Fonction de téléchargement du récapitulatif de notre nouveau pc"""
        try :
            #On demande à l'utilisateur d'indiquer ou il veut enregistrer son fichier
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[('All Files', '*.*'),('Python Files', '*.py'),('Text Document', '*.txt')],initialfile="Récapitulatif")
            #On ouvre, écrit les données, et ferme le fichier
            fichier = open(self.filename,'w')
            fichier.write(self.content)
            fichier.close()
        except FileNotFoundError : #Permet de géré les fois ou l'on n'enregistre pas le fichier
            pass    
    
    def info_bench(self):
        """Fonction pour la configuration du texte pour le bouton info"""
        if self.var:
            self.texte_info1.configure(text="La puissance est calculé en fonction d'un\ntest de performance en poussant les composants au\nmaximum sur plusieurs pc (benchmark).")
            self.var  = False
        elif self.var == False:
            self.texte_info1.configure(text=" ")
            self.var  = True

    def verif_int_entry(self,valeur):  
        """Vérifie que la valeur rentrée dans le Entry est bien un chiffre,
        si ce n'est pas le cas rien ne s'écrit dans le Entry"""
        
        if valeur.isdigit() :
            return True
        return False
    
    def recherchePlusProche(self,typ:str,valeur:int or float,comp:str)->list:
        """
        Parameters
        ----------
        typ : str
            Parametre correspondant soit à "Prix" soit à "Puissance", nous permettant de savoir ce que l'on recherche.
        valeur : int or float
            Le prix ou la puissance que l'on recherche.
        comp : str
            Quel composant on recherche (ex: cpu, gpu ...)

        Returns
        -------
        list
            Renvoie une liste contenant ces informations : le prix, le nom, et la puissance.

        """
        
        if typ == "puissance":
            difference = 10000000
            for elt in self.dico_composant[comp]["liste"] :
                if abs(valeur - self.dico_composant[comp]["liste"][elt][typ]) <= difference :
                    difference = abs(valeur - self.dico_composant[comp]["liste"][elt][typ])
                    compo = [self.dico_composant[comp]["liste"][elt]["nom"],self.dico_composant[comp]["liste"][elt]["prix"],self.dico_composant[comp]["liste"][elt]["puissance"]]
            return compo
        else :
            nb_base = valeur
            recherche = 0        
            n_recherche = ""
            p_recherche = 0
            for elt in self.dico_composant[comp]["liste"] :
                if self.dico_composant[comp]["liste"][elt][typ] == nb_base :#Si le prix / puissance que l'on recherche est égal au prix du composant
                    #On retourne le prix / le nom / la puissance
                    return [self.dico_composant[comp]["liste"][elt]["nom"],self.dico_composant[comp]["liste"][elt]["prix"],self.dico_composant[comp]["liste"][elt]["puissance"]]
                elif self.dico_composant[comp]["liste"][elt][typ] >= recherche and self.dico_composant[comp]["liste"][elt][typ] < nb_base:#Sinon on réduit l'intervalle de recherche
                    recherche = self.dico_composant[comp]["liste"][elt]["prix"]
                    n_recherche = self.dico_composant[comp]["liste"][elt]["nom"]
                    p_recherche = self.dico_composant[comp]["liste"][elt]["puissance"]
            if n_recherche=="": #Si l'on trouve rien
                recherche = list(self.dico_composant[comp]["liste"].items())[-1][1]["prix"]
                n_recherche = list(self.dico_composant[comp]["liste"].items())[-1][1]["nom"]
                p_recherche = list(self.dico_composant[comp]["liste"].items())[-1][1]["puissance"]
            return[n_recherche,recherche,p_recherche]
    
    # ======================================================================= #
    # Fonctions d'animation des différents boutons                            #
    # ======================================================================= #
    
    def survol_on(self,event,dico,bouton,nom_du_bouton):
        bouton['image'] = dico[nom_du_bouton][1]
        
    def survol_off(self,event,dico,bouton,nom_du_bouton): 
        bouton['image']  = dico[nom_du_bouton][0]
        
    def survol_on_2(self,event):
        for dico in self.dico_composant.values():
            if dico["label"] == event.widget or dico["label2"] == event.widget :
                dico["label"]['bg'],dico["label2"]['bg'] = '#505461','#505461'
    
    def survol_off_2(self,event):
        for dico in self.dico_composant.values():
            if dico["label"] == event.widget or dico["label2"] == event.widget :
                dico["label"]['bg'],dico["label2"]['bg'] = '#2f3136','#2f3136'
    
    def survol_on_3(self,event):
        event.widget['bg'],event.widget['bg'] = '#505461','#505461'
        
    def survol_off_3(self,event):
        event.widget['bg'],event.widget['bg'] = '#19232d','#19232d'

   # ======================================================================== #
    
    def fermeture(self):
        """Fonction qui gere la fermeture de la ou des fenetres"""
        if self.botOnline == True: # Si l'assistant est lancé, on ferme les deux
            self.rootAssistant.destroy()
            self.root.destroy()
        else:
            self.root.destroy()   

        
class InterfaceBot(Frame):
    
    def __init__(self,master,app):
        """Creation de l'interface de l'Assistant"""

        self.chat = Bot(app) #On crée une instance de
        self.app = app
        Frame.__init__(self,master)
        
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW",self.closing)
        
        
        self.bg = "#19232d"
        self.bg2 = "#2F3136"
        self.fg = "#000000"
        self.font = "Verdana 10"
            
        #Frame contenant le texte et la scrollbar
        self.frameFirst = Frame(self.master, bd=6)
        self.frameFirst.pack(expand=True, fill=BOTH)
        self.frameFirst.configure(bg=self.bg)
        
        #Scrollbar     
        self.scrollbar = Scrollbar(self.frameFirst, bd=0)
        self.scrollbar.pack(fill=Y, side=RIGHT)
        #Fenetre pour l'affichage du texte
        self.text = Text(self.frameFirst, yscrollcommand=self.scrollbar.set, state=DISABLED,
                         bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=self.bg2, font=self.font, relief=GROOVE,
                                 width=10, height=1)
        self.text.pack(expand=True, fill=BOTH)
        self.scrollbar.config(command=self.text.yview)

        #Frame contenant le champ d'entrée
        self.frameSecond = Frame(self.master, bd=1)
        self.frameSecond.pack(side=LEFT, fill=BOTH, expand=True)
        self.frameSecond.configure(bg=self.bg)
        #Champ d'entrée
        self.fieldEntry = Entry(self.frameSecond,bg=self.bg2, bd=1, justify=LEFT,fg="#6699ff")
        self.fieldEntry.pack(fill=X, padx=6, pady=6, ipady=3)
    
        #Frame contenant le bouton Envoyer
        self.frameThird = Frame(self.master, bd=0)
        self.frameThird.pack(fill=BOTH)

        #Bouton envoyer
        self.sendButton = Button(self.frameThird, text="Envoyer", width=7, relief=GROOVE, bg=self.bg2, fg="#6699ff",
                                      bd=1, command=lambda: self.messageSend(None), activebackground=self.bg,
                                      activeforeground="#000000")
        self.sendButton.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>",self.messageSend)
            
    def closing(self):
        """Fonction qui gère la fermeture de la fenêtre de l'assistant"""
        self.app.botOnline = False
        self.master.destroy()
            
    def messageSend(self,message:str):
        """
        Fonction qui gere l'insertion des messages de l'utilisateur et du bot
        """
        userEntry = self.fieldEntry.get() #On recupere la demande du Bot
        userMessage = "Vous : " + userEntry + "\n"
        #On insere le texte dans la fenetre
        self.text.configure(state=NORMAL,)
        self.text.insert(END,userMessage)
        self.text.configure(state=DISABLED)
        self.text.see(END)
        
        botAnswer = self.chat.responce(userEntry) #On traite la demande + récupération de la réponse du Bot
        botMessage = "Jeff Assistant : " + botAnswer + "\n"
        #On insere le texte dans la fenetre
        self.text.configure(state=NORMAL,fg="#6699ff")
        self.text.insert(END,botMessage)
        self.text.configure(state=DISABLED)
        self.text.see(END) 
        
        self.fieldEntry.delete(0,END)

class Bot:
    def __init__(self,app):
        """Creation d'un Assistant Robot"""
        # Récupération de l'instance de l'application PBS sur laquelle l'assistant sera utilisé
        self.app = app 
        #Récupération de fichier JSON contenant une base de données de questions
        self.data_file = open('BDD.json',encoding='utf-8').read() 
        self.json = json.loads(self.data_file)
        #liste de caractères/mots que l'on remplace/supprime afin de traiter les questions de l'utilisateur correctement
        ignoreNothing = ['?', '!','.']
        ignoreSpace = ["-","_","(",")"]
        ignoreE = ["é","è","ê","ë"]
        ignoreA = ["à","â","ä"]
        ignoreO = ["ô","ö","ò"]
        ignoreU = ["ü","û","ù"]
        ignoreI = ["ï","î","ì"]
        ignoreC = ["ç"]
        ignoreY = ["ÿ"]
        self.ignore_car = {"":ignoreNothing," ":ignoreSpace,"e":ignoreE,"a":ignoreA,
                           "i":ignoreI,"c":ignoreC,"o":ignoreO,"u":ignoreU,"y":ignoreY}
        
        #Creation du dictionnaire contenant les questions et reponses du JSON
        self.BDD = {}
        for data in self.json['QR']:
            questions = data["questions"]     
            questions = [w.lower() for w in questions]  #On transforme les questions en minuscule afin d'eviter tout probleme de correspondance
            #Traitement des caractères indésirables
            for quest in questions:
                index = questions.index(quest)
                for key in self.ignore_car:
                    for elt in self.ignore_car[key]:
                        if elt in quest:
                            quest = quest.replace(elt,key)
                #On supprime les potentielles espaces en fin de lignes
                if len(quest)>0:
                    while quest[-1]==" ":
                        quest = quest[:-1]
                questions.insert(index,quest)
                del questions[index+1] #On supprime le doublon
            self.BDD[data["tag"]]={"questions":questions,"answers":data["answers"]}#On ajoute un dictionnaire dans un autre, avec pour clé le "tag" faisant références aux questions et réponses dans le JSON
        #Dictionnaire qui nous permet de redirigier l'utilisateur vers la bonne page grâce a l'Assistant
        self.dictKey = {("cpuNouveauPc","cpuModifPc"):"Ton processeur :",("osNouveauPc","osModifPc"):"Ton système d'exploitation :",
                        ("gpuNouveauPc","gpuModifPc"):"Ta carte graphique :",("mbNouveauPc","mbModifPc"):"Ta carte mere :",
                        ("ramNouveauPc","ramModifPc"):"Tes RAMs :",("ssdNouveauPc","ssdModifPc"):"Tes disques durs SSD :",("hddNouveauPc","hddModifPc"):"Tes disques durs HDD :"}
        

    def responce(self,question:str)->str:
        """
        Parameters
        ----------
        question : str
            Paramètre correspondant a l'entrée de l'utilisateur.

        Returns
        -------
        Renvoie la réponse adéquate à la question posé.
        """
        
        #Traitement de la question
        question = question.lower() #Passe tout les caracteres en minuscule
        for key in self.ignore_car:
            for elt in self.ignore_car[key]:
                if elt in question:
                    question = question.replace(elt,key)
        #Supprime tout les espaces
        if len(question)>0:
            while question[-1]==" ":
                question = question[:-1]
                
        
        #Cherche la question dans le dictionnaire afin de renvoyer la bonne réponse et de faire les actions nécessaires
        for key in self.BDD:
            if question in self.BDD[key]["questions"]:
                for elt in list(self.dictKey.keys()):
                    if elt[0]==key:
                        self.app.new_pc()
                        self.app.changer_compo(self.dictKey[elt])
                        return self.BDD[key]['answers']
                    elif elt[1]==key:
                        self.app.modifie_pc()
                        self.app.changer_compo(self.dictKey[elt])
                        return self.BDD[key]['answers']
                if key == "ModifierPc":
                    self.app.modifie_pc()
                    return self.BDD["ModifierPc"]['answers']
                elif key == "NouveauPc":
                    self.app.new_pc()
                    return self.BDD[key]['answers']
                elif key == 'AutoPc':
                    self.app.auto_pc()
                    return self.BDD[key]['answers']
                elif key in self.app.info.keys():
                    return self.BDD[key]['answers']+ str(self.app.info[key]) 
                else:
                    if type(self.BDD[key]['answers'])==list and len(self.BDD[key]["answers"])>1:
                        return(choice(self.BDD[key]['answers']))   
                    else:
                        return(self.BDD[key]['answers'])
        return self.BDD["noanswer"]['answers']