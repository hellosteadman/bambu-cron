"""
Defines the frequencies with which a cron job can run
"""

MINUTE = 1
"""Run a job every 60 seconds"""

HOUR = MINUTE * 60
"""Run a job every 60 minutes"""

DAY = HOUR * 24
"""Run a job every 24 hours"""

WEEK = DAY * 7
"""Run a job every 7 days"""

MONTH = -1
"""Run a job every month (largely untested)"""

YEAR = DAY * 365
"""Run a job every 365 days"""