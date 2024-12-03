file_path = "list.txt"

lines = []
def parse_file(file):
    with open(file, 'r') as f:
        file_lines = f.readlines()
        # split lines by " "
        for line in file_lines:
            line = line.replace("\n", "")
            lines.append(line)
            
def check_is_linear(values) -> bool:
    sign = None
    for i in range(1, len(values)):
        actual = values[i]
        previous = values[i - 1]
        if actual >= previous:
            if sign == None:
                sign = "asc"
        elif sign == "asc":
            return False
    
    for i in range(1, len(values)):
        actual = values[i]
        previous = values[i - 1]
        if actual < previous:
            if sign == None:
                sign = "desc"
            elif sign == "asc":
                return False
        elif sign == "desc":
            return False
    return True

def check_range(values):
    # for each linear dataset, check if the range is within 3
    for i in range(1, len(values)):
        if abs(values[i] - values[i - 1]) > 3:
            return False
    return True

def check_doubles(values):
    for i in range(1, len(values)):
        if values.count(values[i]) > 1:
            return False
    return True

def return_possibilities(values):
    possibilities = []
    # Return all possibilities removing one value
    for i in range(0, len(values)):
        new_values = values.copy()
        new_values.pop(i)
        possibilities.append(new_values)
    
    return possibilities

def get_part_one():
    safe = 0
    for line in lines:
        values = [int(value) for value in line.split(" ")]
        if (check_is_linear(values) and check_range(values) and check_doubles(values)):
            safe += 1
    print(f"Part1: {safe}")
    
def get_part_two():
    safe = 0
    for line in lines:
        values = [int(value) for value in line.split(" ")]
        if (check_is_linear(values) and check_range(values) and check_doubles(values)):
            safe += 1
            continue
        
        # if not linear, check if it is possible to remove a value
        possibilities = return_possibilities(values)
        for possibility in possibilities:
            if (check_is_linear(possibility) and check_range(possibility) and check_doubles(possibility)):
                safe += 1
                break
    print(f"Part2: {safe}")     
                    
if __name__ == "__main__":
    parse_file(file_path)
    get_part_one()
    get_part_two()