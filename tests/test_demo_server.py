import os
import unittest

import torch as T

from server.synthesizer import Synthesizer
from tests import get_tests_input_path, get_tests_output_path, get_tests_path
from utils.text.symbols import phonemes, symbols
from utils.generic_utils import load_config, save_checkpoint, setup_model


class DemoServerTest(unittest.TestCase):
    def _create_random_model(self):
        config = load_config(os.path.join(get_tests_output_path(), 'dummy_model_config.json'))
        num_chars = len(phonemes) if config.use_phonemes else len(symbols)
        model = setup_model(num_chars, 0, config)
        output_path = os.path.join(get_tests_output_path())
        save_checkpoint(model, None, None, None, output_path, 10, 10)

    def test_in_out(self):
        self._create_random_model()
        config = load_config(os.path.join(get_tests_input_path(), 'server_config.json'))
        synthesizer = Synthesizer(config)
        synthesizer.tts("Better this test works!!")
