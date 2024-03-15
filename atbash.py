from cipher import Cipher

class AtbashCipher(Cipher):
  """ Class that inherit from cipher and use the AtBashCipher method to encryp/decrypt

  Attributes:
    _cipherbet (str): string of the AtBashCipher
  """
  def __init__(self):
    """ Call super to initialize the alphabet, then create the cipherbet attribute as a list with the letters Z-A in it."""
    super().__init__()
    self._cipherbet = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

  def _encrypt_letter(self, letter):
    """Find the index of the letter in the alphabet and return the encrypted letter

    Args:
        letter (Char): One character in the alphabet
    """
    return self._cipherbet[self.alphabet.index(letter)]

  def _decrypt_letter(self, letter):
    """Find the index of the letter in the cipherbet and return the decrypted letter

    Args:
        letter (Char): One character in the alphabet
    """
    return self.alphabet[self._cipherbet.index(letter)]
