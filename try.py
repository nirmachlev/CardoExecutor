from CardoExecutor import DagWorkflow, LinearWorkflowExecutor, create_context
from CardoLibs.IO.TextFile.TextFileReader import TextFileReader
from CardoLibs.IO.TextFile.TextFileWriter import TextFileWriter
from CardoLibs.IO.Oracle.OracleReader import OracleReader
from CardoLibs.IO.Oracle.OracleWriter import OracleWriter



#connectionString = "Data Source=ORCL;User Id=SYS AS SYSDBA;Password=12345;"
connectionString = "User Id=SYS AS SYSDBA;Password=12345;Data Source=oracle"
tableName = "cats"
reader = OracleReader(table_name=tableName, connection_string=connectionString)
writer = TextFileWriter("C:\\Cardo\\daniel.txt")
flow = DagWorkflow("DanielOracle")
flow.add_last(reader)
flow.add_last(writer)
exec = LinearWorkflowExecutor()
context = create_context("Oracle",environment="local")
exec.execute(flow,context)
