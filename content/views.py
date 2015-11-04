from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index( request ):
    print( request.user )
    if not request.user.is_authenticated():
        #user is not authenticated
        #return redirect( '%s?next=%s' % ( settings.LOGIN_URL, request.path ) )
    else:
        return render( request, 'content/index.html' )



