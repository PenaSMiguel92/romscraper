import internetarchive
import time
from tqdm import tqdm
import threading
import zipfile
import os

working_dir = os.path.dirname(os.path.realpath(__file__))
dump_path = working_dir + '/downloads'
extracted_path = working_dir + '/extracted'

games_to_download = ['Castlevania', 'Conker\'s Bad Fur Day', 'Donkey Kong 64', \
                     'F-ZERO X', 'GoldenEye 007', 'Harvest Moon 64', 'Legend of Zelda, The - Majora\'s Mask', \
                     'Legend of Zelda, The - Ocarina of Time', 'Nightmare Creatures', 'Pokemon Stadium' \
                     'Pokemon Stadium 2', 'Rampage - World Tour', 'San Francisco Rush - Extreme Racing', \
                     'Star Fox 64', 'Super Mario 64', 'Super Smash Bros.']

def initialize_paths(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)


def extract_zip(zip_file, extract_location):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_location)
        print(f"Extracted {zip_file} into {extract_location}")

def extract_files_in_threads(zip_files, extract_location):
    threads = []
    for zip_file in zip_files:
        thread = threading.Thread(target=extract_zip, args=(zip_file, extract_location))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

def extract_roms(extension):
    zip_files = [os.path.join(f'{dump_path}/', file) for file in os.listdir(dump_path) if file.endswith(extension)]
    extract_files_in_threads(zip_files, extracted_path)
    #     extract_files_in_threads(zip_files, f'dump/extracted_data/{state}')


def download_files(identifier, extension):
    search = internetarchive.search_items('identifier:' + identifier)
    for result in search:
        itemid = result['identifier']
    
    item = internetarchive.get_item(itemid)
    files = item.get_files()
    extension_length = len(extension)
    total = len(item.item_metadata.values())
    print(total)
    files_to_download = []
    for file in files:
        if file.name[-extension_length:] != extension:
            continue 
        bracket_index = file.name.find('(')
        game_name = file.name[:bracket_index-1]
        if game_name not in games_to_download:
            continue
        files_to_download.append(file)

    for file in tqdm(files_to_download):
        # file.download(file_path='./downloads')
        print('Downloading: ' + file.name)
        time.sleep(1)

def main():
    # initialize_paths([dump_path, extracted_path])
    # download_files('nintendo-64-romset-usa', '.zip')
    extract_roms('.zip')
    # test = internetarchive.search('https://archive.org/details/nintendo-64-romset-usa')
    

if __name__ == "__main__":
    main()