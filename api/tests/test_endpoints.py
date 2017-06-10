from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from api.models import Workout

class TestWorkouts(APITestCase):
    fixtures = ['test_users', 'test_workouts']

    def setUp(self):
        self.user = User.objects.get(username='test_user_1')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.test_workout_data = {
            'name': 'Test Workout',
            'description': 'This is a test',
            'date': '2017-06-08'
        }

        self.update_name = 'Test Workout Update'
        self.update_description = 'Updated description'
        self.update_date = '2017-06-09'

        self.update_workout_data = {
            'name': self.update_name,
            'description': self.update_description,
            'date': self.update_date
        }

        self.detail_id = 1

        self.create_url = reverse('create_workout')
        self.list_url = reverse('list_workouts')
        self.detail_url = reverse('workout_detail', args=[self.detail_id])
        self.update_url = reverse('update_workout', args=[self.detail_id])

        #Change dates of workout objects to today for testing retrieval
        workouts = Workout.objects.all()
        for workout in workouts:
            workout.date = date.today()
            workout.save()

    def test_create_workout(self):
        '''Test creation of a workout'''
        num_existing_workouts = len(Workout.objects.filter(user=self.user))

        response = self.client.post(self.create_url, self.test_workout_data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        num_workouts = len(Workout.objects.filter(user=self.user))
        self.assertEquals(num_workouts,num_existing_workouts + 1)

    def test_user_workout_list(self):
        '''Test retrieval of user''s workout with default date range'''
        response = self.client.get(self.list_url, format='json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        workout_ids = [rec['id'] for rec in response.data]
        workouts = Workout.objects.filter(pk__in=workout_ids)
        workout_user_ids = set([workout.user.id for workout in workouts])
        
        self.assertEquals(len(workout_user_ids),1)

        (workout_user_id,) = workout_user_ids

        self.assertEquals(workout_user_id,self.user.id)

    def test_workout_detail(self):
        '''Test workout detail view for one of user''s own workouts'''
        response = self.client.get(self.detail_url, format='json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_workout_detail_with_different_user(self):
        '''Test workout detail view for workout belonging to a different user'''
        # authenticate new user
        self.auth_other_user()

        # Try to access workout belonging to test_user_1
        response = self.client.get(self.detail_url, format='json')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_workout(self):
        '''Test update for one of user''s workouts'''

        response = self.client.put(self.update_url, self.update_workout_data, format='json')
        
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_workout = Workout.objects.get(pk=self.detail_id)

        self.assertEquals(updated_workout.name, self.update_name)
        self.assertEquals(updated_workout.description, self.update_description)
        self.assertEquals(str(updated_workout.date), self.update_date)

    def test_update_workout_with_different_user(self):
        '''Test workout update view for workout belonging to different user'''
        self.auth_other_user()

        response = self.client.put(self.update_url, self.update_workout_data, format='json')

        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    # utilities

    def auth_other_user(self):
        new_user = User.objects.get(username='test_user_2')
        self.client = APIClient()
        self.client.force_authenticate(user=new_user)


