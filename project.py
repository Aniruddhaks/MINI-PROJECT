import mysql.connector as sqlitor
mycon=sqlitor.connect(host="localhost",user="root",password="sql123")
from tabulate import tabulate
if mycon.is_connected():
    print("Welcome to TYPE SPEED TEST")
    cur=mycon.cursor()
    query1='use type_speed_test'
    cur.execute(query1)
    mycon.commit()







def sign_up():
    cur=mycon.cursor()
    user_name=input("Enter your Username:")
    user_id=input("Enter your USER ID:")
    passw=input("Enter your password:")
    conf=input("Enter your password for confirmation")
    while True:
        if passw==conf:
            cur.execute('insert into players values("{}","{}","{}")'.format(user_name,user_id,passw))
            cur.execute('insert into high_score (userid) values("{}")'.format(user_id))
            mycon.commit()
            break
        else:
            print("Incorrect password Enter again")
    

def sign_in():
    cur=mycon.cursor()
    user_id=input("enter your user id")
    passw=input("enter your password")
    conf=input("enter your password for confirmation")
    if passw==conf:
        cur.execute(f'select * from players where userid="{user_id}"')
        data=cur.fetchone()
        
        if data[2]==passw:
                
            while True:
                print("enter choice 1 for playing")
                
                print("enter choice 2 for deleting account")
                print("enter choice 3 for signing out")
                c=int(input("Enter a choice"))
                if c==1:
                    play()
                
                elif c==2:
                    delete()
                else:
                    break





def admin():
    import pickle
    f=open("admin.dat","ab")
    d={}
    d["admin1"]="Ansh"
    d["admin2"]="Joshi"
    d["admin3"]="KS"
    d["admin4"]="vikrant05"
    pickle.dump(d,f)
    f.close()
    f=open("admin.dat","rb")
    username=input("enter username")
    password=input("enter your password")
    chk=0
    try:
        user_chk=0
        pwd_chk=0
        while True:
                
                b=pickle.load(f)
                for i in b:
                
                    if i==username:
                        user_chk=1
                        if b[i]==password:
                            pwd_chk=1
                            while True:
                                print("Enter choice 1 for viewing players")
                                
                                print("Enter choice 2 for removing players from user interface")
                                print("Enter choice 3 for exit")
                                c=int(input("Enter the choice"))
                                if c==1:
                                    view()
                                
                                elif c==2:
                                    delete()
                                elif c==3:
                                    chk=1
                                    break
                                    
                                

                                
                                
                                    
                                
                                
                                    
                
                if chk==1:
                    break

                
                    
                                    
                                            
                                                    
    except EOFError:
                if user_chk==0 or pwd_chk==0:
                                print("Wrong password/user name")
                f.close()


def play():
    import subprocess
    

    subprocess.run(["python","sourcecode.py"])
    
            


'''def high_score():
    cur=mycon.cursor()
    user_id=input("enter the user id")
    cur.execute(f'select * from high_score where userid={user_id}')
    data=cur.fetchone()
    print("Player high score is",data[1])
    mycon.commit()'''

def view():
    cur=mycon.cursor()
    cur.execute('select * from players')
    data=cur.fetchall()
    h=["username","userid","password"]
    print(tabulate(data,headers=h,tablefmt='fancy_grid'))
    mycon.commit()

def delete():
    cur=mycon.cursor()
    user_id=input("enter the userid")
    cur.execute(f'delete from players where userid = "{user_id}"')
    cur.execute(f'delete from high_score where userid = "{user_id}"')
    mycon.commit()

def player():
    while True:
        print("enter choice 1 for sign up")
        print("enter choice 2 for sign in")
        print("enter choice 3 for exit")
        c=int(input("enter the choice"))
        if c==1:
            sign_up()
        elif c==2:
            sign_in()
        elif c==3:
            break

while True:
    print("enter choice 1 for player")
    print("enter choice 2 for admin")
    print("enter choice 3 for exit")
    c=int(input("enter the choice"))
    if c==1:
        player()
    elif c==2:
        admin()
    elif c==3:
        break








    



    








