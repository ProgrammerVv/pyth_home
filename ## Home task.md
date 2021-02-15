#Task 1

phrase_1=str(input("Give your phrase number one"))
phrase_2=str(input("Give your phrase number two"))

phrase_1 = (len(phrase_1))
phrase_2 = (len(phrase_2))

if phrase_1 < phrase_2:
    print ('Phrase number two is bigger')
        
if phrase_1 > phrase_2:
    print ('Phrase number one is bigger')
    
if phrase_1 == phrase_2:
    print ('They are equal') 
     

#Task 2
year=int(input("Your year:"))

if year % 2 == 0:
    print ("Visokos")

else:
    print ("Not visokos")


#Task 3

UserDate=int(input("Your date of birth:"))

UserMonth=str(input("Your month of birth:"))

UserYear=int(input("Your year of birth:"))

if (UserDate>=21 and UserDate<=31 and UserMonth=='March') or ( UserMonth=='April' and UserDate>=1 and UserDate<=19):

   print("Zodiac sign: Aries")

elif (UserDate>=20 and UserDate<=30 and UserMonth=='April') or ( UserMonth=='May' and UserDate>=1 and UserDate<=20):

   print("Zodiac sign: Taurus")

elif (UserDate>=21 and UserDate<=31 and UserMonth=='May') or ( UserMonth=='June' and UserDate>=1 and UserDate<=21):

   print("Zodiac sign: Gemini")

elif (UserDate>=22 and UserDate<=30 and UserMonth=='June') or ( UserMonth=='July' and UserDate>=1 and UserDate<=22):

   print("Zodiac sign: Cancer")

elif (UserDate>=23 and UserDate<=31 and UserMonth=='July') or ( UserMonth=='August' and UserDate>=1 and UserDate<=22):

   print("Zodiac sign: Leo")

elif (UserDate>=23 and UserDate<=31 and UserMonth=='August') or ( UserMonth=='September' and UserDate>=1 and UserDate<=22):

   print("Zodiac sign: Virgo")

elif (UserDate>=23 and UserDate<=30 and UserMonth=='September') or ( UserMonth=='October' and UserDate>=1 and UserDate<=23):

   print("Zodiac sign: Libra")

elif (UserDate>=24 and UserDate<=31 and UserMonth=='October') or ( UserMonth=='November' and UserDate>=1 and UserDate<=22):

   print("Zodiac sign: Scorpio")

elif (UserDate>=23 and UserDate<=30 and UserMonth=='November') or ( UserMonth=='December' and UserDate>=1 and UserDate<=21):

   print("Zodiac sign: Sagittarius")

elif (UserDate>=22 and UserDate<=31 and UserMonth=='December') or ( UserMonth=='January' and UserDate>=1 and UserDate<=20):

   print("Zodiac sign: Capricorn")

elif (UserDate>=21 and UserDate<=31 and UserMonth=='January') or ( UserMonth=='February' and UserDate>=1 and UserDate<=18):

   print("Zodiac sign: Aquarius")

elif (UserDate>=19 and UserDate<=29 and UserMonth=='February') or ( UserMonth=='March' and UserDate>=1 and UserDate<=20):

   print("Zodiac sign: Pisces")

#Task 4

UserWidth =int(input("Width :"))
UserLength =int(input("Length :"))
UserHhight =int(input("Height :"))

if (UserWidth < 15 and UserLength < 15 and UserHhight <15):
    print('Use the box №1')

elif (UserLength > 200):
    print('Use the box of ski')

elif (UserWidth < 50 and UserLength < 50 and UserHhight < 50):
    print('Use the box №2')

else:
    print('Use the box №3')




elif (UserWidth > 15 and UserWidth < 50 and UserLength > 15 and UserLength < 50 and UserHhight >15 and UserHhight < 50):


    if (UserLength < 200):
        print('Use the box №2')
    elif (UserLength > 200):
        print('Use the box of ski')
else:
    print('Use the box №3')