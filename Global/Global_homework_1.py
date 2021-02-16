# Створити ряд класів. --> вказівник на батьківський класс
# NetworkClient <-- BaseServer <-- Server <-- BuildServer
# NetworkClient <-- BaseClient <-- Client <-- BuildCLient
# Build --> BuildClient, BuildServer

# Класи  NetworkClient,  Server,  BuildClient и Build повинні мати методи ping.
# В кажному методі ping має прінтитись ім'я класу з котрого викликається метод
# і також має повертатися ім'я класу.
# Метод ping класу Build почергово викликає методи ping класів:
# BuildClient,  NetworkClient и  BuildClient і повертає результат всіх викликів.


class NetworkClient:
    def ping(self):
        print("For ", self.__class__.__name__, " parent class is ", self.__class__.__base__.__name__, sep='')


class BaseServer(NetworkClient):
    pass


class Server(BaseServer):
    def ping(self):
        print("For ", self.__class__.__name__, " parent class is ", self.__class__.__base__.__name__, sep='')


class BuildServer(Server):
    pass


class BaseClient(NetworkClient):
    pass


class Client(BaseClient):
    pass


class BuildClient(Client):
    def ping(self):
        print("For ", self.__class__.__name__, " parent class is ", self.__class__.__base__.__name__, sep='')


class Build(BuildClient, BuildServer):
    def ping(self):
        BuildClient().ping(), NetworkClient().ping(), BuildClient().ping()


Build().ping()
