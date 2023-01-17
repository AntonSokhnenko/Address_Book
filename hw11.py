from collections import UserDict
from datetime import datetime

# 4. setter и getter логику для атрибутов value наследников Field.
class Field:  # родительским для всех полей, в нем потом реализуем логику общую для всех полей.
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)

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
        if value.isdigit() and len(value) == 10:    # обо тут краще метод isnumeric()
            self._value = value
        else:
            print('The number is not correct! Enter a 12-digit number!')
            raise ValueError

class Birthday(Field):    # Добавим поле для дня рождения Birthday. Это поле не обязательное, но может быть только одно.
# 6. Проверку на корректность веденного дня рождения в setter для value класса Birthday
    @Field.value.setter
    def value(self, birthday_date):
        self.value = birthday_date
        try:
            self.value = datetime.strptime(birthday_date, '%m.%d.%Y').date()
            return True
        except ValueError:
            return False


'''class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Only numbers greater zero accepted')
'''

# 2. Класс Record принимает ещё один дополнительный (опциональный) аргумент класса Birthday
# 3. Класс Record реализует метод days_to_birthday, который возвращает количество дней до следующего дня рождения
#  контакта, если день рождения задан.

class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday= None):
        self.name = name
        self.phones = (
            []
        )
        if phone:
            self.add_phone(phone)

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

# 3. Класс Record реализует метод days_to_birthday, который возвращает количество дней до
# следующего дня рождения контакта, если день рождения задан.
    def days_to_birthday(self, birthday_date):
        cur_day = datetime.now().date()
        if not self.birthday_date:
            return None
        birthday_date = datetime.strptime(birthday_date, '%d.%m.%Y').date()
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
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self):   не розумію як його зробити!!!!

# AddressBook реализует метод iterator, который возвращает генератор по записям AddressBook
#  и за одну итерацию возвращает представление для N записей

'''Добавим поле для дня рождения Birthday. Это поле не обязательное, но может быть только одно.
Добавим функционал работы с Birthday в класс Record, а именно функцию days_to_birthday,
которая возвращает количество дней до следующего дня рождения.
добавим функционал проверки на правильность приведенных значений для полей Phone, Birthday.
Добавим пагинацию (постраничный вывод) для AddressBook для ситуаций, когда книга очень большая и 
надо показать содержимое частями, а не всё сразу. Реализуем это через создание итератора по записям.
Критерии приёма:

1.AddressBook реализует метод iterator, который возвращает генератор по записям AddressBook
 и за одну итерацию возвращает представление для N записей.
2. Класс Record принимает ещё один дополнительный (опциональный) аргумент класса Birthday
3. Класс Record реализует метод days_to_birthday, который возвращает количество дней до следующего дня рождения
 контакта, если день рождения задан.
4. setter и getter логику для атрибутов value наследников Field.
5. Проверку на корректность веденного номера телефона в setter для value класса Phone.
6. Проверку на корректность веденного дня рождения в setter для value класса Birthday.'''
