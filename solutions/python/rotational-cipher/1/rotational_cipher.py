def rotate(text, key):
    msg = ""
    for char in text:
        # Only rotate alphabetical characters
        if char.isalpha():
            # Determine the starting ASCII value ('A'=65 or 'a'=95)
            start = ord('A') if char.isupper() else ord('a')
            
            # Shift, wrap around using % 26, and convert back to character
            rotated_char = chr(start + (ord(char) - start + key) % 26)
            msg += rotated_char
        else:
            # Keep punctuation, numbers, and spaces exactly as they are
            msg += char
            
    return msg
        
