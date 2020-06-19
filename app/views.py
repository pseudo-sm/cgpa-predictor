from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import pickle
import numpy as np
import sklearn
loaded_model = pickle.load(open("app/finalized_model.sav", 'rb'))

def index(request):

    return render(request,"index.html")

from random import random
def random_generator():

    return random.randint(10)

def index_action(request):
    sat = request.POST["sat_score"]
    X_test = np.array([[float(sat)]])
    result = str(loaded_model.predict(X_test)[0])

    return HttpResponse("<h1>Score : "+result+"</h1>")
