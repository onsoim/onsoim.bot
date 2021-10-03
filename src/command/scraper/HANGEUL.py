
import re


class HANGEUL():
    def __init__(self):
        self.BASE_CODE, self.CHOSUNG, self.JUNGSUNG = 44032, 588, 28
        self.CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        self.JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
        self.JONGSUNG_LIST = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    def get_all(self):
        for i in range(len(self.CHOSUNG_LIST)):
            for j in range(len(self.JUNGSUNG_LIST) + 1):
                for k in range(len(self.JONGSUNG_LIST)):
                    print(self.BASE_CODE + \
                        i * 22 * len(self.JONGSUNG_LIST) + \
                        j * len(self.JONGSUNG_LIST) + \
                        k
                    )

    def seperate_jamo(self, string):
        a = []
        for s in string:
            if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', s) is not None:
                c = []
                char_code = ord(s) - self.BASE_CODE

                char1 = int(char_code/self.CHOSUNG)
                c += self.CHOSUNG_LIST[char1]

                char2 = int((char_code - (self.CHOSUNG * char1))/self.JUNGSUNG)
                c += self.JUNGSUNG_LIST[char2]

                char3 = int((char_code - (self.CHOSUNG * char1) - (self.JUNGSUNG * char2)))
                c += self.JONGSUNG_LIST[char3]
                a += [c]
            else:
                a += [[s]]
        return a

if __name__ == "__main__":
    hangeul = HANGEUL()
    print("".join([i[0] for i in hangeul.seperate_jamo("오징어 게임")]))
