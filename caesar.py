from cipher import Cipher

class CaesarCipher(Cipher):
  """ Class that inherit from cipher and use the CaesarCipher method to encryp/decrypt

  Attributes:
    _cipherbet (str): string of the CaesarCipher
    _shift (int): shift value
  """
  def __init__(self, shift):
    """ Call super to initialize the alphabet, then create the cipherbet attribute thanks to the shift attribute

    Args:
      shift (Number): shift value
    """
    super().__init__()
    self._shift = shift
    start_cipherbet = shift % 26
    self._cipherbet = self.alphabet[start_cipherbet:] + self.alphabet[:start_cipherbet]
    
  def _encrypt_letter(self, letter):
    """Find the location of the letter in the alphabet and return the encrypted letter

    Args:
        letter (Char): One character in the alphabet
    """
    location = self.alphabet.find(letter)
    return self._cipherbet[location]

  def _decrypt_letter(self, letter):
    """Find the index of the letter in the cipherbet and return the decrypted letter

    Args:
        letter (Char): One character in the alphabet
    """
    location = self._cipherbet.find(letter)
    return self.alphabet[location]
    