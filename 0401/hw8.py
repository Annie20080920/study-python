def text_to_morse(text):
  morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..'
    }

  morse_code = ""
    
  for x in text:
    if x in morse_dict:
      morse_code = morse_code + morse_dict[x] + " "
  return morse_code
  # return ' '.join(morse_code)

text = "HELLO"
print(text_to_morse(text))
