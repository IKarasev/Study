"""
Программа осуществляет шифрование текста с использование
алгоритма RSA

Вариант: 12
"""

import argparse


class CypherRSA:
    def __init__(self, p=167, q=401) -> None:
        if p == 167 or self.is_prime(p):
            self._p = p
        else:
            raise ValueError(
                f"ОШИБКА: Параметр p должен быть простым числом. Заданное p={p}"
            )

        if q == 401 or self.is_prime(q):
            self._q = q
        else:
            raise ValueError(
                f"ОШИБКА: Параметр q должен быть простым числом. Заданное q={q}"
            )

        self.e = 0
        self.n = 0
        self._d = None

        self.gen_keys()

    @classmethod
    def is_prime(cls, a):
        """Проверка является ли число простым"""

        if a < 2:
            return False

        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                return False

        return True

    @classmethod
    def is_coprime(cls, a, b):
        """Проверка, являются ли два числа взаимно простыми"""

        while b:
            a, b = b, a % b

        return a == 1

    def gen_keys(self):
        """Генерация ключей"""

        n = self._p * self._q
        phi = (self._p - 1) * (self._q - 1)

        e = 2

        while e < phi:
            if self.is_coprime(e, phi):
                break
            e += 1

        self.n = n
        self.e = e

        d = 0

        while True:
            if (d * e) % phi == 1:
                break
            d += 1

        self._d = d

    def encript(self, text: str):
        """Зашифровывает заданный текст"""
        encripted = [pow(ord(c), self.e, self.n) for c in text]
        return encripted

    def decript(self, message) -> str:
        """Расшифровывает заданный шифротекст"""
        decripted = [chr(pow(c, self._d, self.n)) for c in message]
        return "".join(decripted)

    def print_pub_key(self):
        print(f"Публичный ключ: {{ n: {self.n}, e: {self.e} }}")

    def print_private_key(self):
        print(f"Закрытый ключ: {{ p:{self._p}, q:{self._q}, d:{self._d} }}")


parser = argparse.ArgumentParser(
    prog="Шифрование и дешифрование используя RSA",
)

parser.add_argument(
    "text",
    type=str,
    help="Входной текст",
)
parser.add_argument(
    "-p",
    type=int,
    action="store",
    help="Параметр p для RSA",
    default=167,
)
parser.add_argument(
    "-q",
    type=int,
    action="store",
    help="Параметр q для RSA",
    default=401,
)

args = parser.parse_args()

cypher = CypherRSA(p=args.p, q=args.q)
cypher.print_pub_key()
cypher.print_private_key()
enc = cypher.encript(args.text)
print(f"Дешифрованный текст:\n{cypher.decript(enc)}")

