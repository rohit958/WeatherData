from data.Data_class import Data_class
from data.Data_child import Data_child
data_parent_obj=Data_class()
data_parent_obj.data_hello()
data_parent_obj.parent_dir()

print("calling from child class")
data_child_obj=Data_child()
data_child_obj.Data_child_Hello()
data_child_obj.Child_dir()
data_child_obj.Data_Hello()