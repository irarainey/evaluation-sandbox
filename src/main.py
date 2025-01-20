import os
import sys
import logging
from dotenv import load_dotenv
from openai import AzureOpenAI


# Main function
def main() -> None:
    # Load environment variables
    load_dotenv()

    # Check if Azure OpenAI environment variables are set
    if not os.getenv("AZURE_OPENAI_ENDPOINT") or not os.getenv("AZURE_OPENAI_API_KEY"):
        logging.error("Required environment variables not set.")
        sys.exit(1)

    # Create an instance of the Azure OpenAI client
    gpt_client = AzureOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version="2024-08-01-preview",
    )

    # And we're done!
    logging.info("Complete!")


# Entry point of the script
if __name__ == "__main__":
    main()
