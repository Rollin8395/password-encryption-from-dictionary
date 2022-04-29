import pyzipper

wordlist = "rockyou.txt"
file = "enc.zip"

fileobject = pyzipper.AESZipFile(file)
with open (wordlist,"rb") as wordlist:
    for word in wordlist:
        try:
            fileobject.pwd = word.strip()
            fileobject.read('ImportantFile.docx')
        except:
            print("trying password-",word.decode().strip())
            continue
        else:
            print("password found-",word.decode().strip())
            exit(0)
print("No password matched")

