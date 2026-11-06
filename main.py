
import random

class Encryptor:
    def __init__(self, *numbers):
        self.__numbers = numbers
        self.__result = self.__encrypt()

    def __encrypt(self):
        result = 0

        for number in self.__numbers:
            operation = random.choice(["+", "-", "*"])

            if operation == "+":
                result += number + random.randint(1, 10)
            elif operation == "-":
                result += number - random.randint(1, 10)
            else:
                result += number * random.randint(1, 10)

        return result

    def __str__(self):
        return f"Результат шифрування: {self.__result}"


cipher = Encryptor(10, 20, 30, 40)

print(cipher)
