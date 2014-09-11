import bottle
from mailchute import settings
from mailchute.api.app import app


def main():  # pragma: no cover
    # import mailchute.api.resource as _
    bottle.run(
        app,
        host=settings.API['host'],
        port=settings.API['port'],
    )
