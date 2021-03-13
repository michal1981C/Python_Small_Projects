import pyperclip
print('WELCOME TO THE CAESAR CIPHER PROGRAM!')

# The string to be encrypted/decrypted
message = str(input('Enter a message: '))

# The encryption/decryption key
key = int(input('Enter a key: '))

# Whether the program encrypts or decrypts
print('ENCRYPT = encrypt, DECRYPT = decrypt')
mode = str(input('What would you like to do?: ')) # Set to either encrypt or decrypt

# Every possible symbol to be ebcrypted or decrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+'

# Store the encrypted/decrypted message
translated = ''

for symbol in message:
    # NOTE: only symbol in SYNBOLS can be encrypted/decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol
        
# Output the translated string:
print('Message succesfully ', str.upper(mode) + 'ED!')
print(translated)
pyperclip.copy(translated)