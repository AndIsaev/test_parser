from abc import ABC, abstractmethod


class Loader(ABC):

    @abstractmethod
    def request_to_resource(self):
        pass

    @abstractmethod
    def parsing_data(self):
        pass

    @abstractmethod
    def insert_data(self):
        pass
