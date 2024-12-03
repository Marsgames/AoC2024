import re

file_path = "list.txt"

input_string = ""

def get_input_string():
    with open(file_path, "r") as file:
        input_string = file.read()
    return input_string

def get_couples(input):
    regex = r"mul\((\d{1,3},\d{1,3})\)"
    couples = re.findall(regex, input)
    return couples

def multiply_couples(couples):
    result = 0
    for couple in couples:
        a, b = couple.split(",")
        result += int(a) * int(b)
    return result

def handle_dos():
    new_input = input_string.split("don't()")[0]
    
    for substring in  input_string.split("don't()")[1:]:
        # remove from beginning to first "do()"
        substring = substring.split("do()")[1:]
        new_input = f"{new_input}{substring}"
    return get_couples(new_input)
    
if __name__ == "__main__":
    input_string = get_input_string()
    # input_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    couples = get_couples(input_string)
    print(f"Part 1: {multiply_couples(couples)}")
    new_couples = handle_dos()
    print(f"Part 2: {multiply_couples(new_couples)}")