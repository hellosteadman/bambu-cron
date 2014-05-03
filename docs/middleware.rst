Poor man's cron
===============

If you're unable to setup a cron job, or you want to easily test how jobs are running while you're
developing, you can use the ``CronMiddleware`` class.

Add ``bambu_cron.middleware.CronMiddleware`` to your ``MIDDLEWARE_CLASSES`` list, and on every request,
Bambu Cron will check for new cron jobs and run those that are due.