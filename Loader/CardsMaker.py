import pandas as pd
class DisplayCards():
    def __init__(self, NAME_LIST_PASS_I, TYPES_LIST_PASS_I, ID_LIST_PASS_I, RELADD_LIST_PASS_I, LENGTH_PASS_I,REL_ADD_passI,ANS,COMMENTS):
        self.NAME_LIST_PASS_I = NAME_LIST_PASS_I
        self.TYPES_LIST_PASS_I = TYPES_LIST_PASS_I
        self.ID_LIST_PASS_I = ID_LIST_PASS_I
        self.RELADD_LIST_PASS_I = RELADD_LIST_PASS_I
        self.LENGTH_PASS_I = LENGTH_PASS_I
        self.REL_ADD_passI = REL_ADD_passI
        self.COMMENTS = COMMENTS
        self.ANS = ANS
        self.ESD_DF = pd.DataFrame()
        self.TXT_DF = pd.DataFrame()

    def CreateESDCard(self):
        dict1 = {
            "NAME": self.NAME_LIST_PASS_I,
            "TYPE": self.TYPES_LIST_PASS_I,
            "ID": self.ID_LIST_PASS_I,
            "Rel Add": self.RELADD_LIST_PASS_I,
            "LENGTH": self.LENGTH_PASS_I
        }

        self.ESD_DF = pd.DataFrame(dict1)

    def CreateTXTCard(self):
        dict2 = {
            "Rel Add": self.REL_ADD_passI,
            "Contents": self.ANS,
            "Comments": self.COMMENTS
        }

        self.TXT_DF = pd.DataFrame(dict2)

    def CreateRLDCard(self,ID_LISTS,FLAGS,ADD_REL):
        dict3 = {
            "ESD Id":ID_LISTS,
            "FLAG":FLAGS,
            "LENGTH":[4 for i in range(len(FLAGS))],
            "Rel Add":ADD_REL
        }
        self.RLD_DF = pd.DataFrame(dict3)