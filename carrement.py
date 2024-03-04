import glob
from PIL import Image, ImageDraw



def dessiner_forme(image: Image, x: int, y: int, taille: int, forme: str, epaisseur: int = 5, thumbnail: bool = True) -> Image:
    draw = ImageDraw.Draw(image)

    x += 5
    y += 5

    half = taille / 2
    if forme == "L":
        fill = "green" if thumbnail else "black"
        draw.line([(x, y), (x, y + half)], fill = fill, width=epaisseur)
        draw.line([(x, y + half), (x + half, y + half)], fill = fill, width=epaisseur)
    elif forme == "R":
        fill = "yellow" if thumbnail else "black"
        draw.line([(x, y), (x, y - half)], fill=fill, width=epaisseur)
        draw.line([(x, y - half), (x + half, y - half)], fill=fill, width=epaisseur)
    elif forme == "J":
        fill = "blue" if thumbnail else "black"
        draw.line([(x, y), (x + half, y)], fill=fill, width=epaisseur)
        draw.line([(x + half, y), (x + half , y - half)], fill=fill, width=epaisseur)
    elif forme == "I":
        fill = "red" if thumbnail else "black"
        draw.line([(x, y), (x + half, y)], fill=fill, width=epaisseur)
        draw.line([(x + half, y), (x + half, y + half)], fill=fill, width=epaisseur)
    return image

def dessiner_perle(image: Image,x: int, y:int, couleur: str):
    draw = ImageDraw.Draw(image)
    forme = [(x, y), (x + 15, y + 15)]
    draw.arc(forme, start = 0, end = 360, fill =couleur)
    return image

def dessiner_rectangle(image: Image, x: int, y: int, xtaille: int, ytaille: int):
    draw = ImageDraw.Draw(image)
    draw.line([(x, y), (x, y + ytaille)], fill="black", width=1)
    draw.line([(x, y + ytaille), (x + xtaille, y + ytaille)], fill="black", width=1)
    draw.line([(x + xtaille, y + ytaille), (x + xtaille, y)], fill="black", width=1)
    draw.line([(x + xtaille, y ), (x , y)], fill="black", width=1)
    return image


# Ouvre le fichier scores.csv
csv_file = open("source/scores.csv", "r")
compteur = 1

nb_perles = 5
L = [nb_perles, nb_perles, nb_perles, nb_perles]
I = [nb_perles, nb_perles, nb_perles, nb_perles]
R = [nb_perles, nb_perles, nb_perles, nb_perles]
J = [nb_perles, nb_perles, nb_perles, nb_perles]


