from abc import ABC, abstractmethod

# --- Strategy Interface ---
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# --- Concrete Strategies ---
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float):
        print(f"Paid ${amount} using Credit Card: {self.card_number[-4:]}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"Paid ${amount} using PayPal account: {self.email}")

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet: str):
        self.wallet = wallet

    def pay(self, amount: float):
        print(f"Paid ${amount} using Bitcoin wallet: {self.wallet[:6]}...")

# --- Context ---
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy: PaymentStrategy = None

    def add_item(self, item: str, price: float):
        self.items.append((item, price))

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def checkout(self):
        if not self.payment_strategy:
            raise Exception("Payment method not set!")

        total = sum(price for _, price in self.items)
        print(f"Total: ${total}")
        self.payment_strategy.pay(total)

# --- Client code ---
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Book", 15)
    cart.add_item("Pen", 5)

    # Pay with Credit Card
    cart.set_payment_strategy(CreditCardPayment("1234-5678-9876-5432"))
    cart.checkout()

    # Pay with PayPal
    cart.set_payment_strategy(PayPalPayment("user@example.com"))
    cart.checkout()

    # Pay with Bitcoin
    cart.set_payment_strategy(BitcoinPayment("1XyZ123ABCwallet"))
    cart.checkout()




###########################################################
from abc import ABC, abstractmethod

# --- Strategy Interface ---
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

# --- Concrete Strategies ---
class BubbleSort(SortStrategy):
    def sort(self, data: list) -> list:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        print("Sorting with Bubble Sort...")
        return arr

class QuickSort(SortStrategy):
    def sort(self, data: list) -> list:
        print("Sorting with Quick Sort...")
        return self._quick_sort(data)

    def _quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self._quick_sort(left) + middle + self._quick_sort(right)

class MergeSort(SortStrategy):
    def sort(self, data: list) -> list:
        print("Sorting with Merge Sort...")
        return self._merge_sort(data)

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

# --- Context ---
class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort_data(self, data: list):
        return self.strategy.sort(data)

# --- Client code ---
if __name__ == "__main__":
    data = [34, 7, 23, 32, 5, 62]

    sorter = Sorter(BubbleSort())
    print(sorter.sort_data(data))  # Bubble Sort

    sorter.set_strategy(QuickSort())
    print(sorter.sort_data(data))  # Quick Sort

    sorter.set_strategy(MergeSort())
    print(sorter.sort_data(data))  # Merge Sort
