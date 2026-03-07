
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Drop collections directly using pymongo
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workout.drop()

        # Create teams
        marvel = Team.objects.create(id='team_marvel', name='Marvel')
        dc = Team.objects.create(id='team_dc', name='DC')

        # Create users
        ironman = User.objects.create(id='user_ironman', email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        captain = User.objects.create(id='user_captain', email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True)
        batman = User.objects.create(id='user_batman', email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        superman = User.objects.create(id='user_superman', email='superman@dc.com', name='Superman', team='DC', is_superhero=True)

        # Add members to teams (store emails)
        marvel.members = [ironman.email, captain.email]
        marvel.save()
        dc.members = [batman.email, superman.email]
        dc.save()

        # Create activities
        Activity.objects.create(id='activity_ironman_run', user=ironman, type='Running', duration=30, date='2026-03-07')
        Activity.objects.create(id='activity_batman_cycle', user=batman, type='Cycling', duration=45, date='2026-03-07')

        # Create leaderboard
        Leaderboard.objects.create(id='leaderboard_marvel', team=marvel, points=200)
        Leaderboard.objects.create(id='leaderboard_dc', team=dc, points=180)

        # Create workouts
        Workout.objects.create(id='workout_pushups', name='Pushups', description='Do 20 pushups', suggested_for='Marvel')
        Workout.objects.create(id='workout_situps', name='Situps', description='Do 30 situps', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
