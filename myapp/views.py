from django.shortcuts import render,redirect
from .models import User,Doctor,Appointment,Contact
import requests
import random
from django.http import JsonResponse
# Create your views here.

def validate_email(request):
	email=request.GET.get('email')
	data={
		'is_taken':User.objects.filter(email__iexact=email).exists()
	}
	return JsonResponse(data)

def index(request):
	doctors=Doctor.objects.all()
	return render(request,'index.html',{'doctors':doctors})

def doctor_index(request):
	return render(request,'doctor-index.html')

def about(request):
	return render(request,'about.html')

def doctor_about(request):
	user=User.objects.get(email=request.session['email'])
	doctor=Doctor.objects.get(doctor=user)
	return render(request,'doctor-about.html',{'doctor':doctor})

def doctor_appointment(request):
	user=User.objects.get(email=request.session['email'])
	doctor=Doctor.objects.get(doctor=user)
	appointments=Appointment.objects.filter(doctor=doctor,appointment_status="Pending")
	request.session['appointment_count']=len(appointments)
	return render(request,'doctor-appointments.html',{'appointments':appointments})

def doctor_pending_appointment(request):
	user=User.objects.get(email=request.session['email'])
	doctor=Doctor.objects.get(doctor=user)
	appointments=Appointment.objects.filter(doctor=doctor,appointment_status="Pending")
	return render(request,'doctor-appointment.html',{'appointments':appointments})

def doctor_attended_appointment(request):
	user=User.objects.get(email=request.session['email'])
	doctor=Doctor.objects.get(doctor=user)
	appointments=Appointment.objects.filter(doctor=doctor,appointment_status="Attended")
	return render(request,'doctor-appointment.html',{'appointments':appointments})

def doctor_cancelled_appointment(request):
	user=User.objects.get(email=request.session['email'])
	doctor=Doctor.objects.get(doctor=user)
	appointments=Appointment.objects.filter(doctor=doctor,appointment_status="Cancelled")
	return render(request,'doctor-appointment.html',{'appointments':appointments})

def patient_view_prescription(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	return render(request,'patient-view-prescription.html',{'appointment':appointment})

def doctor_profile(request):
	user=User.objects.get(email=request.session['email'])
	doctor=Doctor()
	try:
		doctor=Doctor.objects.get(doctor=user)
	except:
		pass
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		doctor.doctor=user
		doctor.clinic_address=request.POST['clinic_address']
		doctor.qualification=request.POST['qualification']
		doctor.speciality=request.POST['speciality']
		doctor.save()
		msg="Profile Update Successfully"
		return render(request,'doctor-profile.html',{'user':user,'doctor':doctor,'msg':msg})
	else:
		return render(request,'doctor-profile.html',{'user':user,'doctor':doctor})

def service(request):
	return render(request,'service.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				subject=request.POST['subject'],
				message=request.POST['message']
			)
		msg="Contact Saved Successfully"
		return render(request,'contact.html',{'msg':msg})
	else:
		return render(request,'contact.html')

def price(request):
	return render(request,'price.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						usertype=request.POST['usertype'],
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic']
					)
				msg="User Sign Up Successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password & Confirm Password Does Not Matched"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			print(user)
			if user.password==request.POST['password']:
				if user.usertype=="patient":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					return redirect('index')
				else:
					doctor=Doctor.objects.get(doctor=user)
					appointments=Appointment.objects.filter(doctor=doctor,appointment_status="Pending")
					print(appointments)
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					request.session['appointment_count']=len(appointments)
					return render(request,'doctor-index.html')
			else:
				msg="Incorrect Password"		
				return render(request,'login.html',{'msg':msg})
		except Exception as e:
			print(e)
			msg="Email Not Registered"		
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def book_appointment(request,pk):
	doctor=Doctor.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		Appointment.objects.create(
				doctor=doctor,
				user=user,
				date=request.POST['date'],
				time=request.POST['time'],
				health_issue=request.POST['health_issue']
			)
		msg="Appointment Booked Successfully"
		url = "https://www.fast2sms.com/dev/bulkV2"
		querystring = {"authorization":"DwF5Auzh16qo3fXC2JMSTcOiyBEZmWH0eR8GIg4NbQrpUnKsjvhz0YwyOCGvHJEFuXRrTc7feDVaM1NA","message":"Appointment Booked Successfully","language":"english","route":"q","numbers":str(user.mobile)}
		headers = {
		    'cache-control': "no-cache"
		}
		response = requests.request("GET", url, headers=headers, params=querystring)
		return render(request,'appointment.html',{'doctor':doctor,'user':user,'msg':msg})
	else:
		return render(request,'appointment.html',{'doctor':doctor,'user':user})

def patient_appointment(request):
	user=User.objects.get(email=request.session['email'])
	appointments=Appointment.objects.filter(user=user)
	return render(request,'patient-appointment.html',{'appointments':appointments})

def patient_cancel_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	if request.method=="POST":
		appointment.cancel_reason=request.POST['cancel_reason']
		appointment.appointment_status="Cancelled"
		appointment.save()
		msg="Appointment Cancelled Successfully"
		return render(request,'patient-cancel-appointment.html',{'appointment':appointment,'msg':msg})
	else:
		return render(request,'patient-cancel-appointment.html',{'appointment':appointment})

def doctor_attend_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	if request.method=="POST":
		appointment.prescription=request.POST['prescription']
		appointment.appointment_status="Attended"
		appointment.save()
		return redirect('doctor-appointment')
	else:
		return render(request,'doctor-attend-appointment.html',{'appointment':appointment})

def forgot_password(request):
	if request.method=="POST":
		try:
			otp=random.randint(1000,9999)
			user=User.objects.get(email=request.POST['email'])
			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"DwF5Auzh16qo3fXC2JMSTcOiyBEZmWH0eR8GIg4NbQrpUnKsjvhz0YwyOCGvHJEFuXRrTc7feDVaM1NA","variables_values":str(otp),"route":"otp","numbers":str(user.mobile)}
			headers = {
			    'cache-control': "no-cache"
			}
			response = requests.request("GET", url, headers=headers, params=querystring)
			msg="Please Enter OTP Sent To Your Mobile"
			return render(request,'otp.html',{'email':user.email,'otp':otp,'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'forgot-password.html',{'msg':msg})
	else:
		return render(request,'forgot-password.html')

def verify_otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']

	if otp==uotp:
		return render(request,'new-password.html',{'email':email})
	else:
		msg="Invalid OTP"
		return render(request,'otp.html',{'email':email,'otp':otp,'msg':msg})

def new_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(email=email)
		user.password=np
		user.save()
		msg="Password Updated Successfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="New Password & Confirm New Password Does Not Matched"
		return render(request,'new-password.html',{'email':email,'msg':msg})