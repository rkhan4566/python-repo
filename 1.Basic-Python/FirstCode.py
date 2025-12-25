#custom exception(raise and throw an exception)
class error(Exception):
    pass

class dobexception(error):
    pass

year=int(input("entre your DOB"))
age=2025-year
try:
    if age>=20 and age<=30:
        print("you are egligible to cxam")
    else:
        raise dobexception
except dobexception:
    print("you are not egligible for exam")

    