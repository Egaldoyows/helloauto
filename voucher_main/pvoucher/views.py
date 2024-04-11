from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.db.models import Q
from .models import Notes,Projects,Vouchers
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    note_list=Notes.objects.all()
    show='only unread'
    act='Show all messages?'
    return render(request,'home.html',{'note_list':note_list,'show':show,'act':act})




def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                mess='Username Exists'
                return redirect('login-page')
            
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=uname,email=email,password=password)
                user.set_password(password)
                user.save()
                mess='Registration successfull'
        else:
            mess='Passwords did not match'
        
    else:
        mess='Didnt receive data'
    
        
    return render(request,'accounts/register.html',{'message': mess})


#user login view
def login(request):
    return render(request,'accounts/login.html',{})

data_dict=User.objects.all()

#Create new Message

def  newnote(request):
    
    notes =Notes
    if request.method=='POST':
        subject=request.POST['sub']
        body=request.POST['body']
        audience= request.POST['aud']
        if Notes.objects.filter(subject=subject).exists():
            return render(request,'notes/newnote.html',{'mess':'Ooops! A note with similar subject exists' ,'list':data_dict})
            
            
        else:
            note=Notes.objects.create(subject=subject,body=body,audience=audience)
            
            messages.info(request,'Note created')
            return render(request,'notes/newnote.html',{'mess':'New Notice Saved Successfully','list':data_dict})

    else:
        return render(request,'notes/newnote.html',{'list':data_dict})
    
    #View one message
def noteView(request):
    query = request.GET['data']
    mynote=Notes.objects.filter(pk=query)
    return render(request,'notes/mynote.html',{ 'mynote':mynote})

#view one Voucher

def voucherView(request):
    vid=request.GET['id']
    voucher=Vouchers.objects.filter(id=vid)
    return render(request,'vouchers/voucher.html',{'voucher':voucher})

def vlistview(request):
    if request.method=='POST':
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        unsigned=Vouchers.objects.all().count()
        vlist=Vouchers.objects.filter(payment_date__range=(startdate, enddate)).order_by('-payment_date')
        return render(request,'vouchers/voucherlst.html',{'vlist':vlist,'start':startdate,'end':enddate,'vlist':vlist, 'unsigned':unsigned})
    else:
    
        vlist=Vouchers.objects.order_by('-date_created')[:5]
        if vlist is not None:
            unsigned=Vouchers.objects.all().count()
            return render(request,'vouchers/voucherlst.html',{'vlist':vlist,'unsigned':unsigned})
        else:
            feedback= "No vouchers to show"
            return render(request,'vouchers/voucherlst.html',{'feedback':feedback})
    
def deleteV(request):
    if request.method=='GET':
        id=request.GET['id']
        Vouchers.objects.filter(id=id).delete()
        feedback='Voucher Deleted, Go back'
        return render(request,'vouchers/voucherlst.html',{'feedback':feedback})
    
    else:
        feedback='Sorry, Could not delete Voucher, Please try again'
        return render(request,'vouchers/voucherlst.html',{'feedback':feedback})

    

    

def createVoucher(request):
    people=User.objects.filter(is_staff=False)
    new_voucher=Vouchers
    if request.method=='POST':
        source=request.POST['source']
        recp=request.POST['recp']
        acc=request.POST['acc']
        mode=request.POST['mode']
        proj=request.POST['proj']
        desc1=request.POST['desc1']
        desc2=request.POST['desc2']
        desc3=request.POST['desc3']
    
        
        amnt1=request.POST['amnt1']
        amnt2=request.POST['amnt2']
        amnt3=request.POST['amnt3']
        
        inv=request.POST['inv']
        p_date=request.POST['date']
        Comment=request.POST['comment']
        approved=request.POST['approved']
        prepared=request.POST['prepared']
        company=request.POST['company']
        
        
        if 'KES' in source:
            currency='KES'
            
        elif 'USD' in source:
            currency = 'USD'
        else:
            currency = 'None'
            
        if desc2:
            descript2 = desc2
        else:
            descript2 = ""
            
        if desc3:
            descrip3=desc3
        else:
            descrip3 = ""
            
            
        if amnt2:
            amoun2 = amnt2
        else:
            amoun2 = int()
            
        if amnt3:
            amoun3=amnt3
        else:
            amoun3 = int()
            
            
        total= int(amnt1)+int(amoun2)+int(amoun3)
            
            
    
            
            
   
        new_voucher=Vouchers.objects.create(receipient=recp,account=acc,desc1=desc1,desc2=descript2,desc3=descrip3,amount1=amnt1,amount2=amoun2,amount3=amoun3,total=total,payment_mode=mode,project=proj,currency=currency,invoice_no=inv,payment_date=p_date,prepared=prepared,approved=approved,company=company,comment=Comment)
        new_voucher.save()
        feedback='SUCCESS! Voucher saves Successfully'
        
        return render(request,'vouchers/createvoucher.html',{'people':people,'feedback':feedback})
        
        
        
        
    else:
        feedback='FAILED! The Voucher was not saves, Please Try again'
        return render(request,'vouchers/createvoucher.html',{'people':people})
    
    
    
    
    
    
        
        
    



    
    
    
