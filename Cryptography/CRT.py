def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def CRT(congruences):
    N = 1
    for _, ni in congruences:
        N *= ni

    x = 0
    for ri, ni in congruences:
        Ni = N // ni
        Mi = modular_multiplicative_inverse(Ni, ni)
        x += ri * Ni * Mi

    return x % N

def get_congruencies():
    congruences=[]
    num_congruences= int(input("Enter the number of congruencies"))

    for i in range(num_congruences):
        ri = int(input(f"Enter the Remainder r{i+1}"))
        mi = int(input(f"Enter the modulus m{i+1}"))
        congruences.append((ri,mi))

    return congruences

congruences = get_congruencies()
solution = CRT(congruences)
print("The solution to the system of congruences is:", solution)
