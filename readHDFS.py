from fastparquet import ParquetFile

pf = ParquetFile('D:\\d_erp2_wh_info\\000000_0')
df = pf.to_pandas()
df2 = pf.to_pandas(['wh_addr','wh_code'])