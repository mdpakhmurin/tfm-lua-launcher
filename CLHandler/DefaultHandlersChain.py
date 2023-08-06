from CLHandler import (
    BaseHandlersChain,
    BundleHandler,
    WrongHandler,
    RunHandler,
    HelpHandler,
    WrongHandler,
)


class DefaultHandlersChain(BaseHandlersChain):
    def __init__(self) -> None:
        super().__init__()

        self.register(BundleHandler())
        self.register(RunHandler())
        self.register(HelpHandler())
        self.register(WrongHandler())
