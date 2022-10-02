import os
from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from shop.models import *

# Create your views here.
def home(request):
    prd = Product.objects.all()
    return render(request,'home.html',{"prd":prd})

def Eadmin(request):
    return render(request,"admin.html")

def Euser(request):
    crt = User.objects.get(username=us_name)
    return render(request,'customr.html',{'crt':crt})

def loginpage(request):
    return render(request,'Login.html')

def signuppage(request):
    return render(request,'signup.html')

def add_product(request):
    catg = Category.objects.all()
    return render(request,'admin/aproduct.html',{'catg':catg})

def showproduct(request):
    scatg = Category.objects.all()
    sprd = Product.objects.all()
    return render(request,'admin/sproduct.html',{'cat':scatg,'prod':sprd})

def edit_product(request,od):
    ecatg = Category.objects.all()
    prd = Product.objects.get(id=od)
    return render(request,'admin/eproduct.html',{'ecatg':ecatg,'prod':prd})

def add_category(request):
    return render(request,'admin/acategory.html')

def show_category(request):
    catgry = Category.objects.all()
    return render(request,'admin/shocateg.html',{'catg':catgry})

def edit_category(request,od):
    catgry = Category.objects.get(id=od)
    return render(request,'admin/ecategory.html',{'catg':catgry})

def show_user(request): #admin.....
    usr = Customer.objects.all()
    return render(request,'admin/showusers.html',{'user':usr})

def uprofile(request):
    data = User.objects.get(username=us_name)
    print(data)
    global data1
    data1= Customer.objects.get(c_user=data)
    print(data1)
    return render(request,'customer/profile.html',{'data':data, 'data1':data1})   


@login_required(login_url='loginpage')
def cart(request):
    usr = User.objects.get(username=us_name)
    ctm = Customer.objects.get(c_user = usr)
    print(ctm)
    return render(request,'cart.html',{'cart1':ctm})

us_name = ''
def Login(request):
    if request.method == 'POST':
        global us_name
        u_name = request.POST['logname']
        us_name = u_name
        pawd = request.POST['passw']
        log= auth.authenticate(username = u_name, password = pawd)
        if log is not None:
            if log.is_staff:
                auth.login(request,log)
                return redirect('Eadmin')
            else:
                auth.login(request,log)
                return redirect('Euser')
        else:
            print("User name or password does not match. Try again.")
            return redirect('Login')

def Signup(request):
    if request.method == 'POST':
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        usernam= request.POST['uname']
        e_mail = request.POST['E-mail']
        pnum = request.POST['tphone']
        paswd = request.POST['pswd']
        cpaswd = request.POST['cpswd']
        if paswd == cpaswd:
            if User.objects.filter(password = paswd).exists():
                print("This user name already exists")
                return redirect('signuppage')
            else:
                user = User.objects.create_user(username=usernam, first_name=Fname,
                            last_name=Lname,email=e_mail,
                            password=paswd)
                user.save()
                customer=User.objects.get(username=usernam) # for adding id in foriegn key column
                custm = Customer(First_name=Fname,Last_name=Lname,
                        Phone_numbr=pnum, E_mail=e_mail,c_user=customer)
                custm.save()
                return redirect('home')
        else:
            print("password id not matc try agian!")
            return redirect('home')

def eprofile(request):
    if request.method=='POST':
        us = User.objects.get(username=us_name)
        us.first_name=request.POST['pfname']
        us.last_name=request.POST['plname']
        us.save()
        #cust = Customer.objects.get(c_user=us)
        data1.First_name = request.POST['pfname']
        data1.Last_name = request.POST['plname']
        data1.Phone_numbr = request.POST['phnmbr']
        data1.Address = request.POST['adds']
        data1.Landmark = request.POST['lmark']
        data1.Pincode = request.POST['code']

        try:
            if len(request.FILES)!=0:
                try:
                    if len(data1.photo)>0:
                        os.remove(data1.photo.path)
                    data1.S_Photo = request.FILES['pht']
                except:
                    None
                data1.photo = request.FILES['pht']
        except:
            data1.photo = request.FILES['pht']

        data1.save()
        return redirect('Euser')

def a_category(request):
    if request.method == 'POST':
        pcatg = request.POST['pcatgr']
        catg = Category(product_category= pcatg)
        catg.save()
        return redirect('add_category')

def e_category(request,od):
    if request.method == 'POST':
        catg = Category.objects.get(id=od)
        catg.product_category = request.POST['npcatgr']
        catg.save()
        return redirect('show_category')


def a_product(request):
    if request.method == 'POST':
        pname = request.POST['prname']
        pdes = request.POST['prdesc']
        pprice = request.POST['prprice']
        pstock = request.POST['prstock']
        pimg = request.FILES['primg']
        catg = request.POST['adcatg']
        cat = Category.objects.get(id=catg)

        add = Product(Product_name=pname,Product_detail=pdes,
        Product_price=pprice,Product_stock=pstock,Product_img=pimg,catgr=cat
        )
        add.save()
        return redirect('add_product')

def e_product(request,od):
    if request.method == 'POST':
        prod = Product.objects.get(id=od)
        prod.Product_name = request.POST['nprname']
        prod.Product_detail = request.POST['nprdesc']
        prod.Product_price = request.POST['nprprice']
        prod.Product_stock = request.POST['nprstock']
        prod.Product_img = request.FILES['nprimg']
        catg = request.POST['nadcatg']
        cat = Category.objects.get(id=catg)
        prod.catgr = cat
        prod.save()
        return redirect('showproduct')

@login_required(login_url='loginpage')
def add_cart(request,od):
    prdt = Product.objects.get(id=od)
    usr = User.objects.get(username=us_name)
    cut = Customer.objects.get(c_user=usr)
    cart = Cart(user=usr,product=prdt)
    cart.save()
    cut.cart=cart
    cut.save()
    return redirect('cart')

def delete_product(request,od):
    delt = Product.objects.get(id=od)
    delt.delete()
    return redirect('showproduct')


def deletecust(request,od):
    cust = Customer.objects.get(id=od)
    catm = cust.c_user.id
    usr = User.objects.get(id=catm)
    usr.delete()
    cust.delete()
    return redirect("show_user")


@login_required(login_url='loginpage')
def Logout(request):
    auth.logout(request)
    global us_name
    us_name =''
    return redirect('home')