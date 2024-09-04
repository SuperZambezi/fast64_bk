
bk_MapModelDataTableStart = 0x10CD0

# FORMAT:
# (
#   "Map Model Name",
#   (
#       (vanilla) address of compressed model file (?), 
#       address of model-file offset within model-file datatable
#   )
# )
bk_DictMapModelOffsetTable = {
    "(0x00) ??? - Unknown 01":                     (0x5D93D0, 0x101E8),
    "(0x01) TTC - Treasure Trove Cove":            (0x5D93D0, 0x101F0),
    "(0x02) TTC - Treasure Trove Cove B":          (0x6015B8, 0x101F8),
    "(0x03) TTC - Crab Shell A":                   (0x604450, 0x10200),
    "(0x04) TTC - Crab Shell B":                   (0x6086D0, 0x10208),
    "(0x05) TTC - Pirate Ship A":                  (0x60A0B8, 0x10210),
    "(0x06) TTC - Pirate Ship B":                  (0x60EC18, 0x10218),
    "(0x07) TTC - Sand Castle A":                  (0x60FC30, 0x10220),
    "(0x08) TTC - Sand Castle B":                  (0x61E308, 0x10228),
    "(0x09) TTC - Sharkfood Island A":             (0x61F250, 0x10230),
    "(0x0A) GV  - Gobi's Valley A":                (0x625688, 0x10238),
    "(0x0B) GV  - Gobi's Valley B":                (0x6456C8, 0x10240),
    "(0x0C) GV  - Match Game":                     (0x646058, 0x10248),
    "(0x0D) ??? - Unknown 02":                     (0x6540B0, 0x10250),
    "(0x0E) GV  - Maze A":                         (0x6540B0, 0x10258),
    "(0x0F) GV  - Maze B":                         (0x6653F8, 0x10260),
    "(0x10) GV  - Water Pyramid A":                (0x665A28, 0x10268),
    "(0x11) GV  - Water Pyramid B":                (0x66C888, 0x10270),
    "(0x12) GV  - Rupee's House":                  (0x66D220, 0x10278),
    "(0x13) GV  - Inside the Sphinx":              (0x6728F0, 0x10280),
    "(0x14) GV  - Blue Egg Chamber A":             (0x678678, 0x10288),
    "(0x15) MMM - Mad Monster Mansion A":          (0x67D580, 0x10290),
    "(0x16) MMM - Mad Monster Mansion B":          (0x6A9990, 0x10298),
    "(0x17) MMM - Drainpipe A":                    (0x6AF8C0, 0x102A0),
    "(0x18) MMM - Cellar A":                       (0x6B1F00, 0x102A8),
    "(0x19) MMM - Secret Church Room A":           (0x6BE500, 0x102B0),
    "(0x1A) MMM - Secret Church Room B":           (0x62C318, 0x102B8),
    "(0x1B) MMM - Dining Room A":                  (0x6C3DE0, 0x102C0),
    "(0x1C) MMM - Church A":                       (0x6D58F8, 0x102C8),
    "(0x1D) MMM - Church B":                       (0x6EAD10, 0x102D0),
    "(0x1E) MMM - Tumbler's Shed":                 (0x6EBA00, 0x102D8),
    "(0x1F) MMM - Egg Room A":                     (0x6FE850, 0x102E0),
    "(0x20) MMM - Egg Room B":                     (0x703290, 0x102E8),
    "(0x21) MMM - Note Room A":                    (0x7050E8, 0x102F0),
    "(0x22) MMM - Note Room B":                    (0x709C80, 0x102F8),
    "(0x23) MMM - Feather Room A":                 (0x70BAE0, 0x10300),
    "(0x24) MMM - Feather Room B":                 (0x714648, 0x10308),
    "(0x25) MMM - Bathroom A":                     (0x7153A8, 0x10310),
    "(0x26) MMM - Bathroom B":                     (0x71D218, 0x10318),
    "(0x27) MMM - Bedroom A":                      (0x71FE10, 0x10320),
    "(0x28) MMM - Bedroom B":                      (0x72B478, 0x10328),
    "(0x29) MMM - Gold Feather Room A":            (0x72C938, 0x10330),
    "(0x2A) MMM - Gold Feather Room B":            (0x732870, 0x10338),
    "(0x2B) MMM - Well A":                         (0x734548, 0x10340),
    "(0x2C) MMM - Well B":                         (0x73A920, 0x10348),
    "(0x2D) MMM - Drainpipe B":                    (0x73B3D8, 0x10350),
    "(0x2E) MMM - Septic Tank A":                  (0x73BFC0, 0x10358),
    "(0x2F) MMM - Septic Tank B":                  (0x742170, 0x10360),
    "(0x30) MMM - Dining Room B":                  (0x742C38, 0x10368),
    "(0x31) MMM - Cellar B":                       (0x745520, 0x10370),
    "(0x32) ??? - Dark Room":                      (0x746348, 0x10378),
    "(0x33) CS  - Intro A":                        (0x7464A0, 0x10380),
    "(0x34) CS  - Ncube A":                        (0x749710, 0x10388),
    "(0x35) CS  - Grunty's Final Words A":         (0x749798, 0x10390),
    "(0x36) CS  - Ncube B":                        (0x766FA0, 0x10398),
    "(0x37) CS  - Intro B":                        (0x767470, 0x103A0),
    "(0x38) CS  - Banjo's House A":                (0x767808, 0x103A8),
    "(0x39) CS  - Grunty's Final Words B":         (0x7702E8, 0x103B0),
    "(0x3A) CS  - Banjo's House B":                (0x774520, 0x103B8),
    "(0x3B) CS  - Beach Ending B":                 (0x774AF0, 0x103C0),
    "(0x3C) CS  - With Falling twords Ground A":   (0x7757A8, 0x103C8),
    "(0x3D) ??? - Unknown 03":                     (0x778C98, 0x103D0),
    "(0x3E) CS  - Floor 5 B":                      (0x778C98, 0x103D8),
    "(0x3F) CS  - Beach Ending A":                 (0x7796E0, 0x103E0),
    "(0x40) MM  - Mumbo's Mountain A":             (0x77CF08, 0x103E8),
    "(0x41) MM  - Mumbo's Mountain B":             (0x7A2148, 0x103F0),
    "(0x42) MM  - Termite Hill A":                 (0x7A5AF8, 0x103F8),
    "(0x43) MM  - Termite Hill B":                 (0x7AB908, 0x10400),
    "(0x44) G   - Mumbo's Skull":                  (0x7AC9A8, 0x10408),
    "(0x45) ??? - Unknown 04":                     (0x7BC388, 0x10410),
    "(0x46) RBB - Rusty Bucket Bay A":             (0x7BC388, 0x10418),
    "(0x47) RBB - Rusty Bucket Bay B":             (0x7EA870, 0x10420),
    "(0x48) RBB - Machine Room A":                 (0x7F25C8, 0x10428),
    "(0x49) RBB - Machine Room B":                 (0x804F70, 0x10430),
    "(0x4A) RBB - Big Fish Warehouse A":           (0x807618, 0x10438),
    "(0x4B) RBB - Big Fish Warehouse B":           (0x812E58, 0x10440),
    "(0x4C) RBB - Boat Room A":                    (0x813D18, 0x10448),
    "(0x4D) RBB - Boat Room B":                    (0x81C910, 0x10450),
    "(0x4E) RBB - Container 1 A":                  (0x81E740, 0x10458),
    "(0x4F) RBB - Container 2 A":                  (0x825958, 0x10460),
    "(0x50) RBB - Container 3 A":                  (0x82AFB0, 0x10468),
    "(0x51) RBB - Captain's Cabin A":              (0x8308F0, 0x10470),
    "(0x52) RBB - Captain's Cabin B":              (0x837C38, 0x10478),
    "(0x53) RBB - Sea Grublin's Cabin A":          (0x8388C8, 0x10480),
    "(0x54) RBB - Boss Boom Box Room A":           (0x8448F0, 0x10488),
    "(0x55) RBB - Boss Boom Box Room B":           (0x849248, 0x10490),
    "(0x56) RBB - Boss Boom Box Room (2) A":       (0x8448F0, 0x10488),
    "(0x57) RBB - Boss Boom Box Room (2) B":       (0x849248, 0x10490),
    "(0x58) RBB - Navigation Room A":              (0x849768, 0x10498),
    "(0x59) RBB - Boom Box Room (Pipe) A":         (0x856D08, 0x104A0),
    "(0x5A) RBB - Boom Box Room (Pipe) B":         (0x85F9B8, 0x104A8),
    "(0x5B) RBB - Kitchen A":                      (0x8600F0, 0x104B0),
    "(0x5C) RBB - Kitchen B":                      (0x86C340, 0x104B8),
    "(0x5D) RBB - Anchor Room A":                  (0x86D2B0, 0x104C0),
    "(0x5E) RBB - Anchor Room B":                  (0x877548, 0x104C8),
    "(0x5F) RBB - Navigation Room B":              (0x877E38, 0x104D0),
    "(0x60) FP  - Freezeezy Peak A":               (0x8786C0, 0x104D8),
    "(0x61) FP  - Freezeezy Peak B":               (0x894618, 0x104E0),
    "(0x62) FP  - Igloo A":                        (0x8968B0, 0x104E8),
    "(0x63) FP  - Christmas Tree A":               (0x89EBB8, 0x104F0),
    "(0x64) FP  - Wozza's Cave A":                 (0x8A5FE0, 0x104F8),
    "(0x65) FP  - Wozza's Cave B":                 (0x8B4978, 0x10500),
    "(0x66) FP  - Igloo B":                        (0x8B6AC8, 0x10508),
    "(0x67) SM  - Spiral Mountain A":              (0x8B8AB0, 0x10510),
    "(0x68) SM  - Spiral Mountain B":              (0x8EA050, 0x10518),
    "(0x69) BGS - Bubblegloop Swamp A":            (0x8F0E48, 0x10520),
    "(0x6A) BGS - Bubblegloop Swamp B":            (0x918878, 0x10528),
    "(0x6B) BGS - Mr. Vile A":                     (0x9225D8, 0x10530),
    "(0x6C) BGS - Tiptup Quior A":                 (0x92A940, 0x10538),
    "(0x6D) BGS - Tiptup Quior B":                 (0x930E98, 0x10540),
    "(0x6E) ??? - Test Map A":                     (0x931908, 0x10548),
    "(0x6F) ??? - Test Map B":                     (0x931E70, 0x10550),
    "(0x70) CCW - Click Clock Woods A":            (0x9323D0, 0x10558),
    "(0x71) CCW - Spring A":                       (0x966C48, 0x10560),
    "(0x72) CCW - Summer A":                       (0x9981C8, 0x10568),
    "(0x73) CCW - Autumn A":                       (0x9D0A50, 0x10570),
    "(0x74) CCW - Winter A":                       (0xA07400, 0x10578),
    "(0x75) CCW - Wasp Hive A":                    (0xA422D8, 0x10580),
    "(0x76) CCW - Nabnut's House A":               (0xA4D040, 0x10588),
    "(0x77) CCW - Whiplash Room A":                (0xA55A18, 0x10590),
    "(0x78) CCW - Nabnut's Attic 1":               (0xA5CA20, 0x10598),
    "(0x79) CCW - Nabnut's Attic 2 A":             (0xA63548, 0x105A0),
    "(0x7A) CCW - Nabnut's Attic 2 B":             (0xA674B8, 0x105A8),
    "(0x7B) CCW - Click Clock Woods B":            (0xA68620, 0x105B0),
    "(0x7C) CCW - Spring B":                       (0xA69A48, 0x105B8),
    "(0x7D) CCW - Summer B":                       (0xA6CA70, 0x105C0),
    "(0x7E) CCW - Autumn B":                       (0xA700C0, 0x105C8),
    "(0x7F) CCW - Winter B":                       (0xA73680, 0x105D0),
    "(0x80) GL  - Quiz Room":                      (0xA795B8, 0x105D8),
    "(0x81) ??? - Unknown 05":                     (0xA9E628, 0x105E0),
    "(0x82) ??? - Unknown 06":                     (0xA9E628, 0x105E8),
    "(0x83) ??? - Unknown 07":                     (0xA9E628, 0x105F0),
    "(0x84) ??? - Unknown 08":                     (0xA9E628, 0x105F8),
    "(0x85) CC  - Clanker's Cavern A":             (0xAD0AC8, 0x10600),
    "(0x86) CC  - Clanker's Cavern B":             (0xAD5618, 0x10608),
    "(0x87) CC  - Inside Clanker Witch Switch A":  (0xAF06F0, 0x10610),
    "(0x88) CC  - Inside Clanker A":               (0xADE710, 0x10618),
    "(0x89) CC  - Inside Clanker B":               (0xAEFC90, 0x10620),
    "(0x8A) CC  - Inside Clanker Gold Feathers A": (0xAF06F0, 0x10628),
    "(0x8B) GL  - Floor 1 A":                      (0xAF79C8, 0x10630),
    "(0x8C) GL  - Floor 2 A":                      (0xB1CFF8, 0x10638),
    "(0x8D) GL  - Floor 3 A":                      (0xB43A00, 0x10640),
    "(0x8E) GL  - Floor 3 - Pipe Room A":          (0xB6B290, 0x10648),
    "(0x8F) GL  - Floor 3 - TTC Entrance A":       (0xB74FB8, 0x10650),
    "(0x90) GL  - Floor 5 A":                      (0xB870C0, 0x10658),
    "(0x91) GL  - Floor 6 A":                      (0xBA0D90, 0x10660),
    "(0x92) GL  - Floor 6 B":                      (0xBC8E88, 0x10668),
    "(0x93) GL  - Floor 3 - CC Entrance A":        (0xBC9C90, 0x10670),
    "(0x94) GL  - Boss A":                         (0xBEA360, 0x10678),
    "(0x95) GL  - Lava Room":                      (0xBF1FD0, 0x10680),
    "(0x96) GL  - Floor 6 - MMM Entrance A":       (0xC062C8, 0x10688),
    "(0x97) GL  - Floor 6 - Coffin Room A":        (0xC1DA88, 0x10690),
    "(0x98) GL  - Floor 4 A":                      (0xC29188, 0x10698),
    "(0x99) GL  - Floor 4 - BGS Entrance A":       (0xC422C0, 0x106A0),
    "(0x9A) GL  - Floor 7 A":                      (0xC66F78, 0x106A8),
    "(0x9B) GL  - Floor 7 - RBB Entrance A":       (0xC76D28, 0x106B0),
    "(0x9C) GL  - Floor 7 - MMM Puzzle A":         (0xC937A8, 0x106B8),
    "(0x9D) GL  - Floor 9 A":                      (0xCBEA38, 0x106C0),
    "(0x9E) GL  - Floor 8 - Path to Quiz A":       (0xCDE770, 0x106C8),
    "(0x9F) GL  - Floor 3 - CC Entrance B":        (0xCE9AE0, 0x106D0),
    "(0xA0) GL  - Floor 7 B":                      (0xCE7098, 0x106D8),
    "(0xA1) GL  - Floor 7 - RBB Entrance B":       (0xCEA600, 0x106E0),
    "(0xA2) GL  - Floor 7 - MMM Puzzle B":         (0xCEB3C0, 0x106E8),
    "(0xA3) GL  - Floor 1 B":                      (0xCEC260, 0x106F0),
    "(0xA4) GL  - Floor 2 B":                      (0xCEC988, 0x106F8),
    "(0xA5) GL  - Floor 3 - Pipe Room B":          (0xCED148, 0x10700),
    "(0xA6) GL  - Floor 4 B":                      (0xCEF058, 0x10708),
    "(0xA7) GL  - First Cutscene Inside":          (0xCF14B0, 0x10710),
    "(0xA8) GL  - Floor 4 - TTC Entrance B":       (0xD1ADF8, 0x10718),
    "(0xA9) GL  - Floor 3 - BGS Entrance B":       (0xD1DDE8, 0x10720),
    "(0xAA) GL  - Floor 3 B":                      (0xD18F30, 0x10728),
    "(0xAB) GL  - Floor 9 B":                      (0xD202A0, 0x10730),
    "(0xAC) GL  - Floor 8 - Path to Quiz B":       (0xD212E0, 0x10738),
    "(0xAD) GL  - Boss B":                         (0xD22888, 0x10740),
}


