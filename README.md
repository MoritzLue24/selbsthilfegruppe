# selbsthilfegruppe
Ein Discord Bot für einen PloudOS Minecraft Server.

## Config
Die configdatei befindet sich bei ./config.cfg
```json
{
	"ploudos": {
		"username": "XXXXXXXXXXXX",
		"password": "XXXXXXXXXXXX",
		"server-name": "XXXXXXXXXXXX"
	},
	"discord": {
		"token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
	},
	"logging": {
		"version": 1,
        "disabled_existing_loggers": false,
        "formatters": {
            "verbose": {"format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"},
            "simple": {"format": "%(levelname)-10s - %(module)-15s : %(message)s"}
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "simple"
            },
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "formatter": "verbose",
                "filename": "info.log",
                "mode": "w"
            }
        },
        "loggers": {
            "bot": {
                 "handlers": ["console", "file"],
                 "level": "INFO",
                 "propagate": false
            },
			"discord": {
				"handlers": ["console", "file"],
				"level": "INFO",
				"propagate": false
			}
        }
	}
}
```
