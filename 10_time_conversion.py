# 10_time_conversion.py

#Way1
def time_conversion(s: str) -> str:
    period = s[-2:]              # AM or PM
    parts = s[:-2].split(':')    # [hh, mm, ss]
    hour = int(parts[0])

    if period == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f'{hour:02d}:{parts[1]}:{parts[2]}'

#Way2
def time_conversion_2(s: str) -> str:
    period = s[-2:]
    hh, mm, ss = s[:-2].split(':')

    hour = int(hh) % 12
    if period == 'PM':
        hour += 12

    return f'{hour:02d}:{mm}:{ss}'

#Way3 'Pythonic'
def time_conversion_3(s: str) -> str:
    hour = int(s[:2]) % 12 + (12 if s[-2:] == 'PM' else 0)
    return f'{hour:02d}{s[2:-2]}'

if __name__ == "__main__":
    print(time_conversion('12:05:46AM'))  # 00:05:46
    print(time_conversion('12:05:50PM'))  # 12:05:50
    print(time_conversion('11:05:50PM'))  # 23:05:50
