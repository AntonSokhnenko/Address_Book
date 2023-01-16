from collections import UserDict


class Field:  # родительским для всех полей, в нем потом реализуем логику общую для всех полей.
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


class Phone(Field):
    pass
    # def init(self, phone):
    #     self.phone = phone


class Record:  # добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name.
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = (
            []
        )  #  необязательное поле с телефоном и таких одна запись (Record) может содержать несколько.
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, phone_number_old: Phone, phone_number_new: Phone):
        if phone_number_old in self.phones:
            self.phones.remove(phone_number_old)
            self.phones.append(phone_number_new)
        else:
            print(f"In this record no phone {phone_number_old}")

    def del_phone(self, phone_number: Phone):
        self.phones.remove([phone_number])


class AddressBook(UserDict):  # наследуется от UserDict.
    def add_record(self, record: Record):
        self.data[record.name.value] = record



if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')
