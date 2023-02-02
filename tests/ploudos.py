import sys, json, PloudosAPI


with open("config.cfg", "r") as f:
    cfg = json.loads(f.read())

session = PloudosAPI.login(cfg["ploudos"]["username"], cfg["ploudos"]["password"])
servers = session.get_servers_with_name(cfg["ploudos"]["server-name"])

try:
    server = servers[0]
except IndexError:
    logger.critical("Server with name '{cfg['ploudos']['server-name']}' not found.")
    sys.exit(1)

server.start()
