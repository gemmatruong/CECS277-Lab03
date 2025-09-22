class Contact:
    def __init__(self, fn, ln, ph, addr, city, zip):
        self.f_name = fn
        self.l_name = ln
        self.phone = ph
        self.address = addr
        self.city = city
        self.zip = zip

    def __lt__(self, other):
        if self.l_name == other.l_name:
            return self.f_name < other.f_name
        return self.l_name < other.l_name
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}\n{self.phone}\n{self.address}\n{self.city} {self.zip}"
    
    def __repr__(self):
        return f"{self.f_name},{self.l_name},{self.phone},{self.address},{self.city},{self.zip}"
    