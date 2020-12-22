from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.utils import timezone
from django.shortcuts import redirect
from django.db.models import Sum

def index(request):
    return render(request, 'my_app/index.html', {})

def clients_list(request):
    clients = Client.objects.order_by('last_name')

    table = ""
    for client in clients:
        table += """<tr>
            <td>%s %s %s</td>
            <td>%i</td>
        </tr>""" % (client.last_name, client.first_name, client.middle_name if client.middle_name else "", client.policy_number)

    return render(request, 'my_app/clients.html', {'table': table})

def funds_list(request):
    funds = Fund.objects.all()

    table = ""
    for fund in funds:
        table += """<tr>
            <td>%s</td>
            <td>%i</td>
        </tr>""" % (fund.id, fund.balance)
    return render(request, 'my_app/funds.html', {'table': table})

def contracts_list(request):
    contracts = Contract.objects.order_by('date')

    table = ""
    for contract in contracts:
        table += """<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%i</td>
            <td>%s</td>
            <td>%s</td>
        </tr>""" % (contract.client, contract.fund, contract.insurance_amount, contract.conditions, contract.date)

    return render(request, 'my_app/contracts.html', {'table': table})

def clients_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('clients_list')
    else:
        form = ClientForm()
        return render(request, 'my_app/clients_new.html', {'form': form})

def funds_new(request):
    if request.method == "POST":
        form = FundForm(request.POST)

        if form.is_valid():
            fund = form.save(commit=False)
            fund.save()
            return redirect('funds_list')
    else:
        form = FundForm()
        return render(request, 'my_app/funds_new.html', {'form': form})

def contracts_new(request):
    if request.method == "POST":
        form = ContractForm(request.POST)

        if form.is_valid():
            contract = form.save(commit=False)
            contract.date = timezone.now()
            contract.save()
            return redirect('contracts_list')
    else:
        form = ContractForm()
        return render(request, 'my_app/contracts_new.html', {'form': form})
