from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import DogBreedInfo,DogInfo,CatBreedInfo,CatInfo,RabbitInfo,RabbitBreedInfo

# Create your views here.

def index(request):
    return render(request, 'petdogs/homepage.html')


#DOG*************************************************************************************
def tabledog(request):
        breedinfo=DogBreedInfo.objects.all()
        return render(request,'petdogs/TABLE1.html', {'breed_info': breedinfo})

def insertpagedog(request):
    breedinfo = DogBreedInfo.objects.all()
    return render(request,'petdogs/dog.html',{'breed_info': breedinfo})

def insertdonedog(request):
    if not request.POST["petname"]:
        b = DogBreedInfo.objects.all()
        dic = {"breed_info": b, "petname": True}
        return render(request, 'petdogs/dog.html', dic)
    elif not request.POST["height"]:
        b = DogBreedInfo.objects.all()
        dic = {"breed_info": b, "petheight": True}
        return render(request, 'petdogs/dog.html', dic)
    elif not request.POST["weight"]:
        b = DogBreedInfo.objects.all()
        dic = {"breed_info": b, "petweight": True}
        return render(request, 'petdogs/dog.html', dic)

    else:
        petinfo=DogInfo()
        petinfo.pet_name=request.POST["petname"]
        petinfo.pet_breed=DogBreedInfo.objects.get(pk=request.POST["breed"])
        petinfo.gender=request.POST["gender"]
        petinfo.height=request.POST["height"]
        petinfo.weight=request.POST["weight"]
        petinfo.save()
        return render(request, 'petdogs/homepage.html')

def tableretrivedog(request,pet_id):
    breedinfo=DogBreedInfo.objects.all()
    pet=DogInfo.objects.get(pk=pet_id)
    return render(request,'petdogs/dog.html',{"pet":pet,'breed_info':breedinfo})

def insertupdatedog(request,pet_id):
    petinfo = DogInfo.objects.get(pk=pet_id)
    petinfo.pet_name = request.POST["petname"]
    petinfo.pet_breed = DogBreedInfo.objects.get(pk=request.POST["breed"])
    petinfo.gender = request.POST["gender"]
    petinfo.height = request.POST["height"]
    petinfo.weight = request.POST["weight"]
    petinfo.save()
    return render(request, 'petdogs/homepage.html')

def deleterecorddog(request,pet_id):
    pet=DogInfo.objects.get(pk=pet_id)
    pet.delete()
    return render(request,'petdogs/homepage.html')


#CAT****************************************************************************************
def tablecat(request):
    breedinfo=CatBreedInfo.objects.all()
    return render(request,'petdogs/TABLE2.html', {'breed_info': breedinfo})
    #to show the insert page and send all the breed data to page


def insertpagecat(request):
    breedinfo = CatBreedInfo.objects.all()
    return render(request,'petdogs/cat.html',{'breed_info': breedinfo})


def insertdonecat(request):
    if not request.POST["petname"]:
        b = CatBreedInfo.objects.all()
        dic = {"breed_info": b, "petname": True}
        return render(request, 'petdogs/cat.html', dic)
    elif not request.POST["height"]:
        b = CatBreedInfo.objects.all()
        dic = {"breed_info": b, "petheight": True}
        return render(request, 'petdogs/cat.html', dic)
    elif not request.POST["weight"]:
        b = CatBreedInfo.objects.all()
        dic = {"breed_info": b, "petweight": True}
        return render(request, 'petdogs/cat.html', dic)
    else:
        petinfo=CatInfo()
        petinfo.pet_name=request.POST["petname"]
        petinfo.pet_breed=CatBreedInfo.objects.get(pk=request.POST["breed"])
        petinfo.gender=request.POST["gender"]
        petinfo.height=request.POST["height"]
        petinfo.weight=request.POST["weight"]
        petinfo.save()
        return render(request, 'petdogs/homepage.html')


def tableretrivecat(request,pet_id):
    breedinfo=CatBreedInfo.objects.all()
    pet=CatInfo.objects.get(pk=pet_id)
    return render(request,'petdogs/cat.html',{"pet":pet,'breed_info':breedinfo})


def insertupdatecat(request,pet_id):
    petinfo = CatInfo.objects.get(pk=pet_id)
    petinfo.pet_name = request.POST["petname"]
    petinfo.pet_breed = CatBreedInfo.objects.get(pk=request.POST["breed"])
    petinfo.gender = request.POST["gender"]
    petinfo.height = request.POST["height"]
    petinfo.weight = request.POST["weight"]
    petinfo.save()
    return render(request, 'petdogs/homepage.html')


def deleterecordcat(request,pet_id):
    pet=CatInfo.objects.get(pk=pet_id)
    pet.delete()
    return render(request,'petdogs/homepage.html')



#RABBIT*******************************************************************************



def tablerabbit(request):
    breedinfo=RabbitBreedInfo.objects.all()
    return render(request,'petdogs/TABLE3.html', {'breed_info': breedinfo})
    #to show the insert page and send all the breed data to page


def insertpagerabbit(request):
    breedinfo = RabbitBreedInfo.objects.all()
    return render(request,'petdogs/rabbit.html',{'breed_info': breedinfo})



def insertdonerabbit(request):
    if not request.POST["petname"]:
        b = RabbitBreedInfo.objects.all()
        dic = {"breed_info": b, "petname": True}
        return render(request, 'petdogs/rabbit.html', dic)
    elif not request.POST["height"]:
        b = RabbitBreedInfo.objects.all()
        dic = {"breed_info": b, "petheight": True}
        return render(request, 'petdogs/rabbit.html', dic)
    elif not request.POST["weight"]:
        b = RabbitBreedInfo.objects.all()
        dic = {"breed_info": b, "petweight": True}
        return render(request, 'petdogs/rabbit.html', dic)
    else:
        petinfo=RabbitInfo()
        petinfo.pet_name=request.POST["petname"]
        petinfo.pet_breed=RabbitBreedInfo.objects.get(pk=request.POST["breed"])
        petinfo.gender=request.POST["gender"]
        petinfo.height=request.POST["height"]
        petinfo.weight=request.POST["weight"]
        petinfo.save()
        return render(request, 'petdogs/homepage.html')


def tableretriverabbit(request,pet_id):
    breedinfo=RabbitBreedInfo.objects.all()
    pet=RabbitInfo.objects.get(pk=pet_id)
    return render(request,'petdogs/rabbit.html',{"pet":pet,'breed_info':breedinfo})


def insertupdaterabbit(request,pet_id):
    petinfo = RabbitInfo.objects.get(pk=pet_id)
    petinfo.pet_name = request.POST["petname"]
    petinfo.pet_breed = RabbitBreedInfo.objects.get(pk=request.POST["breed"])
    petinfo.gender = request.POST["gender"]
    petinfo.height = request.POST["height"]
    petinfo.weight = request.POST["weight"]
    petinfo.save()
    return render(request, 'petdogs/homepage.html')


def deleterecordrabbit(request,pet_id):
    pet=RabbitInfo.objects.get(pk=pet_id)
    pet.delete()
    return render(request,'petdogs/homepage.html')
