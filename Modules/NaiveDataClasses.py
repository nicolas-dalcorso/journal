# Data
class Data:
    __slots__ = 'id', 'data'
    id:int;
    data:object;
    
    def _getData(self, data) -> object or None:
        return data;
    
    def _getID(self) -> int:
        import random
        return random.randint(1,9999);
    
    def __init__(self, data) -> None:
        self.id         = self._getID();
        self.data       = self._getData(data);
        
    def __repr__(self) -> str:
        return f"Data({self.data})";
    
    def __str__(self) -> str:
        return str(self.data);