"""from contextlib import contextmanager
import json
from urllib.parse import urlparse, parse_qs

from rest_framework.test import APITestCase
import re

from requests.exceptions import HTTPError
from requests.models import Response
from social_core.backends import facebook, google

from core.models import User
import core.tests.fixtures as fixtures

SOCIAL_URL = "/api/2.0/social/{}/"
class TryToken:
    def try_token(self, token):
        return self.post(
            SOCIAL_URL.format(self.provider),
            data={'access_token': token},
        )


class TestInvalidProvider(TryToken, APITestCase):
    provider = 'yahoo'

    def test_only_allowed_backends_work(self):
        for token in USER_INFO:
            with self.subTest(token=token):
                resp = self.try_token(token)

                self.assertEqual(resp.status_code, 404)

USER_INFO = {
    'user_1': {
        'id': '00001',
        'name': 'Foo Bar',
        'email': 'foo@bar.com',
    },
    'user_2': {
        'id': '00002',
        'name': 'Pooh Bear',
        'email': 'winnie@100acre.net',
    },
}

def respond_to(request):
    token = parse_qs(urlparse(request.url).query)['access_token'][0]
    status = 200
    try:
        body = USER_INFO[token]
    except KeyError:
        body = {'errors': 'Invalid Token'}
        status = 401
    return (status, {}, json.dumps(body))

@contextmanager
def mocked(endpoint):
    with re.RequestsMock() as rsps:
        rsps.add_callback(re.GET, endpoint,
                          callback=respond_to,
                        content_type='application/json',
                          match_querystring=True,
                          )
        yield rsps

class SocialAuthTests(TryToken):
    def test_new_user_creation(self):
        for token, data in USER_INFO.items():
            with self.subTest(token=token), mocked(self.mock_url):
                resp = self.try_token(token)
                self.assertEqual(self.status_head(resp), 2)
                self.assertIn('token', resp.data)
                self.assertNotEqual(resp.data['token'], token)
                self.assertEqual(User.objects.filter(email=data['email']).count(), 1)
                user_model = User.objects.get(email=data['email'])
                self.assertEqual(user_model.username, user_model.email)

    def test_existing_user_login(self):
        for token, data in USER_INFO.items():
            User.objects.create_user(data['email'], email=data['email'],
                                    first_name=data['name'], last_name='')

            with self.subTest(token=token), mocked(self.mock_url):
                resp = self.try_token(token)
                self.assertEqual(self.status_head(resp), 2)
                self.assertIn('token', resp.data)
                self.assertNotEqual(resp.data['token'], token)
                self.assertEqual(User.objects.filter(email=data['email']).count(), 1)
                user = User.objects.get(email=data['email'])
                self.assertEqual(user.get_full_name(), data['name'])

    def test_invalid_social_token(self):
        usernames = {u.username for u in User.objects.all()}
        token = 'invalid_token'
        resp = self.try_token(token)
        self.assertEqual(self.status_head(resp), 4)
        self.assertNotIn('token', resp.data)
        new_usernames = {u.username for u in User.objects.all()}
        self.assertEqual(usernames, new_usernames)

QUERY_STRINGS_RE = '\?([\w-]+(=[\w-]*)?(&[\w-]+(=[\w-]*)?)*)?$'

class TestFacebook(SocialAuthTests, APITestCase):
    provider = 'facebook'
    base_url = facebook.FacebookOAuth2.USER_DATA_URL.replace('.', r'\.')
    mock_url = re.compile(
        base_url + QUERY_STRINGS_RE
    )

class TestGoogle(SocialAuthTests, APITestCase):
    provider = 'google-oauth2'
    base_url = 'https://www.googleapis.com/plus/v1/people/me'.replace('.', r'\.')
    mock_url = re.compile(
        base_url + QUERY_STRINGS_RE
    )

"""