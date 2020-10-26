#!/bin/bash

# Copyright (C) 2020 by sandy1709

echo "
'##::::'##::'######::'########:'########::'########:::'#######::'########:
 ##:::: ##:'##... ##: ##.....:: ##.... ##: ##.... ##:'##.... ##:... ##..::
 ##:::: ##: ##:::..:: ##::::::: ##:::: ##: ##:::: ##: ##:::: ##:::: ##::::
 ##:::: ##:. ######:: ######::: ########:: ########:: ##:::: ##:::: ##::::
 ##:::: ##::..... ##: ##...:::: ##.. ##::: ##.... ##: ##:::: ##:::: ##::::
 ##:::: ##:'##::: ##: ##::::::: ##::. ##:: ##:::: ##: ##:::: ##:::: ##::::
. #######::. ######:: ########: ##:::. ##: ########::. #######::::: ##::::
 :.......::::......:::........::..:::::..::........::::.......::::::..:::::                 
"

echo "
'##::::'##::'######::'########:'########::'########:::'#######::'########:
 ##:::: ##:'##... ##: ##.....:: ##.... ##: ##.... ##:'##.... ##:... ##..::
 ##:::: ##: ##:::..:: ##::::::: ##:::: ##: ##:::: ##: ##:::: ##:::: ##::::
 ##:::: ##:. ######:: ######::: ########:: ########:: ##:::: ##:::: ##::::
 ##:::: ##::..... ##: ##...:::: ##.. ##::: ##.... ##: ##:::: ##:::: ##::::
 ##:::: ##:'##::: ##: ##::::::: ##::. ##:: ##:::: ##: ##:::: ##:::: ##::::
. #######::. ######:: ########: ##:::. ##: ########::. #######::::: ##::::
:.......::::......:::........::..:::::..::........::::.......::::::..:::::
"

if [[ -n $HEROKU_API_KEY && -n $HEROKU_APP_NAME ]]; then
    herokuErr=$(python ./.github/herokugiturl.py)
    if [[ "$herokuErr" ]]; then 
        echo "$herokuErr"
    else
        HEROKU_GIT_URL="https://api:$HEROKU_API_KEY@git.heroku.com/$HEROKU_APP_NAME.git"
    fi
fi

FILE=/app/.git

if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    if [[ "$HEROKU_GIT_URL" ]]; then
        git clone "$HEROKU_GIT_URL" cat_ubh || git clone https://github.com/suhaash02/Dextro_userbot cat_ubc
        mv cat_ubh/.git . || mv cat_ubc/.git .
        rm -rf cat_ubh || rm -rf cat_ubc
    else
        git clone https://github.com/suhaash02/Dextro_userbot cat_ub
        mv cat_ub/.git .
        rm -rf cat_ub
    fi
fi

python -m userbot
 9  .github/herokugiturl.py 
@@ -0,0 +1,9 @@
import heroku3

from userbot.Config import Config

try:
    if Config.HEROKU_APP_NAME not in heroku3.from_key(Config.HEROKU_API_KEY).apps():
        raise Exception(f"Invalid HEROKU_APP_NAME  {Config.HEROKU_APP_NAME}")
except Exception as e:
    print(str(e))
