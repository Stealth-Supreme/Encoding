import string
import random

secret_code = {'a': 'UAI', 'b': 'rBr', 'c': 'lzG', 'd': 'haV', 'e': 'vRo', 'f': 'qnN', 'g': 'kzv', 'h': 'wwL', 'i': 'mml', 'j': 'MZV', 'k': 'lUp', 'l': 'qaa', 'm': 'Qap', 'n': 'NUs', 'o': 'aMs', 'p': 'bOs', 'q': 'Ube', 'r': 'nRQ', 's': 'gHB', 't': 'Ahg', 'u': 'CPx', 'v': 'kUp', 'w': 'oEZ', 'x': 'QIF', 'y': 'QlJ', 'z': 'jUw', 'A': 'ARq', 'B': 'ava', 'C': 'Vyx', 'D': 'wIq', 'E': 'jMZ', 'F': 'vNG', 'G': 'frF', 'H': 'VZj', 'I': 'umA', 'J': 'BvY', 'K': 'GYw', 'L': 'KAk', 'M': 'fbF', 'N': 'Kvx', 'O': 'UBN', 'P': 'tBr', 'Q': 'hsh', 'R': 'XIe', 'S': 'ttK', 'T': 'gxf', 'U': 'RyR', 'V': 'Vua', 'W': 'jWl', 'X': 'Wzu', 'Y': 'tMB', 'Z': 'qFm'}
#Message me if you want to get another dictionary. Here is another sample dictionary:
sample_secret_code = {'a': 'CHq', 'b': 'DJp', 'c': 'vGJ', 'd': 'bFb', 'e': 'vtX', 'f': 'tGM', 'g': 'hnT', 'h': 'YAZ', 'i': 'vcX', 'j': 'emE', 'k': 'phn', 'l': 'tfV', 'm': 'oIy', 'n': 'iKT', 'o': 'GhD', 'p': 'UNj', 'q': 'YUO', 'r': 'lcf', 's': 'ZEN', 't': 'DCr', 'u': 'cnv', 'v': 'HYW', 'w': 'ybk', 'x': 'QNI', 'y': 'IfG', 'z': 'cUB', 'A': 'bhZ', 'B': 'GnK', 'C': 'sbJ', 'D': 'uWF', 'E': 'vqQ', 'F': 'xmL', 'G': 'ztT', 'H': 'vVl', 'I': 'fyn', 'J': 'lCg', 'K': 'dWX', 'L': 'kcV', 'M': 'yYJ', 'N': 'kWu', 'O': 'Gmv', 'P': 'csT', 'Q': 'ufI', 'R': 'QMR', 'S': 'Dvf', 'T': 'njA', 'U': 'rbm', 'V': 'BQx', 'W': 'cdw', 'X': 'zOh', 'Y': 'HeE', 'Z': 'OpK'}
#If you want to use this dictionary, change the variable names.
letters = string.ascii_letters
special_characters = string.punctuation

def coding(message):#use this function for coding
    code = []
    for i, let in enumerate(message):
        if let in secret_code:
            code.append(secret_code.get(let))   
        else:
            code.append(let)

    code = "".join(code)
    print(code)

def finding_keys(value):
    for key, target_value in secret_code.items():
        if target_value == value:
            found_key = key
            return found_key

def decoding(code):
    s = 0
    temp = []
    decoded = []
    for j,let in enumerate(code):
        if let in letters:
            temp.append(let)
            s += 1
            if s%3 == 0:
                decoded.append(''.join(temp))
                temp = []
        else:
            decoded.append(let)
    for i,value in enumerate(decoded):
        if value in special_characters:
            decoded[i] = str(value)
        elif value == " ":
            decoded[i] = " "
        else:
            decoded[i] = finding_keys(value)
    final_message = "".join(decoded)
    print(final_message)

#Leave a comment to rate my work
