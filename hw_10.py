from collections import UserDict


class Field:  # родительским для всех полей, в нем потом реализуем логику общую для всех полей.
    pass



class AddressBook(UserDict):    # наследуется от UserDict.
    def add_record(self, record: Record):
        self.data[record.name.value] = Record

    def contact_search(self, self.name,  ):


# Потім треба додати методи які в завданні вимагають:
# 1. AddressBook реалізує метод add_record, який додає Record у self.data.
# Записи Record у AddressBook зберігаються як значення у словнику.
# В якості ключів використовується значення Record.name.value.

class Name(Field):       # обязательное поле с именем.
    def __init__(self, name):
        self.name = name


class Phone(Field):      #  необязательное поле с телефоном и таких одна запись (Record) может содержать несколько.
    def __init__(self, phone):
        self.phone = phone


class Record:    # добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name.
    def __init__(self, name: Name, *phones):
        self.name = name
        self.phones = list(phones)

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, phone_number_old: Phone, phone_number_new: Phone):
        pass

    def del_phone(self, phone_number: Phone):
        pass


 # def replace(self, index, field_item):
 #        self.fields[index] = field_item
 #
 #    @index_error_decorator
 #    def delete(self, idx):
 #        idx = int(idx)
 #        self.fields.pop(idx)
 #
 #    @index_error_decorator
 #    def update(self, field_idx, value):
 #        field_idx = int(field_idx)
 #        field = self.fields[field_idx]
 #        field.validate(value)


# Record зберігає об'єкт Name в окремому атрибуті.
# Record зберігає список об'єктів Phone в окремому атрибуті.
# Record реалізує методи для додавання/видалення/редагування об'єктів Phone.
# зберігання об*єктів вже реалізовано(див. вище)
# треба написати методи "для додавання/видалення/редагування об'єктів Phone"
# def add_phone(self, phone_number: Phone):......
# def change_phone(self, phone_number_old: Phone, phone_number_new: Phone):
# def del_phone(self, phone_number: Phone):








# Реализованы все классы из задания.
# Записи Record в AddressBook хранятся как значения в словаре. В качестве ключей используется значение Record.name.value.
# Record хранит объект Name в отдельном атрибуте.
# Record хранит список объектов Phone в отдельном атрибуте.
# Record реализует методы для добавления/удаления/редактирования объектов Phone.
# AddressBook реализует метод add_record, который добавляет Record в self.data.



# В этой домашней работе вы должны реализовать такие классы:


# Класс AddressBook, который наследуется от UserDict, и мы потом добавим логику поиска по записям в этот класс.
# Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name.
# Класс Field, который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.
# Класс Name, обязательное поле с именем.
# Класс Phone, необязательное поле с телефоном и таких одна запись (Record) может содержать несколько.
# Критерии приёма
# Реализованы все классы из задания.
# Записи Record в AddressBook хранятся как значения в словаре. В качестве ключей используется значение Record.name.value.
# Record хранит объект Name в отдельном атрибуте.
# Record хранит список объектов Phone в отдельном атрибуте.
# Record реализует методы для добавления/удаления/редактирования объектов Phone.
# AddressBook реализует метод add_record, который добавляет Record в self.data.


# def __delete__(self):
#         self.name = input('Введите имя которе нужно удалить: ')
#         del Address.stored[self.name]

# def add(self, record):
#         self.records[self.last_record_id] = record
#         record_id = self.last_record_id
#         self.last_record_id += 1
#         return record_id


#     def replace(self, record_id, record):
#         if record_id not in self.records:
#             raise KeyError(f"Record {record_id} not found")
#         self.records[record_id] = record

#     @index_error_decorator
#     def delete(self, record_id):
#         key = int(record_id)
#         self.records.pop(key)

#     def str_search(self, search_str: str):
#         result = {}
#         for record_id, record in self.records.items():
#             if search_str in record:
#                 result[record_id] = record
#         return result

#     def multiple_search(self, **search_items):
#         result = {}
#         for record_id, record in self.records.items():
#             if record.multiple_search(**search_items):
#                 result[record_id] = record
#         return result
