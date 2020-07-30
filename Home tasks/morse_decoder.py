MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def decode_word(code):
    return ''.join(MORSE[letter] for letter in code.split())

def morse_decoder(code):
    return ' '.join(decode_word(word) for word in code.split('   ')).capitalize()

if __name__ == '__main__':
    print("Example:")
    print(morse_decoder("... --- -- .   - . -..- -")) 
    print(morse_decoder("..--- ----- .---- ---.."))
    print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))

