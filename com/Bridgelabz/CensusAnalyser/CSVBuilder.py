from abc import ABC, abstractmethod


class CSVBuilder(ABC):
    @abstractmethod
    def record_counter(self):
        pass
