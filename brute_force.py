from zipfile import ZipFile

zip_file = input("enter path of encrypted file : ")
pass_list = open(input("enter path of password file : "))
passwordlst = pass_list.read().split("\n")
success = False
for i in passwordlst:
    try:
        password = i
        with ZipFile(zip_file) as zf:
            zf.extractall(pwd=bytes(password,'utf-8'))
        print("success!!")
        success = True
        break
    except:
        pass
if not success:
    print("failed :(")
if success:
    print("contents : "+ open("/home/sashreek/PycharmProjects/GCI/brute_force_test").read())
