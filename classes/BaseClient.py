class BaseClient:
    """
    A base class that can be used to setup receiving and driving with a 3rd party client
    """
    def __init__(self, client, name):
        self.client = client
        self.name = name