from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = 18005, "Петрозаводск", "ул. Правды", 40, 161
from_address = 354008, "Сочи", "ул. Виноградная", 117, 1

sending = Mailing
sending(to_address, from_address, 975, 1234567890)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)