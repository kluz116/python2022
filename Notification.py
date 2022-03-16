from abc import ABC,abstractmethod

class Notification(ABC):


    @abstractmethod
    def notify(self, message,email):
        pass
    

class Email(Notification):
    
    def notify(self,message:str,email:str):
        print(f"Sending message {message} to email {email}")



if __name__ == '__main__':
    obj = Email('Hello Allan Musembya','allan@yahoo.com')
