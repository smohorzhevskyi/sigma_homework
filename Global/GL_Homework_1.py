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
