# -*- coding: utf-8 -*-
# 负责维护一个类变量中所有联系人的列表，初始化姓名和地址
# 第三章案例学习


class ContactList(list):
    def search(self, name):
        """返回所有包含名称中包含搜索值的联系人"""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Supplier(Contact):
    def order(self, order):
        print("if this were a real system we would send {} order to {}".format(order, self.name))


class Friend(Contact, AddressHolder):
    def __init__(self, phone="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone


class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)


class EmailableContact(Contact, MailSender):
    pass



