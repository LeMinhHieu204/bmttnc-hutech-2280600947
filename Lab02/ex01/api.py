from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher  # Nhập khẩu lớp CaesarCipher
from cipher.vigenere import VigenereCipher  # Nhập khẩu lớp VigenereCipher
app = Flask(__name__)

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json  # Nhận dữ liệu JSON từ yêu cầu
    plain_text = data['plain_text']  # Lấy văn bản gốc
    key = data['key']  # Lấy khóa
    
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)  # Mã hóa văn bản
    return jsonify({'encrypted_text': encrypted_text})  # Trả về phản hồi JSON

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json  # Nhận dữ liệu JSON từ yêu cầu
    cipher_text = data['cipher_text']  # Lấy văn bản đã mã hóa
    key = data['key']  # Lấy khóa
    
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)  # Giải mã văn bản
    return jsonify({'decrypted_text': decrypted_text})  # Trả về phản hồi JSON
# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)