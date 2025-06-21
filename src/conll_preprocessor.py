import pandas as pd
import re
import os

class CoNLLPreprocessor:
    """
    A class to preprocess Amharic messages for Named Entity Recognition (NER)
    by formatting them into the CoNLL format.
    """

    def __init__(self, csv_path: str, output_path: str, sample_size: int = 40):
        """
        Initializes the preprocessor with the input CSV file, output path,
        and the number of messages to sample.

        :param csv_path: Path to the CSV file containing preprocessed messages
        :param output_path: Path to save the CoNLL-formatted output file
        :param sample_size: Number of random messages to extract and tokenize
        """
        self.csv_path = csv_path
        self.output_path = output_path
        self.sample_size = sample_size
        self.messages = []  # Holds sampled messages for processing

    def load_messages(self):
        """
        Loads and samples a subset of messages from the CSV file.
        Raises an error if the file is not found.
        """
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"CSV file not found: {self.csv_path}")

        df = pd.read_csv(self.csv_path)

        # Sample non-null messages from the 'text' column
        self.messages = df['text'].dropna().sample(n=self.sample_size, random_state=42).tolist()
        print(f"Loaded {len(self.messages)} messages from CSV.")

    def tokenize(self, text: str):
        """
        Tokenizes an Amharic message into words and punctuation.

        :param text: The input message text
        :return: List of tokens
        """
        return re.findall(r'\w+|[^\s\w]', text, re.UNICODE)

    def write_conll_file(self):
        """
        Writes the tokenized messages to a file in CoNLL format.
        Each token is placed on a new line with a default label "O".
        A blank line separates each message.
        """
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

        with open(self.output_path, 'w', encoding='utf-8') as f:
            for message in self.messages:
                tokens = self.tokenize(message)
                for token in tokens:
                    f.write(f"{token} O\n")  # Initial label is "O" (non-entity)
                f.write("\n")  # Separate each message with a blank line

        print(f"Saved CoNLL-format file to: {self.output_path}")

    def run(self):
        """
        Orchestrates the preprocessing workflow:
        1. Load messages
        2. Tokenize and write to CoNLL format
        """
        self.load_messages()
        self.write_conll_file()

# Script entry point
if __name__ == "__main__":
    preprocessor = CoNLLPreprocessor(
        csv_path="data/preprocessed_data.csv",       # Input: preprocessed CSV file
        output_path="data/conll_raw_sample.txt",     # Output: CoNLL format file
        sample_size=40                               # Number of messages to label
    )
    preprocessor.run()
