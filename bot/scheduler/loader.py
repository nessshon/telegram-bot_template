from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from bot.scheduler import BASE_DIR

job_stores = {
    'default': SQLAlchemyJobStore(url=f'sqlite:///{BASE_DIR}/file/scheduler.sqlite')
}

scheduler = AsyncIOScheduler(
    jobstores=job_stores, timezone="Asia/Tashkent"
)
