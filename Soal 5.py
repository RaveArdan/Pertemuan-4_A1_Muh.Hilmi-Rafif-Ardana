kata = input()
rev_kata = kata[::-1]

if kata == rev_kata:
    print("Palindrom")
else :
    print("Bukan palindrom")