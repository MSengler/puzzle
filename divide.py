from PIL import Image
import os
import sys


def divide_image(image_path, output_folder, rows, cols):
    """
    Divise une image en plusieurs parties égales.
    
    :param image_path: Chemin de l'image d'entrée.
    :param output_folder: Dossier où les morceaux découpés seront sauvegardés.
    :param rows: Nombre de rangées.
    :param cols: Nombre de colonnes.
    """
    try:
        # Charger l'image
        img = Image.open(image_path)
        img_width, img_height = img.size
        
        # Calculer la taille de chaque morceau
        piece_width = img_width // cols
        piece_height = img_height // rows
        
        # Créer le dossier de sortie s'il n'existe pas
        os.makedirs(output_folder, exist_ok=True)
        
        # Découper l'image
        for row in range(rows):
            for col in range(cols):
                left = col * piece_width
                upper = row * piece_height
                right = left + piece_width
                lower = upper + piece_height
                
                # Extraire la partie de l'image
                piece = img.crop((left, upper, right, lower))
                
                # Sauvegarder chaque morceau
                piece_name = f"piece_{row}_{col}.png"
                piece_path = os.path.join(output_folder, piece_name)
                piece.save(piece_path)
                print(f"Enregistré : {piece_path}")
        
        print(f"Toutes les pièces ont été sauvegardées dans {output_folder}")
    
    except Exception as e:
        print(f"Erreur : {e}")


"""
if __name__ == '__main__':
    divide_image(image_path, "static/images", 2, 4)
"""