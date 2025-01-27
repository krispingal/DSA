from abc import ABC, abstractmethod


class Dictionary(ABC):
    @abstractmethod
    def get(self, key, default=None):
        """Retrieve value for a given key, with optional default."""
        pass

    @abstractmethod
    def put(self, key, value):
        """Insert or update key-value pair."""
        pass

    @abstractmethod
    def delete(self, key):
        """Remove a key-value pair."""
        pass

    @abstractmethod
    def contains(self, key):
        """Check if key exists in dictionary."""
        pass
