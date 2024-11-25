import struct
import argparse
import os

def process_dig(file_path):
    """
    Обработка файла *.DAT

    Args:
        file_path: Путь к файлу *.DAT
    """
    
    try:
        file_name_without_extension = file_path.split(".")[0]
        output_file_path = f"{file_name_without_extension}.png"

        with open(file_path, 'rb') as f, open(output_file_path, "wb") as w:
            # Проверка заголовка
            header = f.read(4)
            if header != b'DIMG':
                print("Файл не распознан.")
                return
            w.write(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52')

            #collor = struct.unpack('<I', f.read(4))[0]
            collor, W_img, H_img, unk1, size_img, unk2 = struct.unpack('<IIIIII', f.read(24))
            #print(size_img)
            img = f.read(size_img)

            w.write(struct.pack('>II', W_img, H_img))
            w.write(b'\x08')
            match collor:
                case 0:
                    w.write(b'\x06')
                case 1:
                    w.write(b'\x02')
                case 5:
                    w.write(b'\x02')
                case 4:
                    w.write(b'\x04')
                case 3:
                    w.write(b'\x00')
                case _:
                    w.write(b'\x00')
            w.write(b''.join([
                b'\x00\x00\x00\x42\xC2\xBC\xBE\x00\x00\x00\x09\x70\x48\x59\x73\x00',
                b'\x00\x01\xB1\x00\x00\x01\xB1\x01\x61\x98\x28\x0E']))
            w.write(struct.pack('>I', size_img))
            w.write(b'\x49\x44\x41\x54')
            w.write(img)
            w.write(b'\x65\x0C\x6F\xAD\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82')
    except FileNotFoundError:
        print("Файл не найден.")


if __name__ == "__main__":
  #parser = argparse.ArgumentParser(description='Конвертирование DIG в PNG')
  #parser.add_argument('dig_file', help='Путь к *.DIG')
  #args = parser.parse_args()

  files = os.listdir()
  # Пройти по всем файлам
  for file in files:
    # Проверить, есть ли у файла расширение .dig
    if file.endswith(".dig"):
        # Обработать файл
        print(f"Обработка файла: {file}")
        process_dig(file)


  #process_dig(args.dig_file)