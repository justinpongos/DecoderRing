#  Name: Louis Pavlovsky & Justin Pongos
#  Date: 03/12/24

#  Desc: This is a secret decoder ring program where you can encrypt or decrypt a message using two different kinds of ciphers, atbash cipher and ceaser cipher. When encrypting using caesar you will be prompted to enter a message and a shift value than it will be stored in the txt file. When decrypting you will be prompted to enter a shift value and it will decrypt the text in the message.txt. On the other hand, when encrypting using atbash you will be prompted to enter a message and it will store it in a txt file switching each letter to the reverse alphabet. When you decrypt it, it will take the txt from the file and decrypt it.
import atbash
import caesar
import check_input

def main():

  print("Secret Decoder Ring:")
  print(f"1. Encrypt\n2. Decrypt")
  decoder = check_input.get_int_range("", 1, 2)

  if decoder == 1:
    print("Enter encryption type:")
  else:
    print("Enter decryption type:")
  print(f"1. Atbash\n2. Caesar")
  encryption = check_input.get_int_range("", 1, 2)

  #  Encryption/Decryption type Atbash
  if encryption == 1:  
    at_bash_tool = atbash.AtbashCipher()
    if decoder == 1:
      message = input("Enter message: " )
      with open("message.txt", "w") as file:
        file.write(at_bash_tool.encrypt_message(message))
        print("Encrypted message saved to \"message.txt\".")
    else:
      with open("message.txt", "r") as file:
        print("Reading encrypted message from “message.txt”.")
        encrypted_message = file.read()
        print(f"Decrypted message: {at_bash_tool.decrypt_message(encrypted_message)}")
        
  #  Encryption/Decryption type Ceasar
  if encryption == 2:  
    if decoder == 1:
      message = input("Enter message: " )
      shift = check_input.get_int_range("Enter shift value: ", 0, 25)
      caesar_tool = caesar.CaesarCipher(shift)
      with open("message.txt", "w") as file:
        file.write(caesar_tool.encrypt_message(message))
        print("Encrypted message saved to \"message.txt\".")
    else:
      shift = check_input.get_int_range("Enter shift value: ", 0, 25)
      caesar_tool = caesar.CaesarCipher(shift)
      with open("message.txt", "r") as file:
        print("Reading encrypted message from “message.txt”.")
        encrypted_message = file.read()
        print(f"Decrypted message: {caesar_tool.decrypt_message(encrypted_message)}")
main()

