import os

def save(firmname):
    directory = "C:/Users/User/Documents/berufswahl/Bewerbungsdossier/Bewerbungschreiben/Informatiker"
    os.chdir(directory)
    os.makedirs(firmname, exist_ok=True)  # Use exist_ok=True to avoid errors if the directory already exists
