import tkinter as tk
from tkinter import filedialog

def vyrobit_okno():
    hlavni_okno = tk.Tk()
    hlavni_okno.title("Aplikace pro výběr souboru")
    hlavni_okno.geometry("600x200") # Nastavíme velikost okna

    # 2. Vytvoříme popisek s instrukcemi
    instrukce = tk.Label(hlavni_okno, text="Klikněte na tlačítko pro výběr PNG souboru:")
    instrukce.pack(pady=10) # 'pack' umístí widget do okna

    # 3. Vytvoříme tlačítko
    #    Klíčový je parametr 'command=vyber_soubor'
    #    Předáváme jméno funkce (bez závorek!), která se má spustit po kliknutí.
    tlacitko = tk.Button(
        hlavni_okno,
        text="Vybrat soubor...",
        command=lambda: vyber_soubor(label_s_cestou),  # Toto je ta magie
    )
    tlacitko.pack(pady=10)

    # 4. Vytvoříme popisek (Label), kam vypíšeme výsledek
    label_s_cestou = tk.Label(hlavni_okno, text="Zatím nic nevybráno...")
    label_s_cestou.pack(pady=20)

    # 5. Spustíme hlavní smyčku aplikace
    #    Program zde čeká na akce uživatele (např. kliknutí na tlačítko)
    print("Spouštím GUI, čekám na akci...")
    hlavni_okno.mainloop()

def vyber_soubor(label_s_cestou: tk.Label):
    """
    Tato funkce je volána tlačítkem.
    Už NEVYTVÁŘÍ vlastní 'root' okno.
    """
    print("Otevírám dialog pro výběr souboru...")
    
    file_path = filedialog.askopenfilename(
        title="Vyberte PNG obrázek",
        filetypes=[
            ("PNG files", "*.png"),
            ("All files", "*.*")
        ]
    )
    
    if file_path:
        # Pokud byl soubor vybrán, aktualizujeme text v popisku (labelu)
        print(f"Vybrán soubor: {file_path}")
        label_s_cestou.config(text=f"Vybráno: {file_path}")
        print("Uzavírám GUI...")
        return file_path
        
        # TADY MŮŽETE ZAVOLAT DALŠÍ FUNKCI PRO ZPRACOVÁNÍ
        # např. zpracuj_obrazek(file_path)
        
    else:
        # Pokud uživatel klikl na 'Zrušit'
        print("Výběr zrušen.")
        label_s_cestou.config(text="Nebyl vybrán žádný soubor.")

# --- Tvorba hlavního GUI ---

# 1. Vytvoříme hlavní (a jediné) okno aplikace


# Kód zde bude pokračovat až po zavření okna

vyrobit_okno()