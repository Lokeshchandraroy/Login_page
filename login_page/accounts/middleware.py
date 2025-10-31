from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth import logout

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if hasattr(request, 'user') and request.user.is_authenticated:
            now = timezone.now().timestamp()
            last_activity = request.session.get('last_activity', now)
            
            # Check if session expired (more than 60 seconds)
            if now - last_activity > 60:
                logout(request)
                request.session.flush()  # clear session
                return redirect('login')

            # Update activity timestamp
            request.session['last_activity'] = now

        return response
