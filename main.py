import internetarchive
from tqdm import tqdm
import threading
import zipfile
import os



def main():
    test = internetarchive.search_items('https://archive.org/details/nintendo-64-romset-usa')
    print(test)

if __name__ == "__main__":
    main()