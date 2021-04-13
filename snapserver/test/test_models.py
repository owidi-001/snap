from django.test import TestCase
from snapserver.models import User, Profile, Post
from django.utils import timezone
from snapserver.forms import UserRegisterForm, CreatePostForm


class UserModelTest(TestCase):
    def create_admin_user(self, username='mrmarangi', email='mrmarangi4@gmail.com', admin=True, staff=True):
        return User.objects.create(username=username, email=email, admin=admin, staff=staff)

    def create_staff_user(self, username='owidi', email='sirowidi@gmail.com', staff=True):
        return User.objects.create(username=username, email=email, staff=staff)

    def create_normal_user(self, username='young', email='young@gmail.com'):
        return User.objects.create(username=username, email=email)

    def test_user(self):
        print('testing User')
        admin_user = self.create_admin_user()
        staff_user = self.create_staff_user()
        normal_user = self.create_normal_user()
        self.assertTrue(isinstance(admin_user, User))
        self.assertTrue(isinstance(staff_user, User))
        self.assertTrue(isinstance(normal_user, User))
        self.assertEqual(admin_user.__str__(), admin_user.username)
        self.assertEqual(staff_user.__str__(), staff_user.username)
        self.assertEqual(normal_user.__str__(), normal_user.username)
        self.assertEqual(admin_user.get_user_mail(), admin_user.email)
        self.assertEqual(staff_user.get_user_mail(), staff_user.email)
        self.assertEqual(normal_user.get_user_mail(), normal_user.email)
        print('Done testing user')


# # testing profile
# class ProfileModelTest(TestCase):
#     def create_profile(self, first_name='mr', last_name='marangi', phone='0791381653', biography='my simple bio'):
#         user_obj_create = UserModelTest().create_normal_user()
#         user_obj = user_obj_create.objects.get(username='young')
#         username = user_obj.username
#         email = user_obj.email
#         return Profile.objects.create(username=username, first_name=first_name, last_name=last_name, email=email,
#                                       phone=phone, biography=biography)
#
#     def test_profile_creation(self):
#         profile = self.create_profile()
#         self.assertTrue(isinstance(profile, Profile))


# testing post model
class PostModelTest(TestCase):
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
