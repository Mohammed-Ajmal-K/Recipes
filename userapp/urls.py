from django.urls import path
from userapp import views

urlpatterns=[
    path('userpage/',views.userpage,name="userpage"),
    path('user_recipepage/<i_name>',views.user_recipepage,name="user_recipepage"),
    path('singlerecipe/<int:recipe_id>/',views.singlerecipe,name="singlerecipe"),

    path('userdashboard/',views.userdashboard,name="userdashboard"),
    path('add_userecipe/',views.add_userecipe,name="add_userecipe"),
    path('saveuser_recipe/',views.saveuser_recipe,name="saveuser_recipe"),

    path('aboutpage/',views.aboutpage,name="aboutpage"),

    path('registerpage/',views.registerpage,name="registerpage"),
    path('saveregister/',views.saveregister,name="saveregister"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('favoritepage/',views.favoritepage,name="favoritepage"),
    path('savefavorites/',views.savefavorites,name="savefavorites"),
    path('deletefavs/<int:favid>/',views.deletefavs,name="deletefavs"),
    path('feedbackpage',views.feedbackpage,name="feedbackpage"),
    path('savefeedback',views.savefeedback,name="savefeedback"),
    path('search/',views.search_results, name="search_results"),
    path('downloadpage/<int:favid>/',views.downloadpage, name="downloadpage"),
    path('download/',views.download, name="download")


]

