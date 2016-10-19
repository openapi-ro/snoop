DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hoover-snoop',
    }
}

DEBUG = True
SECRET_KEY = 'FIME: generate random string'

SNOOP_ROOT = '/path/to/test/data'

SNOOP_ELASTICSEARCH_URL = 'http://localhost:9200'
SNOOP_ELASTICSEARCH_INDEX = 'hoover'

SNOOP_TIKA_SERVER_ENDPOINT = 'http://localhost:9998'
SNOOP_TIKA_FILE_TYPES = ['doc', 'pdf', 'xls', 'ppt']
SNOOP_TIKA_MAX_FILE_SIZE = 32 * (2 ** 20)  # 32mb
SNOOP_ANALYZE_LANG = False

SNOOP_MSGCONVERT_SCRIPT = 'msgconvert'
SNOOP_MSG_CACHE = 'path/to/msg/cache'

SNOOP_ARCHIVE_CACHE_ROOT = '/path/to/archive/cache'
SNOOP_SEVENZIP_BINARY = '7z'

SNOOP_PST_CACHE_ROOT = '/path/to/pst/cache'
SNOOP_READPST_BINARY = 'readpst'

SNOOP_GPG_HOME = '/path/to/gpg/home'
SNOOP_GPG_BINARY = 'gpg'

SNOOP_LOG_DIR = '/path/to/log/dir'
