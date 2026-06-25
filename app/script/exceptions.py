class ScriptError(Exception):
    """Base Script Exception"""
    pass


class ScriptNotFound(ScriptError):
    """Script file not found"""
    pass


class UnsupportedScriptFormat(ScriptError):
    """Unsupported script format"""
    pass