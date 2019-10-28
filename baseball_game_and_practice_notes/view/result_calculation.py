from baseball_game_and_practice_notes.models import GameNote


def calculate_plate_appearance():
    plate_appearance = 0
    game_data = GameNote.objects.all()
    for data in game_data:
        if data.fielder_result_1 is not None:
            plate_appearance += 1
        if data.fielder_result_2 is not None:
            plate_appearance += 1
        if data.fielder_result_3 is not None:
            plate_appearance += 1
        if data.fielder_result_4 is not None:
            plate_appearance += 1
        if data.fielder_result_5 is not None:
            plate_appearance += 1
        if data.fielder_result_6 is not None:
            plate_appearance += 1
        if data.fielder_result_7 is not None:
            plate_appearance += 1
        if data.fielder_result_8 is not None:
            plate_appearance += 1
        if data.fielder_result_9 is not None:
            plate_appearance += 1
        if data.fielder_result_10 is not None:
            plate_appearance += 1
    return plate_appearance


def calculate_not_include_at_bat():
    not_include_at_bat_count = 0
    not_include_at_bat_case = ('投犠打', '捕犠打', '一犠打', '二犠打', '三犠打', '遊犠打', '投犠飛', '捕犠飛', '一犠飛', '二犠飛',
                               '三犠飛', '遊犠飛', '左犠飛', '中犠飛', '右犠飛', '四球', '死球', '敬遠', '打撃妨', '守妨害')
    game_data = GameNote.objects.all()
    for data in game_data:
        for case in not_include_at_bat_case:
            if data.fielder_result_1 == case:
                not_include_at_bat_count += 1
            if data.fielder_result_2 == case:
                not_include_at_bat_count += 1
            if data.fielder_result_3 == case:
                not_include_at_bat_count += 1
            if data.fielder_result_4 == case:
                not_include_at_bat_count += 1
            if data.fielder_result_5 == case:
                not_include_at_bat_count += 1
            if data.fielder_result_6 == case:
                not_include_at_bat_count += 1
            if data.fielder_result_7 == case:
                not_include_at_bat_count += 1
            if data.fielder_result_8 == case:
                not_include_at_bat_count += 1
            if data.fielder_result_9 == case:
                not_include_at_bat_count += 1
            if data.fielder_result_10 == case:
                not_include_at_bat_count += 1
    return not_include_at_bat_count


def calculate_at_bat():
    return calculate_plate_appearance() - calculate_not_include_at_bat()


def calculate_run_batted_in():
    rbi_count = 0
    game_data = GameNote.objects.all()
    for data_1 in game_data:
        rbi_count += data_1.fielder_result_1_RBI
    for data_2 in game_data:
        rbi_count += data_2.fielder_result_2_RBI
    for data_3 in game_data:
        rbi_count += data_3.fielder_result_3_RBI
    for data_4 in game_data:
        rbi_count += data_4.fielder_result_4_RBI
    for data_5 in game_data:
        rbi_count += data_5.fielder_result_5_RBI
    for data_6 in game_data:
        rbi_count += data_6.fielder_result_6_RBI
    for data_7 in game_data:
        rbi_count += data_7.fielder_result_7_RBI
    for data_8 in game_data:
        rbi_count += data_8.fielder_result_8_RBI
    for data_9 in game_data:
        rbi_count += data_9.fielder_result_9_RBI
    for data_10 in game_data:
        rbi_count += data_10.fielder_result_10_RBI
    return rbi_count


def calculate_hits():
    hits_count = 0
    game_data = GameNote.objects.all()
    hits_case = ('投ゴロ安', '捕ゴロ安', '一ゴロ安', '二ゴロ安', '三ゴロ安', '遊ゴロ安', '左ゴロ安', '中ゴロ安', '右ゴロ安', '投飛安',
                 '投飛安', '捕飛安', '一飛安', '一飛安', '二飛安', '三飛安', '遊飛安', '左飛安', '中飛安', '右飛安', '投直安', '一直安',
                 '二直安', '三直安', '遊直安', '左直安', '中直安', '右直安', '投ゴロ2', '捕ゴロ2', '一ゴロ2', '二ゴロ2', '三ゴロ2',
                 '遊ゴロ2', '左ゴロ2', '中ゴロ2', '右ゴロ2', '投飛2', '捕飛2', '一飛2', '二飛2', '三飛2', '遊飛2', '左飛2', '中飛2',
                 '右飛2', '投直2', '一直2', '二直2', '三直2', '遊直2', '左直2', '中直2', '右直2', '投ゴロ3', '捕ゴロ3', '一ゴロ3',
                 '二ゴロ3', '三ゴロ3', '遊ゴロ3', '左ゴロ3', '中ゴロ3', '右ゴロ3', '投飛3', '捕飛3', '一飛3', '二飛3', '三飛3', '遊飛3',
                 '左飛3', '中飛3', '右飛3', '投直3', '一直3', '二直3', '三直3', '遊直3', '左直3', '中直3', '右直3', '左本', '中本', '右本')
    for data in game_data:
        for case in hits_case:
            if data.fielder_result_1 == case:
                hits_count += 1
            if data.fielder_result_2 == case:
                hits_count += 1
            if data.fielder_result_3 == case:
                hits_count += 1
            if data.fielder_result_4 == case:
                hits_count += 1
            if data.fielder_result_5 == case:
                hits_count += 1
            if data.fielder_result_6 == case:
                hits_count += 1
            if data.fielder_result_7 == case:
                hits_count += 1
            if data.fielder_result_8 == case:
                hits_count += 1
            if data.fielder_result_9 == case:
                hits_count += 1
            if data.fielder_result_10 == case:
                hits_count += 1
    return hits_count
