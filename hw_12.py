from collections import UserDict
from datetime import datetime
import pickle


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)


class Name(Field):  # обязательное поле с именем.
    pass
    # def init(self, name):
    #     self.name = name



class Phone(Field):     # 5. Проверку на корректность веденного номера телефона в setter для value класса Phone.

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value.isdigit() and len(value) == 10:  # обо тут краще метод isnumeric()
            self.__value = value
        else:
            print('The number is not correct! Enter a 12-digit number!')
            raise ValueError



class Birthday(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            self.__value = datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            print('Not correct format: use dd.mm.yyyy')


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name = name
        self.phones = (
            []
        )
        if phone:
            self.add_phone(phone)

        self.birthday = birthday

    def __repr__(self): # краще метод repr - тоді якщо обьект в списку чи словнику то він відобразиться
        birthday_str = datetime.strftime(self.birthday.value, '%d.%m.%Y')
        return '{:^5} | {:^5} | {:^5}'.format(self.name.value, ' '.join([ph.value for ph in self.phones]), birthday_str)

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
        if not self.birthday:
            return None
        birthday_date = self.birthday.value
        cur_date = datetime.now().date()
        birthday_date = birthday_date.replace(year=datetime.now().year)
        if cur_date > birthday_date:
            birthday_date = birthday_date.replace(year=datetime.now().year + 1)
            difference = birthday_date - cur_date
            return f'{difference.days} days'
        else:
            difference = birthday_date - cur_date
            return f'{difference.days} days'

file_name = 'data.bin'

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self, n=2):  # не розумію як його зробити!!!!
        self.n = n  # це кількість записів на сторінці
        index = 1
        print_block = '-' * 50 + '\n'  # це типу строка для розділу сторінок
        for record in self.data.values():  # ітерується по записам record
            print_block += str(record) + '\n'
            if index < n:
                index += 1
            else:  # якщо індекс більше числа н то повертаються записи (в нашому випадку два записи)
                yield print_block
                index, print_block = 1, '-' * 50 + '\n'
        yield print_block  # тут повертається все що залишилось

    def next(self, n=2):
        result = "List of all users:\n"
        print_list = self.iterator(n)
        for item in print_list:  # на кожній ітерації наш ітератор повертає по 2 записи
            result += f"{item}"  # ми іх збираємо в змінну і повертаємо
        return result

# функція пошуку
    def search_contact(self, record):
        user_request = record
        result = ""
        if len(user_request) < 3:
            return f"Please enter at least 3 characters to search for a contact!"
        for key, val in self.data.items():
            if user_request in key or user_request in val:
                result += f"{key}: {val}\n"
            return result


    def write_file(self):
        with open(file_name, "wb") as fh:
            pickle.dump(self.data, fh)


    def read_file(self):
        with open(file_name, "rb") as fh:
            self.data = pickle.load(fh)


address_book = AddressBook()

def main():
    try:
        AddressBook.read_file()
    except:
        AddressBook.write_file()
        AddressBook.read_file()



if __name__ == '__main__':
    main()
