

class Config(object):
    """docstring for Config"""
    CELERY_BROKER_URL     = 'redis://192.168.1.11:6379/0'
    CELERY_RESULT_BACKEND = 'redis://192.168.1.11:6379/0'
    LOG_PATH              = '/opt/pixelpals/logs/pixelserver.log'

    PIXEL_PALS = ['smb3Mario',
                  'Megaman',
                  'VaultBoy',
                  'smb3Luigi',
                  'smb3FireMario',
                  'MegamanSolarBlaze',
                  'BWVaultBoy',
                  'Link',
                  'smbMario',
                  'smbLuigi',
                  'SFRyu',
                  'SFChunli'
                  ]
