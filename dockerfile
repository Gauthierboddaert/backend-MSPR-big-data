FROM python:3.9

# Installer les dépendances
RUN pip install requests beautifulsoup4 python-dotenv pandas openpyxl matplotlib datetime

# Copier le fichier main.py dans le conteneur
COPY main.py /app/main.py

# Définir le répertoire de travail
WORKDIR /app

# Commande pour lancer le processus en arrière-plan et rediriger la sortie vers un fichier de journal
CMD ["bash", "-c", "python ./main.py > output.log 2>&1 & tail -f /dev/null"]
