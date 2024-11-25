import struct
import csv
import argparse
import re

def ror(value, shift):
    """Функция для циклического сдвига вправо (ROR)."""
    return ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF

def rol(value, shift):
    """Функция для циклического сдвига влево (ROL)."""
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def process_localize_dat_import(file_path,csv_file):
    """
    Обработка файла LOCALIZE_.DAT

    Args:
        file_path: Путь к файлу LOCALIZE_.DAT
    """
    
    try:
        with open(file_path, 'rb') as f, open(csv_file, "r", newline="", encoding="utf_8_sig") as csv_file, open("LOCALIZE_.DAT", "wb") as w:
            # Проверка заголовка
            header = f.read(4)
            if header != b'ALOC':
                print("Файл не распознан.")
                return
            w.write(header+f.read(48))

            reader = csv.reader(csv_file)
            next(reader)  # Пропускаем заголовок
            
            text_list = []

            #offset_start_text=478776
            offset_start_text=2688

            #for _ in range(10968):
            for _ in range(10968):
                row = next(reader)

                #print(row[2])

                ID_Text = struct.unpack('<I', f.read(4))[0]
                #print(ID_Text)

                # Текущий оффсет в бинарном файле
                current_offset = f.tell()
                file_offset=offset_start_text
                
                if ID_Text == 0:
                    w.write(struct.pack('<I', int(ID_Text)))

                    w.write(f.read(4))
                    f.read(24)

                    text_JPN = len(row[2].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    text_US = len(row[3].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    text_ZH_CN = len(row[4].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    text_ZH_TW = len(row[5].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    text_KO = len(row[6].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    text_ES = len(row[7].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    #print(text_ES)
                    
                    offset_start_text=offset_start_text
                    w.write(struct.pack('<I', offset_start_text))
                    if text_JPN == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_JPN+4
                        size=text_JPN%8
                        if size != 0:
                            padding = 8 - size
                            text_JPN += padding
                        else:
                            padding = 8
                            text_JPN += padding
                        offset_start_text += text_JPN
                    w.write(struct.pack('<I', offset_start_text))
                    if text_US == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_US+4
                        size=text_US%8
                        if size != 0:
                            padding = 8 - size
                            text_US += padding
                        else:
                            padding = 8
                            text_US += padding
                        offset_start_text += text_US
                    w.write(struct.pack('<I', offset_start_text))
                    if text_ZH_CN == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_ZH_CN+4
                        size=text_ZH_CN%8
                        if size != 0:
                            padding = 8 - size
                            text_ZH_CN += padding
                        else:
                            padding = 8
                            text_ZH_CN += padding
                        offset_start_text += text_ZH_CN
                    w.write(struct.pack('<I', offset_start_text))
                    if text_ZH_TW == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_ZH_TW+4
                        size=text_ZH_TW%8
                        if size != 0:
                            padding = 8 - size
                            text_ZH_TW += padding
                        else:
                            padding = 8
                            text_ZH_TW += padding
                        offset_start_text += text_ZH_TW
                    w.write(struct.pack('<I', offset_start_text))
                    if text_KO == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_KO+4
                        size=text_KO%8
                        if size != 0:
                            padding = 8 - size
                            text_KO += padding
                        else:
                            padding = 8
                            text_KO += padding
                        offset_start_text += text_KO
                    w.write(struct.pack('<I', offset_start_text))
                    if text_ES == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_ES+4
                        size=text_ES%8
                        if size != 0:
                            padding = 8 - size
                            text_ES += padding
                        else:
                            padding = 8
                            text_ES += padding
                        offset_start_text += text_ES
                    #w.write(struct.pack('<I', offset_start_text))
                else:
                    w.write(struct.pack('<I', int(ID_Text)))
                    value = struct.unpack('<I', f.read(4))[0]
                    #print(value)
                    w.write(struct.pack('<I', int(value)))
                    w.write(f.read(8))
                    f.read(24)

                    text_JPN = len(row[2].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    text_US = len(row[3].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    text_ZH_CN = len(row[4].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    text_ZH_TW = len(row[5].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    text_KO = len(row[6].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                    text_ES = len(row[7].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))

                    offset_start_text=offset_start_text
                    w.write(struct.pack('<I', offset_start_text))
                    if text_JPN == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_JPN+4
                        size=text_JPN%8
                        if size != 0:
                            padding = 8 - size
                            text_JPN += padding
                        else:
                            padding = 8
                            text_JPN += padding
                        offset_start_text += text_JPN
                    w.write(struct.pack('<I', offset_start_text))
                    if text_US == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_US+4
                        size=text_US%8
                        if size != 0:
                            padding = 8 - size
                            text_US += padding
                        else:
                            padding = 8
                            text_US += padding
                        offset_start_text += text_US
                    w.write(struct.pack('<I', offset_start_text))
                    if text_ZH_CN == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_ZH_CN+4
                        size=text_ZH_CN%8
                        if size != 0:
                            padding = 8 - size
                            text_ZH_CN += padding
                        else:
                            padding = 8
                            text_ZH_CN += padding
                        offset_start_text += text_ZH_CN
                    w.write(struct.pack('<I', offset_start_text))
                    if text_ZH_TW == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_ZH_TW+4
                        size=text_ZH_TW%8
                        if size != 0:
                            padding = 8 - size
                            text_ZH_TW += padding
                        else:
                            padding = 8
                            text_ZH_TW += padding
                        offset_start_text += text_ZH_TW
                    w.write(struct.pack('<I', offset_start_text))
                    if text_KO == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_KO+4
                        size=text_KO%8
                        if size != 0:
                            padding = 8 - size
                            text_KO += padding
                        else:
                            padding = 8
                            text_KO += padding
                        offset_start_text += text_KO
                    w.write(struct.pack('<I', offset_start_text))
                    if text_ES == 0:
                        offset_start_text += 8
                    else:
                        #offset_start_text += text_ES+4
                        size=text_ES%8
                        if size != 0:
                            padding = 8 - size
                            text_ES += padding
                        else:
                            padding = 8
                            text_ES += padding
                        offset_start_text += text_ES

                    if value > 1:
                        for _ in range(value-1):
                            row = next(reader)
                            w.write(f.read(8))
                            f.read(24)

                            text_JPN = len(row[2].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                            text_US = len(row[3].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                            text_ZH_CN = len(row[4].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                            text_ZH_TW = len(row[5].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                            text_KO = len(row[6].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
                            text_ES = len(row[7].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8'))
        
                            offset_start_text=offset_start_text
                            w.write(struct.pack('<I', offset_start_text))
                            if text_JPN == 0:
                                offset_start_text += 8
                            else:
                                #offset_start_text += text_JPN+4
                                size=text_JPN%8
                                if size != 0:
                                    padding = 8 - size
                                    text_JPN += padding
                                else:
                                    padding = 8
                                    text_JPN += padding
                                offset_start_text += text_JPN
                            w.write(struct.pack('<I', offset_start_text))
                            if text_US == 0:
                                offset_start_text += 8
                            else:
                                #offset_start_text += text_US+4
                                size=text_US%8
                                if size != 0:
                                    padding = 8 - size
                                    text_US += padding
                                else:
                                    padding = 8
                                    text_US += padding
                                offset_start_text += text_US
                            w.write(struct.pack('<I', offset_start_text))
                            if text_ZH_CN == 0:
                                offset_start_text += 8
                            else:
                                #offset_start_text += text_ZH_CN+4
                                size=text_ZH_CN%8
                                if size != 0:
                                    padding = 8 - size
                                    text_ZH_CN += padding
                                else:
                                    padding = 8
                                    text_ZH_CN += padding
                                offset_start_text += text_ZH_CN
                            w.write(struct.pack('<I', offset_start_text))
                            if text_ZH_TW == 0:
                                offset_start_text += 8
                            else:
                                #offset_start_text += text_ZH_TW+4
                                size=text_ZH_TW%8
                                if size != 0:
                                    padding = 8 - size
                                    text_ZH_TW += padding
                                else:
                                    padding = 8
                                    text_ZH_TW += padding
                                offset_start_text += text_ZH_TW
                            w.write(struct.pack('<I', offset_start_text))
                            if text_KO == 0:
                                offset_start_text += 8
                            else:
                                #offset_start_text += text_KO+4
                                size=text_KO%8
                                if size != 0:
                                    padding = 8 - size
                                    text_KO += padding
                                else:
                                    padding = 8
                                    text_KO += padding
                                offset_start_text += text_KO
                            w.write(struct.pack('<I', offset_start_text))
                            if text_ES == 0:
                                offset_start_text += 8
                            else:
                                #offset_start_text += text_ES+4
                                size=text_ES%8
                                if size != 0:
                                    padding = 8 - size
                                    text_ES += padding
                                else:
                                    padding = 8
                                    text_ES += padding
                                offset_start_text += text_ES
            
            csv_file.seek(0)
            next(reader)

            w.write(f.read(2692))

            for _ in range(12223):
                #print('test')
                row = next(reader)

                text_JPN = row[2].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8')
                text_US = row[3].replace("[n_nr]","\n").encode('utf-8')
                text_ZH_CN = row[4].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8')
                text_ZH_TW = row[5].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8')
                text_KO = row[6].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8')
                text_ES = row[7].replace("[n_rn]","\r\n").replace("[n_nr]","\n").encode('utf-8')

                if len(text_JPN) == 0:
                    w.write(b"\x00" * 8)
                else:
                    #w.write(text_JPN+b"\x00\x00\x00\x00")
                    size=len(text_JPN)%8
                    if size != 0:
                        padding = 8 - size
                        text_JPN += b'\x00' * padding
                    else:
                        padding = 8
                        text_JPN += b'\x00' * padding
                    w.write(text_JPN)
                if len(text_US) == 0:
                    w.write(b"\x00" * 8)
                else:
                    #w.write(text_US+b"\x00\x00\x00\x00")
                    size=len(text_US)%8
                    if size != 0:
                        padding = 8 - size
                        text_US += b'\x00' * padding
                    else:
                        padding = 8
                        text_US += b'\x00' * padding
                    w.write(text_US)

                if len(text_ZH_CN) == 0:
                    w.write(b"\x00" * 8)
                else:
                    #w.write(text_ZH_CN+b"\x00\x00\x00\x00")  
                    size=len(text_ZH_CN)%8
                    if size != 0:
                        padding = 8 - size
                        text_ZH_CN += b'\x00' * padding
                    else:
                        padding = 8
                        text_ZH_CN += b'\x00' * padding
                    w.write(text_ZH_CN)
                if len(text_ZH_TW) == 0:
                    w.write(b"\x00" * 8)
                else:
                    #w.write(text_ZH_TW+b"\x00\x00\x00\x00") 
                    size=len(text_ZH_TW)%8
                    if size != 0:
                        padding = 8 - size
                        text_ZH_TW += b'\x00' * padding
                    else:
                        padding = 8
                        text_ZH_TW += b'\x00' * padding
                    w.write(text_ZH_TW) 
                if len(text_KO) == 0:
                    w.write(b"\x00" * 8)
                else:
                    #w.write(text_KO+b"\x00\x00\x00\x00")    
                    size=len(text_KO)%8
                    if size != 0:
                        padding = 8 - size
                        text_KO += b'\x00' * padding
                    else:
                        padding = 8
                        text_KO += b'\x00' * padding
                    w.write(text_KO)
                if len(text_ES) == 0:
                    w.write(b"\x00" * 8)
                else:
                    #w.write(text_ES+b"\x00\x00\x00\x00")
                    size=len(text_ES)%8
                    if size != 0:
                        padding = 8 - size
                        text_ES += b'\x00' * padding
                    else:
                        padding = 8
                        text_ES += b'\x00' * padding
                    w.write(text_ES)
            
            #w.seek(478776)
            
    except FileNotFoundError:
        print("Файл не найден.")


def process_localize_dat(file_path,csv_file):
    """
    Обработка файла LOCALIZE_.DAT

    Args:
        file_path: Путь к файлу LOCALIZE_.DAT
    """

    try:
        with open(file_path, 'rb') as f, open(csv_file, "w", newline="", encoding="utf_8_sig") as csv_file:
            # Проверка заголовка
            header = f.read(4)
            if header != b'ALOC':
                print("Файл не распознан.")
                return
            
            # Создаем объект CSV-писателя
            writer = csv.writer(csv_file)

            # Записываем заголовок CSV-файла
            writer.writerow(["id_текста", "Offset_start", "JPN", "US", "ZH_CN", "ZH_TW", "KO", "ES"])

            # Переход в оффсет 52
            f.seek(52)

            line=0

            offset_start_text=478776
            # Обработка данных
            for _ in range(10968):
                ID_Text = struct.unpack('<I', f.read(4))[0]
                #print(ID_Text)

                if ID_Text == 0:
                    
                    # Чтение 4 байт
                    f.read(4)
                    # Чтение 6 * 4 байт
                    #data = f.read(24)
                    JPN,US,ZH_CN,ZH_TW,KO,ES  = struct.unpack("<IIIIII", f.read(24))
                    #print(US)
                    row = [ID_Text, JPN]
                    for language_code in [JPN, US, ZH_CN, ZH_TW, KO, ES]:
                        current_offset = f.tell()
                        
                        f.seek(language_code+offset_start_text)
                        #Считываем текст
                        text = ""
                        byte = f.read(1)
                        while byte != b"\x00":  # Читаем до нулевого байта
                            text += byte.decode("latin-1")
                            byte = f.read(1)
                        # latin-1 -> utf-8
                        text = text.encode('latin-1').decode('utf-8').replace("\r\n","[n_rn]").replace("\n","[n_nr]")
                        #writer.writerow([ID_Text, text])
                        row.append(text)
                        f.seek(current_offset)
                    line=line+1
                    row.append(line)
                    writer.writerow(row)

                else:
                    # Запись значения
                    value = struct.unpack('<I', f.read(4))[0]
                    #print(value)

                    # Чтение 8 байт
                    f.read(8)

                    # Чтение 6 * 4 байт
                    #data = f.read(24)
                    JPN,US,ZH_CN,ZH_TW,KO,ES  = struct.unpack("<IIIIII", f.read(24))

                    row = [ID_Text, JPN]
                    for language_code in [JPN, US, ZH_CN, ZH_TW, KO, ES]:
                        current_offset = f.tell()
                        f.seek(language_code+offset_start_text)
                        #Считываем текст
                        text = ""
                        byte = f.read(1)
                        while byte != b"\x00":  # Читаем до нулевого байта
                            text += byte.decode("latin-1")
                            byte = f.read(1)
                        # latin-1 -> utf-8
                        text = text.encode('latin-1').decode('utf-8').replace("\r\n","[n_rn]").replace("\n","[n_nr]")
                        #writer.writerow([ID_Text, text])
                        row.append(text)
                        f.seek(current_offset)
                    line=line+1
                    row.append(line)
                    writer.writerow(row)

                    # Чтение данных по оффсету (если значение больше 1)
                    if value > 1:
                        for _ in range(value-1):
                            f.read(8)
                            # Чтение 6 * 4 байт
                            #data = f.read(24)
                            JPN,US,ZH_CN,ZH_TW,KO,ES  = struct.unpack("<IIIIII", f.read(24))
                            #print(value)
                            row = [ID_Text, JPN]
                            for language_code in [JPN, US, ZH_CN, ZH_TW, KO, ES]:
                                current_offset = f.tell()
                                f.seek(language_code+offset_start_text)
                                #Считываем текст
                                text = ""
                                byte = f.read(1)
                                while byte != b"\x00":  # Читаем до нулевого байта
                                    text += byte.decode("latin-1")
                                    byte = f.read(1)
                                # latin-1 -> utf-8
                                text = text.encode('latin-1').decode('utf-8').replace("\r\n","[n_rn]").replace("\n","[n_nr]")
                                #writer.writerow([ID_Text, text])
                                row.append(text)
                                f.seek(current_offset)
                            line=line+1
                            row.append(line)
                            writer.writerow(row)
            #exit()

            # Переход в оффсет 478776
            #f.seek(478776)

            # Запись адресса оффсета
           # offset_address = f.tell()

            # Установка оффсета в 0
            #f.seek(offset_address)
            #f.write(b'\x00' * 4)

            # Обработка записанных данных
            #with open("_extracted_text.txt", "w", encoding="utf_8_sig") as text_file:
            #    for i in range(0, len(data), 4):
            #        offset = struct.unpack('<I', data[i:i+4])[0]
            #        f.seek(offset)
            #        text = f.read(1).decode("utf-8")
            #        while text != '\x00':
            #            text_file.write(text)
            #            text = f.read(1).decode("utf-8")
            #        text_file.write("\n")

    except FileNotFoundError:
        print("Файл не найден.")

def process_file_ror(input_file, output_file):
    """Функция для обработки файла."""
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        data = f_in.read(478776)
        data_text = f_in.read()
        processed_data = bytearray()

        k=0

        for i in range(0, len(data_text), 4):
            if k==0:
                # Читаем 4 байта (dword)
                dword = int.from_bytes(data_text[i:i+4], byteorder='little')

                # Выполняем операции, аналогичные коду дизассемблера
                dword = ror(dword, 3)
                processed_data.extend(dword.to_bytes(4, byteorder='little'))
                k=1
            else:
                dword = int.from_bytes(data_text[i:i+4], byteorder='little')
                #print(dword)
                dword = ror(dword, 4)
                processed_data.extend(dword.to_bytes(4, byteorder='little'))
                k=0

        f_out.write(data)
        f_out.write(processed_data)

def process_file_rol(input_file, output_file):
    """Функция для обработки файла."""
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        data = f_in.read(478776)
        data_text = f_in.read()
        processed_data = bytearray()

        k=0

        for i in range(0, len(data_text), 4):
            if k==0:
                # Читаем 4 байта (dword)
                dword = int.from_bytes(data_text[i:i+4], byteorder='little')

                # Выполняем операции, аналогичные коду дизассемблера
                dword = rol(dword, 3)
                processed_data.extend(dword.to_bytes(4, byteorder='little'))
                k=1
            else:
                dword = int.from_bytes(data_text[i:i+4], byteorder='little')
                dword = rol(dword, 4)
                processed_data.extend(dword.to_bytes(4, byteorder='little'))
                k=0

        f_out.write(data)
        f_out.write(processed_data)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Извлечение\запись языков в ASTLIBRA.')
  parser.add_argument('Dat_file', help='Путь к LOCALIZE_.DAT')
  parser.add_argument('languages_file', help='Путь к файлу языков.')
  parser.add_argument('-e', '--extract', action='store_true', help='Извлечь языки из LOCALIZE_.DAT.')
  parser.add_argument('-p', '--update', action='store_true', help='Обновить языки в LOCALIZE_.DAT.')
  args = parser.parse_args()

  if args.extract:
    process_localize_dat(args.Dat_file, args.languages_file)
  elif args.update:
    process_localize_dat_import(args.Dat_file, args.languages_file)
    #process_file_rol("LOCALIZE_.DAT_tmp", "LOCALIZE_.DAT")
  else:
    print("Вы должны указать либо -e (извлечь), либо -p (обновить).")