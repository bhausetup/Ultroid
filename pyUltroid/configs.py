# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID, "10876438")
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", "3e2fe9a88ec96946a42bc46233bd495b")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", "BQAJ3Ml-2RG3-nRjuLBCDC79RfwhvqCFt1xxA5oBFkax25-u0j-JqQ_uC8Xkui9G7UaWEK-99rTHbILkxg55z6I_M9B3t_A1PPQfhinAC6KS393Ht8qOxEiPrI1pNrP1s17-aqy2-6novhPvmllYr2moIjbHP-MuB-WDtRUqkFpvyIPRVwRq6pGU2deDsc6P4jFG4CSAZyZ1NjxhAd0SjJLQQCnulCHH6t6DeqZPmxjGwm2NrIXQu-l7NLVurRflhNsVY6F1EYGk393bzGwVDp4vJpaMHBoWrdm3msdupsABbFQ4jXoIRRGDwRJITwOU-ybPJfYWoGTew2iFdjqCoZAUdGK0IgA")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", "http://redis-14347.c17.us-east-1-4.ec2.cloud.redislabs.com:14347"))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", "SOKBvp1JnuxsJlZCHwmr1VLNlT4qA18w")
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", "6136299677:AAFXOwWpoPmyShMO7GtISRdYszxZZzCZ024")
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
