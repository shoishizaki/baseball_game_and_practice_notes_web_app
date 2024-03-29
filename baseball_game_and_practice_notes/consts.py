WEATHER_CHOICES = (
        ('晴','☀️ 晴'),
        ('曇','☁️ 曇'),
        ('雨','☔️ 雨'),
        ('雪','❄️ 雪'),
)

NUMBER_CHOICES_1 = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
)

NUMBER_CHOICES_2 = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),

)

NUMBER_CHOICES_3 = (
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,4),
)

POSITION_CHOICES = (
        ('投手','投手'),
        ('捕手','捕手'),
        ('一塁手','一塁手'),
        ('二塁手','二塁手'),
        ('三塁手','三塁手'),
        ('遊撃手','遊撃手'),
        ('左翼手','左翼手'),
        ('中堅手','中堅手'),
        ('右翼手','右翼手'),
        ('DH','DH'),
        ('代打','代打'),
        ('代走','代走'),
)

VICTORY_OR_DEFEAT_CHOICES = (
        ('勝ち','勝ち'),
        ('負け','負け'),
        ('引き分け','引き分け'),
)

FIELDER_RESULT_CHOICES = (
        ('空三振','空三振'),
        ('見三振','見三振'),
        ('バント三振','バント三振'),
        ('投ゴロ','投ゴロ'),
        ('捕ゴロ','捕ゴロ'),
        ('一ゴロ','一ゴロ'),
        ('二ゴロ','二ゴロ'),
        ('三ゴロ','三ゴロ'),
        ('遊ゴロ','遊ゴロ'),
        ('左ゴロ','左ゴロ'),
        ('中ゴロ','中ゴロ'),
        ('右ゴロ','右ゴロ'),
        ('投飛','投飛'),
        ('捕飛','捕飛'),
        ('一飛','一飛'),
        ('二飛','二飛'),
        ('三飛','三飛'),
        ('遊飛','遊飛'),
        ('左飛','左飛'),
        ('中飛','中飛'),
        ('右飛','右飛'),
        ('投直','投直'),
        ('一直','一直'),
        ('二直','二直'),
        ('三直','三直'),
        ('遊直','遊直'),
        ('左直','左直'),
        ('中直','中直'),
        ('右直','右直'),
        ('投邪飛','投邪飛'),
        ('捕邪飛','捕邪飛'),
        ('一邪飛','一邪飛'),
        ('二邪飛','二邪飛'),
        ('三邪飛','三邪飛'),
        ('遊邪飛','遊邪飛'),
        ('左邪飛','左邪飛'),
        ('中邪飛','中邪飛'),
        ('右邪飛','右邪飛'),
        ('二邪直','二邪直'),
        ('三邪直','三邪直'),
        ('遊邪直','遊邪直'),
        ('左邪直','左邪直'),
        ('中邪直','中邪直'),
        ('右邪直','右邪直'),
        ('投ゴロ失','投ゴロ失'),
        ('捕ゴロ失','捕ゴロ失'),
        ('一ゴロ失','一ゴロ失'),
        ('二ゴロ失','二ゴロ失'),
        ('三ゴロ失','三ゴロ失'),
        ('遊ゴロ失','遊ゴロ失'),
        ('左ゴロ失','左ゴロ失'),
        ('中ゴロ失','中ゴロ失'),
        ('右ゴロ失','右ゴロ失'),
        ('投飛失','投飛失'),
        ('捕飛失','捕飛失'),
        ('一飛失','一飛失'),
        ('二飛失','二飛失'),
        ('三飛失','三飛失'),
        ('遊飛失','遊飛失'),
        ('左飛失','左飛失'),
        ('中飛失','中飛失'),
        ('右飛失','右飛失'),
        ('投直失','投直失'),
        ('捕直失','捕直失'),
        ('一直失','一直失'),
        ('二直失','二直失'),
        ('三直失','三直失'),
        ('遊直失','遊直失'),
        ('左直失','左直失'),
        ('中直失','中直失'),
        ('右直失','右直失'),
        ('犠打失','犠打失'),
        ('投野選','投野選'),
        ('捕野選','捕野選'),
        ('一野選','一野選'),
        ('二野選','二野選'),
        ('三野選','三野選'),
        ('遊野選','遊野選'),
        ('左野選','左野選'),
        ('中野選','中野選'),
        ('右野選','右野選'),
        ('投犠野','投犠野'),
        ('捕犠野','捕犠野'),
        ('一犠野','一犠野'),
        ('二犠野','二犠野'),
        ('三犠野','三犠野'),
        ('遊犠野','遊犠野'),
        ('投ゴロ併打','投ゴロ併打'),
        ('捕ゴロ併打','捕ゴロ併打'),
        ('一ゴロ併打','一ゴロ併打'),
        ('二ゴロ併打','二ゴロ併打'),
        ('三ゴロ併打','三ゴロ併打'),
        ('遊ゴロ併打','遊ゴロ併打'),
        ('左ゴロ併打','左ゴロ併打'),
        ('中ゴロ併打','中ゴロ併打'),
        ('右ゴロ併打','右ゴロ併打'),
        ('投飛併打','投飛併打'),
        ('捕飛併打','捕飛併打'),
        ('一飛併打','一飛併打'),
        ('二飛併打','二飛併打'),
        ('三飛併打','三飛併打'),
        ('遊飛併打','遊飛併打'),
        ('左飛併打','左飛併打'),
        ('中飛併打','中飛併打'),
        ('右飛併打','右飛併打'),
        ('投直併打','投直併打'),
        ('捕直併打','捕直併打'),
        ('一直併打','一直併打'),
        ('二直併打','二直併打'),
        ('三直併打','三直併打'),
        ('遊直併打','遊直併打'),
        ('左直併打','左直併打'),
        ('中直併打','中直併打'),
        ('右直併打','右直併打'),
        ('投ゴロ安','投ゴロ安'),
        ('捕ゴロ安','捕ゴロ安'),
        ('一ゴロ安','一ゴロ安'),
        ('二ゴロ安','二ゴロ安'),
        ('三ゴロ安','三ゴロ安'),
        ('遊ゴロ安','遊ゴロ安'),
        ('左ゴロ安','左ゴロ安'),
        ('中ゴロ安','中ゴロ安'),
        ('右ゴロ安','右ゴロ安'),
        ('投飛安','投飛安'),
        ('捕飛安','捕飛安'),
        ('一飛安','一飛安'),
        ('二飛安','二飛安'),
        ('三飛安','三飛安'),
        ('遊飛安','遊飛安'),
        ('左飛安','左飛安'),
        ('中飛安','中飛安'),
        ('右飛安','右飛安'),
        ('投直安','投直安'),
        ('一直安','一直安'),
        ('二直安','二直安'),
        ('三直安','三直安'),
        ('遊直安','遊直安'),
        ('左直安','左直安'),
        ('中直安','中直安'),
        ('右直安','右直安'),
        ('投ゴロ2','投ゴロ2'),
        ('捕ゴロ2','捕ゴロ2'),
        ('一ゴロ2','一ゴロ2'),
        ('二ゴロ2','二ゴロ2'),
        ('三ゴロ2','三ゴロ2'),
        ('遊ゴロ2','遊ゴロ2'),
        ('左ゴロ2','左ゴロ2'),
        ('中ゴロ2','中ゴロ2'),
        ('右ゴロ2','右ゴロ2'),
        ('投飛2','投飛2'),
        ('捕飛2','捕飛2'),
        ('一飛2','一飛2'),
        ('二飛2','二飛2'),
        ('三飛2','三飛2'),
        ('遊飛2','遊飛2'),
        ('左飛2','左飛2'),
        ('中飛2','中飛2'),
        ('右飛2','右飛2'),
        ('投直2','投直2'),
        ('一直2','一直2'),
        ('二直2','二直2'),
        ('三直2','三直2'),
        ('遊直2','遊直2'),
        ('左直2','左直2'),
        ('中直2','中直2'),
        ('右直2','右直2'),
        ('投ゴロ3','投ゴロ3'),
        ('捕ゴロ3','捕ゴロ3'),
        ('一ゴロ3','一ゴロ3'),
        ('二ゴロ3','二ゴロ3'),
        ('三ゴロ3','三ゴロ3'),
        ('遊ゴロ3','遊ゴロ3'),
        ('左ゴロ3','左ゴロ3'),
        ('中ゴロ3','中ゴロ3'),
        ('右ゴロ3','右ゴロ3'),
        ('投飛3','投飛3'),
        ('捕飛3','捕飛3'),
        ('一飛3','一飛3'),
        ('二飛3','二飛3'),
        ('三飛3','三飛3'),
        ('遊飛3','遊飛3'),
        ('左飛3','左飛3'),
        ('中飛3','中飛3'),
        ('右飛3','右飛3'),
        ('投直3','投直3'),
        ('一直3','一直3'),
        ('二直3','二直3'),
        ('三直3','三直3'),
        ('遊直3','遊直3'),
        ('左直3','左直3'),
        ('中直3','中直3'),
        ('右直3','右直3'),
        ('左本','左本'),
        ('中本','中本'),
        ('右本','右本'),
        ('投犠打','投犠打'),
        ('捕犠打','捕犠打'),
        ('一犠打','一犠打'),
        ('二犠打','二犠打'),
        ('三犠打','三犠打'),
        ('遊犠打','遊犠打'),
        ('投犠飛', '投犠飛'),
        ('捕犠飛', '捕犠飛'),
        ('一犠飛', '一犠飛'),
        ('二犠飛', '二犠飛'),
        ('三犠飛', '三犠飛'),
        ('遊犠飛', '遊犠飛'),
        ('左犠飛', '左犠飛'),
        ('中犠飛', '中犠飛'),
        ('右犠飛', '右犠飛'),
        ('四球','四球'),
        ('死球','死球'),
        ('敬遠','敬遠'),
        ('打撃妨','打撃妨'),
        ('守妨害','守妨害'),
)
