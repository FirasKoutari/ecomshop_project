import os
import shutil

def supprimer_dossiers(racine_projet, noms_dossiers_a_supprimer):
    # Parcourir l'arborescence des répertoires
    for dossier_racine, sous_dossiers, fichiers in os.walk(racine_projet):
        # Parcourir les sous-dossiers
        for sous_dossier in sous_dossiers:
            # Vérifier si le sous-dossier est dans la liste des dossiers à supprimer
            if sous_dossier in noms_dossiers_a_supprimer:
                chemin_complet = os.path.join(dossier_racine, sous_dossier)
                print(f'Suppression du dossier : {chemin_complet}')
                # Supprimer le dossier et son contenu
                shutil.rmtree(chemin_complet)
                
    print('Suppression terminée.')

# Exemple d'utilisation
racine_projet = 'D:\\Django\\Github\\ecomshop_project\\ecom_project\\eshop'  # Chemin de la racine de votre projet Django
noms_dossiers_a_supprimer = ['migrations', '__pycache__']  # Liste des noms de dossiers à supprimer
supprimer_dossiers(racine_projet, noms_dossiers_a_supprimer)
