import random
def shuffle():
    limit=5000
    dic_player_total_marks = {'HUSSAIN': 0, 'AHMED': 0, 'DAUD': 0, 'ABDULLAH': 0}
    maximum = max(dic_player_total_marks.values())
    while(maximum<limit):
        l_player=[]
        l_marks=[]
        players=['HUSSAIN','AHMED','DAUD','ABDULLAH']
        higher_marks=[1000,500]
        lower_marks=[300,0]
        dic_data={}
        for i in range(2):
            player=random.choice(players)
            l_player.append(player)
            mark=random.choice(higher_marks)
            l_marks.append(mark)
            players.remove(player)
            higher_marks.remove(mark)
            upper_final = list(zip(l_player, l_marks))
            dic_data[player]= mark
            dic_player_total_marks[player] += mark
            print(f'{upper_final[i][0]} got {upper_final[i][1]}')

        for i in range(2):
            player=random.choice(players)
            l_player.append(player)
            mark=random.choice(lower_marks)
            l_marks.append(mark)
            players.remove(player)
            lower_marks.remove(mark)
            lower_final = list(zip(l_player, l_marks))
            dic_data[player]= mark
            dic_player_total_marks[player]+=mark

        wazer= [i[0] for i in upper_final if i[1]==500]  #The player  who got 500 in uper_class

        guess=input(f"{wazer[0]} wazer tell who is chor {lower_final[2][0]} or {lower_final[3][0]}:").upper()

        chor=[i[0] for i in lower_final if i[1]==0] #The player who got 0 marks in lower_level

        if guess in l_player:
            if guess!=chor[0].upper():
                print(f"Wrong guess {chor[0]} was a chor ")
                for key in dic_data.keys():
                    if dic_data[key]==500:
                        dic_data[key]=0
                        dic_data[chor[0]]=500
                        dic_player_total_marks[key] -= 500
                        dic_player_total_marks[chor[0]] += 500
                        break

            else:
                print(f"Right guess {chor[0]} was a chor ")
        else:
            print(f"{guess} not exists in players")

        for player,marks in dic_data.items():
            print(f'{player} got {marks}')

        print(dic_player_total_marks)
        maximum = max(dic_player_total_marks.values())
        ask=input("Do you want to continue or exit (C/E):").upper()
        if ask=="E":
            break
    else:
        count=0
        for key,value in dic_player_total_marks.items():
            if value==maximum:
                k=key
                count+=1
        if count==1:
            print("\t\t\t\tGAME OVER!")
            print("__________________________________________________________")
            print(f'CONGRATULATIONS {k} YOU WON THE GAME WITH {value} POINTS')
            print("__________________________________________________________")
        else:
            print("Tie between players")
shuffle()

