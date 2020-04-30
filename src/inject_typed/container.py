from typing import Type, Any, TypeVar

T1 = TypeVar('T1', covariant=True)


class ContainerException(Exception):
    pass

class Container:

    def add_class(self, clazz: Type[Any]) -> None:
        raise NotImplementedError()

    def bind_value(self, clazz: Type[Any], value: Any) -> None:
        raise NotImplementedError()

    def get(self,  clazz: Type[T1]) -> T1:
        raise NotImplementedError()
