from flask import Flask, render_template, request
import random
import string
import re

app = Flask(__name__)

def text_to_numbers(text):
    return [ord(char.upper()) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])

def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def encrypt(plaintext, key):
    plain_nums = text_to_numbers(plaintext)
    key_nums = text_to_numbers(key)
    cipher_nums = [(p + k) % 26 for p, k in zip(plain_nums, key_nums)]
    return numbers_to_text(cipher_nums)

def decrypt(ciphertext, key):
    cipher_nums = text_to_numbers(ciphertext)
    key_nums = text_to_numbers(key)
    plain_nums = [(c - k + 26) % 26 for c, k in zip(cipher_nums, key_nums)]
    return numbers_to_text(plain_nums)

def is_valid_input(text):
    return re.fullmatch(r'[A-Z]+', text) is not None

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    error = ""
    if request.method == "POST":
        action = request.form["action"]
        
        if action == "encrypt":
            text = request.form["text"].upper().replace(" ", "")
            if not is_valid_input(text):
                error = "Plaintext hanya boleh berisi huruf A-Z tanpa spasi."
            else:
                key = generate_key(len(text))
                ciphertext = encrypt(text, key)
                result = {"text": text, "key": key, "cipher": ciphertext}
        elif action == "decrypt":
            cipher = request.form["cipher"].upper().replace(" ", "")
            key = request.form["key"].upper().replace(" ", "")
            if not is_valid_input(cipher) or not is_valid_input(key):
                error = "Ciphertext dan Key hanya boleh berisi huruf A-Z tanpa spasi."
            else:
                plaintext = decrypt(cipher, key)
                result = {"cipher": cipher, "key": key, "text": plaintext}
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)