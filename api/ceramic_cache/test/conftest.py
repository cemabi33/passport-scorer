from django.conf import settings
from scorer.test.conftest import sample_address, sample_provider, verifiable_credential


def pytest_configure():
    try:
        settings.CERAMIC_CACHE_API_KEY = "supersecret"
    except:
        pass