from address import Address
from mailing import Mailing

to_address = Address('600000', "Москва", "Ленина", "1", "99")
from_address = Address('620000', "Екатеринбург", "Ленина", '1', "100")


delivery = Mailing(to_address, from_address, 1524, '28032004')



print(f'Отправление {delivery.track} из {delivery.from_address.index}, {delivery.from_address.city}, {delivery.from_address.street}, {delivery.from_address.house} - {delivery.from_address.apartment} в {delivery.to_address.index}, {delivery.to_address.city}, {delivery.to_address.street}, {delivery.to_address.house} - {delivery.to_address.apartment}. Стоимость {delivery.cost} руб')


