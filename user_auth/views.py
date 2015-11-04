from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index( request ):
    #get all the users 
    users = User.objects.all()

    if request.method == 'POST':
                
        name = request.POST[ 'your_name' ]
        password = request.POST[ 'your_pass' ] 

        #check if the user exits
        user = authenticate( username = name, password = password )

        if user is not None:
            if user.is_active:
                login( request, user )
                context = {
                            'users': users
                }

                return render( request, 'content/index.html', context )

            else:
                print("the password is valid, but the account has been disabled")

        else:
            print("the username and password were incorrect.")
            

    return render( request, 'user_auth/index.html', {} )
   

def welcome( request ):
    return render( request, 'user_auth/welcome.html' )

