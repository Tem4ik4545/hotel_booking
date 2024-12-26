from django.core.management.base import BaseCommand
from apps.hotels.models import Hotel
from apps.rooms.models import Room
import random

class Command(BaseCommand):
    help = "Заполняет базу данных 30 отелями и комнатами"

    HOTEL_NAMES = [
        "Отель Москва", "Гранд Отель Европа", "Отель Санкт-Петербург", "Отель Белград",
        "Премьер Отель", "Отель Сочи Парк", "Отель Уют", "Отель Арбат", "Рэдиссон Блю",
        "Отель Невский Палас", "Городская Резиденция", "Отель Крымский Бриз", "Отель Орбита",
        "Отель Пальмира", "Отель Петровский", "Плаза Гранд", "Бизнес Отель Альянс",
        "Отель Волга", "Отель Престиж", "Отель Олимпийский", "Отель Вега", "Отель Каскад",
        "Отель Централ Парк", "Ривьера Отель", "Парк Инн", "Отель Кантри Хаус", "Отель Славянский Дом",
        "Отель Династия", "Отель Тропикана", "Отель Золотой Берег"
    ]

    LOCATIONS = [
        "Москва, Россия", "Санкт-Петербург, Россия", "Казань, Россия", "Сочи, Россия",
        "Екатеринбург, Россия", "Краснодар, Россия", "Новосибирск, Россия", "Владивосток, Россия",
        "Нижний Новгород, Россия", "Самара, Россия", "Калининград, Россия", "Ялта, Россия",
        "Ростов-на-Дону, Россия", "Челябинск, Россия", "Уфа, Россия"
    ]

    ROOM_TYPES = ["single", "double", "suite", "family", "deluxe"]

    def handle(self, *args, **kwargs):
        self.stdout.write("Заполнение базы данных отелями и комнатами...")

        hotels_created = 0
        rooms_created = 0

        for i, hotel_name in enumerate(self.HOTEL_NAMES):
            location = random.choice(self.LOCATIONS)
            description = f"Прекрасный отель {hotel_name} в локации {location}. Идеально для отдыха и бизнеса."
            rating = round(random.uniform(3.0, 5.0), 1)

            # Создание отеля
            hotel = Hotel.objects.create(
                name=hotel_name,
                location=location,
                description=description,
                rating=rating
            )
            hotels_created += 1

            # Создание комнат для каждого отеля
            for room_number in range(101, random.randint(105, 110)):
                room_type = random.choice(self.ROOM_TYPES)
                price = random.randint(50, 500) * 10  # Цена в диапазоне от 500 до 5000
                is_available = random.choice([True, False])

                Room.objects.create(
                    hotel=hotel,
                    room_number=str(room_number),
                    room_type=room_type,
                    price=price,
                    is_available=is_available
                )
                rooms_created += 1

        self.stdout.write(self.style.SUCCESS(
            f"Успешно добавлено {hotels_created} отелей и {rooms_created} комнат."
        ))
