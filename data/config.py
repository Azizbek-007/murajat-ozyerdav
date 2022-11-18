from environs import Env

env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # admins
IP = env.str("ip")  
