def sexa_2_dec(tme_):
    tme_dec = float(tme_[0:2]) + float(tme_[3:5])/60
    return(tme_dec)

def wrkd_hrs(time_1, time_2):
    t_1 = sexa_2_dec(time_1)
    t_2 = sexa_2_dec(time_2)
    hours_ = t_2 - t_1
    return(hours_)

def tms_by_day(days_tms):
    tms_ = [x[2:len(x)] for x in days_tms]
    days_ = [x[0:2] for x in days_tms]
    
    #print(tms_)
    #print(days_)
    
    pays = list()
    hrs_total = list()
    days_total = list()
    for i in range(0,len(days_tms)):
        #print(tms_[i][0:5])
        
        days_total.append(days_[i])
        if sexa_2_dec(tms_[i][0:5])>=0 and sexa_2_dec(tms_[i][0:5])<=9:
            #print('Es mayor que 12 am')
            if sexa_2_dec(tms_[i][6:10])<=9:
                #print('Es menor que 9 am, un solo horario')
                hrs_total.append(wrkd_hrs(tms_[i][0:5], tms_[i][6:10]))
                pays.append(mat_[0][days.index(days_[i]) ] )
                
            elif sexa_2_dec(tms_[i][6:10])>9 and sexa_2_dec(tms_[i][6:10])<=18:
                #print('Mayor que 9 y menor que 18, dos horarios')
                hrs_total.append(wrkd_hrs(tms_[i][0:5], '09:00'))
                hrs_total.append(wrkd_hrs('09:00', tms_[i][6:10] ))
                pays.append(mat_[0][days.index(days_[i]) ] )
                pays.append(mat_[1][days.index(days_[i]) ] )
                
                days_total.append(days_[i])
                
            elif sexa_2_dec(tms_[i][6:10])>9 and sexa_2_dec(tms_[i][6:10])<=sexa_2_dec('23:59'):
                #print('Mayor que 18 y menor a las 24, tres horarios')
                hrs_total.append(wrkd_hrs(tms_[i][0:5], '09:00'))
                hrs_total.append(9)
                hrs_total.append(wrkd_hrs('18:00', tms_[i][6:10]))
                pays.append(mat_[0][days.index(days_[i]) ] )
                pays.append(mat_[1][days.index(days_[i]) ] )
                pays.append(mat_[2][days.index(days_[i]) ] )
                
                days_total.append(days_[i])
                days_total.append(days_[i])
                
                
        if sexa_2_dec(tms_[i][0:5])>=9 and sexa_2_dec(tms_[i][0:5])<=18:
            
            if sexa_2_dec(tms_[i][6:10])<=18:
                hrs_total.append(wrkd_hrs(tms_[i][0:5], tms_[i][6:10]))
                pays.append(mat_[1][days.index(days_[i]) ] )
                
            elif sexa_2_dec(tms_[i][6:10])>18 and sexa_2_dec(tms_[i][6:10])<=sexa_2_dec('23:59'):
                #print('Mayor que 9 y menor que 18, dos horarios')
                hrs_total.append(wrkd_hrs(tms_[i][0:5], '18:00'))
                hrs_total.append(wrkd_hrs('18:00', tms_[i][6:10] ))
                pays.append(mat_[1][days.index(days_[i]) ] )
                pays.append(mat_[2][days.index(days_[i]) ] )
                
                days_total.append(days_[i])
                
        if sexa_2_dec(tms_[i][0:5])>=18:
            hrs_total.append(wrkd_hrs(tms_[i][0:5], tms_[i][6:10]))
            pays.append(mat_[2][days.index(days_[i]) ] )
                
    #print(hrs_total)
    #print(days_total)
    #print(pays)
    
    mat_total = [days_total, hrs_total, pays]
    return(mat_total)


# CREATION OF PAYMENT TABLE
days = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
wk_01_09 = [25,25,25,25,25,    30,30]
wk_09_18 = [15,15,15,15,15,    20,20]
wk_18_00 = [20,20,20,20,20,    25,25]

mat_ = list( [wk_01_09, wk_09_18, wk_18_00])

# INPUT TESTS
file_nme_ = raw_input('Type file name: ')
file_ = open(file_nme_, "r")
input_ = file_.read()

worker = input_[0:input_.find('=') ]

nme = input_.split(',')
nme[0] = nme[0][input_.find('=')+1:len(nme[0])]

hrs_nd_pays = tms_by_day(nme)
pay= sum([a * b for a,b in zip(hrs_nd_pays[1], hrs_nd_pays[2])])

print('The amount to pay to '+worker+' is: '+str(pay))
