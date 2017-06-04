


from django.shortcuts import render

def index(request):
    # defining the variable
    number = 6
    thing = "Thing name"
    # passing the variable to the view
    return render(request, 'index.html', {
        'number': number,
        # don't forget to pass it in, and the last comma
        'thing': thing,
    })

