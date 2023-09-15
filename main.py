import Modules.NaiveDataStructures as datas
if __name__ == '__main__':
    lista = datas.LinkedList();
    
    for i in range(1009):
        lista.insert(str(i));
        
    for n in lista:
        print(n.data);