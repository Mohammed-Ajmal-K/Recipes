from django.urls import path
from adminapp import views

urlpatterns=[
    path('adminpage/',views.adminpage,name="adminpage"),
    path('itemspage/',views.itemspage,name="itemspage"),
    path('saveitems/',views.saveitems,name="saveitems"),
    path('displayitems/',views.displayitems,name="displayitems"),
    path('edititems<int:itemid>/',views.edititems,name="edititems"),
    path('updateitems<int:itemid>/',views.updateitems,name="updateitems"),
    path('deleteitems<int:itemid>/',views.deleteitems,name="deleteitems"),
    path('recipepage/',views.recipepage,name="recipepage"),
    path('saverecipe/',views.saverecipe,name="saverecipe"),
    path('displayrecipe/',views.displayrecipe,name="displayrecipe"),
    path('editrecipe<int:rid>/',views.editrecipe,name="editrecipe"),
    path('updaterecipe<int:rid>/',views.updaterecipe,name="updaterecipe"),
    path('deleterecipe<int:rid>/',views.deleterecipe,name="deleterecipe"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout")

]