from django.shortcuts import render,redirect
from .models import Product,BussinessCustomer,Order
from django.http import HttpResponse
import logging
#
# from django.core.mail import send_mail
#
# send_mail('subject', 'body of the message', 'sender@example.com', ['receiver1@example.com', 'receiver2@example.com'])



db_logger = logging.getLogger('db')
# db_logger = logging.getLogger('db')
db_logger.info('info message')
db_logger.warning('warning message')

try:
    1/0
except Exception as e:
    db_logger.exception(e)





# FOR SHOWING ALL OPTIONS
def Home(request):
    return render(request,'home.html')
    # product_list = Product.objects.all()
    # return render(request,'order.html',{"product":product_list})

# FOR REGISTERING PRODUCT\
def register_product(request):
    if request.method == "POST":
        id = request.POST["id"]
        print(id)
        name = request.POST.get("name")
        cost = request.POST.get("cost")
        exp = request.POST.get("exp")
        qty= request.POST.get("qty")
        obj = Product(id=id, pname=name, pcost=cost, pexpd=exp,quantity=qty)
        print(obj)
        obj.save()
        return render(request,'padded.html')
    return render(request, 'pregister.html')

# FOR REGISTERING BUSSINESS CUSTOMER
def register_bcustmer(request):
    context= {"f": "Welcome to Register Customer"}
    if request.method == "POST":
        bcid = request.POST['bcid']
        name = request.POST['cname']
        email = request.POST['email']
        add = request.POST['add']
        pwd1 = request.POST['p']
        pwd2 = request.POST['c']
        if pwd1==pwd2:
            obj = BussinessCustomer(bcid= bcid,cname=name ,cemail=email ,cadd=add,pwd=pwd1,cpwd=pwd2)
            obj.save()
            # return redirect("login_bcustomer")
            return render(request,"login.html",{"rs": "Registration successful!! Please "})
        else:
            context ={'msg' :"Password did not Match","try":"Try again"}
            return render(request,"bregister.html",context)

    return render(request, 'bregister.html',context)

def login_bcustomer(request):
    if request.method =="POST":
        username = request.POST['un']
        pwd = request.POST['pw']

        qs= BussinessCustomer.objects.filter(cname= username,pwd=pwd)
        if len(qs)!=0:
            return render(request,"lhome.html")  #login success html page
        else:
            context= {"msg": " Failed !! Invalid credentials Try again"}
            return render(request,"login.html",context)
    return render(request,'login.html')

## FOR  CONTROLING  WHOLE ORDER
def view_product(request):
    product_list = Product.objects.all()
    return render(request,'order.html',{"product":product_list})


# def product_delete(request,p_id):
#     d= Product.objects.get(id=p_id)
#     d.delete()
#     return redirect(order_product)

def product_delete(request):
    if request.method=="POST":
        did = request.POST["pid"]
        d= Product.objects.filter(id=did)

        d.delete()
        return redirect("view_product")
    
    return render(request,"delete.html")



def update_product(request,pid):
    update_product = Product.objects.get(id=pid)
    if request.method=="POST":

        ncost = request.POST["cost"]
        nqty = request.POST["qty"]
        obj= Product.objects.filter(id=pid).update(pcost=ncost,quantity=nqty)


        product_list = Product.objects.all()
        return render(request,'order.html',{"product":product_list,"msg":"PRODUCT UPDATED !!!"})

        # return redirect("view_product")
    return render(request,"update.html",{"up": update_product})

def payment(request):
    if request.method =="POST":
        name= request.POST.get('name')
        amount = int(request.POST.get('amount'))*100
        email = request.POST.get("email")
        client = razorpay.Client(auth =("rzp_test_rD0wv59lvmLapP","ajYc8euRPGfd31WCxgmP8NZN"))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        coffe = Coffe(name=name,amount=amount,email=email,payment_id = payment['id'],)
        coffe.save()
        return render(request,'payment.html',{'payment':payment})
    return render(request,"payment.html")
########################## UNDER WORKING      W  O   P
# def ordered(request):
#     if request.method=="POST":
#         pid = request.POST["pid"]
#         qty = request.POST["qty"]
#         qtyi=int(qty)
#         obj = Product.objects.get(id=pid)
#         print("----",obj)
#
#         return render(request,"osuccess.html")
#     # o = Order.objects.get(product_id=o_id)
#     return render(request,"osuccess.html")

# def ordered(request,oid):
#     # print(oid)
#     if request.method=="POST":
#         newc = request.POST["ncost"]
#         print(newc)
#         u= Product.objects.filter(id=oid).update(pcost=newc)
#         return redirect('order_product')
#     return render(request,"uinput.html")
