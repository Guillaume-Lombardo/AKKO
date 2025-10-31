import subprocess
import os
import sys

# On se place dans le répertoire du script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Lancement de Streamlit sans admin, comme un citoyen opprimé
subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app.py"], shell=True)
