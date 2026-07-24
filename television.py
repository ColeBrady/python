

class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__volume_b4_mute = 0


    def power(self):
        if not self.__status:
            self.__status = True

        else:
            self.__status = False


    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__volume_b4_mute = self.__volume
                self.__volume = self.MIN_VOLUME

            else:
                self.__muted = False
                self.__volume = self.__volume_b4_mute


    def channel_up(self):
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

            else:
                self.__channel += 1


    def channel_down(self):
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

            else:
                self.__channel -= 1


    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.mute()

            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1


    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.mute()

            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1


    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'