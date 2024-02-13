from django.shortcuts import render,redirect
from adminapp.models import cuisinedb
from adminapp.models import recipedb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# from userapp import views


# Create your views here.
def adminpage(request):
    return render(request,"adminpage.html")
def itemspage(request):
    return render(request,"addcuisines.html")
def saveitems(request):
    if request.method=="POST":
        data=request.POST.get
        name=data('name')
        image=request.FILES['img']
        description=data('des')
        items=cuisinedb(name=name,image=image,description=description)
        items.save()
        messages.success(request, "New cuisine added successfully")
        return redirect(itemspage)
def displayitems(request):
    idata=cuisinedb.objects.all()
    return render(request,"displayitems.html",{'idata':idata})
def edititems(request,itemid):
    idata=cuisinedb.objects.get(id=itemid)
    return render(request,"edititems.html",{'idata':idata})
def updateitems(request,itemid):
    if request.method=="POST":
        data=request.POST.get
        name=data('name')
        description =data('des')
        try:
            image = request.FILES['img']
            fs=FileSystemStorage()
            image=fs.save(image.name,image)
        except MultiValueDictKeyError:
            image=cuisinedb.objects.get(id=itemid).image
        cuisinedb.objects.filter(id=itemid).update(name=name,image=image,description=description)
        messages.success(request, "cuisine data updated successfully")
        return redirect(displayitems)
def deleteitems(request,itemid):
    idata=cuisinedb.objects.filter(id=itemid)
    idata.delete()
    return redirect(displayitems)
def recipepage(request):
    idata=cuisinedb.objects.all()
    return render(request,"addrecipe.html",{'idata':idata})
def saverecipe(request):
    if request.method=="POST":
        data=request.POST.get
        item=data('item')
        rname=data('r_name')
        rimage=request.FILES['r_img']
        about=data('about')
        ingredients=data('ing')
        rdesc=data('r_desc')
        rdata= recipedb(item=item,recipe_name=rname,recipe_image=rimage,ingredients=ingredients,recipe_desc=rdesc,about=about)
        rdata.save()
        messages.success(request, "New recipe added successfully")
        return redirect(recipepage)
def displayrecipe(request):
    rdata=recipedb.objects.all()
    return render(request,"displayrecipe.html",{'rdata':rdata})
def editrecipe(request,rid):
    idata=cuisinedb.objects.all()
    rdata=recipedb.objects.get(id=rid)
    return render(request,"editrecipe.html",{'rdata':rdata,'idata':idata})
def updaterecipe(request,rid):
    if request.method=="POST":
        data=request.POST.get
        item=data('item')
        rname=data('r_name')
        ingredients=data('ing')
        rdesc=data('r_desc')
        try:
            rimage = request.FILES['r_img']
            fs=FileSystemStorage()
            rimage=fs.save(rimage.name,rimage)
        except MultiValueDictKeyError:
            rimage=recipedb.objects.get(id=rid).recipe_image
        recipedb.objects.filter(id=rid).update(item=item,recipe_name=rname,recipe_image=rimage,ingredients=ingredients,recipe_desc=rdesc)
        return redirect(displayrecipe)
def deleterecipe(request,rid):
    rdata=recipedb.objects.filter(id=rid)
    rdata.delete()
    return redirect(displayrecipe)
def loginpage(request):
    return render(request,"loginpage.html")
def adminlogin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = uname
                request.session['password'] = pwd
                messages.success(request, "login successfully")
                return redirect(adminpage)
            else:
                messages.error(request, "invalid username or password")
                return redirect(loginpage)
        else:
            messages.error(request, "invalid username or password")
            return redirect(loginpage)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

