from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value) -> None:
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

class Name(Field):  # обязательное поле с именем.
    pass
    # def init(self, name):
    #     self.name = name


# 5. Проверку на корректность веденного номера телефона в setter для value класса Phone.
class Phone(Field):

    @Field.value.setter
    def value(self, value):
        if value.isdigit() and len(value) == 9:
            self._value = value
        else:
            print('The number is not correct! Enter a 12-digit number!')
            raise ValueError

# Добавим поле для дня рождения Birthday. Это поле не обязательное, но может быть только одно.
# 6. Проверкa на корректность веденного дня рождения в setter для value класса Birthday
class Birthday(Field):

    @Field.value.setter
    def value(self, value):
        self.value = value
        try:
            print(value)
            self.value = datetime.strptime(value, '%m.%d.%Y').date()
            return True
        except ValueError:
            return False


class Record:

    def __init__(self, name: Name, phone: Phone = None, birthday_date: Birthday= None):
        self.name = name
        self.phones = (
            []
        )
        if phone:
            self.add_phone(phone)
        self.birthday_date = birthday_date

    def __str__(self):
        return '{:<10}'.format(self.name.value) + ':' + ', '.join(self.phones)

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, phone: Phone, phone_new: Phone):
        if self.del_phone(phone):
            self.add_phone(phone_new)
            return True
        return False

    def del_phone(self, phone: Phone):
        for i, p in enumerate(self.phones):
            if p.value == phone.value:
                return self.phones.pop(i)

    def days_to_birthday(self):
        cur_day = datetime.now().date()
        if not self.birthday_date:
            return None
        birthday_date = datetime.strptime('%d.%m.%Y').date()
        cur_date = datetime.now().date()
        birthday_date = birthday_date.replace(year=datetime.now().year)
        if cur_date > birthday_date:
            birthday_date = birthday_date.replace(year=datetime.now().year + 1)
            difference = birthday_date - cur_date
            return difference.days
        else:
            difference = birthday_date - cur_date
            return difference.days


class AddressBook(UserDict):
    # def __init__(self):
    #     super().__init__()
    #     self.n = None

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self, n=2, days=0):
        self.n = n
        index = 1
        print_block = '-' * 50 + '\n'
        for record in self.data.values():
            if days == 0 or (record.birthday.value is not None and record.days_to_birthday(record.birthday) <= days):
                print_block += str(record) + '\n'
                if index < n:
                    index += 1
                else:
                    yield print_block
                    index, print_block = 1, '-' * 50 + '\n'
        yield print_block
