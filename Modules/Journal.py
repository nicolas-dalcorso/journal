from NaiveDataClasses import Data
import json

class Manager:
    __slots__ = 'name', 'size', 'objects', 'content';
    
    def __init__(self, name:str="root") -> None:
        self.name = name;
        self.size = 0;
        self.objects = [];
        self.content = self._getContent();
        
    def _getContent(self) -> dict:
        return {
                'activities' : 0
            };
        
    
    def __activity(self) -> int:
        self.content['activities'] += 1;
        return self.content['activities'];
    
    def _id(self,qtype:type)->int:
        if(qtype==Activity):
            return self.__activity();
        else:
            return 0;
    
    def request(self, query:str, qtype:type):
        if(query=='id'):
            return self._id(qtype);
        else:
            return;
        
    def __repr__(self) -> str:
        return f"Manager({self.name},{self.size})";

class FileBasedManager(Manager):
    def _getContent(self) -> dict:
        return super()._getContent();
    
    def _getContent(self) -> dict:
        try:
            with open(self.filename, "r") as f:
                self.content = json.load(f);
        except FileNotFoundError:
            self.content = super()._getContent();
            f = open(self.filename, "w");
            json.dump(self.content, f);
            f.close();
        finally:
            return self.content
    
    def __init__(self, name: str = "root", filepath:str=r"./") -> None:
        self.filename   = str(filepath);
        super().__init__(name);
        self.content    = self._getContent();
        
    def _id(self, qtype: type) -> int:
        if(qtype==Activity):
            return self.__activity();
        else:
            return None;
        
    def __activity(self) -> int:
        self.content['activities'] += 1;
        return self.content['activities'];
        

s
class Activity(Data):
    __slots__ = 'id', 'time_0', 'time_1', 'name', 'tags', 'description', 'commentaries', 'Manager'
    
    def _getID(self) -> int:
        return self.Manager.request('id', type(self));
    
    def _getData(self, data) -> object or None:
        if(len(data) != 7):
            return None;
        else:
            id_activity, time_0, time_1, name, tags, description, commentaries = data;
            return {
                'id_activity': id_activity,
                'time_0' : time_0,
                'time_1' : time_1,
                'name' : name,
                'tags' : tags,
                'description' : description,
                'commentaries' : commentaries
            };
        
    def __init__(self, data:tuple, Manager: Manager) -> None:
        self.Manager = Manager;
        super().__init__(data);
        
    def __repr__(self) -> str:
        return super().__repr__();
        
if __name__ == '__main__':
    man = FileBasedManager(filepath="root");
    act = Activity((1,2,3,4,5,6,7), man);
    print(act.id)
    act = Activity((1,2,3,4,5,6,7), man);
    print(act.id);
    act = Activity((1,2,3,4,5,6,7), man);
    print(act.id);
    