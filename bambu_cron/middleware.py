import bambu_cron

bambu_cron.autodiscover()
class CronMiddleware(object):
    def process_request(self, *args, **kwargs):
        bambu_cron.site.run()