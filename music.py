class Trek:
    def __init__(self,name,singer,year,
                 autor,long):
        self.__name=name
        self.__singer=singer
        self.autor=autor
        self.year=year
        self.long=long
        self.work=False
        

        
    def __str__(self):
        s="Наименование трека "+self.__name+" "+"\n"
        s+="Исполнитель: "+self.__singer+" "+"\n"
        s+="Автор: "+self.autor+"\n"
        s+="Год выпуска: "+self.year+"\n"
        s+="Продолжительность: "+self.long+"\n"
        if self.work==True:
            s += "Сейчас трек играет.\n"
        else:
            s += "Сейчас трек выключен.\n"
            
        s+="\n"
        
        return s
    def __repr__(self):
        return self.__str__()


    def set_name(self, name):#изменить название трека
          self.__name = name


    def  get_name(self):#показать назваание трека
          return self.__name
    
    
    def change_work_on(self):
        self.work = True
    def change_work_off(self):
        self.work = False


class Alb:
    def __init__(self,person,charact,copasity,trek_list):
        self.person=person
        self.charact=charact
        self.copasity=copasity
        self.trek_list=trek_list
    def __str__(self):
        s2 = "Исполнитель альбома: "+self.person+"\n"
        s2 += "Характеристика: " +self.charact+"\n"
        s2 += "Жанр: "+self.copasity+"\n"
        s2 += "Треки в альбоме:\n\n"+self.trek_list
        return s2
    def __repr__(self):
        return self.__str__()
