from smartphone import Smartphone

phone1 = Smartphone('nokia', '3110', '+79122222222')
phone2 = Smartphone('sumsung', 's10', '+79122225252')
phone3 = Smartphone('honor', 'g7', '+7912220001')
phone4 = Smartphone('realme', 'gt10', '+79222225252')
phone5 = Smartphone('xiaomi', 's7', '+79522225252')

catalog = [phone1, phone2, phone3, phone4]

for phone in catalog:
    print(f'Марка телефона: {phone.brand}, модель: {phone.model}, номер телефона: {phone.phone_number}')