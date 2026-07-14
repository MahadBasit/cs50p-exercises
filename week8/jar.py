class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or type(capacity) == bool or capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if (self._cookies + n) > self._capacity: 
            raise ValueError
        else:
            self._cookies += n
        return self._cookies

    def withdraw(self, n):
        if n > self._cookies:
            raise ValueError
        else:
            self._cookies -= n
        return self._cookies

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies