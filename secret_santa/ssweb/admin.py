from django.contrib import admin

from .models import Game, Invite, Participant, Pairing

@admin.action(description='Generate pairings for the selected games')
def generate_pairings_for_games(game_admin, request, queryset):
    for game in queryset:
        game.generate_pairings()

class GameAdmin(admin.ModelAdmin):
    actions=[generate_pairings_for_games]

admin.site.register(Game, GameAdmin)
admin.site.register(Invite)
admin.site.register(Participant)
admin.site.register(Pairing)