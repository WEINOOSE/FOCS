DRS = 500
plus_time = 0

import pandas as pd
last_df_df = pd.DataFrame()

class Track():
    def __init__(self,title,country,performance,speed,wing,chassis,deg,rain_odd,time,lap,sc,overtake_chance):
        self.title = title
        self.country = country
        self.performance = performance
        self.speed = speed
        self.wing = wing
        self.chassis = chassis
        self.deg = deg
        self.rain_odd = rain_odd
        self.time = time
        self.lap = lap
        self.sc = sc
        self.overtake_chance = overtake_chance

# for 2022 regulations, here is the plus' and minus' values.
# Top Speed = -1, Acceleration = 1
# Straight = -1, Cornering = 1
# Non-Downforce = -1, Downforce = 1
# Agile Chassis = -1, Bulky Chassis = 1

# Title,Name,Performance,Speed,Wing,Chassis,Degration between 0.90 and 1.10, Time, Lap

bhr = Track('Bahrain GP','Bahrain',1,-1,1,1,1.10,1.5,90.5,57,15,0.86)
skh = Track('Sakhir GP','Sakhir',-1,-1,-1,-1,1.10,1.5,55.5,87,10,0.90)
ksa = Track('Saudi Arabian GP','Jeddah',-1,1,1,1,0.90,1.5,88.2,50,65,0.65)
aus = Track('Australian GP','Melbourne',1,1,1,1,0.90,12.5,78,58,50,0.65)
mal = Track('Malaysian GP','Sepang',-1,-1,-1,-1,1.10,25.5,92.5,56,15,0.80)
chn = Track('Chinese GP','Shangai',-1,1,1,-1,1.10,35.5,94,56,25,0.70)
can = Track('Canadian GP','Montreal',1,1,1,0,1.05,2.5,72.5,70,60,0.65)
mia = Track('Miami GP','Miami',1,1,1,1,1.05,3.5,88.5,45,65,0.65)
mnk = Track('Monaco GP','Monaco',1,1,1,-1,0.95,2.5,72.5,78,70,0.76)
esp = Track('Spanish GP','Catalunya',-1,1,1,1,1.10,1.5,78.5,66,25,0.30)
eif = Track('Eifel GP','Nordschleife',1,1,1,1,1.05,25.5,87,60,25,0.60)
imo = Track('Emilia Romagna GP','Imola',-1,-1,-1,1,1.00,42.5,75.5,63,25,0.45)
mug = Track('Tuscan GP','Mugello',-1,1,1,1,0.90,12.5,77,59,25,0.60)
rus = Track('Russian GP','Sochi',1,-1,1,-1,0.90,40.5,94,53,50,0.45)
aze = Track('Azerbaijan GP','Baku',-1,1,1,-1,0.90,2.5,103,51,60,0.70)
tur = Track('Turkish GP','Istanbul',-1,-1,1,1,0.90,35.5,84,58,25,0.70)
eur = Track('European GP','Valencia',1,1,1,-1,0.90,1.5,96,57,65,0.60)
por = Track('Portuguese GP','Portimao',-1,1,-1,1,1.00,5.5,78.5,66,25,0.85)
gbr = Track('British GP','Silverstone',-1,-1,1,1,0.95,37.5,87.5,52,25,0.85)
ger = Track('German GP','Höckenheim',-1,1,1,1,1.05,37.5,74.5,67,25,0.70)
dut = Track('Dutch GP','Zandvoort',-1,1,1,1,1.05,17.5,70,72,25,0.70)
aut = Track('Austrian GP','Spielberg',-1,-1,-1,1,0.95,17.5,65.5,71,25,0.90)
fra = Track('French GP','Le Castellet',-1,1,1,1,1.15,17.5,90.5,53,25,0.50)
hun = Track('Hungarian GP','Hungary',1,1,1,1,1.05,22.5,77,70,25,0.50)
bel = Track('Belgian GP','Spa-Francorchamps',-1,-1,-1,1,1.00,37.5,104.5,44,25,0.90)
ita = Track('Italian GP','Monza',-1,-1,-1,1,0.90,12.5,81.5,53,25,0.90)
sin = Track('Singapore GP','Marina Bay',1,1,1,-1,1.05,25.5,99,59,70,0.45)
fuj = Track('Pacific GP','Fuji',1,1,-1,1,1.10,35.5,82.5,67,25,0.70)
jpn = Track('Japanese GP','Suzuka',-1,1,-1,1,1.15,10.5,90,53,25,0.60)
usa = Track('United States GP','Austin',-1,1,1,1,0.90,12.5,94.5,56,25,0.65)
mex = Track('Mexico City GP','Mexico City',-1,-1,-1,-1,1.00,1.5,76.5,71,25,0.65)
bra = Track('Brazilian GP','Interlagos',-1,-1,-1,1,1.05,42.5,70,71,45,0.85)
ind = Track('Indian GP','India',-1,1,1,-1,1.10,25.5,82,60,25,0.65)
qat = Track('Qatar GP','Qatar',-1,1,-1,1,0.90,1.5,82,57,25,0.75)
abu = Track('Abu Dhabi GP','Abu Dhabi',-1,1,1,-1,0.90,1.5,97,55,45,0.65)

