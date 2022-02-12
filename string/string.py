# # Swaping the string
#
# s=input("Enter your text: ")
#
# def swap_case(s):
#     r=s.swapcase()
#     return r
# result= swap_case(s)
# print(result)

# spliting and joing text
line = input("Enter your text: ")
def join_and_split(line):
    s=line.split(" ")
    j= "_".join(s)
    return j

result = join_and_split(line)
print(result)

# printing full name using f-string
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)