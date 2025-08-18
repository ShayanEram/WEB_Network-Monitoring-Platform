import ctypes
import os
import platform

# Detect platform and load the correct shared library
if platform.system() == 'Windows':
    lib_path = os.path.abspath('encrypt.dll')
else:
    lib_path = os.path.abspath('./encrypt.so')

# Load the C shared library
lib = ctypes.CDLL(lib_path)

# Define argument and return types
lib.encrypt.argtypes = [ctypes.c_char_p]
lib.encrypt.restype = ctypes.c_char_p

lib.decrypt.argtypes = [ctypes.c_char_p]
lib.decrypt.restype = ctypes.c_char_p

def encrypt(text: str) -> str:
    """Encrypt a string using the C module."""
    encrypted = lib.encrypt(text.encode('utf-8'))
    return encrypted.decode('utf-8')

def decrypt(text: str) -> str:
    """Decrypt a string using the C module."""
    decrypted = lib.decrypt(text.encode('utf-8'))
    return decrypted.decode('utf-8')
