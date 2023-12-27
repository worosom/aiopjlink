class PJLinkException(Exception):
    """ Base exception for PJLink library issues. """
    pass


class PJLinkNoConnection(PJLinkException):
    """ Projector did not respond to the connection request. """
    pass


class PJLinkConnectionClosed(PJLinkException):
    """ Projector closed the connection. """
    pass


class PJLinkProtocolError(PJLinkException):
    """ Unexpected communication to or from the projector. """
    pass


class PJLinkUnexpectedResponseParameter(PJLinkException):
    """ Unable to parse a response parameter. """
    pass


class PJLinkPassword(PJLinkException):
    """ Invalid or absent password. """
    pass


class PJLinkProjectorError(PJLinkException):
    """ Projector raised an error when handling a command. """
    pass


class PJLinkERR1(PJLinkProtocolError):
    """ ERR 1, undefined command, as specified in (§2.2)
    """
    pass


class PJLinkERR2(PJLinkException):
    """ ERR 2, out of parameter, as specified in (§2.2)
    """
    pass


class PJLinkERR3(PJLinkException):
    """ ERR 3, unavailable at the current time or in the current projector state, as specified in (§2.2) """
    pass


class PJLinkERR4(PJLinkException):
    """ ERR 4, projector or display failure, as specified in (§2.2) """
    pass
