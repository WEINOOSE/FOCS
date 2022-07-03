import pandas as pd
import database as f1
from random import randint, uniform, choice
import numpy as np
import shutil
from os import remove

print()

def SESSION(tracknamespace):

    driver = pd.DataFrame(pd.read_excel(f'drivers.xlsx'))
    car = pd.DataFrame(pd.read_excel(f'manufacturers.xlsx'))

    # # #

    driver = driver.drop(axis=1, columns=['LEAGUE'])
    driver = driver.drop(axis=1, columns=['OVERALL'])
    driver['STAR'] = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    driver['HEALTH'] = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]

    # # #

    car = car.drop(axis=1, columns=['CLASS'])
    car['LOSS'] = [0,0,0,0,0,0,0,0,0,0]
    car = car.sort_values('OVERALL',ascending=False)

    # # #

    for i in f1.circuits:
        if i.country == str(tracknamespace):
            track = i

    match_table_in_order,gain_times_in_order = [], []
    formula = [track.performance,track.speed,track.wing,track.chassis]
    formula_f = []

    c = 0
    while c < 10:
        formula_f.append(formula)
        c += 1
    
    """
    for Example for car.values[:,2:6]:
    i0 > Performance Section > Top Speed = 1, Acceleration = -1
    i1 > Straight = -1, Cornering = 1
    i2 > Non-Downforce = -1, Downforce = 1
    i3 > Agile Chassis = -1, Bulky Chassis = 1
    """
    overall_list = list(car['OVERALL'])
    minimum_overall = min(overall_list)

    weather = 0
    rain_odd = randint(0,100)
    
    for i,j in zip(car.values[:,2:6].tolist(),formula_f):
        total_point = 0
        for wo,wu in zip(i,j):
            if int(wo) == int(wu):
                total_point += 4
            else:
                total_point += 1
        match_table_in_order.append(total_point)
    
    for i,j in zip(match_table_in_order,car.values[:,7:8].tolist()):
        matching_rating = float(i)
        car_rating = float(j[0])
        coef = abs(minimum_overall - car_rating)
        engine_scene = 0
        result = ((((((((matching_rating**3) + (car_rating**5) + ((coef*2)**5))*5)/10**6)) - 0)/15) + engine_scene)*10
        gain_times_in_order.append(float(result))

    car['LOSS'] = gain_times_in_order

    data = pd.merge(driver, car, how="outer").sort_values('LOSS',ascending=False)
    templist = data['LOSS'].tolist()
    templist.reverse()
    data['LOSS']= templist
    data = data.sort_values('TITLE')
    data = data.sort_values('LOSS')

    # CAR ORDER HAS FINISHED
    # LET'S SEE WHAT DRIVERS CAN DO

    slick,green,blue = f1.s.initial,f1.i.initial,f1.w.initial
    qualifying_results,interval,status = [],[],[]
    perfect_time = track.time

    def QUALI(status_string,cofd,cofw,supporting_divider,supreme_divider,weather_integer,tyre):
        pace,wet =i[0],i[2]
        pace_int = randint(0,(200-(pace*2))**2)
        wet_int = randint(0,(100-(wet))**2)
        status.append(f'QUALIFYING | {track.title} - {track.country} | Track: {status_string}')
        pace2 = (((pace_int*cofd)+(wet_int*cofw))/supporting_divider)/supreme_divider
        laps, quali_laps, car_status = [], 0, 100
        f1.weather = weather_integer
        while (quali_laps < randint(2,5)) and (car_status == 100):
            chance, poly = uniform(0,(i[5]/12.5)),uniform(-(i[3]/8),0)
            if (i[6]/33)**3 > randint(0,1000):
                # VEHICLE FAILURE
                car_status = 0
                print(f'{f[1]} has faced with an {choice(f1.dnf)} issue, he is out.')
            elif i[5]**3 > randint(0,1250):
                # PERSONAL FAILURE
                if 25 > randint(0,750):
                    quali_laps += 1
                else:
                    car_status = 0
                    print(f'{f[1]} has crashed the car during the qualifying session, he is out.')
            else:
                if tyre == slick:
                    laps.append((pace2*0.2)+(perfect_time*1)+(tyre*1)+(z*2)+(chance*0.9)+(poly*0.9)-(2.5)+(track.time/45)+f1.plus_time)
                else:
                    forreal = ((100-wet)/10)
                    laps.append((pace2*0.2)+(perfect_time*1)+(tyre*1)+(z*2)+(chance*0.9)+(poly*0.9)-(5.0)+forreal+(track.time/45)+f1.plus_time)
                quali_laps += 1
        
        if (car_status == 0) and (len(laps) == 0):
            qualifying_results.append(99500)
        else:
            qualifying_results.append(min(laps))

    for i,z,f in zip(data.values[:,4:14],templist,data.values):
        if rain_odd < int(track.rain_odd):
            if rain_odd < 50:
                QUALI('Dump',1.2,0.8,2,500,1,green)
            else:
                QUALI('Wet',1,1,2,375,1,blue)
        else:
            QUALI('Dry',2,0,2,500,0,slick)

    data['QUALIFYING'] = qualifying_results
    data = data.sort_values('QUALIFYING',ascending=True)

    pole_time = min(qualifying_results)
    for i in list(data['QUALIFYING']):
        diff = i-pole_time
        if diff == 0:
            mini = pole_time/60
            sec = (mini-int(mini))*60
            actual_time = f'{str(int(mini))}:{round(sec,3)}' 
            interval.append(actual_time)
        else:
            interval.append(f'+{round(diff,3)}')

    interval_v2 = [interval[0]]
    for puq in interval[1:len(interval)]:
        puqw = int(puq[1:len(puq)][0])
        if puqw >= 9:
            interval_v2.append('DNQ')
        else:
            interval_v2.append(puq)
    data['QUALIFYING'] = interval_v2
    data['GRID'] = list(range(1,21))
    data_q = data[['GRID','TITLE','DRIVER','QUALIFYING']].groupby(['GRID']).min()
    print(f'\n{status[0]}\n\n{data_q}\n')
    data['QUALIFYING'] = interval

    classic_start,race_interval,race_interval_begin = list(np.arange(0,6.0,0.3)), [],[]
    for i,z in zip(classic_start,data.values[:,4:14]):
        if weather == 1:    
            start_luck0 = (randint(100-int(z[9]),int(z[9]))/20)
            start_luck1 = (randint(100-int(z[2]),int(z[2]))/20)
            start_luck = (start_luck0*0.3)+(start_luck1*1.7)*f1.start
        else:
            start_luck = (randint(100-z[9],z[9])/50)*f1.start
        race_interval.append(round(i,3)+start_luck)
    begin = min(race_interval)
    for l in race_interval:
        lax = l-begin
        race_interval_begin.append(lax)

    data['INTERVAL'] = race_interval_begin

    fx,nx,mx = list(data['QUALIFYING']),[],[]
    fx[0] = 0.00000
    temporary = data
    temporary['QUALIFYING'] = fx
    
    for q,z in zip(list(temporary['DRIVER']),list(data.sort_values('INTERVAL')['DRIVER'])):
        if q == z:
            pass
        else:
            nx.extend([q,z])

    for i in nx:
        if i in mx:
            pass
        else:
            mx.append(i)

    i = 0
    dnf2 = []
    collided, dnfed, forced, scp, action = [], [], [], [], []
    data = data.sort_values('INTERVAL',ascending=True)
    data['QUALIFYING'] = interval_v2
    while i<len(mx):
        dlist = list(data['DRIVER'])
        try:
            di = dlist.index(mx[i+1])
            ai = dlist.index(mx[i])
            def1 = int(pd.DataFrame(data.loc[data['DRIVER'] == mx[i+1]]['DEFENCE'])['DEFENCE'])
            agg1 = int(pd.DataFrame(data.loc[data['DRIVER'] == mx[i+1]]['AGRESSION'])['AGRESSION'])
            att2 = int(pd.DataFrame(data.loc[data['DRIVER'] == mx[i]]['ATTACK'])['ATTACK'])
            agg2 = int(pd.DataFrame(data.loc[data['DRIVER'] == mx[i]]['AGRESSION'])['AGRESSION'])
            defender = (((((def1)/100) + (agg1)*7)/5) + (randint(0,10)/1))
            attacker = (((((att2)/100) + (agg2)*7)/5) + (randint(0,10)/(f1.collision+0.5)))
            if attacker > defender:
                z1 = randint(0,100)
                z3 = randint(0,100)
                if attacker - 1.3 > defender:
                    if z1>=65:
                        print(f'LAP 0 - {mx[i+1]} and {mx[i]} collided with each other, {mx[i+1]} DNF.')
                        dnf2.append(mx[i+1])
                        scp.append(1)
                        dnfed.append([randint(3,7),ai])
                        dnfed.append([999995,di])
                        action.append(1)
                    elif 65>z1>35:
                        print(f'LAP 0 - {mx[i+1]} and {mx[i]} collided with each other, {mx[i]} DNF.')
                        dnf2.append(mx[i])
                        scp.append(1)
                        dnfed.append([randint(3,7),di])
                        dnfed.append([999999,ai])
                        action.append(1)
                    else:
                        print(f'LAP 0 - {mx[i+1]} and {mx[i]} collided with each other, both DNF.')
                        dnf2.append(mx[i])
                        dnf2.append(mx[i+1])
                        scp.append(1)
                        dnfed.append([999995,di])
                        dnfed.append([999999,ai])
                        action.append(1)
                elif attacker - 0.7 > defender:
                    print(f'LAP 0 - {mx[i+1]} and {mx[i]} collided with each other. {mx[i+1]} has took damage and pitted under the safety car.')
                    scp.append(1)
                    collided.append([5.5,di])
                    action.append(0)
                else:
                    if z3>25:
                        print(f'LAP 0 - {mx[i]} forced {mx[i+1]} off the track.')
                        scp.append(0)
                        forced.append([randint(3,11),di])
                        action.append(2)
                    else:
                        print(f'LAP 0 - {mx[i+1]} forced {mx[i]} off the track.')
                        scp.append(0)
                        forced.append([randint(3,11),ai])
                        action.append(2)
            else:
                data = data.sort_values('INTERVAL')
                scp.append(0)
                action.append(3)
            i +=2
        except:
            i +=2

    scl = list(np.arange(0,4.0,0.2))
    ilist = list(data['INTERVAL'])
    if sum(scp)>=1:
        ilist = scl
        for T in action: 
            if T==0:
                for i in collided:
                    ilist[i[1]] += i[0]
            elif T==1:
                for i in dnfed:
                    ilist[i[1]] = i[0]
                ilist = scl
            elif T==2:
                for i in forced:
                    ilist[i[1]] += i[0]
            else:
                pass
    else:
        for Y in action: 
            if  Y == 2:
                for i in forced:
                    ilist[i[1]] += i[0]
            else:
                pass
    zorro = []
    for i in ilist:
        zorro.append(round(i,2))
    data['INTERVAL'] = zorro
    data = data.sort_values('INTERVAL')
    data['LEAD'] = list(range(1,21))
    data.to_csv('temp.csv',header=True)

    # FIRST LAP HAS FINISHED
    # LET'S SEE THE REST OF THE RACE

    def RACE():
        confirm_df = pd.DataFrame()
        overtook_test = 0
        defence_test = 0
        weather, race_conditions, dnf0 = f1.weather, [], []
        if weather == 1: 
            if randint(0,100) > 75:
                weather = 1
                tyre_selection = f1.w
                race_conditions.append(f'{track.lap} LAPS RACE | {track.title} - {track.country} | Track: Wet')
            else:
                weather = 1
                tyre_selection = f1.i
                race_conditions.append(f'{track.lap} LAPS RACE | {track.title} - {track.country} | Track: Dump')
        else:
            weather = 0
            tyre_selection = f1.s
            race_conditions.append(f'{track.lap} LAPS RACE | {track.title} - {track.country} | Track: Dry')
        
        data = pd.DataFrame(pd.read_csv('temp.csv'))
        data['PIT'] = list(np.zeros(20,dtype=int))

        data.sort_values('INTERVAL',ascending=True)

        lap_number,sc_alert = 1,0
        f1tv = data.values[0:]
        tires = 1

        # PREVENT THE DUPLICATE INCIDENTS
        the_name = []
        the_laptime = []
        the_lap = []
        form_of_drivers_today = {}
        klas_of_drivers_today = {}
        lastik_dict = {}
        pit_dict = {}
        s_dict = {}

        daquan = list(data['DRIVER'])

        for i,z in zip(list(data['DRIVER']),f1tv):
            flick = (z[8]*33)+2
            form_of_drivers_today[i] = uniform(0,(flick/165))

        for i,z in zip(list(data['DRIVER']),f1tv):
            klas_of_drivers_today[i] = z[6]/165

        for i,z in zip(list(data['DRIVER']),f1tv):
            lastik_dict[i] = 100

        for i,z in zip(list(data['DRIVER']),f1tv):
            pit_dict[i] = 0

        for i,z in zip(list(data['DRIVER']),f1tv):
            s_dict[i] = 0

        crash_alert = 0
        while lap_number < track.lap:
            new_interval = []
            dnf_temp = []
            for driver in f1tv:
                outeffects = []
                if (weather == 1) or (f1.weather == 1):
                    racecraft = driver[7]
                else:
                    racecraft = driver[6]
                name = driver[2]
                aggression = driver[9]
                fail_odd = driver[10]
                tyre_usage_skill = driver[13]
                fuel_left = tyre_selection.fuel(110,track.lap,lap_number)
                loss_of_the_car = driver[28] + ((uniform(0,((100-driver[7])/2)))/100)
                live_interval = driver[31]
                car_stamina = driver[27]
                DNF_PROB = uniform(0,750*4)

                lastik_dict[name] = driver[16] - ((tyre_selection.tyre(driver[16],track.lap,tires,track.deg))*1.2) + (uniform(tyre_usage_skill*1.5,tyre_usage_skill*2.5))
                
                # VEHICLE FAILURE
                current_status = abs((100 - ((car_stamina**7)/(50**7)))/25)
                if (current_status > DNF_PROB) and (name not in dnf0) and (name not in dnf2):
                    if (track.sc/9.19) >= randint(0,100):
                        print(f'LAP {lap_number} - {name} has faced with an {choice(f1.dnf)} issue, he is out. Safety car has deployed.')
                        sc_alert = 1
                        dnf0.append(name)
                        outeffects.append(99500)
                    else:
                        print(f'LAP {lap_number} - {name} has faced with an {choice(f1.dnf)} issue, he is out.')
                        dnf0.append(name)
                        outeffects.append(99500)
                
                # PERSONAL FAILURE
                current_status_failure = abs((100 - ((((6-fail_odd)*20)**7)/(50**7)))/25)**1.25

                if (current_status_failure > DNF_PROB + (DNF_PROB/50)) and (name not in dnf0) and (name not in dnf2):
                    if (track.sc/9.19) + 10 >= randint(0,100):
                        print(f'LAP {lap_number} - {name} has {choice(f1.barrel)}, he is out. Safety car has deployed.')
                        dnf0.append(name)
                        outeffects.append(99500)
                        sc_alert = 1
                    else:
                        print(f'LAP {lap_number} - {name} has {choice(f1.barrel)}, he is out.')
                        dnf0.append(name)
                        outeffects.append(99500)

                if (current_status_failure > DNF_PROB/2.5) and (name not in dnf0) and (name not in dnf2):
                    meingotmusdassein = uniform(0,10)
                    outeffects.append(meingotmusdassein)
                    if meingotmusdassein > 8.5:
                        print(f'LAP {lap_number} - {name} has spun and damaged the front wing. Safety car has deployed.')
                        outeffects.append(35)
                        dnf_temp.append(name)
                        sc_alert = 1

                # PIT-STOP & PERSONAL FAILURE
                if (lastik_dict[name] < ((((90-(aggression*3)))/(2))+5)):
                    if randint((lastik_dict[name] < ((((90-(aggression*3)))/(2))+5)),100) > 60:
                        tires = 0
                        lastik_dict[name] = 100
                        if weather == 1:
                            tyre_selection = f1.i
                        else:
                            tyre_selection = f1.h

            
                # RACING CODES HERE
                if (tires == 1) and (lap_number != 1):
                    crew = round(uniform(2,5),2)
                    total_pit = 20 + crew
                    pit_dict[name] += 1
                else:
                    total_pit, crew = 0, 0
                    pit_dict[name] += 0

                # # # LAPTIMES ARE ON!

                car_default = f1.plus_time + (loss_of_the_car*2) + track.time + sum(outeffects)
                pit_result = total_pit

                racecraft_indv = (((racecraft**3)/10**6)/2) + uniform(0,0.150)
                
                klas = klas_of_drivers_today[name]*0.35
                todays_form = form_of_drivers_today[name]*0.65
                weather_effect = (weather*(((driver[22]/100)**2)-1))
                
                if tyre_selection.title == 'Intermediate':
                    tttire = tyre_selection.laptime(fuel_left,track.lap,lap_number,lastik_dict[name]) - (((racecraft)/100)*1.5)
                elif tyre_selection.title == 'Wet':
                    tttire = tyre_selection.laptime(fuel_left,track.lap,lap_number,lastik_dict[name]) - (((racecraft)/100)*2)
                else:
                    tttire = tyre_selection.laptime(fuel_left,track.lap,lap_number,lastik_dict[name])
                
                if name in (dnf0 or dnf2):
                    laptime = 99999
                else:
                    laptime = (car_default) + (pit_result) - (racecraft_indv) + (klas) + (todays_form) + (tttire) + (s_dict[name]) - (weather_effect)

                # TOTALIZE AND TO PREVENT DNF'ED PLAYER TO PERFORM AN FASTEST LAP

                if name in dnf_temp:
                    laptime += 50
                    tires = 0
                    if weather == 0:
                        tyre_selection = f1.h
                    else:
                        tyre_selection == f1.i
                    lastik_dict[name] = 100
                    pit_dict[name] += 1

                if (sc_alert == 1 or crash_alert == 1) and (tires >= 10):
                        laptime += 10
                        tires = 0
                        if weather == 0:
                            tyre_selection = f1.h
                        else:
                            tyre_selection == f1.i
                        lastik_dict[name] = 100
                        pit_dict[name] += 1
                else:
                    pass

                new_interval.append(float(laptime) + float(live_interval))
                
                # FOR THE FL'S SAKE
                the_name.append(name)
                if name in dnf2:
                    the_laptime.append(99999)
                else:
                    the_laptime.append(float(laptime))
                the_lap.append(lap_number)


            # SAVING RESULTS
            lap_number += 1
            tires += 1

            data['INTERVAL'] = new_interval

            if (sc_alert == 0 and crash_alert == 0):
                data['INTERVAL'] = new_interval
            else:
                sc_interval_totalized = []
                leader, counterS = min(new_interval), 0
                for i in list(data['INTERVAL']):
                    if i > 90000:
                        sc_interval_totalized.append(99999)
                    else:
                        sc_interval_totalized.append(leader+(counterS*0.2))
                        counterS += 1
                data['INTERVAL'] = sc_interval_totalized
            
            f1.last_df_df = data
            data = data.sort_values('INTERVAL',ascending=True)

            # # # PRINT LAP BY LAP
            """
            squa = []
            furro = data
            for i in list(furro['INTERVAL']):
                squa.append(float(round(i,3)))
            furro['INTERVAL'] = squa
            furro = furro.sort_values('INTERVAL',ascending=True)
            print(f'LAP {lap_number}\n{furro[["LEAD","TITLE","DRIVER","INTERVAL","GRID","PIT"]]}')
            """

            # THE MX ALGORITHM FIRST SEQUEL
            
            mx = []
            fx,qx,nx = list(f1.last_df_df['DRIVER']),list(data['DRIVER']),[]
            
            if lap_number > 2:
                
                for q,z in zip(fx,qx):
                    if q == z:
                        pass
                    else:
                        nx.extend([q,z])

                for i in nx:
                    if i in mx:
                        pass
                    else:
                        mx.append(i)

                    for i in nx:
                        if i in mx:
                            pass
                        else:
                            mx.append(i)

            crash_alert = 0
            s_dict.clear()
            
            for i in list(data['DRIVER']):
                s_dict[i] = 0

            igo = 0
            data = data.sort_values('INTERVAL',ascending=True)
            while igo+1 < len(mx):
                defender_name = mx[igo+1]
                attacker_name = mx[igo]
                if weather == 0:
                    attacker_drs = f1.DRS
                else:
                    attacker_drs = 0
                a = pd.DataFrame(data.loc[data['DRIVER'] == attacker_name]['ERS']).iloc[0][0]
                d = pd.DataFrame(data.loc[data['DRIVER'] == defender_name]['ERS']).iloc[0][0]
                attacker_ers = (uniform(a,a+1))*25
                defender_ers = (uniform(d,d+1))*45
                defender_defence = pd.DataFrame(data.loc[data['DRIVER'] == defender_name]['DEFENCE']).iloc[0][0] + defender_ers
                attacker_attack = pd.DataFrame(data.loc[data['DRIVER'] == attacker_name]['ATTACK']).iloc[0][0]+ attacker_ers + attacker_drs
                defender_agression = (pd.DataFrame(data.loc[data['DRIVER'] == defender_name]['AGGRESSION']).iloc[0][0]) + randint(0,40)
                attacker_agression = (pd.DataFrame(data.loc[data['DRIVER'] == attacker_name]['AGGRESSION']).iloc[0][0]) + a + randint(0,10)
                if defender_defence + randint(f1.DRS-200,f1.DRS+100) > attacker_attack*track.overtake_chance:
                    defence_test += 1
                    s_dict[attacker_name] += 2
                    s_dict[defender_name] += 0
                else:
                    if (attacker_agression > defender_agression+(randint(f1.lower_stamina,f1.upper_stamina))) and (attacker_name and defender_name not in dnf0):
                        if randint(0,100)>50:
                            print(f'LAP {lap_number} - {defender_name} and {attacker_name} got together, both has crashed. Safety car has deployed.')
                            dnf0.append(defender_name)
                            dnf0.append(attacker_name)
                            crash_alert = 1
                        else:
                            print(f'LAP {lap_number} - {defender_name} and {attacker_name} got together, {defender_name} has crashed. Safety car has deployed.')
                            dnf0.append(defender_name)
                            s_dict[attacker_name] += 10
                            crash_alert = 1
                    else:
                        overtook_test += 1
                        s_dict[attacker_name] += 2
                        s_dict[defender_name] += 2
                igo += 2

            # # # # #

            f1tv = data.values[0:]
           
            sc_alert = 0

        data = data.sort_values('INTERVAL',ascending=True)
        data['LEAD'] = list(range(1,21))
        thefl = f'{str(int((min(the_laptime)/60)))}:{round((((min(the_laptime)/60)-int((min(the_laptime)/60)))*60),3)}'
        interval31 = []

        winner_time = min(list(data['INTERVAL']))
        for p in list(data['INTERVAL']):
            diff0 = p-winner_time
            if diff0 == 0:
                mini0 = winner_time/60
                sec0 = (mini0-int(mini0))*60
                actual_time0 = f'{str(int(mini0))}:{round(sec0,3)}' 
                interval31.append(actual_time0)
            else:
                interval31.append(f'+{round(diff0,3)}')
        data['INTERVAL'] = interval31

        # FINAL OUTPUT
        new_interval_dnfs_included = []
        
        for i in list(data['INTERVAL']):
            if list(data['INTERVAL']).index(i) == 0:
                new_interval_dnfs_included.append(i)
            elif float(i[1:]) > 90000:
                new_interval_dnfs_included.append('DNF')
            else:
                new_interval_dnfs_included.append(i)

        data['INTERVAL'] = new_interval_dnfs_included

        pit_df = pd.DataFrame()
        pit_df['DRIVER'] = daquan
        
        sike = []

        for i in list(pit_dict.values()):
            sike.append(i)

        pit_df['PIT'] = sike
        pit_df['INTERVAL'] = new_interval_dnfs_included
        data['PIT'] = list(pit_df['PIT'])
        print(f'\n{race_conditions[0]}\n\n{data[["LEAD","TITLE","DRIVER","INTERVAL","GRID","PIT"]].groupby("LEAD").max()}')
        print(f'\nLAP {the_lap[the_laptime.index(min(the_laptime))]} | {the_name[the_laptime.index(min(the_laptime))]} | {thefl}\nOvertakes: {overtook_test}')
    RACE()

# # #

shutil.rmtree('__pycache__')
SESSION('Bahrain')
remove('temp.csv')