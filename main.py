from customtkinter import *
import random
import string
from tkinter import messagebox

# Création de la fenêtre
app = CTk()
app.geometry("700x600")
app.title("generateur de mot de passe")
set_appearance_mode("light")

mot_de_passe = ""

# Fonctions
def copier_mot_de_passe():
    if mot_de_passe:
        app.clipboard_clear()
        app.clipboard_append(mot_de_passe)
        app.update()

def toggle_dark_mode():
    current_mode = get_appearance_mode()
    if current_mode == "Light":
        set_appearance_mode("dark")
        label.configure(text_color="#138d75")
        entry_min.configure(text_color="#76448a")
        entry_maj.configure(text_color="#76448a")
        entry_chiffres.configure(text_color="#76448a")
        entry_speciaux.configure(text_color="#76448a")
        label_resultat.configure(text_color="#76448a")
        btn.configure(fg_color="#76448a", hover_color="#a569bd", text_color="#fdfefe")
        btn_copier.configure(fg_color="#76448a", hover_color="#a569bd", text_color="#fdfefe")
        btn_darkmode.configure(fg_color="#76448a", hover_color="#a569bd", text_color="#fdfefe")
    else:
        set_appearance_mode("light")
        label.configure(text_color="#d2b4de")
        entry_min.configure(text_color="#d2b4de")
        entry_maj.configure(text_color="#d2b4de")
        entry_chiffres.configure(text_color="#d2b4de")
        entry_speciaux.configure(text_color="#d2b4de")
        label_resultat.configure(text_color="#d2b4de")
        btn.configure(fg_color="#a9cce3", hover_color="#7fb3d5", text_color="#2e86c1")
        btn_copier.configure(fg_color="#a9cce3", hover_color="#7fb3d5", text_color="#2e86c1")
        btn_darkmode.configure(fg_color="#a9cce3", hover_color="#7fb3d5", text_color="#2e86c1")

def generer_mot_de_passe():
    global mot_de_passe
    try:
        a_val = int(entry_min.get())
        b_val = int(entry_maj.get())
        c_val = int(entry_chiffres.get())
        d_val = int(entry_speciaux.get())
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer uniquement des nombres.")
        return

    lettres_min = random.choices(string.ascii_lowercase, k=a_val)
    lettres_maj = random.choices(string.ascii_uppercase, k=b_val)
    chiffres = random.choices(string.digits, k=c_val)
    speciaux = random.choices(string.punctuation, k=d_val)
    liste_finale = lettres_min + lettres_maj + chiffres + speciaux
    random.shuffle(liste_finale)
    mot_de_passe = ''.join(liste_finale)
    label_resultat.configure(text="Mot de passe : " + mot_de_passe)

# Interface initiale
label = CTkLabel(master=app, text="Générateur de mot de passe", font=("Arial", 20, "bold"), text_color="#d2b4de")
label.place(relx=0.5, rely=0.1, anchor="center")

CTkLabel(master=app, text="Lettres Minuscules :", font=("Arial", 20), text_color="#d2b4de").place(relx=0.5, rely=0.3, anchor="e")
entry_min = CTkEntry(master=app, placeholder_text="...", width=50, text_color="#d2b4de")
entry_min.place(relx=0.7, rely=0.3, anchor="e")

CTkLabel(master=app, text="Lettres Majuscules :", font=("Arial", 20), text_color="#d2b4de").place(relx=0.5, rely=0.4, anchor="e")
entry_maj = CTkEntry(master=app, placeholder_text="...", width=50, text_color="#d2b4de")
entry_maj.place(relx=0.7, rely=0.4, anchor="e")

CTkLabel(master=app, text="Chiffres :", font=("Arial", 20), text_color="#d2b4de").place(relx=0.5, rely=0.5, anchor="e")
entry_chiffres = CTkEntry(master=app, placeholder_text="...", width=50, text_color="#d2b4de")
entry_chiffres.place(relx=0.7, rely=0.5, anchor="e")

CTkLabel(master=app, text="Caractères Spéciaux :", font=("Arial", 20), text_color="#d2b4de").place(relx=0.5, rely=0.6, anchor="e")
entry_speciaux = CTkEntry(master=app, placeholder_text="...", width=50, text_color="#d2b4de")
entry_speciaux.place(relx=0.7, rely=0.6, anchor="e")

btn = CTkButton(master=app, text="Générer votre mot de passe", corner_radius=32, fg_color="#a9cce3", hover_color="#7fb3d5", command=generer_mot_de_passe, text_color="#2e86c1")
btn.place(relx=0.5, rely=0.8, anchor="center")

label_resultat = CTkLabel(master=app, text="Mot de passe :", font=("Courier", 12), text_color="#d2b4de")
label_resultat.place(relx=0.5, rely=0.9, anchor="center")

btn_copier = CTkButton(master=app, text="Copier", command=copier_mot_de_passe, fg_color="#a9cce3", text_color="#2e86c1", hover_color="#7fb3d5", corner_radius=32)
btn_copier.place(relx=0.8, rely=0.9, anchor="w")

btn_darkmode = CTkButton(master=app, text="Dark Mode", corner_radius=32, fg_color="#a9cce3", hover_color="#7fb3d5", command=toggle_dark_mode, text_color="#2e86c1")
btn_darkmode.place(relx=0.2, rely=0.1, anchor="e")

app.mainloop()