from environs import Env
from dataclasses import dataclass

@dataclass
class Bots:
    bot_token: str
    admin_id: int

@dataclass
class Settings:
    bots: Bots

def get_settings(path:str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str('TOKEN'),
            admin_id=env.int('admins')
        )
    )

settings = get_settings('input')

klass=['7а','7б','7в','7г','7д','7е','8а','8б','8в','8г','8д','8м','9б','9в','9г','9д']