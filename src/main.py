import pandas as pd
import datetime

class Birthday:
    today = datetime.date.today()
    
    def __init__(self,name,year,month,day):
        print(f'Today: {Birthday.today.strftime("%B %d, %Y")}')
        self.name = name
        self.year = year
        self.month = month
        self.day = day
    
    def get_birthday(self):
        today = datetime.date.today()
        date_of_birth = datetime.date(self.year,self.month,self.day)
        birthday = datetime.date(today.year,self.month,self.day)
        result = (birthday - today).days
        
        if result == 0:
            return f"Dear{self.name} Happy Birthday!"
        
        if result<0:
            return f"Dear {self.name} about {365 - abs(result)} days until your birthday!"
        return f"Dear{self.name} {result} days until your birthday!"
    
    def famous_people(self,df=pd.read_csv("./src/data/famous_birthdates_final.csv")):
    
        famous_people_list = []
        date = datetime.date(self.year,self.month,self.day)
        for item in df['birthDate']:
            if str(date)[5:] == item[5:]:
                famous_people_list.extend(list(df[df['birthDate'] == item]["name"]))
    
        print("These people were born on your birthday: ")
        return famous_people_list
    
    @staticmethod
    def calculate_age_seconds(birthday):
        birthday = str(birthday)
        birthday = datetime.datetime.strptime(birthday,"%m/%d/%Y")
        result = (Time.today - birthday).total_seconds()
        return f"About {result} seconds have passed since you were born!"
    
    
    def __str__(self):
        return f'Dear {self.name}\n your birthday is in {self.year},{self.month},{self.day}'
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name},{self.year},{self.month},{self.day})'