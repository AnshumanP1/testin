import logging

logging.basicConfig(
    filename='data_processing.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

logging.info("Logging configured.")

def process_data():
  """Simulates a data processing workflow with logging."""
  logging.info("Starting data processing")
  # Simulate some processing steps
  logging.warning("Missing optional configuration value")
  # Simulate an error condition
  logging.error("Failed to read input file")
  logging.info("Data processing finished.") # Add a concluding message


if __name__ == '__main__':
  process_data()
