file_path = "list.txt"

# Part1
# input_string = """S00S00S
# 0A0A0A0
# 00MMM00
# SAMXMAS
# 00MMM00
# 0A0A0A0
# S00S00S"""
# Part2
input_string = """M0S0M0
0A0A00
M0S0M0
M0MS0S
0A00A0
S0SM0M"""
array_2d = []

def get_input_string():
    with open(file_path, "r") as file:
        input_string = file.read()
    return input_string

def get_array_2d():
    for line in input_string.split("\n"):
        array_2d.append(line)
    return array_2d

def get_xmas():
    return input_string.count("XMAS")

def get_reverse():
    return input_string.count("SAMX")

def get_down():
    count = 0
    for y in range(0, len(array_2d) - 3):
        line = array_2d[y]
        for x in range(0, len(array_2d[y])):
            a_01 = line[x]
            a_02 = array_2d[y+1][x]
            a_03 = array_2d[y+2][x]
            a_04 = array_2d[y+3][x]
            if array_2d[y][x] == "X" and array_2d[y+1][x] == "M" and array_2d[y+2][x] == "A" and array_2d[y+3][x] == "S":
                count += 1
    return count

def get_up():
    count = 0
    for y in range(3, len(array_2d)):
        line = array_2d[y]
        for x in range(0, len(array_2d[y])):
            a_01 = line[x]
            a_02 = array_2d[y-1][x]
            a_03 = array_2d[y-2][x]
            a_04 = array_2d[y-3][x]
            if array_2d[y][x] == "X" and array_2d[y-1][x] == "M" and array_2d[y-2][x] == "A" and array_2d[y-3][x] == "S":
                count += 1
    return count
        
def get_topright_diagonal():
    count = 0
    # top right
    for y in range(3, len(array_2d)):
        for x in range(0, len(array_2d[y]) - 3):
            if array_2d[y][x] == "X" and array_2d[y-1][x+1] == "M" and array_2d[y-2][x+2] == "A" and array_2d[y-3][x+3] == "S":
                count += 1
    return count

def get_topleft_diagonal():
    count = 0
    # top left
    for y in range(3, len(array_2d)):
        for x in range(3, len(array_2d[y])):
            if array_2d[y][x] == "X" and array_2d[y-1][x-1] == "M" and array_2d[y-2][x-2] == "A" and array_2d[y-3][x-3] == "S":
                count += 1
    return count

def get_bottomright_diagonal():
    count = 0
    # bottom right
    for y in range(0, len(array_2d) - 3):
        for x in range(0, len(array_2d[y]) - 3):
            if array_2d[y][x] == "X" and array_2d[y+1][x+1] == "M" and array_2d[y+2][x+2] == "A" and array_2d[y+3][x+3] == "S":
                count += 1
    return count

def get_bottomleft_diagonal():
    count = 0
    # bottom left
    for y in range(0, len(array_2d) - 3):
        for x in range(3, len(array_2d[y])):
            if array_2d[y][x] == "X" and array_2d[y+1][x-1] == "M" and array_2d[y+2][x-2] == "A" and array_2d[y+3][x-3] == "S":
                count += 1
    return count

def get_nine_batch():
    count = 0
    for y in range(0, len(array_2d) - 2):
        for x in range(0, len(array_2d[y]) - 2):
            tl = array_2d[y][x]
            tr = array_2d[y][x+2]
            mc = array_2d[y+1][x+1]
            bl = array_2d[y+2][x]
            br = array_2d[y+2][x+2]
            if  (mc != "A"):
                continue
            if (tl == tr == "M") and (bl == br == "S"):
                count += 1
                continue
            if (tl == bl == "M") and (tr == br == "S"):
                count += 1
                continue
            if (tr == br == "M") and (tl == bl == "S"):
                count += 1
                continue
            if (bl == br == "M") and (tl == tr == "S"):
                count += 1
                continue
            
    return count


if __name__ == "__main__":
    input_string = get_input_string()
    array_2d = get_array_2d()
    
    print(f"XMAS: {get_xmas()}") # should be 3
    print(f"SAMX: {get_reverse()}") # should be 2
    print(f"DOWN: {get_down()}") # should be 1
    print(f"UP: {get_up()}") # should be 2
    print(f"TOP RIGHT: {get_topright_diagonal()}") # should be 4
    print(f"TOP LEFT: {get_topleft_diagonal()}") # should be 4
    print(f"BOTTOM RIGHT: {get_bottomright_diagonal()}") # should be 1
    print(f"BOTTOM LEFT: {get_bottomleft_diagonal()}") # should be 2
    
    print(f"X-MAS: {get_nine_batch()}") # should be 4
    
    count = get_xmas() + get_reverse() + get_down() + get_up() + get_topright_diagonal() + get_topleft_diagonal() + get_bottomright_diagonal() + get_bottomleft_diagonal()
    print(f"Part 1: {count}")
    print(f"Part 2: {get_nine_batch()}")