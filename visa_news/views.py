from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponseServerError

'''
Error Handling
'''


def handler404(request, exception):
    '''
    Render 404 page
    '''
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    '''
    Render 500 page
    '''
    return render(request, 'errors/500.html', status=500)


def handler403(request, exception):
    '''
    Render 403 page
    '''
    return render(request, 'errors/403.html', status=403)

def trigger_500_error(request):
    '''
    View to trigger a 500 error (Internal Server Error) for testing
    '''
    # Simulate an uncaught exception to trigger the 500 error handler
    raise Exception("This is a simulated server error.")

# View to trigger 403 error
def trigger_403_error(request):
    raise PermissionDenied("Testing the 403 error.")
