from django.contrib import admin
from .models import Team, UserProfile, Activity, Workout, Leaderboard

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'fitness_level']
    search_fields = ['user__username', 'user__email']
    list_filter = ['team', 'fitness_level']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'duration', 'distance', 'date']
    search_fields = ['user__username', 'activity_type']
    list_filter = ['activity_type', 'date']
    ordering = ['-date']

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'duration', 'created_at']
    search_fields = ['name', 'target_muscles']
    list_filter = ['difficulty']

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'points', 'rank', 'period', 'updated_at']
    search_fields = ['user__username', 'team__name']
    list_filter = ['period']
    ordering = ['-points']
