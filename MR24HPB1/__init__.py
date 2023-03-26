from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version('MR24HPB1')
except PackageNotFoundError:
    __version__ = '(local)'

del PackageNotFoundError
del version
