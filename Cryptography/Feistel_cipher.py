def bin_to_int(b):
    return int(b, 2)

def int_to_bin(i, length):
    return format(i, f'0{length}b')

def feistel_round(L, R, K, length):
    K_int = bin_to_int(K)
    R_int = bin_to_int(R)
    L_int = bin_to_int(L)
    Fxn = bin_to_int(int_to_bin(R_int ^ K_int, length))
    nL = R
    nR = int_to_bin(L_int ^ Fxn, length)
    return nL, nR

def feistel_encrypt(L0, R0, keys):
    length = max(len(L0), len(R0))
    L, R = L0, R0
    for K in keys:
        L, R = feistel_round(L, R, K, length)
    return L, R

def feistel_decrypt(L, R, keys):
    length = max(len(L), len(R))
    for K in reversed(keys):
        L, R = feistel_round(L, R, K, length)
    return L, R

L0 = '0110101101011101'
R0 = '10110001111010101'
keys = [
    '0111010010101001',
    '1100100011010100',
    # Add more round keys as needed
]

cipher_L, cipher_R = feistel_encrypt(L0, R0, keys)
plain_L, plain_R = feistel_decrypt(cipher_L, cipher_R, keys)
print(f"Ciphertext: L={cipher_L}, R={cipher_R}")
print(f"Plaintext: L={plain_L}, R={plain_R}")
