import unittest

from django.test import TestCase
from api.models import User, Post
from django.utils import timezone


class UserModelTest(TestCase):
    def create_admin_user(self, email, admin, staff):
        return User.objects.create(email, admin, staff)

    def create_staff_user(self, email, staff):
        return User.objects.create(email, staff)

    def create_normal_user(self, email):
        return User.objects.create(email)

    def test_user(self):
        print('testing User')
        admin_user = self.create_admin_user('mrmarangi4@gmail.com', True, True)
        staff_user = self.create_staff_user('sirowidi@gmail.com', True)
        normal_user = self.create_normal_user('young@gmail.com')

        self.assertTrue(isinstance(admin_user, User))
        self.assertTrue(isinstance(staff_user, User))
        self.assertTrue(isinstance(normal_user, User))

        self.assertEqual(admin_user.__str__(), admin_user.email)
        self.assertEqual(staff_user.__str__(), staff_user.email)
        self.assertEqual(normal_user.__str__(), normal_user.email)

        self.assertEqual(admin_user.get_user_mail(), admin_user.email)
        self.assertEqual(staff_user.get_user_mail(), staff_user.email)
        self.assertEqual(normal_user.get_user_mail(), normal_user.email)
        print('Done testing user')


# testing post model
class PostModelTest(TestCase):
    # user=User.objects.create(email='young@gmail.com')

    def create_post(self, title='test post1', upload='/home/Desktop/index.jpg',
                    caption='test caption'):
        author = UserModelTest().create_normal_user()
        return Post.objects.create(author=author, title=title, caption=caption, upload=upload,
                                   date_posted=timezone.now())

    def test_post_creation(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)

    def tearDown(self):
        print('tear down')


if __name__ == '__main__':
    unittest.main()
