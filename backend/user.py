


class User():
    def __init__(self, id: int, name: str, role: str, is_logged_in: bool):
        self.__id = id
        self.__name = name
        self.__role = role
        self.__is_logged_in = is_logged_in

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    
    @property
    def role(self):
        return self.__role
    
    @property
    def is_logged_in(self):
        return self.__is_logged_in
    
    def log_out(self):
        self.__is_logged_in = False