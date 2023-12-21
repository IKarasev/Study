"""
Реализация протокола Диффи-Хеллмана на эллиптических кривых

Вариант №3
"""
import argparse
import math
from typing import List


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return Point(0, 0)

    def __eq__(self, p1) -> bool:
        return self.x == p1.x and self.y == p1.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class DiffiHellman:
    def __init__(self, a=2, b=3, p=97, gx=3, gy=6) -> None:
        # Проверка, что p - простое
        if p != 97 and not self.is_prime(p):
            raise ValueError(f"p must be prime number (given p = {p})")

        # Проверка a и b - могут быть параметрами эл. кривой
        if (a != 2 or b != 3) and not self.check_ab(a, b, p):
            raise ValueError(f"a and b are incorrect (a={a}, b={b})")

        self.a = a
        self.b = b
        self.p = p

        if (gx != 3 or gy != 6) and not self.check_point_on_curve(gx, gy):
            raise ValueError(
                f"Point G(x,y) is not on set curve (a={a}, b={b}, p={p}):G(x,y)=({gx},{gy})"
            )

        self.g = Point(gx, gy)

    @classmethod
    def check_ab(cls, a: int, b: int, p: int) -> bool:
        """Проверка параметров a и b для элиптической кривой

        Args:
            a (int): параметр а
            b (int): параметр b
            p (int):

        Returns:
            (bool): True - параметры подходят, иначе False
        """
        return 4 * pow(a, 3) + (27 * b * b) % p != 0

    @classmethod
    def is_prime(cls, n: int):
        """Проверка, что число простое

        Args:
            n (int): число

        Returns:
            (bool): True если простое, иначе False
        """

        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @classmethod
    def get_bits(cls, n: int) -> List[int]:
        bits = []
        while n:
            bits.append(n & 1)
            n >>= 1
        bits.reverse()
        return bits

    def check_point_on_curve(self, x: int, y: int) -> bool:
        """Проверка, что заданные координаты лежат на заданной элептической кривой

        Args:
            x (int): Координата x
            y (int): Координата y

        Returns:
            (bool): True - координаты на кривой, иначе False
        """

        y1 = (pow(x, 3) + self.a * x + self.b) % self.p
        return y * y == y1

    def sum_points(self, p1: Point, p2: Point) -> Point:
        """Считает сумму двух точек

        Args:
            p1 (Point): точка 10
            p2 (Point): точка 2

        Returns:
            (Point): Результат суммы
        """
        if p1 == Point.zero():
            return p2

        if p2 == Point.zero():
            return p1

        if p1.x == p2.x:
            m = ((3 * p1.x * p1.x + self.a) * pow(2 * p1.y, -1, self.p)) % self.p
        else:
            m = ((p1.y - p2.y) * pow(p1.x - p2.x, -1, self.p)) % self.p

        r = Point()
        r.x = (m * m - p1.x - p2.x) % self.p
        r.y = (m * (p1.x - r.x) - p1.y) % self.p
        return r

    def multiply_point(self, n: int, p1: Point):
        """Умножение точки на число методом сложения и удвоения

        Args:
            n (int): число-множитель
            p1 (Point): точка

        Returns:
            (Point) : результат умножения
        """
        q = Point.zero()

        for bit in self.get_bits(n):
            if bit == 1:
                q = self.sum_points(q, p1)
            p1 = self.sum_points(p1, p1)

        return q

    def gen_pub_key(self, secret: int):
        """Генерация серкретного ключа

        Args:
            secret (int): секрет

        Returns:
            (Point): публичный ключ
        """
        return self.multiply_point(secret, self.g)

    def gen_priv_key(self, secret: int, pub_key: Point):
        """Генерация закрытого ключа

        Args:
            secret (int):
            pub_key (point): публичный ключ

        Returns:
            (Point): закрытый ключ
        """
        return self.multiply_point(secret, pub_key)


parser = argparse.ArgumentParser()

parser.add_argument(
    "-k1",
    type=int,
    default=6,
    action="store",
    help="Секретный ключ 1",
)

parser.add_argument(
    "-k2",
    type=int,
    default=10,
    action="store",
    help="Секретный ключ 2",
)

parser.add_argument(
    "-a",
    type=int,
    default=2,
    action="store",
    help="parameter a for DH",
)

parser.add_argument(
    "-b",
    type=int,
    default=3,
    action="store",
    help="parameter b for DH",
)

parser.add_argument(
    "-p",
    type=int,
    default=97,
    action="store",
    help="parameter p for DH",
)

parser.add_argument(
    "-gx",
    type=int,
    default=3,
    action="store",
    help="X coordinate for G point",
)


parser.add_argument(
    "-gy",
    type=int,
    default=6,
    action="store",
    help="Y coordinate for G point",
)

args = parser.parse_args()

dh = DiffiHellman(args.a,args.b,args.p,args.gx,args.gy)

pubkey_1 = dh.gen_pub_key(args.k1)
pubkey_2 = dh.gen_pub_key(args.k2)

privkey_1 = dh.gen_priv_key(args.k1, pubkey_2)
privkey_2 = dh.gen_priv_key(args.k2, pubkey_1)

print(f"Пара ключей для секрета 1:\n\tпубличный: {pubkey_1}\n\tприватный: {privkey_1}")
print(f"Пара ключей для секрета 2:\n\tпубличный: {pubkey_2}\n\tприватный: {privkey_2}")

print(f"\nПриватные ключи равны: {privkey_1 == privkey_2}")



