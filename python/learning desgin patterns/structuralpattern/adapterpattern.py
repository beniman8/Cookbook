

# Target Interface
class PaymentProcessor:
    def pay(self, amount: float):
        raise NotImplementedError("Subclasses must implement 'pay' method.")


# Adaptee (incompatible interface)
class ThirdPartyPayment:
    def make_payment(self, value: float):
        print(f"[ThirdParty] Payment of ${value} processed.")


# Adapter
class PaymentAdapter(PaymentProcessor):
    def __init__(self, third_party_payment: ThirdPartyPayment):
        self.third_party_payment = third_party_payment

    def pay(self, amount: float):
        # Translate the call from 'pay' to 'make_payment'
        print("[Adapter] Translating request...")
        self.third_party_payment.make_payment(amount)


# Client code
def process_order(payment_processor: PaymentProcessor, amount: float):
    print("Processing order...")
    payment_processor.pay(amount)
    print("Order completed.\n")


if __name__ == "__main__":
    # Using the Adapter
    third_party = ThirdPartyPayment()
    adapter = PaymentAdapter(third_party)

    # Client uses PaymentProcessor interface
    process_order(adapter, 49.99)
    process_order(adapter, 120.50)


