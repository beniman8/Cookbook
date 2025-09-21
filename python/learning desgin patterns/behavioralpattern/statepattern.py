from abc import ABC, abstractmethod

# ----- State Interface -----
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

# ----- Concrete States -----
class IdleState(State):
    def handle(self, context):
        print("Player is idle. Switching to running...")
        context.set_state(RunningState())

class RunningState(State):
    def handle(self, context):
        print("Player is running. Switching to jumping...")
        context.set_state(JumpingState())

class JumpingState(State):
    def handle(self, context):
        print("Player is jumping. Switching to idle...")
        context.set_state(IdleState())

# ----- Context -----
class PlayerContext:
    def __init__(self):
        self.state = IdleState()  # start in Idle

    def set_state(self, state: State):
        self.state = state

    def request(self):
        self.state.handle(self)

# ----- Example Usage -----
if __name__ == "__main__":
    player = PlayerContext()

    # simulate pressing a button multiple times
    for i in range(6):
        print(f"Step {i+1}:")
        player.request()
        print("-" * 20)




##################################
from abc import ABC, abstractmethod

# ----- State Interface -----
class State(ABC):
    @abstractmethod
    def insert_coin(self, context):
        pass

    @abstractmethod
    def press_button(self, context):
        pass

    @abstractmethod
    def dispense(self, context):
        pass


# ----- Concrete States -----
class NoCoinState(State):
    def insert_coin(self, context):
        print("Coin inserted.")
        context.set_state(HasCoinState())
    
    def press_button(self, context):
        print("Insert a coin first!")
    
    def dispense(self, context):
        print("No coin inserted, cannot dispense.")


class HasCoinState(State):
    def insert_coin(self, context):
        print("Coin already inserted.")
    
    def press_button(self, context):
        print("Button pressed. Dispensing item...")
        context.set_state(DispensingState())
    
    def dispense(self, context):
        print("Press button before dispensing.")


class DispensingState(State):
    def insert_coin(self, context):
        print("Please wait, dispensing in progress.")
    
    def press_button(self, context):
        print("Already dispensing an item.")
    
    def dispense(self, context):
        print("Item dispensed. Returning to idle state.")
        context.set_state(NoCoinState())


# ----- Context -----
class VendingMachine:
    def __init__(self):
        self.state = NoCoinState()  # start without a coin
    
    def set_state(self, state: State):
        self.state = state
    
    def insert_coin(self):
        self.state.insert_coin(self)
    
    def press_button(self):
        self.state.press_button(self)
    
    def dispense(self):
        self.state.dispense(self)


# ----- Example Usage -----
if __name__ == "__main__":
    machine = VendingMachine()

    # Flow 1: Normal purchase
    print("\n--- Purchase Flow ---")
    machine.insert_coin()
    machine.press_button()
    machine.dispense()

    # Flow 2: Error handling
    print("\n--- Wrong Order Flow ---")
    machine.press_button()
    machine.insert_coin()
    machine.dispense()
