import os

base_path=r'C:\\projetos\\boticario\\BotiWeb\\botiweb\\comparer\\'
dir_one='estilos-producao'
dir_two='Boticario.Extranet.Web'

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def cmp_lines(path_1, path_2):
    l1 = l2 = True
    with open(path_1, 'r', encoding = "ISO-8859-1") as f1, open(path_2, 'r', encoding="utf8") as f2:
        while l1 and l2:
            l1 = f1.readline()
            l2 = f2.readline()
            if l1 != l2:
                return False
    return True


files1 = []

for root, dirs, files in os.walk(os.path.join(base_path, dir_one)):
    files1.extend(files)

files2 = []
for root, dirs, files in os.walk(os.path.join(base_path, dir_two)):
    files2.extend(files)

a=[f for f in files1 if f in files2]

extensions=['.css', '.html', '.js']

for file in a:
    if any(ext in file for ext in extensions):
        file_base_path_one=find(file, base_path+dir_one)
        file_base_path_two=find(file, base_path+dir_two)

        if not cmp_lines(file_base_path_one, file_base_path_two) :
            print('[' + file_base_path_one + '] \n [' + file_base_path_two + '] \n\n')
