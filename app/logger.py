import logging

logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] [%(pathname)s:%(lineno)d] %(message)s",
)

logger = logging.getLogger(__name__)
