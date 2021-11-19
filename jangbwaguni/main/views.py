from django.shortcuts import render, get_object_or_404

def main_view(request):
    return render(request, 'main.html')
