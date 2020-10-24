# Dextro_userbot

### The Easy Way to deploy the bot
Get APP ID and API HASH from [HERE](https://my.telegram.org) and BOT TOKEN from [Bot Father](https://t.me/botfather) and then Generate stringsession by clicking on run.on.repl.it button below and then click on deploy to heroku . Before clicking on deploy to heroku just click on fork and star just below

[![Get string session](https://repl.it/badge/github/suhaash02/Dexter_userbot)](https://generatestringsession.suhaash02.repl.run/)

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/suhaash02/Dextro_userbot)
<p align="center">
  <a href="https://github.com/suhaash02/Dextro_userbot/fork">
    <img src="https://img.shields.io/github/forks/suhaash02/Dextro_userbot?label=Fork&style=social">
    
  </a>
  <a href="https://github.com/suhaash02/Dextro_userbot">
    <img src="https://img.shields.io/github/stars/suhaash02/Dextro_userbot?style=social">
  </a>
</p>


[![Dextro_userbot logo](https://telegra.ph/file/174268e8434a45c80b905.jpg)](https://heroku.com/deploy?template=https://github.com/suhaash02/Dextro_userbot)


### Join [here](https://t.me/Dextro_support) for updates and tuts and [here](https://t.me/Dextro_support) for discussion and bugs

### The Normal Way

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration



**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**

Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`

    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
