class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a, self.b = 0, 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
            
        if self.current == 0:
            self.current += 1
            return self.a
            
        if self.current == 1:
            self.current += 1
            return self.b
            
        result = self.a + self.b
        self.a, self.b = self.b, result
        self.current += 1
        return result

if __name__ == "__main__":
    fib = FibonacciIterator(8)
    print(list(fib)) 
