from codecs import open
import random

filename = r"C:\Users\Martijn\Documents\Paradox Interactive\Hearts of Iron IV\mod\KR\history\units\RUS.txt"

new_file = r"C:\Users\Martijn\Documents\Paradox Interactive\Hearts of Iron IV\mod\KR\history\units\RUS_edit.txt"

file = open(filename, 'r', 'utf-8-sig').readlines()

new_file = open(new_file, 'w', 'utf-8-sig')
new_file.truncate(0)

for line in file:
    if 'start_experience_factor' in line:
        last_xp = float(line.split("=")[1].strip())
        new_xp = random.uniform(0.16, 0.25) if last_xp < 0.25 else random.uniform(0.3, 0.36)
        new_file.write("\t\tstart_experience_factor = " + f'{new_xp:1.2f}' + "\n")
    elif 'start_equipment_factor' in line:
        last_equip = float(line.split("=")[1].strip())
        new_equip = random.uniform(0.80, 0.85) if last_xp < 0.25 else random.uniform(0.85, 0.90)
        new_file.write("\t\tstart_equipment_factor = " + f'{new_equip:1.2f}' + "\n")
    else:
        new_file.write(line)