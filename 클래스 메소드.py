class Cs:
    @staticmethod
    def static_method():
        print("Staric")
    @classmethod
    def class_method(self):
        print("Class method")
    def instance_method(self):
        print("Instance method")

i=Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()
