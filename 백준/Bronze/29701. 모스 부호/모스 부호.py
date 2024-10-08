# 주어진 모스 부호와 문자의 쌍을 딕셔너리로 정의한다.
morse_dict = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",  ".": "E", "..-.": "F", "--.": "G",
    "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
    "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U",
    "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z", ".----": "1", 
    "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7",
    "---..": "8", "----.": "9", "-----": "0", "--..--": ",", ".-.-.-": ".", "..--..": "?",
    "---...": ":", "-....-": "-", ".--.-.": "@"
}

# number는 모스 부호로 변환하기 전 문자열의 길이를 나타내는 정수이다.
# morse_list는 원래의 문자열을 모스 부호로 변환한 메시지이다.
number = int(input())
morse_list = input().split()

# 각 모스 부호를 문자로 변환한 후 최종 변환된 문자열 출력한다.
print(''.join(morse_dict[morse] for morse in morse_list))