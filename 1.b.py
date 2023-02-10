def to_lower_case(text):
    return text.lower()

def remove_spaces(text):
    return "".join(i for i in text if i != " ")

def encrypt_playfair_cipher(matrix, plain_text):
    cipher_text = []
    for i in range(0, len(plain_text), 2):
        ele1_x, ele1_y = search_in_matrix(matrix, plain_text[i][0])
        ele2_x, ele2_y = search_in_matrix(matrix, plain_text[i][1])
        if ele1_x == ele2_x:
            c1, c2 = encrypt_row_rule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_column_rule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_rectangle_rule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        cipher_text.append(c1 + c2)
    return "".join(cipher_text)

def search_in_matrix(matrix, element):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element:
                return i, j

def encrypt_row_rule(matrix, ele1_x, ele1_y, ele2_x, ele2_y):
    c1 = matrix[ele1_x][(ele1_y + 1) % 5]
    c2 = matrix[ele2_x][(ele2_y + 1) % 5]
    return c1, c2

def encrypt_column_rule(matrix, ele1_x, ele1_y, ele2_x, ele2_y):
    c1 = matrix[(ele1_x + 1) % 5][ele1_y]
    c2 = matrix[(ele2_x + 1) % 5][ele2_y]
    return c1, c2

def encrypt_rectangle_rule(matrix, ele1_x, ele1_y, ele2_x, ele2_y):
    c1 = matrix[ele1_x][ele2_y]
    c2 = matrix[ele2_x][ele1_y]
    return c1, c2

def generate_key_table(word, alphabet):
    key_letters = set(word)
    key_letters.update(alphabet)
    matrix = [key_letters[i:i + 5] for i in range(0, len(key_letters), 5)]
    return matrix

alphabet = "abcdefghiklmnopqrstuvwxyz"

text = "playfair example"
text = to_lower_case(text)
text = remove_spaces(text)
key = "playfair"
key_table = generate_key_table(key, alphabet
