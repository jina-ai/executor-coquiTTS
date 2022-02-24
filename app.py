from jina import Flow, Document

from executor import CoquiTTS

f = Flow().add(uses=CoquiTTS)

with f:
    r = f.post('/', Document(text='The following code can be copy-paste and run as-is.'))
    r[0].display()
