#!/usr/bin/env python3

from googletrans import Translator
from prettytable import PrettyTable
import argparse
import colorama
import sys


parser = argparse.ArgumentParser(description="Japanese translator.")
parser.add_argument("-t", "--target", required=False, help="Target File containing lists of phrases", metavar="")
args = parser.parse_args()
target = args.target

word_table = PrettyTable(["Source", "Translation", "Pronunciation"])
word_table.padding_width = 1


def main():
    try:
        if target:
            with open(target, "r") as file:
                phrases = file.readlines()
                prog_bar(0, len(phrases))
                for index, line in enumerate(phrases):
                    translator(line)
                    prog_bar(index + 1, len(phrases))
                print(colorama.Fore.RESET)
                print(word_table)
        else:
            while True:
                word = input("Enter word/phrase: ")
                translator(word)
                print(word_table)
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit()
    
    

def translator(target):
    translator = Translator()
    source = translator.detect(target)

    if source.lang == "ja":
        translations = translator.translate(target, dest="en")
        pron = translations.pronunciation
        if not translations.pronunciation:
            pronunciation = translator.translate(translations.text, dest="ja")
            pron = pronunciation.pronunciation
        word_table.add_row([translations.origin, translations.text, pron])
    elif source.lang == "en":
        translations = translator.translate(target, dest="ja")
        word_table.add_row([translations.origin, translations.text, translations.pronunciation])


def prog_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    percent = int(percent)
    bar = "█" * percent + "-" * (100 - percent)
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")


    


if __name__ == "__main__": main()