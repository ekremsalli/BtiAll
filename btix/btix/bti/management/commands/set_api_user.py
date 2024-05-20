from bti.command import BCommand


class Command(BCommand):
    help = "Grant api usage permission to user"
    NAME = 'set_api_user'    

    def add_arguments(self , parser):
        super().add_arguments(parser)
        parser.add_argument('usernames', nargs='+', type=str)

    def process(self, *a, **kw):
        from django.contrib.auth.models import User, Group
        group = Group.objects.get(name='api-user')
        for username in kw.get('usernames'):
            user = User.objects.get(username=username)
            user.is_staff = False
            user.is_supuerser = False
            user.save()
            group.user_set.add(user)

            print(user, user.groups.all())

