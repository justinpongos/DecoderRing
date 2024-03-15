import abc

class Cipher(abc.ABC):
  """ Abstract class that defines the interface for any cipher subclass

  Attributes:
    _alphabet (str): string of the alphabet
  """

  def __init__(self):
    """Initiates the alphabet attribute"""
    self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  @property
  def alphabet(self):
    """Getter of attribute _alphabet

    Returns:
        String: alphabet uppercase
    """
    return self._alphabet

  def encrypt_message(self, message):
    """Build the encryption string using the encrypted letters and ignored characters, and return it.

    Args:
        message (String): message to encrypt

    Returns:
        String: Encrypted message
    """
    encrypted_message = ""
    for letter in message.upper():
      if letter in self._alphabet:
        encrypted_message += self._encrypt_letter(letter)
      else:
        encrypted_message += letter
    return encrypted_message

  def decrypt_message(self, message):
    """Build the encryption string using the decrypted letters and ignored characters, and then return it.

    Args:
        message (String): message to decrypt

    Returns:
        String: Decrypted message
    """
    decrypted_message = ""
    for letter in  message.upper():
      if letter in self._alphabet:
        decrypted_message += self._decrypt_letter(letter)
      else:
        decrypted_message += letter
    return decrypted_message
    
  @abc.abstractmethod
  def _encrypt_letter(self, letter):
    """Abstract method to encrypt one letter

    Args:
        letter (Char): One character in the alphabet
    """
    pass
    
  @abc.abstractmethod
  def  _decrypt_letter(self, letter):
    """Abstract method to decrypt one letter

    Args:
        letter (Char): One character in the alphabet
    """
    pass
