from django.shortcuts import render,redirect
from adminapp.models import cuisinedb,recipedb
from userapp.models import registerdb,favdb,downloaddb,feedbackdb
from django.contrib import messages
from django.shortcuts import render


# Create your views here.
def userpage(request):
    dataitem=cuisinedb.objects.all()
    return render(request,"userpage.html",{'dataitem':dataitem})
def user_recipepage(request,i_name):
    dataitem=cuisinedb.objects.all()
    datarecipe=recipedb.objects.filter(item=i_name)
    return render(request,"recipepage.html",{'dataitem':dataitem,'datarecipe':datarecipe})
def singlerecipe(request,recipe_id):
    recipe=recipedb.objects.get(id=recipe_id)
    dataitem=cuisinedb.objects.all()
    recipe_all=recipedb.objects.all()
    return render(request,"singlerecipe.html",{'recipe':recipe,'dataitem':dataitem,'recipe_all':recipe_all})




def userdashboard(request):
    return render(request,"userdashboard.html")
def add_userecipe(request):
    idata=cuisinedb.objects.all()
    return render(request,"user_recipepage.html",{'idata':idata})
def saveuser_recipe(request):
    if request.method=="POST":
        data=request.POST.get
        item=data('item')
        rname=data('r_name')
        rimage=request.FILES['r_img']
        ingredients=data('ing')
        rdesc=data('r_desc')
        rdata= recipedb(item=item,recipe_name=rname,recipe_image=rimage,ingredients=ingredients,recipe_desc=rdesc)
        rdata.save()
        messages.success(request,"Recipe added successfully")
        return redirect(add_userecipe)
def registerpage(request):
    return render(request,"registerpage.html")

def saveregister(request):
        if request.method == "POST":
            uname = request.POST.get('uname')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            password = request.POST.get('password')
            obj = registerdb(username=uname, email=email, mobile=mobile, password=password)
            obj.save()
            messages.success(request, "Registration completed")
            return redirect(registerpage)

def userlogin(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        password=request.POST.get('pword')
        if registerdb.objects.filter(username=uname,password=password).exists():
            request.session['uname']=uname
            request.session['pword']=password
            messages.success(request,"Log In successfully")
            return redirect(userpage)
        else:
            messages.error(request,"Invalid username or password")
            return redirect(registerpage)

def userlogout(request):
    del request.session['uname']
    del request.session['pword']
    return redirect(userpage)



def aboutpage(request):
    dataitem=cuisinedb.objects.all()
    datarecipe=recipedb.objects.all()
    return render(request,"aboutpage.html",{'datarecipe':datarecipe,'dataitem':dataitem})
def favoritepage(request):
    dataitem = cuisinedb.objects.all()
    fdata=favdb.objects.filter(uname=request.session['uname'])
    return render(request,"favoritespage.html",{'fdata':fdata,'dataitem':dataitem})
def savefavorites(request):
    if request.method=="POST":
        uname=request.POST.get('user')
        recipe=request.POST.get('rname')
        ingr=request.POST.get('ingr')
        desc=request.POST.get('desc')
        obj=favdb(uname=uname,recipe=recipe,ingredients=ingr,description=desc)
        obj.save()
        messages.success(request,"Recipe added to favorites")
        return redirect(favoritepage)
def deletefavs(request,favid):
    fdata=favdb.objects.filter(id=favid)
    fdata.delete()
    return redirect(favoritepage)
def downloadpage(request,favid):
    fdata = favdb.objects.filter(id=favid)
    return render(request,"download.html", {'fdata': fdata})
def download(request):
    if request.method=="POST":
        rname=request.POST.get('name')
        ingr=request.POST.get('ingr')
        desc=request.POST.get('desc')
        obj=downloaddb(rname=rname,ringredients=ingr,rdesc=desc)
        obj.save()
        return redirect(downloadpage)
def feedbackpage(request):
    dataitem=cuisinedb.objects.all()
    return render(request,"feedbackpage.html",{'dataitem':dataitem})
def savefeedback(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        feedback=request.POST.get('fback')
        obj=feedbackdb(uname=name,email=email,feedback=feedback)
        obj.save()
        return redirect(feedbackpage)
def search_results(request):
    if request.method=="GET":
        query = request.GET.get('query')

        cuisine_results=cuisinedb.objects.filter(name__icontains=query)
        recipe_results = recipedb.objects.filter(recipe_name__icontains=query)
        cuisine=cuisinedb.objects.all()


        context = {
            'cuisine_results':cuisine_results,
            'recipe_results': recipe_results,
            'cuisine':cuisine
        }

        return render(request, 'search.html', context)
