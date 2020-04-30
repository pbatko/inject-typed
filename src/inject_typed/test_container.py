from unittest import TestCase

from inject_typed.container import Container, ContainerException


class Foo:
    pass

class Foo2(Foo):
    pass

class Bar:

    def __init__(self, foo: Foo) -> None:
        self.foo = foo

class TestContainer(TestCase):

    def test_creates_instance_from_constructor_type_annotations(self) -> None:
        # given
        tested = Container()
        tested.add_class(Foo)
        tested.add_class(Bar)

        # when
        actual = tested.get(Bar)

        # then
        self.assertIsInstance(actual, Bar)
        self.assertIsInstance(actual.foo, Foo)

    def test_creates_singleton_per_container(self) -> None:
        # given
        tested1 = Container()
        tested1.add_class(Foo)
        tested1.add_class(Bar)

        tested2 = Container()
        tested2.add_class(Foo)
        tested2.add_class(Bar)

        # when & then
        self.assertIs(tested1.get(Bar), tested1.get(Bar))
        self.assertIs(tested2.get(Bar), tested2.get(Bar))
        self.assertIsNot(tested1.get(Bar), tested2.get(Bar))

    def test_binds_values(self) -> None:
        # given
        tested = Container()
        foo = Foo()
        tested.bind_value(clazz=Foo, value=foo)
        tested.add_class(Bar)

        # when & then
        self.assertIs(foo, tested.get(Foo))
        self.assertIsInstance(tested.get(Bar), Bar)


    def test_raises_exception_when_unsatisfied_dependencies(self) -> None:
        # given
        tested = Container()
        tested.add_class(Bar)


        # then
        with self.assertRaises(ContainerException) as ctx:
            tested.get(Bar)

        self.assertIsInstance(ctx.exception, ContainerException)

    def test_raises_exception_when_multiple_class_satisfy_dependencies(self) -> None:
        # given
        tested = Container()
        tested.add_class(Bar)
        tested.add_class(Foo)
        tested.add_class(Foo2)

        # then
        with self.assertRaises(ContainerException) as ctx:
            tested.get(Bar)

        self.assertIsInstance(ctx.exception, ContainerException)
