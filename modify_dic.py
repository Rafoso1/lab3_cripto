import re

def process_passwords(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='latin-1') as infile:
            passwords = infile.read().splitlines()
        
        modified_passwords = [
            password.capitalize() + '0'
            for password in passwords
            if re.match('^[a-zA-Z]', password)
        ]
        
        with open(output_file, 'w', encoding='latin-1') as outfile:
            outfile.write('\n'.join(modified_passwords))
        
        print(f"El diccionario modificado se ha guardado en {output_file}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {input_file}")

if __name__ == "__main__":
    input_file = 'rockyou.txt'
    output_file = 'rockyou_modificado.txt'
    process_passwords(input_file, output_file)
