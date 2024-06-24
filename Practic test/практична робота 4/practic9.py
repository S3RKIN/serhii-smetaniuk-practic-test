class Success:
    def handle_message(self):
        return "Виводить успіх"
class Error:
    def handle_message(self):
        return "Виводить помилку"
class Fifty(Error):
    pass
class Thirty(Error):
    pass
class TwentyFive(Fifty):
    pass
class TwentyFive(Thirty):
    pass
class Ten(Thirty):
    pass
class Fifteen(Success):
    pass
class Five(Success):
    pass
class Begin(Five):
    def process(self):
        return self.handle_message() 
class ThiFive(Five):
    def process(self):
        return self.handle_message()
begin_instance = Begin()
thifive_instance = ThiFive()
print(begin_instance.process())  
print(thifive_instance.process())  