# Lire ligne par ligne
csv_file.seek(0)
for line in csv_file:
    print(f"Traiter carre {compteur}")
    values = line.strip('\n').split(";")
    print(f"Valeurs: {values}")

    forme = values[0]

    image = Image.new("RGB", (700, 450), "white")

    match forme:
        case "R":
            dessiner_forme(image, 0, 50, 100, "R")
            dessiner_forme(image, 250, 300, 200, "R", 10, False)
            # B No op
        case "L":
            dessiner_forme(image, 0, 0, 100, "L")
            dessiner_forme(image, 250, 200, 200, "L", 10, False)
            L[0] = L[0] - 1
        case "J":
            dessiner_forme(image, 0, 50, 100, "J")
            dessiner_forme(image, 250, 300, 200, "J", 10, False)
            J[0] = J[0] - 1
        case "I":
            dessiner_forme(image, 0, 0, 100, "I")
            dessiner_forme(image, 250, 200, 200, "I", 10, False)
            I[0] = I[0] - 1
        case _:
            pass

    forme = values[1]

    match forme:
        case "R":
            dessiner_forme(image, 0, 100, 100, "R")
            dessiner_forme(image, 250, 400, 200, "R", 10, False)
            R[1] = R[1] - 1
        case "L":
            dessiner_forme(image, 0, 50, 100, "L")
            dessiner_forme(image, 250, 300, 200, "L", 10, False)
            # no op L
        case "J":
            dessiner_forme(image, 0, 100, 100, "J")
            dessiner_forme(image, 250, 400, 200, "J", 10, False)
            J[1] = J[1] - 1
        case "I":
            dessiner_forme(image, 0, 50, 100, "I")
            dessiner_forme(image, 250, 300, 200, "I", 10, False)
            I[1] = I[1] - 1
        case _:
            pass

    forme = values[2]

    match forme:
        case "R":
            dessiner_forme(image, 50, 100, 100, "R")
            dessiner_forme(image, 350, 400, 200, "R", 10, False)
            R[2] = R[2] - 1
        case "L":
            dessiner_forme(image, 50, 50, 100, "L")
            dessiner_forme(image, 350, 300, 200, "L", 10, False)
            L[2] = L[2] - 1
        case "J":
            dessiner_forme(image, 50, 100, 100, "J")
            dessiner_forme(image, 350, 400, 200, "J", 10, False)
            # No op for N
        case "I":
            dessiner_forme(image, 50, 50, 100, "I")
            dessiner_forme(image, 350, 300, 200, "I", 10, False)
            I[2] = I[2] - 1
        case _:
            pass

    forme = values[3]

    match forme:
        case "R":
            dessiner_forme(image, 50, 50, 100 , "R")
            dessiner_forme(image, 350, 300, 200, "R", 10, False)
            R[3] = R[3] - 1
        case "L":
            dessiner_forme(image, 50, 0, 100, "L")
            dessiner_forme(image, 350, 200, 200, "L", 10, False)
            L[3] = L[3] - 1
        case "J":
            dessiner_forme(image, 50, 50, 100, "J")
            dessiner_forme(image, 350, 300, 200, "J", 10, False)
            J[3] = J[3] - 1
        case "I":
            dessiner_forme(image, 50, 0, 100, "I")
            dessiner_forme(image, 350, 200, 200, "I", 10, False)
            # VE no op
        case _:
            pass

    # Compléter le numéro avec des zéros pour avoir toujours 3 chiffres
    count_str = str(compteur).zfill(3)

    tmp_folder = "tmp"
    file_path = f"{tmp_folder}/tour_de_jeu_{count_str}.jpg"

    # Ajouter du texte sur l'image
    draw = ImageDraw.Draw(image)
    draw.text((120, 10), f"n° {compteur}", fill="black")

    dessiner_rectangle(image, 190, 5, 80, 105)
    dessiner_rectangle(image, 290, 5, 80, 105)
    dessiner_rectangle(image, 390, 5, 80, 105)
    dessiner_rectangle(image, 490, 5, 80, 105)

    nb_cases = 4
    for i in range(nb_cases):
        print(f"L[{i}] - {L[i]}")
        if L[i] < 0:
            raise Exception("depassement", f"perles L {i}")
        if R[i] < 0:
            raise Exception("depassement", f"perles R {i}")
        if I[i] < 0:
            raise Exception("depassement", f"perles I {i}")
        if J[i] < 0:
            raise Exception("depassement", f"perles J {i}")

    pos_y = 10
    decalage = 20
    for i in range(L[0]):
        dessiner_perle(image, 200, pos_y , "green")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(L[1]):
        dessiner_perle(image, 300, pos_y , "green")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(L[2]):
        dessiner_perle(image, 400, pos_y , "green")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(L[3]):
        dessiner_perle(image, 500, pos_y , "green")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(I[0]):
        dessiner_perle(image, 215, pos_y , "red")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(I[1]):
        dessiner_perle(image, 315, pos_y , "red")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(I[2]):
        dessiner_perle(image, 415, pos_y , "red")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(I[3]):
        dessiner_perle(image, 515, pos_y , "red")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(R[0]):
        dessiner_perle(image, 230, pos_y , "yellow")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(R[1]):
        dessiner_perle(image, 330, pos_y , "yellow")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(R[2]):
        dessiner_perle(image, 430, pos_y , "yellow")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(R[3]):
        dessiner_perle(image, 530, pos_y , "yellow")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(J[0]):
        dessiner_perle(image, 245, pos_y , "blue")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(J[1]):
        dessiner_perle(image, 345, pos_y , "blue")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(J[2]):
        dessiner_perle(image, 445, pos_y , "blue")
        pos_y = pos_y + decalage

    pos_y = 10
    for i in range(J[3]):
        dessiner_perle(image, 545, pos_y , "blue")
        pos_y = pos_y + decalage


    image.save(file_path, "JPEG")

    compteur += 1


def generer_gif(rep_source: str, rep_cible: str):
    image_sorted = [image for image in glob.glob(f"{rep_source}/*.jpg")]
    # Sort the list in alphabetical order
    image_sorted.sort()
    print(image_sorted)

    frames = [Image.open(image) for image in image_sorted]
    frame_one = frames[0]
    frame_one.save(f"{rep_cible}/animation.gif", format="GIF", append_images=frames, save_all=True, duration=600, loop=0)


generer_gif(tmp_folder, "resultat")
