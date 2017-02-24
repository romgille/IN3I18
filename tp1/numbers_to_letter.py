def numberToLetters(number):
    newNumber = number
    i = 10
    list = []
    while newNumber != 0:
        val = newNumber % i
        list.append(val)
        i = i * 10
        newNumber -= val

    dic = {
        0: "", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq",
        6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix", 11: "onze",
        12: "douze", 13: "treize", 14: "quatorze", 15: "quinze", 16: "seize",
        20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante",
        60: "soixante", 80: "quatre-vingt", 100: "cent", 1000: "mille"
            }

    sentence = ""

    nbrSpeciaux = False

    for datum in reversed(list):
        if len(str(datum)) == 7:
            if int(str(datum)[0]) != 1:
                sentence += dic[int(str(datum)[0])] + "-millions-"
            else:
                sentence += dic[int(str(datum)[0])] + "-million-"

        if len(str(datum)) == 6:
            sentence += dic[int(str(datum)[0])] + "-cent-"

        if len(str(datum)) == 5:
            if int(str(datum)[0]) == 1:
                sentence += dic[10] + "-mille-"
            if int(str(datum)[0]) == 2:
                sentence += dic[20] + "-mille-"
            if int(str(datum)[0]) == 3:
                sentence += dic[30] + "-mille-"
            if int(str(datum)[0]) == 4:
                sentence += dic[40] + "-mille-"
            if int(str(datum)[0]) == 5:
                sentence += dic[50] + "-mille-"
            if int(str(datum)[0]) == 6:
                sentence += dic[60] + "-mille-"
            if int(str(datum)[0]) == 7:
                sentence += dic[60] + "-"
                nbrSpeciaux = True
            if int(str(datum)[0]) == 8:
                sentence += dic[80] + "-mille-"
            if int(str(datum)[0]) == 9:
                sentence += dic[80] + "-"
                nbrSpeciaux = True

        if len(str(datum)) == 4:
            if nbrSpeciaux == True:
                if int(str(datum)[0]) == 1:
                    sentence += dic[11] + "-mille-"
                if int(str(datum)[0]) == 2:
                    sentence += dic[12] + "-mille-"
                if int(str(datum)[0]) == 3:
                    sentence += dic[13] + "-mille-"
                if int(str(datum)[0]) == 4:
                    sentence += dic[14] + "-mille-"
                if int(str(datum)[0]) == 5:
                    sentence += dic[15] + "-mille-"
                if int(str(datum)[0]) == 6:
                    sentence += dic[16] + "-mille-"
                if int(str(datum)[0]) == 7:
                    sentence += dic[10] + "-" + dic[7] + "-mille-"
                if int(str(datum)[0]) == 8:
                    sentence += dic[10] + "-" + dic[8] + "-mille-"
                if int(str(datum)[0]) == 9:
                    sentence += dic[10] + "-" + dic[9] + "-mille-"

                nbrSpeciaux = False
            else:
                sentence += dic[int(str(datum)[0])] + "-mille-"

        if len(str(datum)) == 3:
            sentence += dic[int(str(datum)[0])] + "-cent-"

        if len(str(datum)) == 2:
            if int(str(datum)[0]) == 1:
                nbrSpeciaux = True
            if int(str(datum)[0]) == 2:
                sentence += dic[20]
            if int(str(datum)[0]) == 3:
                sentence += dic[30]
            if int(str(datum)[0]) == 4:
                sentence += dic[40]
            if int(str(datum)[0]) == 5:
                sentence += dic[50]
            if int(str(datum)[0]) == 6:
                sentence += dic[60]
            if int(str(datum)[0]) == 7:
                sentence += dic[60] + "-"
                nbrSpeciaux = True
            if int(str(datum)[0]) == 8:
                sentence += dic[80]
            if int(str(datum)[0]) == 9:
                sentence += dic[80] + "-"
                nbrSpeciaux = True

        if len(str(datum)) == 1:
            if nbrSpeciaux == True:
                if int(str(datum)[0]) == 0:
                    sentence += dic[10]
                if int(str(datum)[0]) == 1:
                    sentence += dic[11]
                if int(str(datum)[0]) == 2:
                    sentence += dic[12]
                if int(str(datum)[0]) == 3:
                    sentence += dic[13]
                if int(str(datum)[0]) == 4:
                    sentence += dic[14]
                if int(str(datum)[0]) == 5:
                    sentence += dic[15]
                if int(str(datum)[0]) == 6:
                    sentence += dic[16]
                if int(str(datum)[0]) == 7:
                    sentence += dic[10] + "-" + dic[7]
                if int(str(datum)[0]) == 8:
                    sentence += dic[10] + "-" + dic[8]
                if int(str(datum)[0]) == 9:
                    sentence += dic[10] + "-" + dic[9]

                nbrSpeciaux = False
            else:
                sentence += dic[int(str(datum)[0])]

#    if sentence[-1] == "-":
#        sentence =  sentence[:-1]

    print(sentence)

def main():
    for i in range(1, 1000000):
        numberToLetters(i)
#    numberToLetters(70)

if __name__ == "__main__":
    main()
