"""
Format Command Prompt Text
Optional flag to switch format ON / OFF.
Formatting is ON by default.
Tested on Windows only.
"""
class FormatCmdText:
    Grey = "\033[90m"
    Red = "\033[91m"
    Green = "\033[92m"
    Yellow = "\033[93m"
    Blue = "\033[94m"
    Magenta = "\033[95m"
    Cyan = "\033[96m"
    Bold = "\033[1m"
    Italics = "\033[3m"
    Underline = "\033[4m"
    Esc = "\033[0m"
    
    def __init__(self, format_on=True):
        if not format_on:
            for attr in self:
                setattr(self, attr[0], '')
            
    def __iter__(self):
        attributes = [attr for attr in dir(self) if not attr.startswith("__")]
        for attr in attributes:
            # this yields the attribute's name and value
            yield (attr, getattr(self, attr))


if __name__ == '__main__':
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    fcmd_on = FormatCmdText()
    print(f"\nAttributes with format {fcmd_on.Underline}{fcmd_on.Bold}ON{fcmd_on.Esc}:")
    print(fcmd_on.__class__.__name__, end=": ")
    for attr in fcmd_on:
        if attr[0] != "Esc":
            print(f"{attr[1]}{attr[0]}{fcmd_on.Esc}", end=" ")
    print()
    
    fcmd_off = FormatCmdText(format_on=False)
    print(f"\nAttributes with format {fcmd_off.Underline}{fcmd_off.Bold}OFF{fcmd_off.Esc}:")
    print(fcmd_off.__class__.__name__, end=": ")
    for attr in fcmd_off:
        if attr[0] != "Esc":
            print(f"{attr[1]}{attr[0]}{fcmd_off.Esc}", end=" ")
    print()
    print()
    