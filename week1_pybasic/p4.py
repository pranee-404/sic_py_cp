#Check if a +ve integer is Perfect square
integer = int(input('Enter a Positive Integer'))
root = integer**0.5
if root**2 == integer:
    print(integer, 'is a Perfect Square')