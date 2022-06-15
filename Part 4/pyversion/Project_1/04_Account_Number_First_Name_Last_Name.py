import numbers
import itertools
from datetime import timedelta, datetime

class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.')

        # technically we should check that offset is a
        self._name = str(name).strip()

        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')

        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minute offset must be an integer.')

        if offset_minutes > 59 or offset_minutes < -59:
            raise ValueError('Minutes offset must between -59 and 59 (inclusive).')

        # for time delta sign of minutes will be set to sign of hours
        offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        # offsets are technically bounded between -12:00 and 14:00
        # see: https://en.wikipedia.org/wiki/List_of_UTC_time_offsets
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and + 14:00.')

        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
                self.name == other.name and
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)

    def __repr__(self):
        return (f"TimeZone(name='{self.name}', "
                f"offset_hours={self._offset_hours}, "
                f"offset_minutes={self._offset_minutes})")


class Account:
    transaction_counter = itertools.count(100)

    def __init__(self, account_number, first_name, last_name):
        # in practice we probably would want to add checks to make sure these values are valid / non-empty
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        # if value is None or len(str(value).strip()) == 0:
        #     raise ValueError('First name cannot be empty')
        # self._first_name = value
        self._first_name = Account.validate_name(value, '')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        # if value is None or len(str(value).strip()) == 0:
        #     raise ValueError('Last name cannot be empty')
        # self._last_name = value
        self._last_name = Account.validate_name(value, 'Last name')

    # also going to create a full_name computed property, for ease of use
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # The validation function won't need access to the instance data, so that's a prime candidate for a static method
    @staticmethod
    def validate_name(value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty')
        return str(value).strip()

try:
    a = Account('12345', 'John', '')
except ValueError as ex:
    print(ex)

a = Account('12345', 'Alex', 'Martelli')
print(a.first_name)
print(a.last_name)
print(a.full_name)
