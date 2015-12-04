# coding: utf-8
# license: GPLv3

from tkinter import *
from enemies import *
from hero import *

# from tournament import *
def butt_press(event,hero,dragon,answer):
    if answer.get(): # если ничего не введено - ничего не делаем
        if dragon.check_answer(answer.get()):
            hero.attack(dragon)
            result['text'] = 'Верно!'
            result['bg'] = 'green'
        else:
            dragon.attack(hero)
            result['text'] = 'Вам нанесен удар!'
            result['bg'] = 'red'
        answer.set('') # этот ответ можно стереть

        for i in range(len(drag_health)):
            if dragon_list[i]._health<=0:
               drag_health[i]['text'] =dragon_list[i]._color+' '+dragon_list[i].name+' ПОВЕРЖЕН!'
               drag_health[i]['bg']='red'
            else:
               drag_health[i]['text'] ='здоровья: '+str(dragon_list[i]._health)
        hero_status['text'] = 'Герой - здоровья: '+str(hero._health)+'  опыта: '+str(hero._experience)

        canv.update()


def start_game1():

    global drag_health,dragon_list,canv, hero_status,result
    hero = Hero('a')
    dragon_number = 3
    dragon_list = generate_dragon_list(dragon_number)

    root = Tk()
    root.wm_title('Добро пожаловать в арифметико-ролевую игру с драконами и троллями!')
    fr = Frame(root)
    root.geometry('800x600')
    canv = Canvas(root, bg = 'white')
    canv.pack(fill=BOTH,expand=1)

    row_n=0
    drag_health=[]
    for dragon in dragon_list:
        who1 = canv.create_text(100,row_n*180+20, text = 'Вышел '+dragon._color+' '+dragon.name,font = '28')
        health1 = Label(canv,text = 'здоровья: '+str(dragon._health),font = '28')
        health1.place(x=300,y=row_n*180+10)
        drag_health.append(health1)
        quest1 = canv.create_text(200,row_n*180+50, text = 'Вопрос: '+ dragon.question(),font = '28',width = 400)
        label = canv.create_text(100,row_n*180+80, text = 'Ответ:',font = '28')
        answ1 = StringVar(value='')
        answ2=Entry(canv, textvariable=answ1)
        answ2.place(x = 100, y = row_n*180+120, width = 300, height = 30)
        btn=Button(canv,text='Ответить')
        btn.bind("<Button-1>", lambda event,h=hero, d=dragon,answer=answ1: butt_press(event,h,d,answer))
        btn.place(x = 500, y = row_n*180+120, width = 80, height = 30)

        row_n+=1

        hero_status = Label(canv,text = 'Герой      здоровья: '+str(hero._health)+'  опыта: '+str(hero._experience),font = '28')
        hero_status.place(x=100,y=560)
        hero_status['bg']='green'
        result = Label(canv,text = 'Ваш ход',font='28')
        result.place(x=600,y=560)


    mainloop()

if __name__ == '__main__':
    start_game1()
