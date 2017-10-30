#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

tralphabet = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l",
              "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]

enalphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

tratbash = {"a": "z", "b": "y", "c": "v", "ç": "ü", "d": "u", "e": "t", "f": "ş", "g": "s", "ğ": "r", "h": "p",
            "ı": "ö", "i": "o", "j": "n", "k": "m", "l": "l", "m": "k", "n": "j", "o": "i", "ö": "ı", "p": "h",
            "r": "ğ", "s": "g", "ş": "f", "t": "e", "u": "d", "ü": "ç", "v": "c", "y": "b", "z": "a"}

enatbash = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r",
            "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i",
            "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"}


def ceaser_tr(sentence, num):
    newSentence = ""
    for character in sentence:
        i = -1
        for x in tralphabet:
            i += 1
            if x == character:
                break
        if character in tralphabet:
            if i + num < 29:
                newSentence += tralphabet[i + num]
            else:
                newSentence += tralphabet[(i + num) - 29]
        else:
            newSentence += character
    print("-" * 20)
    print("Cümleniz şuydu: \"", sentence, "\" \nŞifrelenmiş formu: \"", newSentence, "\"")
    print("-" * 20)

def ceaser_en(sentence, num):
    newSentence = ""
    for character in sentence:
        i = -1
        for x in enalphabet:
            i += 1
            if x == character:
                break
        if character in enalphabet:
            if i + num < 26:
                newSentence += enalphabet[i + num]
            else:
                newSentence += enalphabet[(i + num) - 26]
        else:
            newSentence += character
    print("-" * 20)
    print("Your sentence was: \"", sentence, "\" \nEncrypted form:: \"", newSentence, "\"")
    print("-" * 20)

def atbash_tr(userSentence):
    newSentence = ""
    for character in userSentence:
        if character in tratbash:
            newSentence += tratbash[character]
        else:
            newSentence += character
    print("-" * 20)
    print("Cümleniz şuydu: \"", userSentence, "\" \nŞifrelenmiş formu: \"", newSentence, "\"")
    print("-" * 20)

def atbash_en(userSentence):
    newSentence = ""
    for character in userSentence:
        if character in tratbash:
            newSentence += tratbash[character]
        else:
            newSentence += character
    print("-" * 20)
    print("Your sentence was: \"", userSentence, "\" \nEncrypted form:: \"", newSentence, "\"")
    print("-" * 20)

def a1z26_tr(sentence):
    newSentence = ""
    for character in sentence:
        i = -1
        if character in tralphabet:
            for x in tralphabet:
                i += 1
                if x == character:
                    break
            newSentence += "-"
            newSentence += str(i)
        else:
            newSentence += character
    print("-" * 20)
    print("Cümleniz şuydu: \"", sentence, "\" \nŞifrelenmiş formu: \"", newSentence, "\"")
    print("-" * 20)

def a1z26_en(sentence):
    newSentence = ""
    for character in sentence:
        i = -1
        if character in enalphabet:
            for x in enalphabet:
                i += 1
                if x == character:
                    break
            newSentence += "-"
            newSentence += str(i)
        else:
            newSentence += character
    print("-" * 20)
    print("Your sentence was: \"", sentence, "\" \nEncrypted form:: \"", newSentence, "\"")
    print("-" * 20)

def vigenere_en(keyword, sentence):
    keynumbers = []
    for character in keyword:
        i = -1
        for word in enalphabet:
            i += 1
            if character == word:
                break
        keynumbers.append(i)
    y = -1
    newSentence = ""
    for char in sentence:
        if char in enalphabet:
            i = -1
            y += 1
            for word in enalphabet:
                i += 1
                if char == word:
                    break
            i += int(keynumbers[(y % len(keynumbers))])
            if i < 26:
                newSentence += str(enalphabet[i])
            else:
                newSentence += str(enalphabet[(i - 26)])
        else:
            newSentence += char
    print("-" * 20)
    print("Your sentence was: \"", sentence, "\" \nEncrypted form:: \"", newSentence, "\"")
    print("-" * 20)

def vigenere_tr(keyword, sentence):
    keynumbers = []
    for character in keyword:
        i = -1
        for word in tralphabet:
            i += 1
            if character == word:
                break
        keynumbers.append(i)
    y = -1
    newSentence = ""
    for char in sentence:
        if char in tralphabet:
            i = -1
            y += 1
            for word in tralphabet:
                i += 1
                if char == word:
                    break
            i += int(keynumbers[(y % len(keynumbers))])
            if i < 29:
                newSentence += str(tralphabet[i])
            else:
                newSentence += str(tralphabet[(i - 29)])
        else:
            newSentence += char
    print("-" * 20)
    print("Your sentence was: \"", sentence, "\" \nEncrypted form:: \"", newSentence, "\"")
    print("-" * 20)

