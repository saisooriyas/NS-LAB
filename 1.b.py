def playfair_cipher(plaintext, key):
    key = key.replace(" ", "").lower()
    plaintext = plaintext.replace(" ", "").lower()
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    matrix = [[alphabet[i + j] for i in range(0, 25, 5)] for j in range(5)]
    key_map = {}
    for i, c in enumerate(alphabet + key):
        if c not in key_map:
            key_map[c] = i % 5, i // 5

    def encrypt(text):
        result = ""
        for i in range(0, len(text), 2):
            x1, y1 = key_map[text[i]]
            x2, y2 = key_map[text[i + 1]]
            if x1 == x2:
                result += matrix[x1][(y1 + 1) % 5] + matrix[x2][(y2 + 1) % 5]
            elif y1 == y2:
                result += matrix[(x1 + 1) % 5][y1] + matrix[(x2 + 1) % 5][y2]
            else:
                result += matrix[x1][y2] + matrix[x2][y1]
        return result

    plaintext = (plaintext + "x" * (len(plaintext) % 2))
    return encrypt(plaintext)
