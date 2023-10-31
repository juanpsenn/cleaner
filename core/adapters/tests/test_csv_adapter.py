from core.adapters.csv_adapter import CsvFileAdapter

def test_extract_data_from_csv_file():
    adapter = CsvFileAdapter()
    catalog = adapter.extract_data("core/adapters/testdata/list.csv")

    assert catalog
    assert catalog.length == 4
    assert catalog.data[0][0] == "header1"
    assert isinstance(catalog.data[1][2], str)
