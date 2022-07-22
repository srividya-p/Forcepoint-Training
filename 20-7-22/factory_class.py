class LowTableFan:
    def __init__(self) -> None:
        self.type = 'Table Fan'
        self.speed = 'low'
        self.onOff = False

    def switchOn(self):
        if self.onOff:
            print(f"{self.type} is already on.")
            return
        self.onOff = True
        print(f"{self.type} turned on.")

    def switchOn(self):
            if not self.onOff:
                print(f"{self.type} is already off.")
                return
            self.onOff = False
            print(f"{self.type} turned off.")

class HighTableFan:
    pass

class LowExhaustFan:
    pass

class HighExhaustFan:
    pass

class FanFactory():
    @staticmethod
    def createFans(speed):
        if speed == 'low':
            return LowExhaustFan(), LowTableFan()
        elif speed == 'high':
            return HighExhaustFan(), HighTableFan()