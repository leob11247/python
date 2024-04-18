class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.min_volume
        self.__channel = Television.min_channel

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.max_channel:
                self.__channel = Television.min_channel
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.min_channel:
                self.__channel = Television.max_channel
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__volume < Television.max_volume:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            self.__muted = False
            if self.__volume > Television.min_volume:
                self.__volume -= 1

    def __str__(self):
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.min_volume}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

