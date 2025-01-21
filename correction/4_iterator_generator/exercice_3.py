def premiers_generator(limite):
    def est_premier(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    n = 2
    while n < limite:
        if est_premier(n):
            yield n
        n += 1

if __name__ == "__main__":
    premiers = premiers_generator(20)
    print(list(premiers)) 

