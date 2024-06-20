import os
import shutil

def supprimer_dossiers_migrations(racine_projet):
    # Parcourir l'arborescence des répertoires
    for dossier_racine, sous_dossiers, fichiers in os.walk(racine_projet):
        # Parcourir les sous-dossiers
        for sous_dossier in sous_dossiers:
            # Vérifier si le sous-dossier s'appelle "migrations"
            if sous_dossier == 'migrations':
                chemin_complet = os.path.join(dossier_racine, sous_dossier)
                print(f'Suppression du dossier : {chemin_complet}')
                # Supprimer le dossier et son contenu
                shutil.rmtree(chemin_complet)
                
    print('Suppression terminée.')

# Exemple d'utilisation
racine_projet = 'D:\\Django\\Github\\ecomshop_project\\ecom_project\\eshop'  # Chemin de la racine de votre projet Django
supprimer_dossiers_migrations(racine_projet)