circuits = [bhr,skh,ksa,aus,mal,chn,can,mia,mnk,eif,imo,mug,rus,aze,tur,esp,eur,por,gbr,ger,dut,
aut,fra,hun,bel,ita,sin,fuj,jpn,usa,mex,bra,ind,qat,abu]
#######################################################################################

class Tyre():
    def __init__(self,title,initial,downgrade):
        self.title = title
        self.initial = initial
        self.downgrade = downgrade
    def laptime(self,fuel_amount,track_distance,lap,tyre_left):
        # Fuel Issue
        fuel_left = fuel_amount-(((fuel_amount-1)/track_distance)*lap)
        # Tyre Issue
        x = 85-(tyre_left)
        y = 85-(tyre_left)
        furko  = (abs(x)*0.05) + ((abs(y)*self.initial)/100)
        finolo = (track_distance/25) - (tyre_left/20)
        time_loss_due_to_tyre = furko + finolo
        overheat = 3/(track_distance-(lap-1))
        return (fuel_left/20) + (time_loss_due_to_tyre/5) + self.initial + (track_distance-lap)*0.05 + (((100-tyre_left)/100)*3.5) + (overheat*2)
    def fuel(self,fuel_amount,track_distance,lap):
        fuel_left = fuel_amount-(((fuel_amount-1)/(track_distance+1))*lap)
        return fuel_left
    def tyre(self,fuel_amount,track_distance,lap,track_degredation):
        # Fuel Issue
        fuel_left = fuel_amount-(((fuel_amount-1)/track_distance)*lap)
        time_loss_due_to_fuel = (fuel_left*6.5)/110
        # Tyre Issue
        deg_percentage = (self.downgrade*track_degredation)+(time_loss_due_to_fuel/10)
        return deg_percentage*0.75*(lap*track_degredation)

s = Tyre('Slick',-0.350,3.500)
h = Tyre('Hard',1.350,1.500) 
i = Tyre('Intermediate',10.350,0.750) 
w = Tyre('Wet',25.350,0.650)

compounds = [s,h,i,w]
upper_stamina = 15
lower_stamina = 5
# Constants
weather = 0
start = 1
dnf = [
    'MGU-K',
    'MGU-K',
    'engine',
    'engine',
    'engine',
    'engine',
    'engine',
    'engine',
    'tyre blowout',
    'puncture',
    'hydraulics',
    'fuel Pressure',
    'alternator',
    'suspension',
    'steering',
    'gearbox',
    'oil Pressure',
    'brakes',
    'wheel',
    'vibration',
    'tyre pressure',
    'halfshaft',
    'transmission',
    'electrical',
    'throttle'
]

from random import choice

parts = [
    'front wing',
    'rear wing',
    'sidepod',
    'suspension',
    'car'
]

barrel = [
    f'spun and damaged the {choice(parts)}',
    'went into the barriers',
    'missed the braking zone and went into the gravel',
    'lost control and crashed',
    'lost control and broke the suspension'
]