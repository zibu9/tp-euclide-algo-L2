#KABUYA NSUNGULA JUNIOR
#L2 Génie Informatique
#TP de Transmission de données et la Sécurité Informatique

def euclide_algo(a, b):
    r1 = a
    r2 = b

    while r2 != 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r

    return r1

print("KABUYA NSUNGULA Junior \t L2 Génie Informatique \nTP de Transmission de données et la Sécurité Informatique\n")

a = int(input("Entrez la valeur de a : "))
b = int(input("Entrez la valeur de b : "))
pgcd = euclide_algo(a, b)
print(f"PGCD de {a} et {b} est : {pgcd}")

input("Appuyez une touche pour quitter...")
