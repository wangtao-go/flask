from model import BaseModel

class BankModel(BaseModel):
    def find_all(self):
        #super是指的父类，此处为父类的重写
        return super().find_all('bank')



if __name__ == '__main__':
    bank=BankModel()
    print(bank.find_all())




