"""
PyTree is a simple application
which turns your directory of choice
into a tree diagram as such:

└──> .env
└──> certs
    └──> myt.app-key.pem
    └──> myt.app.pem
└──> db-certs
    └──> db-cert.pem
    └──> db-key.pem
└──> docker-compose.yml
└──> nginx.conf
└──> readme.md
└──> resources
    └──> 629fa66d59a03f515bd18677_image.png
    └──> meetings.png
    └──> mp3
        └──> sfx.mp3
└──> website
    └──> pub
        └──> index.php
        └──> login.php
        └──> db_conn.php

"""

import os, time, sys

def print_tree(d, i=0):
    with os.scandir(d) as e:
        for entry in e:
            print('    ' * i + '└──> ', end='', flush=True) # end='' prevents newline after printing, flush=True ensures output written immediately
            sys.stdout.write(entry.name + '\n')
            time.sleep(0.005 * len(entry.name)) # dynamic delay proportional to len of entry name
            if entry.is_dir(): print_tree(entry.path, i + 1)
        if sum(1 for _ in e) == i: input("\nPress Enter to exit...")

directory = ''
while not os.path.exists(directory): directory = input("Enter the directory you'd like to turn into a tree: ")
else: print(f"\n↓ {directory}\n"); print_tree(directory)