from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from flask import Flask
import time

provider = TracerProvider()
jaeger_exporter = JaegerExporter(agent_host_name='localhost',
                                 agent_port=6831
                                 )
processor = BatchSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)


tracer = trace.get_tracer('nome do tracer')

app = Flask(__name__)

@app.route('/')
def index():
  with tracer.start_as_current_span("foo"):
    time.sleep(3)
    return 'teste'