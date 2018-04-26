from django.shortcuts import render
from .models import *

def home(request):
    return render (request, 'home.html', )

def bank(request):
	if request.method == 'POST':
		name =request.POST['name']
		city =request.POST['city']                
													
		bank_name = Banks.objects.get( name=name )
		b_id = bank_name.id
		bank_details = Branches.objects.filter(bank=b_id, city=city)

		return render(request,'bank_info.html', { 'bank_details' : bank_details , 'bank_name' : bank_name })

	return render (request, 'bank.html',)


def branch(request):
	if request.method == 'POST':
		ifsc_code =request.POST['ifsc']
		                
		branch_details = Branches.objects.get(ifsc = ifsc_code)
		bank_name = Banks.objects.get( id=branch_details.bank_id )
		branch_details.name = bank_name.name
		return render(request,'branch_info.html', { 'branch_details' : branch_details})

	return render (request, 'branch.html' ,)