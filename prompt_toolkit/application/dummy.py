from typing import Any, Callable, Optional

from prompt_toolkit.input import DummyInput
from prompt_toolkit.output import DummyOutput

from .application import Application

__all__ = [
    'DummyApplication',
]


class DummyApplication(Application):
    """
    When no :class:`.Application` is running,
    :func:`.get_app` will run an instance of this :class:`.DummyApplication` instead.
    """
    def __init__(self) -> None:
        super().__init__(output=DummyOutput(), input=DummyInput())

    def run(self, pre_run: Optional[Callable[[], None]] = None,
            set_exception_handler: bool = True) -> Any:
        raise NotImplementedError('A DummyApplication is not supposed to run.')

    async def run_async(self, pre_run: Optional[Callable[[], None]] = None) -> Any:
        raise NotImplementedError('A DummyApplication is not supposed to run.')

    async def run_system_command(
            self, command: str,
            wait_for_enter: bool = True,
            display_before_text: str = '',
            wait_text: str = '') -> None:
        raise NotImplementedError

    def suspend_to_background(self, suspend_group: bool = True) -> None:
        raise NotImplementedError
