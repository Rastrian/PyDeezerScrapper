from dataHandler import getData
from exportExcel import executeExport

# data[] -> (data.[].album.id + c) -> (a + b) -> total
artist_id = 4720
query = getData(artist_id)
executeExport(query)