bk_MapModelNames = [
    "(0x00) ??? - Unknown 01",
    "(0x01) TTC - Treasure Trove Cove",
    "(0x02) TTC - Treasure Trove Cove B",
    "(0x03) TTC - Crab Shell A",
    "(0x04) TTC - Crab Shell B",
    "(0x05) TTC - Pirate Ship A",
    "(0x06) TTC - Pirate Ship B",
    "(0x07) TTC - Sand Castle A",
    "(0x08) TTC - Sand Castle B",
    "(0x09) TTC - Sharkfood Island A",
    "(0x0A) GV  - Gobi's Valley A",
    "(0x0B) GV  - Gobi's Valley B",
    "(0x0C) GV  - Match Game",
    "(0x0D) ??? - Unknown 02",
    "(0x0E) GV  - Maze A",
    "(0x0F) GV  - Maze B",
    "(0x10) GV  - Water Pyramid A",
    "(0x11) GV  - Water Pyramid B",
    "(0x12) GV  - Rupee's House",
    "(0x13) GV  - Inside the Sphinx",
    "(0x14) GV  - Blue Egg Chamber A",
    "(0x15) MMM - Mad Monster Mansion A",
    "(0x16) MMM - Mad Monster Mansion B",
    "(0x17) MMM - Drainpipe A",
    "(0x18) MMM - Cellar A",
    "(0x19) MMM - Secret Church Room A",
    "(0x1A) MMM - Secret Church Room B",
    "(0x1B) MMM - Dining Room A",
    "(0x1C) MMM - Church A",
    "(0x1D) MMM - Church B",
    "(0x1E) MMM - Tumbler's Shed",
    "(0x1F) MMM - Egg Room A",
    "(0x20) MMM - Egg Room B",
    "(0x21) MMM - Note Room A",
    "(0x22) MMM - Note Room B",
    "(0x23) MMM - Feather Room A",
    "(0x24) MMM - Feather Room B",
    "(0x25) MMM - Bathroom A",
    "(0x26) MMM - Bathroom B",
    "(0x27) MMM - Bedroom A",
    "(0x28) MMM - Bedroom B",
    "(0x29) MMM - Gold Feather Room A",
    "(0x2A) MMM - Gold Feather Room B",
    "(0x2B) MMM - Well A",
    "(0x2C) MMM - Well B",
    "(0x2D) MMM - Drainpipe B",
    "(0x2E) MMM - Septic Tank A",
    "(0x2F) MMM - Septic Tank B",
    "(0x30) MMM - Dining Room B",
    "(0x31) MMM - Cellar B",
    "(0x32) ??? - Dark Room",
    "(0x33) CS  - Intro A",
    "(0x34) CS  - Ncube A",
    "(0x35) CS  - Grunty's Final Words A",
    "(0x36) CS  - Ncube B",
    "(0x37) CS  - Intro B",
    "(0x38) CS  - Banjo's House A",
    "(0x39) CS  - Grunty's Final Words B",
    "(0x3A) CS  - Banjo's House B",
    "(0x3B) CS  - Beach Ending B",
    "(0x3C) CS  - With Falling twords Ground A",
    "(0x3D) ??? - Unknown 03",
    "(0x3E) CS  - Floor 5 B",
    "(0x3F) CS  - Beach Ending A",
    "(0x40) MM  - Mumbo's Mountain A",
    "(0x41) MM  - Mumbo's Mountain B",
    "(0x42) MM  - Termite Hill A",
    "(0x43) MM  - Termite Hill B",
    "(0x44) G   - Mumbo's Skull",
    "(0x45) ??? - Unknown 04",
    "(0x46) RBB - Rusty Bucket Bay A",
    "(0x47) RBB - Rusty Bucket Bay B",
    "(0x48) RBB - Machine Room A",
    "(0x49) RBB - Machine Room B",
    "(0x4A) RBB - Big Fish Warehouse A",
    "(0x4B) RBB - Big Fish Warehouse B",
    "(0x4C) RBB - Boat Room A",
    "(0x4D) RBB - Boat Room B",
    "(0x4E) RBB - Container 1 A",
    "(0x4F) RBB - Container 2 A",
    "(0x50) RBB - Container 3 A",
    "(0x51) RBB - Captain's Cabin A",
    "(0x52) RBB - Captain's Cabin B",
    "(0x53) RBB - Sea Grublin's Cabin A",
    "(0x54) RBB - Boss Boom Box Room A",
    "(0x55) RBB - Boss Boom Box Room B",
    "(0x56) RBB - Boss Boom Box Room (2) A",
    "(0x57) RBB - Boss Boom Box Room (2) B",
    "(0x58) RBB - Navigation Room A",
    "(0x59) RBB - Boom Box Room (Pipe) A",
    "(0x5A) RBB - Boom Box Room (Pipe) B",
    "(0x5B) RBB - Kitchen A",
    "(0x5C) RBB - Kitchen B",
    "(0x5D) RBB - Anchor Room A",
    "(0x5E) RBB - Anchor Room B",
    "(0x5F) RBB - Navigation Room B",
    "(0x60) FP  - Freezeezy Peak A",
    "(0x61) FP  - Freezeezy Peak B",
    "(0x62) FP  - Igloo A",
    "(0x63) FP  - Christmas Tree A",
    "(0x64) FP  - Wozza's Cave A",
    "(0x65) FP  - Wozza's Cave B",
    "(0x66) FP  - Igloo B",
    "(0x67) SM  - Spiral Mountain A",
    "(0x68) SM  - Spiral Mountain B",
    "(0x69) BGS - Bubblegloop Swamp A",
    "(0x6A) BGS - Bubblegloop Swamp B",
    "(0x6B) BGS - Mr. Vile A",
    "(0x6C) BGS - Tiptup Quior A",
    "(0x6D) BGS - Tiptup Quior B",
    "(0x6E) ??? - Test Map A",
    "(0x6F) ??? - Test Map B",
    "(0x70) CCW - Click Clock Woods A",
    "(0x71) CCW - Spring A",
    "(0x72) CCW - Summer A",
    "(0x73) CCW - Autumn A",
    "(0x74) CCW - Winter A",
    "(0x75) CCW - Wasp Hive A",
    "(0x76) CCW - Nabnut's House A",
    "(0x77) CCW - Whiplash Room A",
    "(0x78) CCW - Nabnut's Attic 1",
    "(0x79) CCW - Nabnut's Attic 2 A",
    "(0x7A) CCW - Nabnut's Attic 2 B",
    "(0x7B) CCW - Click Clock Woods B",
    "(0x7C) CCW - Spring B",
    "(0x7D) CCW - Summer B",
    "(0x7E) CCW - Autumn B",
    "(0x7F) CCW - Winter B",
    "(0x80) GL  - Quiz Room",
    "(0x81) ??? - Unknown 05",
    "(0x82) ??? - Unknown 06",
    "(0x83) ??? - Unknown 07",
    "(0x84) ??? - Unknown 08",
    "(0x85) CC  - Clanker's Cavern A",
    "(0x86) CC  - Clanker's Cavern B",
    "(0x87) CC  - Inside Clanker Witch Switch A",
    "(0x88) CC  - Inside Clanker A",
    "(0x89) CC  - Inside Clanker B",
    "(0x8A) CC  - Inside Clanker Gold Feathers A",
    "(0x8B) GL  - Floor 1 A",
    "(0x8C) GL  - Floor 2 A",
    "(0x8D) GL  - Floor 3 A",
    "(0x8E) GL  - Floor 3 - Pipe Room A",
    "(0x8F) GL  - Floor 3 - TTC Entrance A",
    "(0x90) GL  - Floor 5 A",
    "(0x91) GL  - Floor 6 A",
    "(0x92) GL  - Floor 6 B",
    "(0x93) GL  - Floor 3 - CC Entrance A",
    "(0x94) GL  - Boss A",
    "(0x95) GL  - Lava Room",
    "(0x96) GL  - Floor 6 - MMM Entrance A",
    "(0x97) GL  - Floor 6 - Coffin Room A",
    "(0x98) GL  - Floor 4 A",
    "(0x99) GL  - Floor 4 - BGS Entrance A",
    "(0x9A) GL  - Floor 7 A",
    "(0x9B) GL  - Floor 7 - RBB Entrance A",
    "(0x9C) GL  - Floor 7 - MMM Puzzle A",
    "(0x9D) GL  - Floor 9 A",
    "(0x9E) GL  - Floor 8 - Path to Quiz A",
    "(0x9F) GL  - Floor 3 - CC Entrance B",
    "(0xA0) GL  - Floor 7 B",
    "(0xA1) GL  - Floor 7 - RBB Entrance B",
    "(0xA2) GL  - Floor 7 - MMM Puzzle B",
    "(0xA3) GL  - Floor 1 B",
    "(0xA4) GL  - Floor 2 B",
    "(0xA5) GL  - Floor 3 - Pipe Room B",
    "(0xA6) GL  - Floor 4 B",
    "(0xA7) GL  - First Cutscene Inside",
    "(0xA8) GL  - Floor 4 - TTC Entrance B",
    "(0xA9) GL  - Floor 3 - BGS Entrance B",
    "(0xAA) GL  - Floor 3 B",
    "(0xAB) GL  - Floor 9 B",
    "(0xAC) GL  - Floor 8 - Path to Quiz B",
    "(0xAD) GL  - Boss B"
]

# this will create a blender-conforming Enum List for displaying the map-model names
# WITHOUT writing out a duplicate-heavy tuple list like usual
bk_EnumMapModelNames = []

def get_bk_EnumMapModelNames():
    global bk_EnumMapModelNames

    # if the Enum was already created, just return that
    if (len(bk_EnumMapModelNames) > 0):
        return bk_EnumMapModelNames
    # otherwise, build it first:
    # (eventually, the map-model list should use the enum-names from decomp directly)
    for idx, model_name in enumerate(bk_MapModelNames):
        bk_EnumMapModelNames.append((
            model_name,
            model_name,
            ""
        ))
    return bk_EnumMapModelNames