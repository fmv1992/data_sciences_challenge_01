"""Return a list of usable backends."""

import os
import matplotlib


def list_usable_backends():
    """Test if backend is usable in current environment."""
    backend_string = ("import matplotlib; matplotlib.use(\"{0}\");"
                      "import matplotlib.pyplot as plt")

    command_string = 'python3 -c \'{0}\' 2>/dev/null'

    usable_backends = []
    for backend in matplotlib.rcsetup.all_backends:
        backend_call = backend_string.format(backend)
        command_call = command_string.format(backend_call)
        return_value = os.system(command_call)
        if return_value == 0:
            usable_backends.append(backend)

    return usable_backends

if __name__ == '__main__':
    l = list_usable_backends()
    print(l[0])
