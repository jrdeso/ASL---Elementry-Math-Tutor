import pickle

database = pickle.load(open('userData/database.p','rb'))

userName = raw_input("Please enter your name: ")
if userName in database:
    print("Welcome Back " + userName + ".")
    #get previous num of logins and increment
    x = database[userName]["Logins: "]
    x+=1
    database[userName] = {"Logins: " : x}
else:
    database[userName] = {"Logins: " : 1}
    print("Welcome " + userName + ".")
        
print(database)

pickle.dump(database, open('userData/database.p','wb'))
