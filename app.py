from flask import*
import pymysql
import pymysql.cursors

app=Flask(__name__)

@app.route("/api/signup", methods=["POST"])
def signUp():
    username= request.form['username']
    email= request.form['email']
    phone= request.form['phone']
    password= request.form['password']
    
    print(username,email,phone,password)
    
    
    # create connection to db
    connection=pymysql.connect(host="localhost",user="root",password="",database="elphas_sokogarden")
    # create cursor to handle sql queries
    
    cursor= connection.cursor()
    

    
    # create sql query
    sql="insert into users(username,email,phone,password) values(%s,%s,%s,%s)"
    
    # data to be saved
    data= (username,email,phone,password)
    
    # execute sql query
    cursor.execute(sql,data)
    
    # save the data
    connection.commit()
    # return the response
    return jsonify({"message":"Sign up succesfull"})

# login route
@app.route("/api/login",methods=["POST"]   )
def login():
    email=request.form['email']
    password=request.form['password']
    print(email,password)
    # connect to database
    connection=pymysql.connect(host="localhost",user="root",password="",database="elphas_sokogarden")
    # cursor=connection.cursor()
    # cursor that returns as key-values pair
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    # create an sql query
    sql="select user_id,username,email,phone from users where email=%s and password=%s"
    # data to execute the query
    data=(email,password)
    # execute the query
    cursor.execute(sql,data)
    # check for the response
    if cursor.rowcount==0:
        return jsonify({"Message":"Invalid credentials"})
    else:
        # get the userdata
        user= cursor.fetchone()
        return jsonify({"Message":"login succesfull", "user":user})



if __name__=="__main__":
    app.run(debug=True)