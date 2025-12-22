from pathlib import Path
import logging

from utils.config_loader import load_config, IncompleteJson
from utils.logging_setup import setup_logging
#from Day8.utils.organizer import filter_processed
from utils.organizer import organizer



def main() -> None:
    config_path = Path(__file__).parent / "config.json"

    try:
        conf = load_config(config_path)
    except IncompleteJson as e:
        # logging isn't configured yet
        print(f"Config error: {e}")
        return

    setup_logging(conf)

    target_path = Path(conf["target_path"])
    logging.info("Starting run...")
    organizer(target_path, conf)
    logging.info("Finished run.")


if __name__ == "__main__":
    main()
