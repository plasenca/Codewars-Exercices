from collections import Counter

def solution(roman_num: str) -> int|str:
    
    if isinstance(roman_num, str):
        dicc_roman_num = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num_total = 0
        
        # Optional - Validate the form of the Roman Numeral
        # print(Counter(roman_num))
        
        # Functionality
        list_num_convert = list(map(lambda l: [value for letter, value in dicc_roman_num.items() if letter==l], roman_num))
        list_num_convert = list_num_convert[::-1]
        print(list_num_convert)
        
        for i in list_num_convert:
            
            if list_num_convert[i][0] < list_num_convert[i+1][0]:
                num_total += list_num_convert[i][0]
            
    else: return f"The Roman Numeral({roman_num}) is not a string"
    
if __name__ == '__main__':
    solution("MDCLXVI")