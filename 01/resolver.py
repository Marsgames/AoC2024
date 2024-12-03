file_path = "list.txt"

left = []
right = []
def parse_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        # split lines by " "
        for line in lines:
            split = line.split()
            left.append(split[0])
            right.append(split[1])
            
def sort_list():
    left.sort()
    right.sort()
    
diff = []
def get_diff():
    # get difference between left and right
    for i in range(len(left)):
        diff.append(abs(int(left[i]) - int(right[i])))
        
def get_final_result():
    # get the sum of all differences
    return sum(diff)

def get_similarity_score():
    score = 0
    for i in range(len(left)):
        lefty = left[i]
        if (lefty in right):
            count = int(right.count(lefty))
            # find how manny times left[i] is in right
            score += int(lefty) * count
    return score
        
        
if __name__ == "__main__":
    parse_file(file_path)
    sort_list()
    get_diff()
    print(f"Part1 result: {get_final_result()}")
    print(f"Part2 result: {get_similarity_score()}")
    