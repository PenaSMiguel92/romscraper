import internetarchive
import time
from tqdm import tqdm
import threading
import zipfile
import os

games_to_download = ['Castlevania', 'Conker\'s Bad Fur Day', 'Donkey Kong 64', \
                     'F-ZERO X', 'GoldenEye 007', 'Harvest Moon 64', 'Legend of Zelda, The - Majora\'s Mask', \
                     'Legend of Zelda, The - Ocarina of Time', 'Nightmare Creatures', 'Pokemon Stadium' \
                     'Pokemon Stadium 2', 'Rampage - World Tour', 'San Francisco Rush - Extreme Racing', \
                     'Star Fox 64', 'Super Mario 64', 'Super Smash Bros.']


def main():
    # test = internetarchive.search('https://archive.org/details/nintendo-64-romset-usa')
    search = internetarchive.search_items('identifier:nintendo-64-romset-usa')
    for result in search:
        itemid = result['identifier']
        item = internetarchive.get_item(itemid)
        files = item.get_files()
        for file in tqdm(files):
            if file.name[-4:] != '.zip':
                continue 
            bracket_index = file.name.find('(')
            game_name = file.name[:bracket_index-1]
            if game_name not in games_to_download:
                continue
            
            print('Downloading ' + game_name)

if __name__ == "__main__":
    main()