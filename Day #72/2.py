

class employee:
    def __init__(self, name,id):
        self.name=name
        self.id=id

class programmer(employee):
    def __init__(self, name ,id, lang):
        super().__init__(name, id)
        self.lang=lang

rohan= employee("rohandas", "420")
pratik= employee("pratik", "4231", "Marathi")
pratik.name()
pratik.id()
pratik.lang()