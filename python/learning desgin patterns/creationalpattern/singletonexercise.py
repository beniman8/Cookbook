#### TODO : sequence of number generator ####


class SequenceNumberGenerator:
    
    _sequence =[]
    _starting_num =50

    _num_amount=5
    
    def __init__(self):
        pass
    
    
    #Rules
    
    def add(self,number):
        self._sequence.append(self._starting_num)
        
        for num in range(self._num_amount):
            self._sequence.append(self._starting_num+number)
            self._starting_num=self._starting_num+number
        
    def subtract(self,number):
        self._sequence.append(self._starting_num)
        for num in range(self._num_amount):
            self._sequence.append(self._starting_num-number)
            self._starting_num=self._starting_num-number
            
            
    def divide(self,number):
        self._sequence.append(self._starting_num)
        for num in range(self._num_amount):
            self._sequence.append(self._starting_num/number)
            self._starting_num=self._starting_num/number
            
    def multiply(self,number):
        self._sequence.append(self._starting_num)
        for num in range(self._num_amount):
            self._sequence.append(self._starting_num*number)
            self._starting_num=self._starting_num*number
    
    def show_sequence(self):
        print(self._sequence)
        
        
generator = SequenceNumberGenerator()
generator.multiply(2)
generator.show_sequence()