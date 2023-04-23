from typing import Tuple

from .api import (
    generate_audio,
    text_to_semantic,
    semantic_to_waveform,
    save_as_prompt,
)
from .generation import SAMPLE_RATE, preload_models

def generate_and_save_audio(text: str, output_file: str) -> None:
    """
    Generate audio from the given text and save it to the specified output file.

    Args:
        text (str): The input text to be converted to speech.
        output_file (str): The path to the output file where the generated audio will be saved.

    Returns:
        None
    """
    audio = generate_audio(text)
    save_as_prompt(audio, output_file)


def text_to_waveform(text: str) -> Tuple:
    """
    Convert the given text to a waveform representation.

    Args:
        text (str): The input text to be converted to a waveform.

    Returns:
        Tuple: A tuple containing the waveform data and the sample rate.
    """
    semantic = text_to_semantic(text)
    waveform = semantic_to_waveform(semantic)
    return waveform, SAMPLE_RATE