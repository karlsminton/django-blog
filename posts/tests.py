from django.test import TestCase
from django.utils import timezone
from .models import Post


class PostModelTests(TestCase):
    def test_is_published_when_disabled(self):
        start_time = timezone.now() + timezone.timedelta(days=-1)
        end_time = timezone.now() + timezone.timedelta(days=1)
        subject = Post(
            content='',
            enabled=False,
            published_date=start_time,
            unpublished_date=end_time
        )
        self.assertIs(subject.is_published(), False)

    def test_is_published_within_correct_dates(self):
        start_time = timezone.now() + timezone.timedelta(days=-1)
        end_time = timezone.now() + timezone.timedelta(days=1)
        subject = Post(
            content='',
            enabled=True,
            published_date=start_time,
            unpublished_date=end_time
        )
        self.assertIs(subject.is_published(), True)

    def test_is_unpublished_after_unpublished_date(self):
        start_time = timezone.now() + timezone.timedelta(days=-2)
        end_time = timezone.now() + timezone.timedelta(days=-1)
        subject = Post(
            content='',
            enabled=True,
            published_date=start_time,
            unpublished_date=end_time
        )
        self.assertIs(subject.is_published(), False)

