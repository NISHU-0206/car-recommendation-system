import csv      
f=open('Cars_details.csv','w',newline='')                 
w=csv.writer(f)
w.writerow(['Company name','Model name','Engine(cc)','Mileage(kmpl)','Seating capacity','Price(lakhs)','Colour'])
w.writerow(['Toyota','Fortuner',2755,10.0,7,42.55,('Black,White,Silver')])
w.writerow(['Toyota','Innova crysta',2694,12.0,7,20.30,('Silver,Bronze,White')])
w.writerow(['Toyota','Urban Cruiser',1462,18.76,5,10.0,('Black,Blue,Orange')])
w.writerow(['Toyota','Glanza',1197,23.87,5,8.5,('Black,Blue,Grey,Red')])
w.writerow(['Toyota','Camry',2487,19.16,5,41.20,('White,Brown,Red')])
w.writerow(['Hyundai','Venue',1498,23.7,5,6.99,('Black,Blue,White')])
w.writerow(['Hyundai','Creta',1353,16.8,5,15.0,('Black,Grey,White')])
w.writerow(['Hyundai','Verna',1497,19.0,5,10.2,('Silver,Grey,Red')])
w.writerow(['Hyundai','i20',998,12.6,5,9.0,('Black,Grey,White')])
w.writerow(['Hyundai','Aura',1197,22.0,5,7.0,('Black,Blue,Red')])
w.writerow(['Maruti Suzuki','Swift',1197,12.6,5,8.01,('Black,Red,Blue,White')])
w.writerow(['Maruti Suzuki','Baleno',796,24.7,5,8.12,('Black,Red,Blue,White')])
w.writerow(['Maruti Suzuki','Wegnar',998,21.79,5,7.00,('Black,Red,Blue,Orange')])
w.writerow(['Maruti Suzuki','Alto 800',796,24.7,5,7.3,('Orange,Red,Blue,White')])
w.writerow(['Maruti Suzuki','S presso',998,31.2,5,6.9,('Black,Red,Blue,White')])
w.writerow(['Audi','Q8',2995,9.8,5,99.96,('Black,Red,Brown')])
w.writerow(['Audi','Q7',2967,14.75,5,69.27,('Black,Red,Brown')])
w.writerow(['Audi','Q5',1984,13.47,5,58.93,('Black,Red,Grey')])
w.writerow(['Audi','Q3',1968,16.9,5,34.97,('Black,Red,Brown')])
f.close()

'"For car recommendation."'

a=int(input('Enter engine power:'))
b=float(input('Enter mileage(kmpl):'))
c=int(input('Enter seating capacity:'))
d=float(input('Enter price(in lakhs):'))
with open('Cars_Details.csv','r') as g:
    x=g.readline()
    r=csv.reader(g)
    for i in r:
        if int(i[2])>=a:
            if float(i[3])>=b:
                if int(i[4])>=c:
                    if float(i[5])<=d:
                        print('The perfect car for you is',i[0],i[1])
                        break
    else:
        print('No car is available right now.')
