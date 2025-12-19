class Lab_2:
    def Fibonacci(self,n):
        if n < 1:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0,1]
        else:
            fibonacci = [0,1]
            for i in range(2,n):
                fib_next = fibonacci[i-1]+fibonacci[i-2]
                fibonacci.append(fib_next)
            return fibonacci
    
    def BubbleSort(self,N):
        if len(N) == 0:
            return []
        for i in range(len(N)):
            for j in range(len(N)-i-1):
                if N[j]>N[j+1]:
                    N[j], N[j+1] = N[j+1], N[j]
        return N
    
    def EratosthenSieve(self,n):
        if n < 2:
            return []
        list_erotosthen = [1] * (n+1)
        list_erotosthen[0] = list_erotosthen[1] = 0
        erotosthen_exsi = []
    
        p = 2
        while p ** 2 <= n:
            if list_erotosthen[p]:
                for i in range(p ** 2, n + 1, p):
                    list_erotosthen[i] = 0
            p += 1
    
        for i in range(2,n+1):
            if list_erotosthen[i]:
                erotosthen_exsi.append(i)
        return erotosthen_exsi
