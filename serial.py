"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    >>> serial
    <SerialGenerator start=100 next=101>
    """

    def __init__(self, start=100) -> None:
        """Make a SerialGenerator can provide start point otherwise default is 100"""
        self.start = start
        self.increment = -1

    def generate(self):
        """Increases increment by one, increment starts at -1 so that original number is given the first time"""
        self.increment += 1
        return self.start + self.increment

    def reset(self):
        """Resets increment value to -1, start value stays the same"""
        self.increment = -1

    def __repr__(self) -> str:
        """Change repr string to something more useful"""
        return f'<SerialGenerator start={self.start} next={self.start+1}>'

