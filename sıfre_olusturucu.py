import random
import secrets
import string

def şifre_oluşturma():

    küçük_harfler = string.ascii_lowercase

    büyük_harfler = string.ascii_uppercase

    sayılar = string.digits

    semboller = "!'^+%&/()=?_#$½{[]}?*~`,.><|@"

    karakterler = küçük_harfler + büyük_harfler + sayılar + semboller
    while True:
        şifre = ""
        for i in range(random.randint(7, 12)):
            şifre += secrets.choice(karakterler)
        return şifre




