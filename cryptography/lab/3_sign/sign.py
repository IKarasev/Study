"""
Реализация ЭЦП в соответсвии с ЭЦП ГОСТ Р34.10-94
"""

import argparse
import random
from typing import Tuple


class DigitalSigGost:
    """Предоставляет методы для генерации подписи и ее проверки
    по аналогии с ЭЦП ГОСТ Р34.10-94
    """

    def __init__(self, private=8) -> None:
        # Для ускорения работы воспользуемся небольшими p,q,a
        self.p = 23
        self.q = 11
        self.a = 6

        if private < 2 or private > self.q - 1:
            raise ValueError(
                f"Приватный ключ x={private} должен быть в диапазоне (0, {self.q})"
            )

        self._x = private
        self.y = pow(self.a, private, self.p)

    def get_hash(self, message: str) -> int:
        """Расчщитывает хэш-код (контрольную сумму) для заданной строки
        Используется метод подсчета 1 в битовом
        представлении символов исходного текста
        """
        bites = "".join([f"{ord(c):b}" for c in message])
        ones = bites.count("1")
        h = 1 if ones % self.q == 0 else ones
        return h

    def create_sign(self, message: str) -> Tuple[int, int]:
        """Генерирует электронно-цифровую подпись
        для заданного текста
        """
        h = self.get_hash(message)
        k = 0
        r1 = 0
        s = 0
        while r1 == 0 or s == 0:
            k = random.randrange(1, self.q + 1)
            r1 = pow(self.a, k, self.p) % self.q
            s = (self._x * r1 + k * h) % self.q
        return (r1, s)

    def check_sign(self, message: str, sign: Tuple[int, int]) -> bool:
        """Проверка цифровой подписи"""
        r1, s = sign

        # Проверка параметров подписи
        if r1 <= 0 or r1 >= self.q or s <= 0 or s >= self.q:
            return False

        # Проверка подленности подписи
        h = self.get_hash(message)
        v = pow(h, self.q - 2, self.q)
        z1 = s * v % self.q
        z2 = (self.q - r1) * v % self.q
        u = (pow(self.a, z1) * pow(self.y, z2) % self.p) % self.q

        return u == r1


parser = argparse.ArgumentParser(
    prog="Создание подписи и ее проверка",
)

parser.add_argument(
    "text",
    type=str,
    help="Текст на подпись",
)

parser.add_argument(
    "-s",
    "--secret",
    type=int,
    action="store",
    default=8,
    help="Секретный ключ",
)

args = parser.parse_args()

d = DigitalSigGost(args.secret)
ds = d.create_sign(args.text)

print("Подпись: ", ds)

print("Проверка подписи")
print(f"\tПодпись верна: {d.check_sign(args.text, ds)}")

ds = (ds[0] * 2, ds[1])
print(f"Внесение изменений в подпись, новая подпись: {ds}")
inhex = "".join([hex(i) for i in ds])
print(inhex)
print("Проверка подписи")
print(f"\tПодпись верна: {d.check_sign(args.text, ds)}")

