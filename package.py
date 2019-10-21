name = "pyaaf2"

version = "1.2.0"

authors = [
    "Mark Reid"
]

description = \
    """
    A python module for reading and writing advanced authoring format files.
    """

requires = [
    "cmake-3+",
    "pip-19+",
    "python-2.7+<3"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "pyaaf2-{version}".format(version=str(version))

def commands():
    env.PYTHONPATH.prepend("{root}")
