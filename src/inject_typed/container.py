from typing import Type, Any, TypeVar, Dict
from inspect import signature, _empty

T1 = TypeVar('T1', covariant=True)


class ContainerException(Exception):
    pass


_IGNORED_PARAMS = {'args', 'kwargs', 'self'}


def _class_dependencies(clazz: Type[Any]) -> Dict[str, Any]:
    constructor_signature = signature(clazz.__init__)
    filtered_params = {key: param for (key, param) in constructor_signature.parameters.items() if
                       key not in _IGNORED_PARAMS}
    return filtered_params


def _fulfills_dependency(clazz: Type[Any], dependency: Type[Any]) -> bool:
    return clazz == dependency or dependency in clazz.__bases__


class Container:

    def __init__(self):
        self._classes_dependencies = {}
        self._bindings = {}

    def add_class(self, clazz: Type[Any]) -> None:
        self._classes_dependencies[clazz] = _class_dependencies(clazz)

    def bind_value(self, clazz: Type[T1], value: T1) -> None:
        self._classes_dependencies[clazz] = {}
        self._bindings[clazz] = value

    def get(self, clazz: Type[T1]) -> T1:
        self._perform_checks(clazz)
        if clazz not in self._bindings.keys():
            self._create_instance(clazz)

        return self._bindings[clazz]

    def _create_instance(self, clazz: Type[Any]) -> None:
        dependencies = self._get_dependencies(clazz)
        self._bindings[clazz] = clazz(**dependencies)

    def _get_dependencies(self, clazz) -> Dict[str, Any]:
        return {key: self.get(param.annotation) for (key, param) in self._classes_dependencies[clazz].items()}

    def _perform_checks(self, clazz: Type[Any]) -> None:
        if self._class_not_in_container(clazz):
            raise ContainerException('Class {} not in the container'.format(clazz.__name__))
        if self._any_dependency_unannotated(clazz):
            raise ContainerException('Class {} has untyped dependency'.format(clazz.__name__))
        if self._check_multiple_fulfilling(clazz):
            raise ContainerException('Class {} has dependency matching multiple classes'.format(clazz.__name__))

        self._check_all_dependencies(clazz)

    def _class_not_in_container(self, clazz: Type[Any]) -> bool:
        return clazz not in self._classes_dependencies.keys()

    def _any_dependency_unannotated(self, clazz: Type[Any]) -> bool:
        return any(param.annotation == _empty for param in self._classes_dependencies[clazz].values())

    def _check_multiple_fulfilling(self, clazz: Type[Any]) -> bool:
        fulfilling = [class_key for class_key in self._classes_dependencies.keys() if
                      _fulfills_dependency(class_key, clazz)]
        return len(fulfilling) > 1

    def _check_all_dependencies(self, clazz: Type[Any]) -> None:
        for param in self._classes_dependencies[clazz].values():
            self._perform_checks(param.annotation)
