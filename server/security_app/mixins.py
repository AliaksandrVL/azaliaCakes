from django.shortcuts import redirect


class AnonRequired():
    
    main_url = str()

    def dispatch(self, request, *args, **kwargs):

        if request.user and request.user.is_authenticated:
            return redirect(self.main_url)
        
        return super(AnonRequired, self).dispatch(request, *args, **kwargs)