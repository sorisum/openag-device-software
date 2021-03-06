# Import python types
from typing import Optional

# Import device utilities
from device.utilities.logger import Logger


class DriverError(Exception):
    """Base class for errors raised by driver."""

    message_base: str = ""

    def __init__(
        self, message: Optional[str] = None, logger: Optional[Logger] = None
    ) -> None:
        """Initializes driver error."""

        # Build error message
        if message != None:
            error_message = self.message_base + ": " + message  # type: ignore
        elif self.message_base != "":
            error_message = self.message_base
        else:
            return

        # Display error
        if logger != None:
            logger.error(error_message)  # type: ignore
        else:
            print(error_message)


class InitError(DriverError):
    message_base = "Unable to initialize"


class SetupError(DriverError):
    message_base = "Unable to setup"
