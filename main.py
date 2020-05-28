from music import*
def main():
    a=[]
    file_in=open("file.txt","w")
    file_in.write("ТОВАРЫ:\n")
    file_in.write("\n")
    file_in.close()
    menu(a)
    return

def menu(a):
    global alb
    x=0
    while x!=9:
        print("Меню")
        print("0.Создать альбом(сначала!)")
        print("1.Добавить трек в альбом")
        print("2.Посмотреть данные в музыкальном списке(архиве)")
        print("3.Вывести названия всех треков архива на экран")
        print("4.Изменить название трека из архива")
        print("5.Включить трек")
        print("6.Выключить трек")
        print("7.Выключить все треки, которые играют")
        print("8.Вывести информацию об альбоме и треках, которые в нем находяться")
        print("9.Выход")
        x=int(input())
        if x==0:
            person=input("Какой исполнитель альбома?  ")
            charact=input("Введите основные характеристики альбома: ")
            copasity=input("Жанр альбома: ")
            t=""
            alb=Alb(person,charact,copasity,t)
            print(alb)
        if x == 1:
            menu1(a)
            change(a,alb)
        if x==2:
            print(a)
        

        if x==3:
            for i in range(len(a)):
                print(a[i].get_name())
        if x==4:
            n=int(input("Введите номер трека, название которого вы хотите изменить(по очередности в списке): "))
            for i in range(1, len(a)+1):
                if n==i:
                    ns=input("Введите новое название трека:  ")
                    a[i-1].set_name(ns)
            change(a,alb)
        if x==5:
            n=int(input("Введите номер трека, который вы хотите включить(по очередности в списке): "))
            for i in range(1, len(a)+1):
                if n==i:
                    a[i-1].change_work_on()
            
            change(a,alb)
        if x==6:
            n=int(input("Введите номер трека, который вы хотите выключить(по очередности в списке): "))
            for i in range(1, len(a)+1):
                if n==i:
                    a[i-1].change_work_off()
            
            change(a,alb)
        if x==7:
            print(a)
            for i in range(len(a)):
                if a[i].work==True:
                    a[i].work=False
            
            change(a,alb)
            
        
        if x==8:
            
            print(alb)

            
        
        
def change(a,alb):
    t=""
    for elem in a:
        t+=str(elem)
    trek_list=t#"список" треков
    
    alb.trek_list=trek_list
    
        
            
            
            
    return

#(self,name,charact,id_tov,seria,year,price,made="Russia", nalichie=True)
def menu1(a):
    
    print("Введите cледующие показатели")
    name=str(input("Название трека: "))
    singer=str(input("Исполнитель: "))
    long=str(input("Продолжительность: "))
    autor=str(input("Автор: "))
    year=str(input("Год: "))
    trek=Trek(name,singer,year,
                 autor,long)
    a.append(trek)
    return a
main()

    
