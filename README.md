# WAM and EIHWAM Calculator

This Python script can calculate the Weighted Average Mark (WAM) and Engineering Integrated Honours Weighted Average Mark (EIHWAM) for a set of units. The units, along with their associated grades and credit point values, are stored in a dictionary. The script prompts the user to choose between caluclating the WAM or EIHWAM and then performs the calculation accordingly.

## Usage

### 1. Adding units
To add a new semester's worth of classes, add the new units to the 'class_grades' dictionay in the same format as the existing units. Make sure to add a comma after each unit except the last one.

For example, you can start with this

```
class_grades = {
    # Y1S1 example
    'UNIT1001': {'mark': 95, 'credit points': 6},
    'UNIT1002': {'mark': 85, 'credit points': 6},
    'UNIT1003': {'mark': 75, 'credit points': 3},
    'UNIT1004': {'mark': 65, 'credit points': 3},
    'UNIT1005': {'mark': 55, 'credit points': 6}
}
```

Which, after the next semester, can then be updated to:

```
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
```

And so on.

### 2. Running the Script

Execute the script in a Python environment. The script will prompt you to choose whether to calculate the WAM or the EIHWAM.

```
python grade_calculator.py
```

### 3. Choosing Calculation Mode

When prompted, type either WAM or EIHWAM to perform the respective calculation.

```
Would you like to calculate WAM or EIHWAM?: WAM
```

The script will then calculate and print the result:

```
WAM: 85.00
```

## Functions
### calculate_wam(grades)
Calculates the Weighted Average Mark (WAM) of all units in the class_grades dictionary.
- Parameters: grades (dict) - A dictionary containing the units with their marks and credit points.
- Returns: float - The calculated WAM.

### calculate_eihwam(grades)
Calculates the Engineering Integrated Honours Weighted Average Mark (EIHWAM) of all units in the class_grades dictionary.
- Parameters: grades (dict) - A dictionary containing the units with their marks and credit points.
- Returns: float - The calculated EIHWAM.

### get_mode()
Prompts the user to choose between calculating the WAM or the EIHWAM.
- Returns: str - The selected mode (WAM or EIHWAM).

### main()
The main function that runs the script, prompting the user for input and calling the appropriate calculation function.
