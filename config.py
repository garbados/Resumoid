# instantiate global configuration settings
try:
    from local_settings import Config
except ImportError:
    Config = object
    
# Environment-specific configuration
class Development(Config):
    """
    Development settings
    """
    DEBUG = True
    
class Testing(Config):
    """
    Testing settings
    """
    TESTING = True
    
class Production(Config):
    """
    Production settings
    """
    pass
