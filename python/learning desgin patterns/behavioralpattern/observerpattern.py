from abc import ABC, abstractmethod

# --- Observer Interface ---
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


# --- Concrete Observers ---
class EmailSubscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message: str):
        print(f"[EMAIL to {self.name}] {message}")


class SMSSubscriber(Observer):
    def __init__(self, number):
        self.number = number

    def update(self, message: str):
        print(f"[SMS to {self.number}] {message}")


# --- Subject (Publisher) ---
class NewsPublisher:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber: Observer):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Observer):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, news: str):
        for subscriber in self.subscribers:
            subscriber.update(news)


# --- Client Code ---
if __name__ == "__main__":
    # Create publisher
    publisher = NewsPublisher()

    # Create subscribers
    alice = EmailSubscriber("Alice")
    bob = SMSSubscriber("+123456789")
    carol = EmailSubscriber("Carol")

    # Add them to publisher
    publisher.add_subscriber(alice)
    publisher.add_subscriber(bob)
    publisher.add_subscriber(carol)

    # Publish news
    publisher.notify_subscribers("Breaking News: Observer Pattern in Action!")

    # Remove one and notify again
    publisher.remove_subscriber(bob)
    publisher.notify_subscribers("Update: Bob unsubscribed.")
