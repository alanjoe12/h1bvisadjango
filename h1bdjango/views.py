from django.shortcuts import render
from django.http import HttpResponse
import six
import sys

sys.modules['sklearn.externals.six'] = six
import joblib


def home(request):
    return render(request, "home.html")


def result(request):
    decision_tree = joblib.load('decision_tree_finalModel_H1B.sav')

    lis = []
    lis.append(request.POST['wage'])
    lis.append(request.POST['naics'])
    lis.append(request.POST['employer'])
    lis.append(request.POST['sec_entity'])
    lis.append(request.POST['agent'])
    lis.append(request.POST['soc_title'])

    ans = decision_tree.predict([lis])

    if ans == 1:
        output = 'Certified'
    else:
        output = 'Denied!'

    return render(request, 'result.html', {'ans': output})

