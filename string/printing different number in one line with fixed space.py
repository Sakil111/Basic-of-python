n = int(input("Enter your number: "))

def print_formatted(number):
    l=len(bin(number)[2:])
    for i in range(1,number+1):
        decimal = str(i).rjust(l," ")
        octal = str(oct(i)[2:]).rjust(l," ")
        hexa = str((hex(i)[2:]).upper()).rjust(l," ")
        binary = str(bin(i)[2:]).rjust(l," ")

        print(f"{decimal} {octal} {hexa} {binary}")


print(print_formatted(n))