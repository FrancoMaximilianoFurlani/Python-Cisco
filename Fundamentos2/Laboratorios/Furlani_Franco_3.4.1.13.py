class WeekDayError(Exception):
    pass
	

class Weeker:
    

   # week = ["Lun", "Mar", "Mie", "Jue", "Vie", "Dom"]

    def __init__(self, day):
        self.__week = ["Lun", "Mar", "Mie", "Jue", "Vie", "Dom"]
        self.__day= day
        self.__count = 0
        for i in self.__week:
            self.__count += 1
            
        
        self.__str__
        
    def __str__(self):
        
        return self.__weekday
  

    # def add_days(self, n):
          
    #       self.__aux2 = self.__aux + n
    #       self.__ndia = self.__aux2
          
    #       for x in range(self.__aux__ndia):
    #           self.__dia = self.week[self.__ndia]
            
        

    #def subtract_days(self, n):
        #
        # Escribir código aquí.
        #


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
   # weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lun')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
