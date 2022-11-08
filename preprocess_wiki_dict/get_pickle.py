from os import listdir
import sys
import pickle
from bs4 import BeautifulSoup

# folder traversal functions


def get_max_file_num(language, folder):
    file_list = listdir(f'{language}/{folder}')
    if len(file_list):
        return len(file_list)-1
    return -1


def get_list_of_folder(language):
    return sorted([f for f in listdir(language) if f[0] != '.'])

# save and load functions


def save(dictionary, checkpoint):
    print(checkpoint)
    with open(f'{path}/{language}/backup/dump.pickle', 'wb') as handle:
        pickle.dump(dictionary, handle)
    with open('data_dir/checkpoint', 'w') as txtfile:
        print(checkpoint, file=txtfile)


def load():
    with open(f'{path}/{language}/checkpoint', 'r') as file:
        checkpoint = file.read().strip()
    with open(f'{path}/{language}/backup/dump.pickle', 'rb') as handle:
        dictionary = pickle.load(handle)
    return dictionary, checkpoint

# parse file function


def get_first_paragraf(filepath, dictionary={}, num_entry=-1):
    start = False
    current_id = None
    current_title = None
    current_blob = ""
    if not dictionary:
        dictionary = {
            "id": [],
            "title": [],
            "first_paragraph": []
        }
    count = 0
    global_count = 0
    with open(filepath) as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            if len(line):
                if start:
                    current_blob += line + '\n'

            if len(line) > 3:
                if line[:4] == '<doc':
                    start = True
                    current_blob += line
                if line[:5] == '</doc':
                    start = False
                    current_blob += line
                    soup = BeautifulSoup(current_blob, features='lxml')
                    if soup.doc:
                        current_id = soup.doc['id']
                        current_title = soup.doc['title']
                        dictionary['id'].append(current_id)
                        dictionary['title'].append(current_title)
                        dictionary['first_paragraph'].append(
                            soup.doc.decode_contents())
                    current_blob = ''
                    global_count += 1
            if num_entry != -1 and global_count > num_entry:
                break
    return dictionary


# Check arguments
if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    mode = 'not_load'
if len(sys.argv) > 2:
    language = sys.argv[2]
else:
    language = 'en'
if len(sys.argv) > 3:
    path = sys.argv[3]
else:
    path = ""

# Initialize dictionary
if mode == 'load':
    dic, cp = load()
    folder, num = cp.split('_')
    num = int(num)+1
else:
    dic = {}
    folder = 'AA'
    num = 0
folder_list = get_list_of_folder(language)
folder_start = folder_list.index(folder)
for fol in folder_list[folder_start:]:
    max_num = (get_max_file_num(language, fol))
    while num <= max_num:
        dic = get_first_paragraf(
            f"{language}/{fol}/{'wiki_'+str(num).zfill(2)}", dictionary=dic)
        save(dic, f"{fol}_{str(num).zfill(2)}")
        num += 1
    num = 0
