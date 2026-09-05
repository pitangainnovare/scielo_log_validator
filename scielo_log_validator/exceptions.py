class InvalidLogFileMimeError(Exception):
    ...


class LogFileReadError(Exception):
    kind = 'io'


class TruncatedLogFileError(LogFileReadError):
    kind = 'truncated'


class CorruptedLogFileError(LogFileReadError):
    kind = 'corrupted'


class LogFileIOError(LogFileReadError):
    kind = 'io'


class LogFileIsEmptyError(Exception):
    ...


class LogFileExtensionUndetectableError(Exception):
    ...


class InvalidTimestampContentError(Exception):
    ...
