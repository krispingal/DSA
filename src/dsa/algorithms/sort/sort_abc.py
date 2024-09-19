from abc import ABC, abstractmethod
class Sort:
    @abstractmethod
    def run(self, A: list[int], *args, **kwargs) -> list[int]:
        pass
