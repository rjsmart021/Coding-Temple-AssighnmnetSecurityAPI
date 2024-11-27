#Task 4: Implement Role-based Access Control
from functool import wraps


def test_function_works(*args, **kwargs):
      if args[0] == True:
      return True
    return False

def some_decorator(*decorator_args , **decorator_kwargs):
    def decorator(view_function):
        @wraps(view_function)
        def _wrapped_view(request, *view_args, **view_kwargs):
            print("The required actions will be taken here ! Well, \
            actually inside the _wrapped_view function")
            
            if not test_function_works(*arguments , **keyword_arguments):
                print("The necessary operation that will be taken if \
                        the test case fails !")
                
            return view_function(request, *args, **kwargs)
        return _wrapped_view
    return decorator
