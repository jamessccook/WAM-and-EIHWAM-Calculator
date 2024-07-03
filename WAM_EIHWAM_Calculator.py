# This stores units and their associated grade and credit point value
# To add a new semester worth of classes, add a comma to the end of the last unit and repeat the same format. Leave a comma off the end of the last unit 
class_grades = {
    # Y1S1 example
    'UNIT1001': {'mark': 95, 'credit points': 6},
    'UNIT1002': {'mark': 85, 'credit points': 6},
    'UNIT1003': {'mark': 75, 'credit points': 3},
    'UNIT1004': {'mark': 65, 'credit points': 3},
    'UNIT1005': {'mark': 55, 'credit points': 6},

    # Y1S2 example
    'UNIT1006': {'mark': 93, 'credit points': 6},
    'UNIT1007': {'mark': 86, 'credit points': 6},
    'UNIT1008': {'mark': 79, 'credit points': 3},
    'UNIT1009': {'mark': 88, 'credit points': 3},
    'UNIT1010': {'mark': 81, 'credit points': 6}
}

# Calculates the weighted average mark (WAM) of all units in the class_grades dictionary
def calculate_wam(grades):
    total = 0
    credit_point_total = 0

    # Loops through the data of each unit whilst applying the WAM formula
    for unit_code, info in grades.items():
        total += (info['mark'] * info['credit points'] * int(unit_code[4]))
        credit_point_total += (info['credit points'] * int(unit_code[4]))
    
    result = (total / credit_point_total)

    return result

# Calculates the engineering integrated honours weighted average mark (EIWAM) of all units in the class_grades dictionary
def calculate_eihwam(grades):
    total = 0
    credit_point_total = 0

    # Loops through the data of each unit whilst applying the EIHWAM formula
    for unit_code, info in grades.items():
        if int(unit_code[4]) > 1:
            total += (info['mark'] * info['credit points'] * int(unit_code[4]))
            credit_point_total += (info['credit points'] * int(unit_code[4]))
    
    result = (total / credit_point_total)

    return result

# Gets the desired mode from the user
def get_mode():
    while True:
        mode = input("Would you like to calculate WAM or EIHWAM?: ")
        if mode in ["WAM", "EIHWAM"]:
            return mode
        else:
            print("Invalid mode selected, please try again")

# Calls for the desired calculation
def main():
    mode = get_mode()

    if mode == "WAM":
        result = calculate_wam(class_grades)
        print(f"WAM: {result:.2f}")
    elif mode == "EIHWAM":
        result = calculate_eihwam(class_grades)
        print(f"EIHWAM: {result:.2f}")

if __name__ == "__main__":
    main()
