from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Cipher import AES
import base64
from Crypto.Hash import SHA256

def generate_rsa_pair_key():
  print("Generating....")
  key = RSA.generate(2048)

  private_key = key.exportKey("OpenSSH")
  file_out = open("private_key.txt", "wb")
  file_out.write(private_key)
  file_out.close()

  public_key = key.publickey().exportKey("OpenSSH")
  file_out = open("public_key.txt", "wb")
  file_out.write(public_key)
  file_out.close()
  
def encrypt_message(encrypt_data):

  file_out = open(encrypt_data, "wb")
  recipient_key = RSA.importKey(open("public_key.txt").read())
  
  encryptor = PKCS1_OAEP.new(recipient_key)
  encrypted_msg = encryptor.encrypt(encrypt_data.encode('utf-8'))
  encoded_encrypted_msg = base64.b64encode(encrypted_msg)
  
  file_out.write(encoded_encrypted_msg)
  file_out.close()

def decrypt_message(encrypted_data):
  private_key = RSA.importKey(open("private_key.txt").read())  
  encryptor = PKCS1_OAEP.new(private_key)
  decoded_encrypted_msg = base64.b64decode(encrypted_data)
  decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
  return decoded_decrypted_msg