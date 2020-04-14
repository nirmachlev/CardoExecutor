from CardoExecutor import DagWorkflow, LinearWorkflowExecutor, create_context
from CardoLibs.IO.TextFile.TextFileReader import TextFileReader
from CardoLibs.IO.TextFile.TextFileWriter import TextFileWriter

reader = TextFileReader("D:\\nir.txt")
writer = TextFileWriter("D:\\nir1.txt")
flow = DagWorkflow("nir")
flow.add_last(reader)
flow.add_last(writer)
exec = LinearWorkflowExecutor()
context = create_context("aaa",environment="local")
exec.execute(flow,context)

