from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Team, UserProfile, Activity, Workout, Leaderboard
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Creating teams...')
        # Create teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Assemble! The mightiest heroes of fitness.'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League of fitness and wellness.'
        )

        self.stdout.write('Creating superhero users...')
        # Create superhero users for Marvel
        marvel_heroes = [
            ('ironman', 'Tony Stark', 'tony@stark.com', 'Advanced', 'Genius, billionaire, playboy, philanthropist'),
            ('spiderman', 'Peter Parker', 'peter@parker.com', 'Intermediate', 'Your friendly neighborhood fitness enthusiast'),
            ('captainamerica', 'Steve Rogers', 'steve@rogers.com', 'Advanced', 'I can do this all day!'),
            ('thor', 'Thor Odinson', 'thor@asgard.com', 'Advanced', 'God of Thunder and Fitness'),
            ('blackwidow', 'Natasha Romanoff', 'natasha@avengers.com', 'Advanced', 'Master of martial arts'),
        ]

        # Create superhero users for DC
        dc_heroes = [
            ('superman', 'Clark Kent', 'clark@dailyplanet.com', 'Advanced', 'Man of Steel'),
            ('batman', 'Bruce Wayne', 'bruce@wayne.com', 'Advanced', 'The Dark Knight of Gotham'),
            ('wonderwoman', 'Diana Prince', 'diana@themyscira.com', 'Advanced', 'Amazon warrior princess'),
            ('flash', 'Barry Allen', 'barry@starlabs.com', 'Intermediate', 'Fastest man alive'),
            ('aquaman', 'Arthur Curry', 'arthur@atlantis.com', 'Advanced', 'King of Atlantis'),
        ]

        marvel_users = []
        for username, full_name, email, fitness_level, bio in marvel_heroes:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=full_name.split()[0],
                last_name=' '.join(full_name.split()[1:])
            )
            profile = UserProfile.objects.create(
                user=user,
                team=team_marvel,
                bio=bio,
                fitness_level=fitness_level
            )
            marvel_users.append(user)

        dc_users = []
        for username, full_name, email, fitness_level, bio in dc_heroes:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=full_name.split()[0],
                last_name=' '.join(full_name.split()[1:])
            )
            profile = UserProfile.objects.create(
                user=user,
                team=team_dc,
                bio=bio,
                fitness_level=fitness_level
            )
            dc_users.append(user)

        all_users = marvel_users + dc_users

        self.stdout.write('Creating activities...')
        # Create activities
        activity_types = ['running', 'walking', 'cycling', 'swimming', 'strength']
        for user in all_users:
            for i in range(random.randint(3, 8)):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                distance = random.uniform(1.0, 20.0) if activity_type in ['running', 'walking', 'cycling'] else None
                calories = random.randint(100, 800)
                
                Activity.objects.create(
                    user=user,
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    notes=f"Great {activity_type} session!"
                )

        self.stdout.write('Creating workouts...')
        # Create workout suggestions
        workouts = [
            {
                'name': 'Super Soldier Strength Training',
                'description': 'Captain America inspired full-body workout focusing on strength and endurance.',
                'difficulty': 'Advanced',
                'target_muscles': 'Full Body',
                'duration': 60
            },
            {
                'name': 'Web-Slinger Cardio',
                'description': 'High-intensity cardio workout to build agility and stamina like Spider-Man.',
                'difficulty': 'Intermediate',
                'target_muscles': 'Cardio, Legs',
                'duration': 45
            },
            {
                'name': 'Amazonian Warrior Training',
                'description': 'Wonder Woman inspired combat fitness routine.',
                'difficulty': 'Advanced',
                'target_muscles': 'Full Body',
                'duration': 75
            },
            {
                'name': 'Speedster Sprint Session',
                'description': 'Flash-inspired speed and agility training.',
                'difficulty': 'Intermediate',
                'target_muscles': 'Legs, Cardio',
                'duration': 30
            },
            {
                'name': 'Arc Reactor Core',
                'description': 'Tony Stark approved core strengthening routine.',
                'difficulty': 'Intermediate',
                'target_muscles': 'Core, Abs',
                'duration': 30
            },
            {
                'name': 'Atlantean Swimming Workout',
                'description': 'Aquaman-inspired swimming and water resistance training.',
                'difficulty': 'Advanced',
                'target_muscles': 'Full Body, Swimming',
                'duration': 50
            },
        ]

        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write('Creating leaderboard entries...')
        # Create leaderboard entries
        for user in all_users:
            user_activities = Activity.objects.filter(user=user)
            total_points = sum(act.calories or 0 for act in user_activities)
            
            Leaderboard.objects.create(
                user=user,
                team=user.profile.team,
                points=total_points,
                rank=0,  # Will be calculated
                period='monthly'
            )

        # Update ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-points')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with superhero test data!'))
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Workout.objects.count()} workouts')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
