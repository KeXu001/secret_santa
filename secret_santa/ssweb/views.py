from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import JoinGameForm, ReviewLoginForm
from .models import Invite, Participant, Pairing

def join_game(request, code):
    invite = get_object_or_404(Invite, code=code)

    if request.method == 'POST':
        form = JoinGameForm(request.POST)

        if form.is_valid():
            if Participant.objects.filter(game=invite.game, name=form.cleaned_data['name']).count() > 0:
                form.add_error('name', 'Name already exists')

            else:
                participant = Participant(
                    game=invite.game,
                    name=form.cleaned_data['name'],
                    secret_word=form.cleaned_data['secret_word'],
                    wishlist=form.cleaned_data['wishlist'],
                )
                participant.save()

                request.session['authenticated_participant_id'] = participant.id

                return HttpResponseRedirect(reverse('review', args=(participant.id,)))

    else:
        form = JoinGameForm()

    context = {
        'game': invite.game,
        'review_url': reverse('review-login', args=(code,)),
        'form': form,
    }

    return render(request, 'join_game.html', context)

def review_login(request, code):
    invite = get_object_or_404(Invite, code=code)

    if request.method == 'POST':
        form = ReviewLoginForm(request.POST)

        if form.is_valid():
            participant = Participant.objects.filter(game=invite.game, name=form.cleaned_data['name'])

            if participant.count() == 0:
                form.add_error('name', 'Please make sure you enter your name exactly as before')
            elif participant.count() == 1:
                participant = participant[0]
                if form.cleaned_data['secret_word'] != participant.secret_word:
                    form.add_error('secret_word', 'Secret word does not match records')
                else:
                    request.session['authenticated_participant_id'] = participant.id

                    return HttpResponseRedirect(reverse('review', args=(participant.id,)))

    else:
        form = ReviewLoginForm()

    context = {
        'game': invite.game,
        'form': form,
    }

    return render(request, 'review_login.html', context)

def review(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)

    if 'authenticated_participant_id' not in request.session:
        return HttpResponse('Not authorized', status=401)

    authenticated_participant_id = request.session['authenticated_participant_id']

    if authenticated_participant_id != participant.id:
        return HttpResponse('Not authorized', status=401)

    incoming = Pairing.objects.filter(game=participant.game, receiver=participant)
    outgoing = Pairing.objects.filter(game=participant.game, giver=participant)

    receiving_from = incoming[0].giver if incoming.count() == 1 else None
    giving_to = outgoing[0].receiver if outgoing.count() == 1 else None

    context = {
        'participant': participant,
        'receiving_from': receiving_from,
        'giving_to': giving_to,
    }

    return render(request, 'review.html', context)