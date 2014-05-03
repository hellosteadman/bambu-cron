Management comment
==================

``cron``

Running ``python manage.py cron`` will run all of the jobs that are scheduled to run at that time.

You can specify ``--force`` to force all jobs to run.

Adding ``--debug`` will cause errors to be thrown so you can track them more easily.

Calling ``manage.py cron --setup`` is necessary when add or remove cron jobs, or install new packages that
expose jobs to Bambu Cron.
