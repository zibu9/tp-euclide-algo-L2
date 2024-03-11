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
a = 48
b = 18
gcd = euclide_algo(a, b)
print("KABUYA NSUNGULA Junior \t L2 Génie Informatique \n TP de Transmission de données et la Sécurité Informatique")
print(f"PGCD de {a} et {b} est : {gcd}")
