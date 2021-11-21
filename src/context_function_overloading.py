from inspect import stack
import re
from typing import Any


def contextdispatch(function):
    contexts = {}

    def register(context: str, params_passed: tuple = ()):
        def register_decorator(func):
            contexts[context] = (func, params_passed)

            def running_register(*args, **kwargs):
                return func(*args, **kwargs)

            return running_register

        return register_decorator

    def run_function(*args, **kwargs):
        function_called = stack()[-1].code_context[-1].rstrip('\n')
        for context, func in contexts.items():
            if re.search(pattern=fr"{context}", string=function_called):
                if func[1]:
                    params = re.findall(pattern=fr"{func[1][0]}", string=function_called)
                    if func[1][1] != Any:
                        params = map(func[1][1], params)
                else:
                    params = tuple()
                return func[0](*args, *params, **kwargs)
        else:
            return function(*args, **kwargs)

    run_function.register = register
    return run_function
