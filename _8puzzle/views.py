import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import puzzle


def home(request):
    if request.method == 'POST':
        start0=int(request.POST['start0'])
        start1=int(request.POST['start1'])
        start2=int(request.POST['start2'])
        start3=int(request.POST['start3'])
        start4=int(request.POST['start4'])
        start5=int(request.POST['start5'])
        start6=int(request.POST['start6'])
        start7=int(request.POST['start7'])
        start8=int(request.POST['start8'])
        start=[
            [start0,start1,start2],
            [start3,start4,start5],
            [start6,start7,start8]
        ]
        end0 = int(request.POST['end0'])
        end1 = int(request.POST['end1'])
        end2 = int(request.POST['end2'])
        end3 = int(request.POST['end3'])
        end4 = int(request.POST['end4'])
        end5 = int(request.POST['end5'])
        end6 = int(request.POST['end6'])
        end7 = int(request.POST['end7'])
        end8 = int(request.POST['end8'])
        end = [
            [end0, end1, end2],
            [end3, end4, end5],
            [end6, end7, end8]
        ]
        
        arr = puzzle.Main(start, end)
        puzzles = []
        for i in arr:
            puzzles.append(i.get('node'))
        
        return render(request,'res.html',{'puzzles':puzzles})
        
    return render(request,'home.html')

def res(request):

    return render(request,'res.html')

    
