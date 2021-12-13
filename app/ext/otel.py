from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SpanExporter
)

class Telemetry:
  
  def __init__(self):
    pass 
    
    

class Tracer(Telemetry):
  
  provider = TracerProvider()