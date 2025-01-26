# Lottery Simulation Task
# Create a list or tuple containing 10 numbers and 5 letters.
# Randomly generate a winning combination of 4 elements.
# Then, create a my_ticket with your chosen combination.
# Write a loop that continues generating random combinations until it matches my_ticket.
# Display how many attempts it took to get the winning combination.

import string
import random

class Lottery:
    def __init__(self, numbers=10, letters=5):
        self.numbers = numbers
        self.letters = letters
        self.my_list = []

    def random_series(self):
        """Генерирует список из случайных чисел и букв."""
        self.my_list = [random.choice(string.digits) for _ in range(self.numbers)] + \
                       [random.choice(string.ascii_lowercase) for _ in range(self.letters)]
        return self.my_list

    def my_lucky_number(self):
        """Возвращает случайную выигрышную комбинацию из 4 элементов."""
        self.lucky_numbers = random.sample(self.my_list, 4)
        return f"It is a lucky ticket -> {self.lucky_numbers}"

    def cuantity_of_tickets(self):
        """Считает количество попыток для получения выигрышного билета."""
        if not self.my_list or not self.lucky_numbers:
            raise ValueError("Сначала необходимо сгенерировать серию и выигрышный номер!")

        self.my_ticket=[]
        self.cuantity_of_tries=0
        while self.my_ticket!=self.lucky_numbers:
            self.my_ticket=random.sample(self.my_list, 4)
            self.cuantity_of_tries+=1
        return self.cuantity_of_tries

# Создаем экземпляр и тестируем
my_ekz = Lottery()
print("Generated series:", my_ekz.random_series())
print("Lucky ticket:", my_ekz.my_lucky_number())
print(f"Number of tries to win: {my_ekz.cuantity_of_tickets()}")
