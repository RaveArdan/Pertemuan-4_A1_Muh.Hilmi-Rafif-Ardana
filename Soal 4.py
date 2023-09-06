bill = int(input())
bill_prm = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
prima = "Bilangan prima"
if bill < 0 :
    print("Harus bilangan bulat positif")
elif bill in bill_prm :
    print(prima)
else :
    print("Bukan bilangan prima")
    