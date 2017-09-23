# -*- coding: cp1252 -*-
from matplotlib import pyplot as plt
import numpy as np
import re
from math import log as ln
import string


prepos_liste = "ved, mot, fra, den, ha, det, om, en, kan, de, vi, ikke, og, for, til, er, vil, har, som, at, et, i, p�, mellom, over, under, av, bak, f�r, etter, hos, gjennom, utenom, blant"

prep = prepos_liste.split(", ")

def import_file(infile):
    f = open(infile,'r')
    read_file = f.read()
    word_array = read_file.split(" ")
    return word_array

def countword(words):
    word_count = {}
    found_words = []

    #Liste med alfabetet
    alfa = list(string.ascii_lowercase)
    for word in words:
        #Sjekker om alle tegn er i alfabetet
        i_alfa = True
        for letter in word:
            if not letter in alfa:
                i_alfa=False

        if word in found_words and i_alfa == True and not word in prep:
            word_count[word] +=1
        elif i_alfa == True and not word in prep:
            word_count[word] =1
            found_words.append(word)
    return word_count

def sort_dict(dictionary_unsorted):
    sorted_values= []
    sorted_words = []
    for i in range(0,len(dictionary_unsorted)):
        largest = ''
        value_largest = 0
        for key,value in dictionary_unsorted.iteritems():
            if value > value_largest:
                if not key in sorted_words:
                    largest = key
                    value_largest = value
        sorted_values.append(dictionary_unsorted[largest])
        sorted_words.append(largest)
    return sorted_values,sorted_words


def get_words(infile,no_words):
    word_array = import_file(infile)
    sorted_values,sorted_words = sort_dict(countword(word_array))
    for i in range(0,no_words-1):
        print sorted_words[i]
    return sorted_values, sorted_words

def barplot(values,labels,no_words):
    n = np.arange(no_words-1)
    values = values[:no_words-1]
    labels = labels[:no_words-1]
    plt.bar(n,values)
    plt.ylabel("Antall forekomster av ordet")
    plt.xlabel("Ord")
    plt.title("Ordtelling")
    plt.xticks(n,labels)
    plt.show()


files = [r'hoyre.txt',r'ap.txt']

infile = r'ap.txt'
values,words=get_words(infile,15)
ln_values = [ln(x) for x in values]
barplot(values,words,15)

'''
from matplotlib.backends.backend_pdf import PdfPages

for file in files:
    values,words=get_words(file,15)
    plot1 = barplot(values,words,15)

pp = PdfPages('foo.pdf')
pp.savefig(plot1)
pp.savefig(plot2)
pp.savefig(plot3)
pp.close()
'''
