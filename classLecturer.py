class Lecturer:
    def __init__(self,TelNum,PerNum):

        self.__TelefonNummer = TelNum
        self._PersonalNummer = PerNum
        self._Module = []

    def get_telnum(self):
        return self.__TelefonNummer

    def set_telnum(self,newTelNum):
        self.__TelefonNummer = newTelNum
        return self.__TelefonNummer

    def add_module(self,newmodules):
        self.__Module += newmodules
        return self.__Module

    def can_teach(self,module):
        if module in self._Module:
            return True
        else:
            return False


class Fakulty:
    def __init__(self):
        self._lecturers = []

    def add_lecturer(self,lecturer):
        self._lecturers += [lecturer]

    def find_lecturer(self,module):
        for i in range(len(self._lecturers)):
            if self._lecturers[i].can_teach(module):
                print(self._lecturers[i]._PersonalNummer)
