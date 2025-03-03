import os
import subprocess
import csv
import time

def spust_analyzu(subor, nastroj):
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
    with open(vystupny_subor, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['subor', 'nastroj', 'cas_vykonania', 'pocet_chyb', 'vystup'])

        for subor in os.listdir(priecinok):
            if subor.endswith(".py"):
                subor_cesta = os.path.join(priecinok, subor)

                # Pylint
                vystup, pocet_chyb, cas_vykonania = spust_analyzu(subor_cesta, 'pylint')
                writer.writerow([subor, 'Pylint', cas_vykonania, pocet_chyb, vystup])

                # Pyflakes
                vystup, pocet_chyb, cas_vykonania = spust_analyzu(subor_cesta, 'pyflakes')
                writer.writerow([subor, 'Pyflakes', cas_vykonania, pocet_chyb, vystup])

                # Flake8
                vystup, pocet_chyb, cas_vykonania = spust_analyzu(subor_cesta, 'flake8')
                writer.writerow([subor, 'Flake8', cas_vykonania, pocet_chyb, vystup])

                # Mypy
                vystup, pocet_chyb, cas_vykonania = spust_analyzu(subor_cesta, 'mypy')
                writer.writerow([subor, 'Mypy', cas_vykonania, pocet_chyb, vystup])

analyzuj_subory('gemini', 'vysledky_analyzy.csv')