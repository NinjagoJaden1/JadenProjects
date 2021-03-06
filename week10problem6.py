def translate():
    '''translate() -> None
    Prompts user to enter dictionary files and input and output files
    Changes words in input file according to the dictionary file=
    Write translation in output file'''
    dictFileName =open("pirateWords.txt","r")
    textFileName = open("myinput.txt","r")
    outputFileName = open("myoutputfile.txt","w+")
    d={}


    for line in dictFileName:
        wordlist = line.rstrip().split("|")

        (key, val) = wordlist
        d[key] = val

    print(d)
    z=""
    for line2 in textFileName:
        x=line2.split()
        for value in x:
            print(value)

            if value == "hello" or value == "money" or value == "your" or value == "steal" or value == "you":
                word2 = d[value]
                z+=word2+" "
            else:
                word2=value
                z += word2 + " "

        print(z)




    outputFileName.write(z)


translate()# add your code here


