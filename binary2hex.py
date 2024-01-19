import argparse

def binary_to_hex(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
            hex_string = ''.join([f'\\x{byte:02x}' for byte in binary_data])
            return hex_string
    except Exception as e:
        print(f"Error: {e}")
        return None

parser = argparse.ArgumentParser(description='Convert binary to hex')
parser.add_argument('binary', metavar='binary', type=str, help='binary number')
args = parser.parse_args()

if __name__ == '__main__':
    print(binary_to_hex(args.binary))