from flask import Flask,request   
import linkedin   #Importing linkedin python file from same directory

app = Flask(__name__)    

#Setting URL
URL="https://www.linkedin.com/login"

#Routing path
@app.route('/', methods = ["GET"] )
def checkCredentials(): 
   #Requesting parameters(username,password) by request package      
   username = request.args.get('username')         
   password = request.args.get('password')
   
   #Creating object of Class User
   a = linkedin.User(username,password)

   #Calling login() function from Class User
   if( a.login() ):
      return "Login Successful"
   else: return "Login Unsuccessful" 

if __name__  == "__main__":
   app.run(debug= True)