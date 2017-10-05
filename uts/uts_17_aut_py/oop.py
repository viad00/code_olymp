human_list = []

class Human:
   def __init__(self):
       self.__names = []
       self.say = ''
       human_list.append(self)

   @property
   def name(self):
       return self.__names

   @name.setter
   def name(self, mas):
       for k in mas:
           self.__names.append(k.lower())


sam = Human
sam.name = 'KEK'
sam.say = 'MEME'
print(sam.say)
