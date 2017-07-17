from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from api.models import Workout, Lift

class WorkoutBookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.get(username='test_user_1')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def auth_other_user(self, username):
        new_user = User.objects.get(username=username)
        self.client = APIClient()
        self.client.force_authenticate(user=new_user)

class TestWorkouts(WorkoutBookAPITestCase):
    fixtures = ['test_users', 'test_workouts']

    def setUp(self):
        super().setUp()

        self.test_workout_data = {
            'description': 'This is a test',
            'date': '2017-06-08'
        }

        self.update_description = 'Updated description'
        self.update_date = '2017-06-09'

        self.update_workout_data = {
            'description': self.update_description,
            'date': self.update_date
        }

        self.detail_id = 1

        self.create_url = reverse('workout_create')
        self.list_url = reverse('workouts_list')
        self.detail_url = reverse('workout_detail', args=[self.detail_id])
        self.update_url = reverse('workout_update', args=[self.detail_id])

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
        self.auth_other_user('test_user_2')

        # Try to access workout belonging to test_user_1
        response = self.client.get(self.detail_url, format='json')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_workout(self):
        '''Test update for one of user''s workouts'''

        response = self.client.put(self.update_url, self.update_workout_data, format='json')
        
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_workout = Workout.objects.get(pk=self.detail_id)

        self.assertEquals(updated_workout.description, self.update_description)
        self.assertEquals(str(updated_workout.date), self.update_date)

    def test_update_workout_with_different_user(self):
        '''Test workout update view for workout belonging to different user'''
        self.auth_other_user('test_user_2')

        response = self.client.put(self.update_url, self.update_workout_data, format='json')

        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

class TestLifts(WorkoutBookAPITestCase):
    fixtures = ['test_users', 'test_lifts']

    def setUp(self):
        super().setUp()

        self.test_lift_data = {
            'name': 'Test Workout',
            'description': 'This is a test'
        }

        self.update_name = 'Updated name'
        self.update_description = 'Updated description'
        self.update_lift_data = {
            'name': self.update_name,
            'description': self.update_description
        }

        self.detail_id = 1

        self.create_url = reverse('lift_create')
        self.list_url = reverse('lifts_list')
        self.detail_url = reverse('lift_detail', args=[self.detail_id])
        self.update_url = reverse('lift_update', args=[self.detail_id])

    def test_create_lift(self):
        '''Test creation of a lift'''
        num_existing_lifts = len(Lift.objects.filter(user=self.user))

        response = self.client.post(self.create_url, self.test_lift_data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        num_lifts = len(Lift.objects.filter(user=self.user))
        self.assertEquals(num_lifts,num_existing_lifts + 1)

    def test_user_lift_list(self):
        '''Test retrieval of user''s lifts with default date range'''
        response = self.client.get(self.list_url, format='json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        lift_ids = [rec['id'] for rec in response.data]
        lifts = Lift.objects.filter(pk__in=lift_ids)
        lift_user_ids = set([lift.user.id for lift in lifts])
        
        self.assertEquals(len(lift_user_ids),1)

        (lift_user_id,) = lift_user_ids

        self.assertEquals(lift_user_id,self.user.id)

    def test_lift_detail(self):
        '''Test lift detail view for one of user''s own lifts'''
        response = self.client.get(self.detail_url, format='json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_lift_detail_with_different_user(self):
        '''Test lift detail view for lift belonging to a different user'''
        # authenticate new user
        self.auth_other_user('test_user_2')

        # Try to access lift belonging to test_user_1
        response = self.client.get(self.detail_url, format='json')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_lift(self):
        '''Test update for one of user''s lifts'''

        response = self.client.put(self.update_url, self.update_lift_data, format='json')
        
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_lift = Lift.objects.get(pk=self.detail_id)

        self.assertEquals(updated_lift.name, self.update_name)
        self.assertEquals(updated_lift.description, self.update_description)

    def test_update_lift_with_different_user(self):
        '''Test lift update view for lift belonging to different user'''
        self.auth_other_user('test_user_2')

        response = self.client.put(self.update_url, self.update_lift_data, format='json')

        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

