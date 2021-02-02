class MyClass:
    __secret_value = 1

instance_of = MyClass()
#instance_of.__secret_value
print(dir(MyClass))
print(instance_of._MyClass__secret_value)