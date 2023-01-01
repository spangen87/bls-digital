from django.shortcuts import render


def smart_locks(request):
    """
    A view to render the smart locks page
    """
    return render(request, 'smart_locks/smart_locks.html')
