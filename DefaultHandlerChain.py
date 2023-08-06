from BaseHandlerChain import BaseHandlerChain
from BundleHandler import BundleHandler
from WrongHandler import WrongHandler
from RunHandler import RunHandler
from HelpHandler import HelpHandler


class DefaultHandlerChain(BaseHandlerChain):
    def __init__(self) -> None:
        super().__init__()

        self.register(BundleHandler())
        self.register(RunHandler())
        self.register(HelpHandler())
        self.register(WrongHandler())
