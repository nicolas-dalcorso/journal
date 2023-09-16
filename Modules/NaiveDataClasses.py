# Data
class Data:
    __slots__ = 'id', 'data'
    id:int;
    data:object;
    
    def _getData(self, data) -> object or None:
        return data;
    
    def _getID(self) -> int:
        return int(self.data)
    
    def __init__(self, data) -> None:
        self.data       = self._getData(data);
        self.id         = self._getID();
        
    def __repr__(self) -> str:
        return f"Data({self.data})";
    
    def __str__(self) -> str:
        return str(self.data);