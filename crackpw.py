import zipfile

encrypt_filename = "secretfile.zip"
zFile = zipfile.ZipFile(encrypt_filename)

passFile = open("passwords.txt", "r")
for line in passFile.readlines():
    test_password = line.strip("\n").encode("utf-8")
    try:
        print(test_password)
        zFile.extractall(pwd=test_password)
        print("Match found")
        break
    except Exception as err:
        pass