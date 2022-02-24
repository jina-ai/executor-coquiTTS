import tempfile

from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
from jina import Executor, DocumentArray, requests

model_name = 'tts_models/en/ljspeech/tacotron2-DDC'
manager = ModelManager('models.json')
model_path, config_path, model_item = manager.download_model(model_name)

synthesizer = Synthesizer(model_path,
                          config_path)


class CoquiTTS(Executor):
    """Executor that leverages CoquiTTS engine for text2speech"""

    @requests
    def tts(self, docs: DocumentArray, **kwargs):
        for d in docs:
            with tempfile.NamedTemporaryFile() as tmp:
                w = synthesizer.tts(d.text)
                synthesizer.save_wav(w, tmp.name)
                d.uri = tmp.name
                d.mime_type = 'audio/wav'
                d.convert_uri_to_datauri(base64=True)
