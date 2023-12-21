"""
Программа шифрования дешифрования текста
методом подстановки
Вариант №5
Таблица №2 задание 4
"""

import argparse


class CypherSubstitute:
    """Содержит методы шафрования и дешифрования
    а так же вспомогательные опреации
    """

    # Алфавит подстановки
    _sub_alpha = [
        ("A", "C"),
        ("B", "D"),
        ("C", "A"),
        ("D", "B"),
        ("E", "H"),
        ("F", "I"),
        ("G", "J"),
        ("H", "E"),
        ("I", "F"),
        ("J", "G"),
        ("K", "O"),
        ("L", "P"),
        ("M", "Q"),
        ("N", "R"),
        ("O", "K"),
        ("P", "L"),
        ("Q", "M"),
        ("R", "N"),
        ("S", "U"),
        ("T", "V"),
        ("U", "W"),
        ("V", ":"),
        ("W", "S"),
        ("X", "T"),
        ("Y", "Z"),
        ("Z", " "),
        (" ", "X"),
        (".", "Y"),
        (",", ";"),
        ("!", "?"),
        (":", "-"),
        (";", "."),
        ("?", ","),
        ("-", "!"),
    ]

    @classmethod
    def _encrypt_char(cls, char: str) -> str:
        """Зашифровывает заданный символ"""

        is_lower = char.islower()

        if is_lower:
            char = char.upper()

        enc_char = next((i[1] for i in cls._sub_alpha if i[0] == char), char)

        if is_lower:
            enc_char = enc_char.lower()

        return enc_char

    @classmethod
    def _decript_char(cls, char: str) -> str:
        """Расшифровывает заданный символ"""

        is_lower = char.islower()

        if is_lower:
            char = char.upper()

        decr_char = next((i[0] for i in cls._sub_alpha if i[1] == char), char)

        if is_lower:
            decr_char = decr_char.lower()

        return decr_char

    @classmethod
    def encrypt(cls, text: str) -> str:
        """Зашифровывает указанный текст"""

        encrypted = [cls._encrypt_char(c) for c in text]
        return "".join(encrypted)

    @classmethod
    def decrypt(cls, text: str) -> str:
        """Расшифровывает заданный текст"""

        decrypted = [cls._decript_char(c) for c in text]
        return "".join(decrypted)


parser = argparse.ArgumentParser(
    prog="Кодировани и декодирование методом подстановки",
    description="По умолчанию кодирует заданный текст, для декодирования используйте ключ [-d]",
)
parser.add_argument(
    "text",
    type=str,
    help="Входной текст",
)

parser.add_argument(
    "-d",
    "--decrypt",
    action="store_true",
    default=False,
    help="Декодировать текст",
)

args = parser.parse_args()

if args.decrypt:
    print(CypherSubstitute.decrypt(args.text))
else:
    print(CypherSubstitute.encrypt(args.text))

