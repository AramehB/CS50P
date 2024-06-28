class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Error: Jar capacity cannot be negative.")        #when program comes here, we will raise error if capacity is neg, so user will go back to the try function below to fix
        self.capacity = capacity

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

def main():
    ...


if __name__ == "__main__":
    main()
