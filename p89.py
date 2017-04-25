numeral_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000};

def solve():
    total_savings = 0;
    for line in open('p089_roman.txt').read().splitlines():
        total_savings = total_savings + compute_space_saving(line);
    return total_savings;

def compute_space_saving(roman_numeral):
    return len(roman_numeral) - len(encode_roman_numeral(parse_roman_numeral(roman_numeral)));

def parse_roman_numeral(roman_numeral):
    numeral_length = len(roman_numeral);
    total = 0;
    for i, numeral in enumerate(roman_numeral):
        value = numeral_map[numeral];
        if i < numeral_length - 1:
            next_value = numeral_map[roman_numeral[i + 1]];
            if value < next_value:
                total = total - value;
            else:
                total = total + value;
        else:
            total = total + value;
    return total;

def encode_roman_numeral(value):
    encoded_numeral = '';
    while value > 0:
        if value >= 1000:
            encoded_numeral = encoded_numeral + 'M';
            value = value - 1000;
        elif value >= 900:
            encoded_numeral = encoded_numeral + 'CM';
            value = value - 900;
        elif value >= 500:
            encoded_numeral = encoded_numeral + 'D';
            value = value - 500;
        elif value >= 400:
            encoded_numeral = encoded_numeral + 'CD';
            value = value - 400;
        elif value >= 100:
            encoded_numeral = encoded_numeral + 'C';
            value = value - 100;
        elif value >= 90:
            encoded_numeral = encoded_numeral + 'XC';
            value = value - 90;
        elif value >= 50:
            encoded_numeral = encoded_numeral + 'L';
            value = value - 50;
        elif value >= 40:
            encoded_numeral = encoded_numeral + 'XL';
            value = value - 40;
        elif value >= 10:
            encoded_numeral = encoded_numeral + 'X';
            value = value - 10;
        elif value >= 9:
            encoded_numeral = encoded_numeral + 'IX';
            value = value - 9;
        elif value >= 5:
            encoded_numeral = encoded_numeral + 'V';
            value = value - 5;
        elif value >= 4:
            encoded_numeral = encoded_numeral + 'IV';
            value = value - 4;
        elif value >= 1:
            encoded_numeral = encoded_numeral + 'I';
            value = value - 1;
    return encoded_numeral;
