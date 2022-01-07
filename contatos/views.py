import json
import re

from django.shortcuts import render, redirect
from hubspot import HubSpot
from hubspot.crm.contacts import ApiException, SimplePublicObjectInput

from contatos.entities.contato import Contato
from contatos.forms import ContatoForm
from neurotech.utils import get_env


def autenticacao(request):
    env = get_env()
    return redirect(env.get('HUBSPOT_OAUTH_URL'))


def home(request):
    return render(request, 'contatos/home.html')


def listar_contatos(request):
    # code = request.GET.get('code')
    # api_key = 'd4b55c9c-05ef-4049-b15c-0a7e3b096e2c'
    error = None
    contacts = []
    api_key = request.POST.get('apiKey')
    if api_key is None:
        api_key = request.session.get('api_key')
    if api_key:
        try:
            api_client = HubSpot(api_key=api_key)
            request.session.setdefault('api_key', api_key)
            crm_contacts = api_client.crm.contacts.get_all()

            for crm_contact in crm_contacts:
                contact = Contato(
                    id=crm_contact.id,
                    createdate=crm_contact.created_at,
                    email=crm_contact.properties.get('email'),
                    firstname=crm_contact.properties.get('firstname'),
                    hs_object_id=crm_contact.properties.get('hs_object_id'),
                    lastmodifieddate=crm_contact.updated_at,
                    lastname=crm_contact.properties.get('lastname'),
                )
                contacts.append(contact)
        except ApiException as e:
            error = e
    else:
        error = 'Não foi possível validar a sua API KEY!'
    context = {
        # 'code': code,
        'contacts': contacts,
        'error': error,
    }
    return render(request, 'contatos/contatos.html', context)


def cadastrar_contato(request):
    error = None
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            telefone = form.cleaned_data["telefone"]
            data_aniversario = form.cleaned_data["data_aniversario"]
            peso = form.cleaned_data["peso"]

            api_key = request.session.get('api_key')
            if api_key:
                api_client = HubSpot(api_key=api_key)

                properties = {
                    'email': email,
                    'phone': telefone,
                    'date_of_birth': data_aniversario,
                    'weight': peso,
                }

                simple_public_object_input = SimplePublicObjectInput(properties=properties)
                try:
                    api_key = request.session.get('api_key')
                    api_client = HubSpot(api_key=api_key)
                    api_response = api_client.crm.contacts.basic_api.create(
                        simple_public_object_input=simple_public_object_input
                    )
                    return redirect('listar_contatos')
                except ApiException as e:
                    if e.status == 409:
                        error_message = json.loads(e.body)
                        contact_id = re.findall('\\d+', error_message.get('message'))[0]
                        api_response = api_client.crm.contacts.basic_api.update(contact_id, simple_public_object_input)
                        return redirect('listar_contatos')
            else:
                error = 'API KEY não localizada!'
    else:
        form = ContatoForm(request.POST)
    context = {
        'form': form,
        'isEdit': False,
        'error': error,
    }
    return render(request, "contatos/form_contato.html", context)


def editar_contato(request, pk):
    error = None
    api_key = request.session.get('api_key')
    form = ContatoForm()
    if api_key:
        api_client = HubSpot(api_key=api_key)
        try:
            contato_antigo = api_client.crm.contacts.basic_api.get_by_id(pk)
            initial_data = {
                'id': contato_antigo.id,
                'createdate': contato_antigo.created_at,
                'email': contato_antigo.properties.get('email'),
                'firstname': contato_antigo.properties.get('firstname'),
                'hs_object_id': contato_antigo.properties.get('hs_object_id'),
                'lastmodifieddate': contato_antigo.updated_at,
                'lastname': contato_antigo.properties.get('lastname'),
            }

            form = ContatoForm(request.POST or None, initial=initial_data)
            form.fields['email'].widget.attrs['readonly'] = True
            if request.method == 'POST':
                if form.is_valid():
                    telefone = form.cleaned_data["telefone"]
                    data_aniversario = form.cleaned_data["data_aniversario"]
                    peso = form.cleaned_data["peso"]

                    properties = {
                        'phone': telefone,
                        'date_of_birth': data_aniversario,
                        'weight': peso,
                    }

                    simple_public_object_input = SimplePublicObjectInput(properties=properties)
                    api_response = api_client.crm.contacts.basic_api.update(pk, simple_public_object_input)
                    return redirect('listar_contatos')
        except ApiException as e:
            error = f'Erro: {e}'
    else:
        error = 'API KEY não localizada!'
    context = {
        'form': form,
        'isEdit': True,
        'error': error,
    }
    return render(request, "contatos/form_contato.html", context)


def remover_contato(request, pk):
    error = None
    api_key = request.session.get('api_key')
    form = ContatoForm()
    if api_key:
        api_client = HubSpot(api_key=api_key)
        try:
            contato_antigo = api_client.crm.contacts.basic_api.get_by_id(pk)
            initial_data = {
                'id': contato_antigo.id,
                'createdate': contato_antigo.created_at,
                'email': contato_antigo.properties.get('email'),
                'firstname': contato_antigo.properties.get('firstname'),
                'hs_object_id': contato_antigo.properties.get('hs_object_id'),
                'lastmodifieddate': contato_antigo.updated_at,
                'lastname': contato_antigo.properties.get('lastname'),
            }

            form = ContatoForm(request.POST or None, initial=initial_data)
            form.fields['email'].widget.attrs['readonly'] = True
            form.fields['email'].widget.attrs['disabled'] = True
            form.fields['telefone'].widget.attrs['disabled'] = True
            form.fields['telefone'].widget.attrs['disabled'] = True
            form.fields['data_aniversario'].widget.attrs['disabled'] = True
            form.fields['data_aniversario'].widget.attrs['disabled'] = True
            form.fields['peso'].widget.attrs['disabled'] = True
            form.fields['peso'].widget.attrs['disabled'] = True
            if request.method == 'POST':
                api_response = api_client.crm.contacts.basic_api.archive(pk)
                return redirect('listar_contatos')
        except ApiException as e:
            error = f'Erro: {e}'
    else:
        error = 'API KEY não localizada!'
    context = {
        'form': form,
        'isDelete': True,
        'error': error,
    }
    return render(request, "contatos/form_contato.html", context)
