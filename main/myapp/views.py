from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Contact,Profile,Dish,Order,Team,Booking,Reviews,Category
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate



# Create your views here.
def home(request):
    team_members = Team.objects.all()
    reviews = Reviews.objects.all()
    menu = Dish.objects.all()
    category = Category.objects.all()
    
    print(reviews)
    return render(request,'index.html',context={"team_members":team_members,'reviews':reviews,'menu':menu,'category':category})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name,email,subject,message)
        Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
            
        )
        
        messages.success(request, f"Dear {name}, Thanks for your time.")
        
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')

def register(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        contact = request.POST.get('number')
        
        print(name,email,password,contact)
        try:
            usr = User.objects.create_user(email,email,password)
            usr.first_name = name
            usr.save()

            profile = Profile(user=usr,contact_number=contact)
            profile.save()
            context['status'] = f"User '{name}' registered successfully!"
        except Exception as e:
            context['status'] = f"User with this email already exists."
                   
    return render(request,'register.html',context)

def check_user_exist(request):
    email = request.GET.get('usern')
    check = User.objects.filter(username=email)
    if len(check)==0:
        return JsonResponse({'status':0,'message':'Not Exists'})
    else:
        return JsonResponse({'status':1,'message':'A user with this email already exist!'})
    
def signin(request):
    context={}
    if request.method == 'POST':
        email = request.POST.get('email')
        passw = request.POST.get('password')
        
        check_user = authenticate(username=email,password=passw)
        if  check_user:
            login(request,check_user)
            if check_user.is_superuser or check_user.is_staff:
                return redirect('/admin/')
            return redirect('/dashboard')
            context.update({'message':'Login success!','class':'alert-success'})
        else:
            context.update({'message':'Invalid Login Details!','class':'alert-danger'})
            
    return render(request,'login.html',context)

def dashboard(request):
    # fetch user details
    context={}
    login_user = get_object_or_404(User,id=request.user.id)
    profile = Profile.objects.get(user__username=request.user.username)
    context['profile']=profile
    
    # Update profile
    if "update_profile" in request.POST:
        name = request.POST.get('name')
        contact = request.POST.get('contact_number')
        add = request.POST.get('address')
        pic = request.FILES.get('profile_pic')
        
        profile.user.first_name = name
        profile.user.save()
        profile.contact_number = contact
        profile.address = add
        profile.save()
        
        if "profile_pic" in request.FILES:
            pic =  request.FILES.get('profile_pic')
            profile.profile_pic = pic
            profile.save()
        
        context['status'] = 'Profile updated successfully!'
        
    # Change password
    if "change_pass" in request.POST:
        c_password = request.POST.get('current_password')
        n_password = request.POST.get('new_password')
        print(c_password,n_password)
       

        check = login_user.check_password(c_password)
        if check==True:
            login_user.set_password(n_password)
            login_user.save()
            login(request, login_user)
            context['status'] = 'Password Updated Successfully!' 
        else:
            context['status'] = 'Current Password Incorrect!'
            
    # My Orders - 
    orders = Order.objects.filter(customer__user__id=request.user.id )
    context['orders'] = orders
                
                
        
    return render(request,'dashboard.html',context)

def user_logout(request):
    logout(request)
    return redirect('/')

def all_dishes(request):
    context={}
    dishes = Dish.objects.all()
    print(dishes)
    
    return render(request,'all_dishes.html',context={'dishes':dishes})

def team(request):
    team_members = Team.objects.all()
    print(team_members)
    return render(request,'team.html',context={'team_members':team_members})

def book_table(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        time = request.POST.get('time')
        print(name,email,contact,date,time)
        booking = Booking.objects.create(
            name=name,
            email=email,
            contact=contact,
            date=date,
            time=time
        )
        booking.save()
       
    
    return render(request,'book_table.html')

def review(request):
    if request.method=='POST':
        name=request.POST.get('name')
        profession=request.POST.get('profession')
        feedback=request.POST.get('feedback')
        image=request.FILES.get('image')
        print(image)
        
        Reviews.objects.create(name = name,
                               profession = profession,
                               feedback = feedback,
                               image=image)
        review = Reviews.objects.all()
        messages.info(request, f"Dear {name}, Your review is added, Thanks for your time.")
        return redirect('/',context={'review':review})
    
        
    return render(request,'review.html',context={'review':Reviews.objects.all()})

def viewmenu(request,category):
    menu = Dish.objects.all().filter(category=category)

    return render(request,'viewmenu.html',context={'menu':menu})