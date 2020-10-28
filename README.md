# Dextro_userbot



### The Easy Way to deploy the bot
Get APP ID and API HASH from [HERE](https://my.telegram.org) and BOT TOKEN from [Bot Father](https://t.me/botfather) and then Generate stringsession by clicking on run.on.repl.it button below and then click on deploy to heroku . Before clicking on deploy to heroku just click on fork and star just below

![logo](https://telegra.ph/file/317af157cbeb1bd621043.png)



[![Get string session](https://repl.it/badge/github/suhaash02/Dextro_userbot)](https://dextrouserbot.theavengers.repl.run/)

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/suhaash02/Dextro_userbot/tree/main"> <img src="https://telegra.ph/file/885e585979bf53662fb23.png." alt="Deploy to Heroku" width="200" height="33.33"/></a></p>

### Join [here](https://t.me/Dextro_support) for updates and tuts and [here](https://t.me/Dextro_support) for discussion and bugs

### The Normal Way

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98aq0f581e"
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
