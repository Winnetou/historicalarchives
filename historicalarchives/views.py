from django.shortcuts import render_to_response

def Index(request):
    return render_to_response("historicalarchives/index.html")
