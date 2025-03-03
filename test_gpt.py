import os
import subprocess
import csv
import time

def spust_analyzu(subor, nastroj):
    """Spustí nástroj statickej analýzy na daný súbor a vráti výsledky."""
    start_time = time.time()
    try:
        vystup = subprocess.check_output([nastroj, subor], stderr=subprocess.STDOUT, text=True)
        pocet_chyb = len(vystup.splitlines())
    except subprocess.CalledProcessError as e:
        vystup = e.output
        pocet_chyb = len(vystup.splitlines())
    except FileNotFoundError:
        return None, 0, "Nástroj nenájdený"
    end_time = time.time()
    cas_vykonania = end_time - start_time
    return vystup, pocet_chyb, cas_vykonania

def analyzuj_subory(priecinok, vystupny_subor):
    """Analyzuje všetky Python súbory v priečinku a zapisuje výsledky do CSV."""
    with open(vystupny_subor, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Subor', 'Nastroj', 'Cas_vykonania (s)', 'Pocet_chyb', 'Vystup'])

        for subor in os.listdir(priecinok):
            if subor.endswith(".py"):
                subor_cesta = os.path.join(priecinok, subor)
                print(f"Analyzujem súbor: {subor}")

                for nastroj in ['pylint', 'pyflakes', 'flake8', 'mypy']:
                    vystup, pocet_chyb, cas_vykonania = spust_analyzu(subor_cesta, nastroj)
                    
                    # Ak nástroj nebol nájdený, pridá chybové hlásenie
                    if vystup is None:
                        vystup = f"{nastroj} nebol nájdený alebo nie je nainštalovaný."

                    writer.writerow([subor, nastroj, round(cas_vykonania, 2), pocet_chyb, vystup])

                    # Výstup pre lepšiu viditeľnosť v konzole
                    print(f"{nastroj}: {pocet_chyb} chýb, čas: {round(cas_vykonania, 2)}s")
                    print("-" * 80)

# Analýza priečinkov 'gpt' a 'gpt_true'
analyzuj_subory('gpt', 'vysledky_analyzy_gpt.csv')
analyzuj_subory('gpt_true', 'vysledky_analyzy_gpt_true.csv')
