import bottle
import sqlalchemy
from mailchute import db
from mailchute.api.exception import NotFound, BadRequest
from mailchute.model import IncomingEmail, RawMessage
from mailchute.api.serializer import (
    response, ResponseDTO, InboxDTO, IncomingEmailDTO, RawMessageDTO)


app = bottle.app()


@app.route('/emails')
@response('emails', IncomingEmailDTO)
def get_emails():
    inbox = bottle.request.query.get('inbox', None)
    if not inbox:
        raise BadRequest("'inbox' must be specified")


@app.route('/inboxes/<recipient>')
@response('inboxes', InboxDTO)
def get_inbox(recipient):
    emails = (
        db.session.query(IncomingEmail).filter_by(recipient=recipient).all()
    )

    return type('inbox', (object,), {
        'name': recipient,
        'emails': emails,
    })


@app.route('/inboxes/<recipient>/raw_messages/<raw_message_id>')
@response('raw_messages', RawMessageDTO)
def get_raw_message(recipient, raw_message_id):
    try:
        return (
            db.session.query(RawMessage).join(IncomingEmail)
            .filter(IncomingEmail.recipient == recipient)
            .filter(RawMessage.raw_message_id == raw_message_id)
            .one()
        )
    except sqlalchemy.orm.exc.NoResultFound:
        raise NotFound()


@app.hook('after_request')
def enable_cors():
    ALLOWED_METHODS = 'PUT, GET, POST, DELETE, OPTIONS'
    ALLOWED_HEADERS = \
        'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    bottle.response.headers['Access-Control-Allow-Methods'] = ALLOWED_METHODS
    bottle.response.headers['Access-Control-Allow-Headers'] = ALLOWED_HEADERS
