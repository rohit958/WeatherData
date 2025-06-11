import os
from data.Data_class import Data_class

class Data_child(Data_class):
    def Data_child_Hello (self):
        print("Hello from data Child!")
    def Child_dir(self):
        print(os.getcwd())

    def Data_Hello(self):
        super().data_hello()