# Ryan Lau WeiChen Liu Daniel Liu
#SoftDev
#K04-DictWord
#2022-09-22
#Time Spent: 0.4 Hour


"""
DISCO:
-random.randint() accepts two arguements, inclusive of both
-You Can Access The Value Pair By Using The Key as the "Index"

QCC:
-How Can We Manually Generate Random-Ness Without Importing Random?

OPS SUMMARY:
-First we wrote the heading. Then we initialized the dictionary of
period:students as the key:value pairs. Then we imported random and
then made functions to first choose the random period, then another
function to return a random student or ducky based on the output of the random period function.
The next day, we tried to optimize our approach. We used .keys() and returned a list of keys, and radnomly selected a key which is the period. Then, we returned a random student
based on the random period that we used as an index for accessing the associated list of students in that period.
"""

import random

krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"],
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
         }

def select_random_period():
    periods = list(krewes.keys())
    return random.choice(periods)

def select_random_student(period):
    return random.choice(krewes[period])

random_period = select_random_period()
random_devo = select_random_student(random_period)
print(f"{random_period} : {random_devo}")
