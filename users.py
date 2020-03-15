NAME_INDEX = 0
MEMORY_INDEX = 1

def txt_to_matrix(txt) -> list:
    matrix = []
    for line in txt:
        line = line.split(',')
        line[MEMORY_INDEX] = line[MEMORY_INDEX].replace('\n','') 
        matrix.append(line)
    return matrix

def bytes_to_megabytes(bytes_list) -> list:
    megabytes = []
    for b in bytes_list:
        megabytes.append(float(b) / 1048576) # [1024 bytes = kbyte] * [1024 kbytes = 1 mbyte]
    return megabytes

def total_occupied_space(megabytes) -> float:
    total = sum(float(mb) for mb in megabytes)
    return total

def avarage_occupied_space(total_occupied_space, num_users) -> float:
    return total_occupied_space / num_users

def used_percentage(megabytes, total) -> list:
    percentage = []
    for mb in megabytes:
        percentage.append(100 * mb / total) 
    return percentage

with open('users.txt', 'r') as txt_users:
    txt_users = txt_users.readlines()

users = txt_to_matrix(txt_users)

bytes_list = []
for user_i in range(len(users)):
    bytes_list.append(users[user_i][MEMORY_INDEX])

megabytes = bytes_to_megabytes(bytes_list)

total = total_occupied_space(megabytes)
avarage = avarage_occupied_space(total, len(users))
percentage = used_percentage(megabytes, total)

with open('relatorio.txt', 'w') as txt_relatorio:
    txt_relatorio.write(f'ACME Inc.\t\tUso de espaço em disco pelo usuários\n\n')
    txt_relatorio.write('------------------------------------------------------\n\n')
    txt_relatorio.write(f'Nr.\t\tUsuário\t\t\tEspaço utilizado\t% do uso\n\n')

    for i, user in enumerate(users):
        txt_relatorio.write(f'{(i + 1)}\t\t{user[NAME_INDEX]:<10}\t\t\t{round(megabytes[i], 2):>9}\t\t{round(percentage[i], 2):>7}%\n')

    txt_relatorio.write(f'\n\nEspaço total ocupado: {round(total, 2)} MB\nEspaço médio ocupado: {round(avarage, 2)} MB')