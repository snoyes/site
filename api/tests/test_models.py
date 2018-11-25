from datetime import datetime

from django.test import SimpleTestCase

from ..models import (
    DeletedMessage, DocumentationLink,
    Message, MessageDeletionContext,
    ModelReprMixin, OffTopicChannelName,
    Role, SnakeFact,
    SnakeIdiom, SnakeName,
    SpecialSnake, Tag,
    User
)


class SimpleClass(ModelReprMixin):
    def __init__(self, is_what):
        self.the_cake = is_what


class ReprMixinTests(SimpleTestCase):
    def setUp(self):
        self.klass = SimpleClass('is a lie')

    def test_shows_attributes(self):
        expected = "<SimpleClass(the_cake='is a lie')>"
        self.assertEqual(repr(self.klass), expected)


class StringDunderMethodTests(SimpleTestCase):
    def setUp(self):
        self.objects = (
            DeletedMessage(
                id=45,
                author=User(
                    id=444, name='bill',
                    discriminator=5, avatar_hash=None
                ),
                channel_id=666,
                content="wooey",
                deletion_context=MessageDeletionContext(
                    actor=User(
                        id=5555, name='shawn',
                        discriminator=555, avatar_hash=None
                    ),
                    creation=datetime.utcnow()
                ),
                embeds=[]
            ),
            DocumentationLink(
                'test', 'http://example.com', 'http://example.com'
            ),
            OffTopicChannelName(name='bob-the-builders-playground'),
            SnakeFact(fact='snakes are cute'),
            SnakeIdiom(idiom='snake snacks'),
            SnakeName(name='python', scientific='3'),
            SpecialSnake(
                name='Pythagoras Pythonista',
                info='The only python snake that is born a triangle'
            ),
            Role(
                id=5, name='test role',
                colour=0x5, permissions=0
            ),
            Message(
                id=45,
                author=User(
                    id=444, name='bill',
                    discriminator=5, avatar_hash=None
                ),
                channel_id=666,
                content="wooey",
                embeds=[]
            ),
            MessageDeletionContext(
                actor=User(
                    id=5555, name='shawn',
                    discriminator=555, avatar_hash=None
                ),
                creation=datetime.utcnow()
            ),
            User(
                id=5, name='bob',
                discriminator=1, avatar_hash=None
            ),
            Tag(
                title='bob',
                embed={'content': "the builder"}
            )
        )

    def test_returns_string(self):
        for instance in self.objects:
            self.assertIsInstance(str(instance), str)