while True:
    language = int(input("1-Türkçe, 2-English:"))

    if language == 1:
        cipher = int(input("Şifreleyicinizi seçin: 1-Sezar, 2-Atbash, 3-A1Z26, 4-Vigenere, 5-Karışık"))

        if cipher == 1:
            userSentence = input("Cümleniz:")
            numberType = int(input("Seçiniz:\n1-Şifreleme sayısını kendim seçmek istiyorum.\n2-Sayı şansa seçilsin."))
            if numberType == 1:
                number = int(input("Şifreleme sayısını yazın (1 ile 29 arasında):"))
            elif numberType == 2:
                number = random.randint(1, 29)
            ceaser_tr(userSentence, number)

        elif cipher == 2:
            userSentence = input("Cümleniz:")
            atbash_tr(userSentence)

        elif cipher == 3:
            userSentence = input("Cümleniz:")
            a1z26_tr(userSentence)

        elif cipher == 4:
            userSentence = input("Cümleniz:")
            key = input("Anahtar kelimeniz:")
            vigenere_en(key, userSentence)

        elif cipher == 5:
            firstCipher = int(input("Birinci şifreleyicinizi giriniz:"))
            secondCipher = int(input("İkinci şifreleyicinizi giriniz:"))

            if firstCipher == 1:
                userSentence = input("Cümleniz:")
                numberType = int(input("Seçin:\n1-Şifreleme sayısını kendim seçmek istiyorum.\n2-Sayı şansa seçilsin."))

                if numberType == 1:
                    number = int(input("Şifreleme sayısını yazın (1 ile 29 arasında):"))
                elif numberType == 2:
                    number = random.randint(1, 29)
                ceaser_tr(userSentence, number)

            elif firstCipher == 2:
                userSentence = input("Cümleniz:")
                atbash_tr(userSentence)

            elif firstCipher == 3:
                userSentence = input("Cümleniz:")
                a1z26_tr(userSentence)

            elif firstCipher == 4:
                userSentence = input("Cümleniz:")
                key = input("Anahtar kelimeniz:")
                vigenere_en(key, userSentence)

            if secondCipher == 1:
                userSentence = input("Cümleniz:")
                numberType = int(
                    input("Seçiniz:\n1-Şifreleme sayısını kendim seçmek istiyorum.\n2-Sayı şansa seçilsin."))
                if numberType == 1:
                   number = int(input("Şifreleme sayısını yazın (1 ile 29 arasında):"))
                elif numberType == 2:
                    number = random.randint(1, 29)
                ceaser_tr(userSentence, number)

            elif secondCipher == 2:
                userSentence = input("Cümleniz:")
                atbash_tr(userSentence)

            elif secondCipher == 3:
                userSentence = input("Cümleniz:")
                a1z26_tr(userSentence)

            elif secondCipher == 4:
                userSentence = input("Cümleniz:")
                key = input("Anahtar kelimeniz:")
                vigenere_en(key, userSentence)
    elif language == 2:
        cipher = int(input("Choose your cipher: 1-Ceaser, 2-Atbash, 3-A1Z26, 4-Vigenere 5-Complex"))
        if cipher == 1:
            userSentence = input("Your sentence:")
            numberType = int(input("Choose: \n1-I want to choose a number for cipher. \n2-Choose a number randomly"))
            if numberType == 1:
                number = int(input(""))
            elif numberType == 2:
                number = random.randint(1, 26)
            ceaser_en(userSentence, number)

        elif cipher == 2:
            userSentence = input("Your sentence:")
            atbash_en(userSentence)

        elif cipher == 3:
            userSentence = input("Your sentence:")
            a1z26_en(userSentence)

        elif cipher == 4:
            userSentence = input("Your sentence:")
            key = input("Your key word")
            vigenere_en(key, userSentence)

        elif cipher == 5:
            firstCipher = int(input("Choose your first cipher: 1-Ceaser, 2-Atbash, 3-A1Z26, 4-Vigenere"))
            secondCipher = int(input("Choose your second cipher: 1-Ceaser, 2-Atbash, 3-A1Z26, 4-Vigenere"))
            if firstCipher == 1:
                userSentence = input("Your sentence:")
                numberType = int(input("Choose:\n1-I want to choose a number for cipher.\n2-Choose a number randomly"))
                if numberType == 1:
                    number = int(input(""))
                elif numberType == 2:
                    number = random.randint(1, 26)
                ceaser_en(userSentence, number)
                print("Write encrypted form to section below this text.")

            elif firstCipher == 2:
                userSentence = input("Your sentence:")
                atbash_en(userSentence)
                print("Write encrypted form to section below this text.")

            elif firstCipher == 3:
                userSentence = input("Your sentence:")
                a1z26_en(userSentence)
                print("Write encrypted form to section below this text.")

            elif firstCipher == 4:
                userSentence = input("Your sentence:")
                key = input("Your key word")
                vigenere_en(key, userSentence)
                print("Write encrypted form to section below this text.")

            if secondCipher == 1:
                userSentence = input("Your sentence:")
                numberType = int(
                    input("Choose: \n1-I want to choose a number for cipher. \n2-Choose a number randomly"))
                if numberType == 1:
                    number = int(input(""))
                elif numberType == 2:
                    number = random.randint(1, 26)
                ceaser_en(userSentence, number)
            elif secondCipher == 2:
                userSentence = input("Your sentence:")
                atbash_en(userSentence)

            elif secondCipher == 3:
                userSentence = input("Your sentence:")
                a1z26_en(userSentence)

            elif secondCipher == 4:
                userSentence = input("Your sentence:")
                key = input("Your key word")
                vigenere_en(key, userSentence)

# Cihan Alperen Bosnalı
# 10 May 2017
