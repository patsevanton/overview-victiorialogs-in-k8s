
import argparse
import logging
import random
import time

def setup_logging():
    """Sets up the logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

def generate_logs(rate, duration):
    """Generates logs at a specified rate for a given duration."""
    end_time = time.time() + duration if duration else None
    log_levels = [logging.INFO, logging.WARNING, logging.ERROR]
    log_messages = [
        "User logged in successfully",
        "Failed to connect to database",
        "Invalid input received",
        "Processing request",
        "Request completed",
    ]

    while not end_time or time.time() < end_time:
        level = random.choice(log_levels)
        message = random.choice(log_messages)
        logging.log(level, message)
        time.sleep(1 / rate)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kubernetes Log Generator")
    parser.add_argument(
        "--rate", type=int, default=1, help="Logs per second"
    )
    parser.add_argument(
        "--duration", type=int, help="Duration in seconds (optional)"
    )
    args = parser.parse_args()

    setup_logging()
    generate_logs(args.rate, args.duration)
