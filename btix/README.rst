====
BTIX
====

BTIX is an ERP (Logo) integration support package.

Quick start
-----------

1. Add "btix" to your INSTALLLED_APPS settings like this::

   INSTALLED_APPS = [
    ...,
    'btix',
   ]

2. Check various tests::

   ./manage.py test_settings
   ./manage.py test_erp_models
   ./manage.py test_asking
   ./manage.py test_integrator

3. Good to go
