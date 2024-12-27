#number to roman
def int_to_roman(num):
    a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    b = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    rom_num = ""
    for i in range(len(a)):
        while num >= a[i]:#1987 >= 1000,987 >= 900 ,87 >= 50,37 >= 10,27 >= 10,17 >= 10 ,7 >= 5,2 >= 1,1 >= 1
            rom_num += b[i]
            num -= a[i]
    return rom_num
print(int_to_roman(1987))
#roman to number
def roman_to_int(num):
    a=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    result=0
    for v,i  in a:
        while num.startswith(i):
            result+=v
            num=num.removeprefix(i)
    print(result)
roman_to_int("MXX")


       
    


