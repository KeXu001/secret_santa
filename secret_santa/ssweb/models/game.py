
import uuid
import random

from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def participants(self):
        return Participant.objects.filter(game=self)

    def generate_pairings(self):
        # delete existing pairings
        Pairing.objects.filter(game=self).delete()

        participants = list(self.participants)
        random.shuffle(participants)

        participants_cycled_1 = participants[1:] + participants[0:1]

        for a, b in zip(participants, participants_cycled_1):
            pairing = Pairing(game=self, giver=a, receiver=b)
            pairing.save()

class Invite(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    code = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return '{} ({})'.format(self.game.name, self.code)

class Participant(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    secret_word = models.CharField(max_length=100)
    wishlist = models.TextField(max_length=400)

    def __str__(self):
        return '{} ({})'.format(self.name, self.game.name)

class Pairing(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    giver = models.ForeignKey('Participant', on_delete=models.CASCADE, related_name='giver')
    receiver = models.ForeignKey('Participant', on_delete=models.CASCADE, related_name='receiver')

    def __str__(self):
        return '{} ({}->{})'.format(self.game, self.giver.name, self.receiver.name)