import re

class Cards:
    def __init__(self, PROGRAM_LENGTH, SYMBOLS_I):
        self.SYMBOLS_I = SYMBOLS_I
        self.NAME_LIST_PASS_I = []
        self.TYPES_LIST_PASS_I = []
        self.ID_LIST_PASS_I = []
        self.RELADD_LIST_PASS_I = []
        self.LENGTH_PASS_I = []
        self.REL_ADD_passI = []
        self.ANS = []
        self.RESULT = []
        self.COMMENTS = []
        self.RLD_CARD_SYMBOLS = []
        self.RLD_DICT = {}
        self.PROGRAM_LENGTH = PROGRAM_LENGTH
        self.ID = 2

    def ESD_CARD(self, ESD_CARD_DICT_SD_I, ESD_CARD_DICT_LD_I, ESD_CARD_DICT_ER_I):
        for i in ESD_CARD_DICT_SD_I:
            self.NAME_LIST_PASS_I.append(i)
            self.TYPES_LIST_PASS_I.append(ESD_CARD_DICT_SD_I[i])
            self.ID_LIST_PASS_I.append("01")
            self.RELADD_LIST_PASS_I.append("00")
            self.LENGTH_PASS_I.append(self.PROGRAM_LENGTH)

        for i in ESD_CARD_DICT_LD_I:
            FLAG = 0
            self.NAME_LIST_PASS_I.append(i)
            self.TYPES_LIST_PASS_I.append(ESD_CARD_DICT_LD_I[i])
            FLAG2 = 0
            self.ID_LIST_PASS_I.append("--")
            for j in range(len(self.SYMBOLS_I)):
                if i in self.SYMBOLS_I[j]:
                    FLAG = 1
                    self.RELADD_LIST_PASS_I.append(self.SYMBOLS_I[j][0])
            if FLAG:
                self.RELADD_LIST_PASS_I.append("--")
            self.LENGTH_PASS_I.append("--")
        for i in ESD_CARD_DICT_ER_I:
            self.NAME_LIST_PASS_I.append(i)
            self.TYPES_LIST_PASS_I.append(ESD_CARD_DICT_ER_I[i])
            self.ID_LIST_PASS_I.append("0" + str(self.ID))
            self.RLD_DICT[i] = "0" + str(self.ID)
            self.ID += 1
            self.RELADD_LIST_PASS_I.append("00")
            self.LENGTH_PASS_I.append("--")

    def TXT_CARD(self,TXT_CARDS_COMMENTS_I):
        for i in range(len(TXT_CARDS_COMMENTS_I)):
            self.REL_ADD_passI.append(f"{i * 4} - {(i + 1) * 4 - 1}")
        for txt in TXT_CARDS_COMMENTS_I:
            x = re.findall("[+]|-", txt)
            if len(x):
                idx = re.search("[(]", txt).start()
                new_txt = txt[idx + 1:len(txt) - 1]
                r1 = re.search("[-]", new_txt)
                r2 = re.search("[+]", new_txt)
                result = re.split("[+]|[-]", new_txt)
                present = 0
                symbol = ""
                number = '"'
                # evaluation = 0
                self.RESULT.append(result)
                # replace Symbols with their values and apply eval() function
                for sym in self.SYMBOLS_I:
                    for _ in result:
                        if _ in sym:
                            new_txt = new_txt.replace(_, str(sym[0]))
                        else:
                            # new_txt = new_txt.replace(_,"0")
                            try:
                                num = int(_)
                            except:
                                new_txt = new_txt.replace(_, "0")

                self.ANS.append([eval(new_txt)])
                self.COMMENTS.append([new_txt])

            else:
                idx = re.search("[(]", txt).start()
                new_txt = txt[idx + 1:len(txt) - 1]
                self.RESULT.append([new_txt])
                present = 0
                value = 0
                for sym in self.SYMBOLS_I:
                    if new_txt in sym:
                        # ANS.append(sym[0])
                        present = 1
                        value = int(sym[0])
                        break
                self.ANS.append([str(value)])
                self.COMMENTS.append([str(value)])