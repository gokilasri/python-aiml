# #object oriented programming language
# #in py everthing is an object
# x="String"
# print(type(x))
# x.lower()
# help(str)
# len(x)
# x.islower()
# x+"hello"
# if 'x' in x:
#     print(x)# finding x in the string

# #in built classes
# (13).bit_count()


#user define class
class My_class:
    x=5
my_class_obj = My_class()
print(type(my_class_obj))
my_class_obj.x

class vehicle:
    def __init__(self,vtype,vage):
        self.vtype = vtype
        self.vage = vage

    def describe_vehical(self):
        return f"the vehical is of the type{self.vtype} and is {self.vage}years old"
my_vehicle = vehicle("Bike",3)
print(my_vehicle.describe_vehical())

#inheritance
class car(vehicle):#car is child vehicle is child
    def __init__(self, v , t, brand):
        vehicle().__init__(v,t)
        self.b=brand
    def fetch_brand(self):
        return f"{self.b}"
my_car = car("car",7,"porsche")
my_car.describe_vehical()
my_car.fetch_brand()