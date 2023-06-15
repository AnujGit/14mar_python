from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        scount = SocietyMember.objects.all().count()
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            context = {'uid' : uid, 'cid' : cid, 'scount': scount}
            return render(request,"Chairman/index.html", context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            context = {'uid' : uid, 'sid' : sid, 'scount': scount}
            return render(request,"Chairman/s_index.html", context)
    else:
        return render (request, "chairman/login.html")  

def login(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        scount = SocietyMember.objects.all().count()
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            context = {'uid' : uid, 'cid' : cid, 'scount': scount}
            return render(request,"Chairman/index.html", context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            context = {'uid' : uid, 'sid' : sid, 'scount': scount}
            return render(request,"Chairman/s_index.html", context)

    scount = SocietyMember.objects.all().count()
    if request.POST:
        p_email = request.POST['email']
        p_password = request.POST['password']

        try:
            uid = User.objects.get(email = p_email)
            if uid.password == p_password:
                if uid.role == 'chairman':
                    request.session['email'] = uid.email
                    cid = Chairman.objects.get(user_id = uid)
                    context = {'uid' : uid, 'cid' : cid, 'scount': scount}
                    return render(request,"Chairman/index.html", context)
                else:
                    request.session['email'] = uid.email
                    sid = SocietyMember.objects.get(user_id = uid)
                    context = {'uid' : uid, 'sid' : sid, 'scount': scount}
                    return render(request,"Chairman/s_index.html", context)
        except:
            msg = "Invalid Email. Please try again"
            context = {'msg' : msg}
            return render(request,"Chairman/login.html",context)
        else:
            msg = "Invalid Password. Please try again"
            context = {'msg' : msg}
            return render(request,"Chairman/login.html",context)
    else:
        print("Refreshed")
    return render(request,"Chairman/login.html")

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,"Chairman/login.html")
    else:
        return render(request,"Chairman/login.html")
    
def signup(request):
    return render(request,"Chairman/regi ster.html")

def forgotpassword(request):
    return render(request,"Chairman/forgot-password.html")

def profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            context = {'uid' : uid, 'cid' : cid}
            return render(request,"Chairman/c_profile.html", context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            context = {'uid' : uid, 'sid' : sid}
            return render(request,"Chairman/s_profile.html", context)
    else:
        return render (request, "chairman/login.html")  
    
def changepassword(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        cpassword = request.POST['currentpassword']
        npassword = request.POST['newpassword']
        if cpassword == uid.password:
            uid.password = npassword
            uid.save()
            msg = "Password Changed Successfully"
            del request.session['email']
            context = {'msg':msg}
            return render (request, "chairman/login.html", context)
        else:
            msg = "Invalid Current Password"
            if uid.role == 'chairman':
                cid = Chairman.objects.get(user_id = uid)
                context = {'uid' : uid, 'cid' : cid, 'msg':msg}
                return render(request,"Chairman/c_profile.html", context)
            else:
                sid = SocietyMember.objects.get(user_id = uid)
                context = {'uid' : uid, 'sid' : sid, 'msg':msg}
                return render(request,"Chairman/s_profile.html", context)
    else:
        return render (request, "chairman/login.html")
    
def updateprofile(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            if request.POST:
                cid.firstname = request.POST['firstname']
                cid.lastname = request.POST['lastname']
                cid.house_no = request.POST['house_no']
                cid.contact_no = request.POST['contact_no']
                
                if 'mypicture' in request.FILES:
                    cid.pic = request.FILES['mypicture']
                    cid.save()

                cid.save()
                msg = "Profile Updated Successfully"
            context = {'uid':uid, 'cid':cid, 'msg':msg}
            return render(request,"Chairman/c_profile.html", context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            if request.POST:
                sid.firstname = request.POST['firstname']
                sid.lastname = request.POST['lastname']
                sid.house_no = request.POST['house_no']
                sid.contact_no = request.POST['contact_no']

                if 'mypicture' in request.FILES:
                    sid.pic = request.FILES['mypicture']
                    sid.save()

                sid.save()
                msg = "Profile Updated Successfully"
            context = {'uid' : uid, 'sid' : sid, 'msg':msg}
            return render(request,"Chairman/s_profile.html", context)
    else:
        return render (request, "chairman/login.html")  
    
def add_media(request): 
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            if request.POST:
                medianame = request.POST['medianame']
                mediafile = request.FILES['mediafile']
                if medianame == "video" or medianame == "Video":
                    eid = EventGallery.objects.create(user_id = uid, media_type = medianame, video=mediafile)
                    msg = "Video successfully uploaded"
                else:
                    eid = EventGallery.objects.create(user_id = uid, media_type = medianame, pic=mediafile)
                    msg = "Image successfully uploaded"

                context = {'uid':uid, 'cid':cid, 'msg':msg}
                return render(request,"Chairman/add_media.html", context)
            else:
                context = {'uid':uid, 'cid':cid}
                return render(request,"Chairman/add_media.html", context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            if request.POST:
                medianame = request.POST['medianame']
                mediafile = request.FILES['mediafile']
                if medianame == "video" or medianame == "Video":
                    eid = EventGallery.objects.create(user_id = uid, media_type = medianame, video=mediafile)
                    msg = "Video successfully uploaded"
                else:
                    eid = EventGallery.objects.create(user_id = uid, media_type = medianame, pic=mediafile)
                    msg = "Image successfully uploaded"
                mem = 'Member'
                context = {'uid':uid, 'sid':sid, 'msg':msg,'mem':mem}
                return render(request,"Chairman/add_media.html", context)
            else:
                mem = 'Member'
                context = {'uid':uid, 'sid':sid,'mem':mem}
                return render(request,"Chairman/add_media.html", context)
    else:
        return render (request, "chairman/login.html")
    
    
def image_gallery(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            all_images = EventGallery.objects.filter(media_type = "Image")
            context = {'uid':uid, 'cid':cid, 'all_images':all_images}
            return render(request,"Chairman/image_gallery.html", context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            all_images = EventGallery.objects.filter(media_type = "Image")
            mem = 'Member'
            context = {'uid':uid, 'sid':sid, 'all_images':all_images,'mem':mem}
            return render(request,"Chairman/image_gallery.html", context)
    else:
        return render (request, "chairman/login.html")
    
def video_gallery(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            all_videos = EventGallery.objects.filter(media_type = "Video")
            context = {'uid':uid, 'cid':cid, 'all_videos':all_videos}
            return render(request,"Chairman/video_gallery.html", context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            all_videos = EventGallery.objects.filter(media_type = "Video")
            mem = 'Member'
            context = {'uid':uid, 'sid':sid, 'all_videos':all_videos, 'mem':mem}
            return render(request,"Chairman/video_gallery.html", context)
    else:
        return render (request, "chairman/login.html")
     
def deletevideo(request,pk):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            videoid = EventGallery.objects.get(id=pk)
            videoid.delete()
            all_videos = EventGallery.objects.filter(media_type = "Video")
            context = {'uid':uid, 'cid':cid, 'all_videos':all_videos}
            return render(request,"Chairman/video_gallery.html", context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            videoid = EventGallery.objects.get(id=pk)
            videoid.delete()
            all_videos = EventGallery.objects.filter(media_type = "Video")
            mem = 'Member'
            context = {'uid':uid, 'sid':sid, 'all_videos':all_videos, 'mem':mem}
            return render(request,"Chairman/video_gallery.html", context)
    else:
        return render (request, "chairman/login.html")
    

def deleteimage(request,pk):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            imageid = EventGallery.objects.get(id=pk)
            imageid.delete()
            all_images = EventGallery.objects.filter(media_type = "Image")
            context = {'uid':uid, 'cid':cid, 'all_images':all_images}
            return render(request,"Chairman/image_gallery.html", context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            imageid = EventGallery.objects.get(id=pk)
            imageid.delete()
            all_images = EventGallery.objects.filter(media_type = "Image")
            mem = 'Member'
            context = {'uid':uid, 'sid':sid, 'all_images':all_images, 'mem':mem}
            return render(request,"Chairman/image_gallery.html", context)
    else:
        return render (request, "chairman/login.html")    
    
def addmember(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            if request.POST:
                muserid = User.objects.create(email = request.POST['email'],
                                              password = request.POST['password'],
                                              role = "Society Member")
                
                if 'pic' in request.FILES:
                    sid = SocietyMember.objects.create(user_id = muserid,
                                                    
                                                    firstname = request.POST['firstname'],
                                                    lastname = request.POST['lastname'],
                                                    house_no = request.POST['housenumber'],
                                                    contact_no = request.POST['contactnumber'],
                                                    blood_group = request.POST['bloodgroup'],
                                                    job_description = request.POST['jobdescription'],
                                                    work_address = request.POST['jobaddress'],
                                                    no_of_family_address = request.POST['family'],
                                                    vehicle_details = request.POST['vehicledetails'],
                                                    pic = request.FILES['profileimage'])
                else:
                    sid = SocietyMember.objects.create(user_id = muserid,
                                                    
                                                    firstname = request.POST['firstname'],
                                                    lastname = request.POST['lastname'],
                                                    house_no = request.POST['housenumber'],
                                                    contact_no = request.POST['contactnumber'],
                                                    blood_group = request.POST['bloodgroup'],
                                                    job_description = request.POST['jobdescription'],
                                                    work_address = request.POST['jobaddress'],
                                                    no_of_family_address = request.POST['family'],
                                                    vehicle_details = request.POST['vehicledetails'])
                
                msg = "Society Member Created Successfully! "
                mem = 'Member'
                context = {'uid':uid, 'cid':cid, 'msg':msg, 'mem':mem}  
                return render(request,"Chairman/addmember.html", context)
            else:
                return render(request,"Chairman/addmember.html")
        else:
            pass
    else:
            return render (request, "chairman/login.html")   
    

def allmembers(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            allmem = SocietyMember.objects.all()
            context = {'uid':uid, 'cid':cid, 'allmem':allmem}
            return render(request,"Chairman/allmembers.html", context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            allmem = SocietyMember.objects.all().exclude(user_id = uid)
            mem = 'Member'
            context = {'uid':uid, 'sid':sid, 'allmem':allmem, 'mem':mem}
            return render(request,"Chairman/allmembers.html", context)
    else:
        return render (request, "chairman/login.html") 