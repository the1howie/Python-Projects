## Convert Hindu-Arabic i.e., Decimal numbers in base 10 to Roman numerals
## My version online: https://the1howie.trinket.io/sites/roman-numerals 
## Tested with: https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php

VALID_CHARS = ("I", "V", "X", "L", "C", "D", "M", "_")

CHARS_DICT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "_": 1000,  # times 1000
}


def validate_int(num):
    if num.strip() == "":
        return None
    try:
        return int(num)
    except Exception as e:
        # raise Exception(e)
        print(str(e).capitalize())
        return None


def convert_number(arabic, roman, unitVal, sym10fold, sym5times, sym1unit, thousand=""):
    # unitVal is the value of 10% or the "unit"
    #   e.g. for numbers up to 10 it is 1;
    #   e.g. for numbers from 10 to 100 it is 10, etc.
    # sym10fold, sym5times, sym1unit are the symbols for 10x, 5x and 1x unit.
    # thousand is the symbol for multiples of thousand that are not preceeded by I.

    # create the dictionary of values
    values = {x: int(unitVal * x) for x in range(1, 10)}

    # check if there is a different symbol for a thousand
    if thousand == "":
        thousand = sym1unit

    # create the dictionary for the Roman symobls
    symbols = {
        1: thousand,
        2: thousand * 2,
        3: thousand * 3,
        4: sym1unit + sym5times,
        5: sym5times,
        6: sym5times + thousand,
        7: sym5times + thousand * 2,
        8: sym5times + thousand * 3,
        9: sym1unit + sym10fold,
    }

    # set up the starting index
    found_idx = False
    if unitVal == 10**6:
        idx = 3
    else:
        idx = len(symbols)

    # find the index for the correct value that divides into the Arabic number.
    while not found_idx and idx > 0:
        if arabic // values[idx] != 0:
            found_idx = True
        else:
            idx -= 1

    # Adjust i.e., reduce the Arabic number
    # Append to the Roman numeral string
    if idx > 0:
        multiples = arabic // values[idx]
        arabic -= values[idx] * multiples
        roman += symbols[idx] * multiples

    return roman, arabic


def to_roman(arabic):
    # convert Arabic to Roman numbers sequentially.
    if arabic is None:
        return ""

    # the limit number
    if arabic > 3999999 or arabic < 1:
        return "Enter a valid Integer from 1 to 3,999,999."

    # calling the convert function in decreasing order of "unit" value
    roman = ""
    roman, arabic = convert_number(arabic, roman, 1000000, "", "", "_M")
    roman, arabic = convert_number(arabic, roman, 100000, "_M", "_D", "_C")
    roman, arabic = convert_number(arabic, roman, 10000, "_C", "_L", "_X")
    roman, arabic = convert_number(arabic, roman, 1000, "_X", "_V", "_I", "M")
    roman, arabic = convert_number(arabic, roman, 100, "M", "D", "C")
    roman, arabic = convert_number(arabic, roman, 10, "C", "L", "X")
    roman, arabic = convert_number(arabic, roman, 1, "X", "V", "I")

    return roman


def bella_stampa(roman):
    # "bella stampa" is pretty print in Italian.
    # after trying overline bars the only thing that I could think of
    # for multiples of 1000 is write a dash in the line above.
    bars = roman.split("_")
    count = len(bars) - 1
    print("_" * count)
    print("".join(bars))


def validate_str(txt):
    valid_txt = txt.strip().upper()
    if valid_txt == "":
        return ""
    for c in valid_txt:
        if c not in VALID_CHARS:
            return None
    if "__" in valid_txt or valid_txt[-1] == "_":
        return None
    return valid_txt


def times1000(roman):
    # convert text to a list of values
    values = [CHARS_DICT[c] for c in roman]
    new_values = []
    times1000 = False
    for c, v in zip(roman, values):
        if c == "_":
            times1000 = True
        else:
            new_values.append(v * (1000 if times1000 else 1))
            times1000 = False
    return new_values


def add_subt_roman(values):
    if len(values) == 1:
        return values
    new_values = []
    for x in range(len(values) - 1):
        if values[x] < values[x + 1]:
            new_values.append(-1 * values[x])
        else:
            new_values.append(values[x])
    new_values.append(values[-1])
    return new_values


def to_arabic(roman):
    if roman == "" or roman is None:
        return 0
    values = times1000(roman)
    signed_values = add_subt_roman(values)
    return sum(signed_values)


def main():
    print("◻" * 37)
    print("Converter: ")
    print("\t1. Decimal to Roman")
    print("\t2. Roman to Decimal")
    print("\t3. List Roman & Decimal pairs")
    print("\t0. Exit")
    selection = validate_int(input("\nSelect 1/2/3/0: "))
    if selection == 1:
        arabic = validate_int(input("Enter a Decimal number: "))
        roman = to_roman(arabic)
        print("\nThe equivalent Roman numeral:")
        bella_stampa(roman)
    elif selection == 2:
        print("Hint: For multiples of 1000, say 5000, type an underline as _V.")
        roman = validate_str(input("Enter Roman numberals: "))
        if roman is None:
            print("Invalid input! Try again.")
            print(f"Valid characters: {', '.join(VALID_CHARS)}")
        else:
            arabic = to_arabic(roman)
            print("\nThe equivalent Decimal number:")
            print(f"{arabic:,d}")
    elif selection == 3:
        print("The Roman & Decimal pairs:")
        for k, v in CHARS_DICT.items():
            print(f"\t{k} = {'×' if k=='_' else ''}{v:d}")
    elif selection == 0:
        print(f"\n{' '*28}Good bye!")
        print("◻" * 37)
    print()
    return selection != 0


if __name__ == "__main__":
    carry_on = True
    while carry_on:
        carry_on = main()
