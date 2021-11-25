import os
from pathlib import Path

from bauh.api.paths import DESKTOP_ENTRIES_DIR, CONFIG_DIR, TEMP_DIR, CACHE_DIR
from bauh.commons import resource
from bauh.commons.util import map_timestamp_file

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_PATH = '{}/.local/share/bauh/web'.format(Path.home())
WEB_CACHE_DIR = f'{CACHE_DIR}/web'
INSTALLED_PATH = '{}/installed'.format(WEB_PATH)
ENV_PATH = '{}/env'.format(WEB_PATH)
FIXES_PATH = '{}/fixes'.format(WEB_PATH)
NODE_DIR_PATH = '{}/node'.format(ENV_PATH)
NODE_PATHS = {NODE_DIR_PATH + '/bin'}
NODE_BIN_PATH = '{}/bin/node'.format(NODE_DIR_PATH)
NPM_BIN_PATH = '{}/bin/npm'.format(NODE_DIR_PATH)
NODE_MODULES_PATH = '{}/node_modules'.format(ENV_PATH)
NATIVEFIER_BIN_PATH = '{}/.bin/nativefier'.format(NODE_MODULES_PATH)
ELECTRON_CACHE_DIR = f'{ENV_PATH}/electron'
ELECTRON_DOWNLOAD_URL = 'https://github.com/electron/electron/releases/download/v{version}/electron-v{version}-linux-{arch}.zip'
ELECTRON_SHA256_URL = 'https://github.com/electron/electron/releases/download/v{version}/SHASUMS256.txt'
ELECTRON_WIDEVINE_URL = 'https://github.com/castlabs/electron-releases/releases/download/v{version}-wvvmp/electron-v{version}-wvvmp-linux-{arch}.zip'
ELECTRON_WIDEVINE_SHA256_URL = 'https://github.com/castlabs/electron-releases/releases/download/v{version}-wvvmp/SHASUMS256.txt'
URL_ENVIRONMENT_SETTINGS = 'https://raw.githubusercontent.com/vinifmor/bauh-files/master/web/env/v1/environment.yml'
DESKTOP_ENTRY_PATH_PATTERN = DESKTOP_ENTRIES_DIR + '/bauh.web.{name}.desktop'
URL_FIX_PATTERN = "https://raw.githubusercontent.com/vinifmor/bauh-files/master/web/fix/{url}.js"
URL_SUGGESTIONS = "https://raw.githubusercontent.com/vinifmor/bauh-files/master/web/env/v1/suggestions.yml"
UA_CHROME = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
TEMP_PATH = f'{TEMP_DIR}/web'
SEARCH_INDEX_FILE = f'{WEB_CACHE_DIR}/index.yml'
SUGGESTIONS_CACHE_FILE = f'{WEB_CACHE_DIR}/suggestions.yml'
SUGGESTIONS_CACHE_TS_FILE = map_timestamp_file(SUGGESTIONS_CACHE_FILE)
CONFIG_FILE = f'{CONFIG_DIR}/web.yml'
ENVIRONMENT_SETTINGS_CACHED_FILE = f'{WEB_CACHE_DIR}/environment.yml'
ENVIRONMENT_SETTINGS_TS_FILE = f'{WEB_CACHE_DIR}/environment.ts'
NATIVEFIER_BASE_URL = 'https://github.com/nativefier/nativefier/archive/v{version}.tar.gz'


def get_icon_path() -> str:
    return resource.get_path('img/web.svg', ROOT_DIR)
