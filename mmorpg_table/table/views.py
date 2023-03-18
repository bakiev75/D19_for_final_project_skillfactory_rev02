from datetime import datetime

from django.shortcuts import render


def index(request):
    data = datetime.now()
    print(f'Привет мир в консоли {data}')
    return render(request, 'index.html', context={'index_val_1': data})
