#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:42:24 2020

@author: kodiuser
"""

import random
from random import randint
from gtts import gTTS
import os
home = "/mnt/medialib/GitHub/Python/Playpen/"
for f in os.listdir(home):
    r = f.replace("  ","")
    if( r != f):
        os.rename(f,r)

home = "/mnt/medialib/GitHub/Python/Playpen/"
lang = 'en-au'
text = ['  Abalone'
,'  Atlantic Puffin'
,'  Atlantic Sailfish'
,'  Bioluminescent Octopus'
,'  Blue Mussel'
,'  Blue Whale'
,'  Brain Coral'
,'  Chesapeake Blue Crab'
,'  Christmas Tree Worm'
,'  Common Bottlenose Dolphin'
,'  Common Clownfish'
,'  Common Fangtooth'
,'  Common Two Banded Seabream'
,'  Dugong'
,'  Emperor Penguin'
,'  European Lobster'
,'  European Pilchard'
,'  Finless Porpoise'
,'  Flying Fish'
,'  Giant Clam'
,'  Giant Squid'
,'  Goblin Shark'
,'  Goose Barnacle'
,'  Gorgonian'
,'  Great Scallop'
,'  Great White Shark'
,'  Harp Seal'
,'  Hermit Crab'
,'  Horseshoe Crab'
,'  Humpback Whale'
,'  Japanese Spider Crab'
,'  Killer Whale'
,'  Kuruma Prawn'
,'  Leafy Sea Dragon'
,'  Leatherback Sea Turtle'
,'  Lions Mane Jellyfish'
,'  Macaroni Penguin'
,'  Marine Iguana'
,'  Moray Eel'
,'  Narwhal'
,'  Nautilis'
,'  Nudibranch'
,'  Pacific Bluefin Tuna'
,'  Pacific Sea Horse'
,'  Polar Bear'
,'  Portuguese Man o War'
,'  Puffer Fish'
,'  Red Lion Fish'
,'  Red Sea Urchin'
,'  Royal Star Fish'
,'  Sea Cucumber'
,'  Sea Lamprey'
,'  Sea Otter'
,'  Sockeye Salmon'
,'  South American Sea Lion'
,'  Southern Elephant Seal'
,'  Sperm Whale'
,'  Spotted Eagle Ray'
,'  Sword Fish'
,'  Tiger Pistol Shrimp'
,'  Walrus'
,'  Wandering Albatross'
,'  Whale Shark'
,'  Yellow Bellied Sea Snake']

for i in range(len(text)):
        tts = gTTS(text=text[i], lang=lang)
        filename = os.path.join(home,text[int(i)] + ".mp3")
        tts.save(filename)
        os.system("mpg321 " + "'" + filename + "'")


