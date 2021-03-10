import xlsxwriter

def executeExport(query):
    artist_info = query[0]
    album_artist_name = artist_info[0] # artist name
    album_artist_link = artist_info[1] # link url name
    print("[#2] Export Xlsx: Init export...")

    workbook = xlsxwriter.Workbook(str(album_artist_name) + '.xlsx')
    bold = workbook.add_format({'bold': True})
    blue = workbook.add_format({'color': 'blue'})
    center = workbook.add_format({'align': 'center'})
    __formatMusicWorksheet(workbook, bold, blue, query)
    __formatAlbumWorksheet(workbook, bold, blue, center, query)
    workbook.close()

def __formatMusicWorksheet(workbook, bold, blue, query):
    print("[#2] Export Xlsx: Init Music Worksheet format...")
    worksheet = workbook.add_worksheet("Musics")
    worksheet.set_column(0, 0, 80)
    worksheet.set_column(1, 2, 15)
    worksheet.write('A1', 'Song Name', bold)
    worksheet.write('B1', 'Song Duration', bold)
    worksheet.write('C1', 'Song Rank', bold)

    songs_info = query[2]

    trackname_list, duration_list, rank_list, link_list = [[], [], [], []] 
    for song in songs_info:
        trackname_list.append(song[0])
        duration_list.append(song[1])
        rank_list.append(song[2])
        link_list.append(song[3])

    row = 1
    col = 0
    for link in link_list:
        worksheet.write_url(row, col, link)
        row +=1
    row = 1
    col = 0
    for trackname in trackname_list:
        worksheet.write(row, col, trackname, blue)
        row +=1
    row = 1
    col = 1
    for trackduration in duration_list:
        worksheet.write(row, col, trackduration)
        row +=1
    row = 1
    col = 2
    for trackrank in rank_list:
        worksheet.write(row, col, trackrank)
        row +=1
    print("[#2] Export Xlsx: finished Music format...")

def __formatAlbumWorksheet(workbook, bold, blue, center, query):
    worksheet = workbook.add_worksheet('Albuns')
    worksheet.set_column(0, 0, 50)
    worksheet.set_column(1, 4, 18)
    worksheet.write('A1', 'Album Name', bold)
    worksheet.write('B1', 'Album Duration', bold)
    worksheet.write('C1', 'Album Release Date', bold)
    worksheet.write('D1', 'Album Fans', bold)
    print("[#2] Export Xlsx: Init Artist Worksheet format...")

    albuns_info = query[1]

    name_list, duration_list, fans_list, link_list, release_date_list = [[], [], [], [], []] 
    for album in albuns_info:
        name_list.append(album[0])
        duration_list.append(album[1])
        release_date_list.append(album[2])
        fans_list.append(album[3])
        link_list.append(album[4])

    row = 1
    col = 0
    for link in link_list:
        worksheet.write_url(row, col, link)
        row +=1
    row = 1
    col = 0
    for name in name_list:
        worksheet.write(row, col, name, blue)
        row +=1
    row = 1
    col = 1
    for duration in duration_list:
        worksheet.write(row, col, duration)
        row +=1
    row = 1
    col = 2
    for release_date in release_date_list:
        worksheet.write(row, col, release_date, center)
        row +=1
    row = 1
    col = 3
    for fans in fans_list:
        worksheet.write(row, col, fans)
        row +=1
    print("[#2] Export Xlsx: finished Artist format...")