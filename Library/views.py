# from django.shortcuts import render
from datetime import date,timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from Library.models import Users
from Library.models import Books
from django.views.decorators.csrf import csrf_exempt
# from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.mail import send_mail
# from Library.models import available_books
# from Library.models import book_transaction
def Library(request):
    # if request.user.is_anonymous:
    #     return redirect('/login')
    return render(request,'home.html')






def add_user(request):
    # Users.objects.all().delete()
    return render(request,'User/add_user.html')
@ csrf_exempt
def create_user(request):
    
    first_name=request.POST["first_name"]
    last_name=request.POST["lastname"]
    user_name=first_name+" "+last_name
    email=request.POST["email"]
    gender=request.POST["gender"]
    mobile_no=request.POST["mob"]
    category=request.POST["category"]
    user_id=request.POST["user_id"]
    limit = 0
    duration=0
    penalty=0
    count=0
    if category=="Under Graduate":
        limit=2
        duration=1
    elif category=="Post Graduate":
        limit=4
        duration=1
    elif category=="Research Scholar":
        limit=6
        duration=3
    elif category=="Faculty Member":
        limit=10
        duration=6

    Users.objects.create(user_name=user_name,gender=gender,email=email,mobile=mobile_no,catagory=category,limit=limit,duration=duration,penalty=penalty,count=count,user_id=user_id)
    return HttpResponseRedirect("/")




def all_user(request):
    use = Users.objects.all()
    context = {'users':use}
    return render(request,'User/all_user.html',context)

def home(request):
    return render(request,'home.html')



def books(request): 
    allbooks = Books.objects.all()
    context = {'book':allbooks}
    return render(request,'books.html',context)

# def add_book_to_user(request):
#     id = request.POST['id']
#     user_id = Users.objects.filter(pk=id).values_list("user_id").get()[0]
#     isbn = request.POST['isbn']
#     title = available_books.objects.filter(ISBN=isbn).values_list("title").get()[0]
#     issue_date = date.today()
#     deadline = issue_date - timedelta(days=1)
#     count = Users.objects.filter(pk=id).values_list("count").get()[0]
#     limit = Users.objects.filter(pk=id).values_list("limit").get()[0]
#     if count < limit:
#         book_transaction.objects.create(user_id=Users.objects.get(id=id),ISBN=isbn,title = title,issue_date = issue_date,deadline=deadline)
#         available_books.objects.filter(ISBN=isbn).delete()
#         book_added = Books.objects.get(title = title)
#         book_added.copies -= 1
#         book_added.save()
#         u = Users.objects.get(pk=id)
#         u.count += 1
#         u.save()
#     book_issued = book_transaction.object.filter(user_id=user_id)
#     name = Users.objects.get(pk=id).user_name.split()[0]
#     user = {"user":Users.objects.get(pk=id),"name":name,"book_issud":book_issued}
#     return render(request,"user/profile_view.html",user)

@ csrf_exempt
def view_book(request):
    id = request.POST['id']
    book_id = Books.objects.get(pk=id)
    context = {'book':book_id}
    
    return render(request,'bookProfile.html',context)

@csrf_exempt
def send_book(request):
    user_id = request.POST['user_id']
    id = request.POST['id']
    eu = Users.objects.get(user_id = user_id)
    email = eu.email
    print(email)
    books = Books.objects.get(pk=id)
    title = books.title
    print(title)
    print(str(books.ebook_url))
    send_mail("E-book test dev/config","You can download the book ","website.tester.django@gmail.com",[email],fail_silently=True)
    # print(str(books.ebook_url))
    # send_mail("E-book test dev/config","You can download the book "+str(title)+" from the following link "+ 
    # str(books.ebook_url),"website.tester.django@gmail.com",[email],fail_silently=True)
    # print("Sending Email")
    # mail_title = title
    # message = 'This is a test email.' 
    # recipients = email
    # emailu = settings.DEFAULT_FROM_EMAIL
    # send_mail(mail_title, message, emailu, recipients, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD) 
    # print("Email Sent")


    return render(request,'books.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username)
        print(password)
        print(user)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect(request,'book.html')
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/login")



@ csrf_exempt
def edit_user(request):
    userid=request.POST["edit_user_detail"]
    name=Users.objects.get(pk=userid).user_name.split()
    if(len(name)==1):
        name.append(" ")
    user={"user":Users.objects.get(pk=userid),"firstname":name[0],"lastname":name[1]}
    return render(request,"user/edit_user.html",user)
@ csrf_exempt
def update_user(request):
    id=request.POST["id"]
    user=Users.objects.get(pk=id)
    user.email=request.POST["email"]
    user.mobile=request.POST["mob"]
    user.save()
    # return HttpResponseRedirect("User/all_user.html")
    return redirect("/all_user")


@ csrf_exempt
def profile_view(request):
    id=request.POST["id"]
    name=Users.objects.get(pk=id).user_name.split()[0]
    user_id=Users.objects.filter(pk=id).values_list("user_id").get()[0]
    # books_issued=book_transaction.objects.filter(user_id=user_id)
    user={"user":Users.objects.get(pk=id),"name":name}
    return render(request,"user/profile_view.html",user)
    # ,"book_issued":books_issued