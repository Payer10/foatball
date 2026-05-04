# from django.urls import path
# from .views import RegisterView, LoginView , UserDetailView
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'users', UserDetailView)

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
# ] + router.urls



from django.urls import path
from .views import SignupView, ResendVerification, VerifyEmailView, SignInViwe, ForgotPasswordView, VerificationResetCodeView, ResetPasswordView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('resend-verification/', ResendVerification.as_view(), name='resend_verification'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('signin-user/', SignInViwe.as_view(), name="user-signin"),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('verification-forgot/', VerificationResetCodeView.as_view(), name='verify-forgot'),
    path('reset-password/', ResetPasswordView.as_view(), name="reset_password")
]