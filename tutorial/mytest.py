import pickle
import json
import requests


def unicodesTest():

    uniCodes = []
    with open('links/university_codes', 'rb') as file:
        uniCodes = pickle.load(file)
        [print("https://yokatlas.yok.gov.tr/lisans-univ.php?u="+code[0]) for code in uniCodes]


def proxiesTest():
    
    r = requests.get("https://sveltekit-on-the-edge.vercel.app/")
    print(r.content)

def readProgLinks():
    with open("program_links", "rb") as file:
        l = pickle.load(file)
        print(len(l))

unicodesTest()
