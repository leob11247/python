class Television:
    """
    Represents a television with basic functionalities.
    """

    min_volume = 0
    """
    The minimum volume level.
    """

    max_volume = 2
    """
    The maximum volume level.
    """

    min_channel = 0
    """
    The minimum channel number.
    """

    max_channel = 3
    """
    The maximum channel number.
    """

    def __init__(self) -> None:
        """
        Initializes a new Television object with default settings.
        """
        self.__status = False  # TV starts off
        self.__muted = False
        self.__volume = Television.min_volume
        self.__channel = Television.min_channel

    def power(self) -> None:
        """
        Toggles the power state of the television (on/off).
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes or unmutes the television if it's powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increases the TV channel. Wraps around to the minimum channel if at the maximum.
        """
        if self.__status:
            if self.__channel == Television.max_channel:
                self.__channel = Television.min_channel
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the TV channel.
        Wraps around to the maximum channel if at the minimum.
        """
        if self.__status:
            if self.__channel == Television.min_channel:
                self.__channel = Television.max_channel
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the TV volume if powered on and not already at the maximum.
        Unmutes if muted.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.max_volume:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the TV volume if powered on and not already at the minimum.
        Unmutes if muted.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.min_volume:
                self.__volume -= 1
            else:
                self.__volume = Television.min_volume

    def __str__(self)  -> str:
        """
        Returns a string representation of the TV's current state (power, channel, volume).
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.min_volume}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"