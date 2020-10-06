





label imachine:
    jump_out NOP1









label NOP1:
    call iscene ("NOP1")
    jump_out op_video

label op_video:
    call iscene ("op_vid1")
    jump_out NOP2

label NOP2:
    call iscene ("NOP2")
    jump_out tc_act1

label tc_act1:
    call act_op ("tc_act1.mkv")
    jump_out A1

label A1:
    call iscene ("A1")
    call imenu ("choiceA1")

    if _return == m1:

        call iscene ("A1a")
    else:

        $ attraction_sc += 1
        call iscene ("A1b")
    call iscene ("A1c")
    jump_out A2

label A2:
    call iscene ("A2")
    if seen_scene ("A1a"):
        call iscene ("A2a")
    else:
        call iscene ("A2b")
    call iscene ("A2c")
    if seen_scene ("A1b"):
        call iscene ("A2d")
    else:
        call iscene ("A2e")
    call iscene ("A2f")
    jump_out A3

label A3:
    call iscene ("A3")
    call imenu ("choiceA3")
    if _return == m1:

        $ attraction_hanako += 1
        call iscene ("A3a")
    elif _return == m2:

        call iscene ("A3b")
    else:

        $ attraction_sc += 1
        call iscene ("A3c")
    call iscene ("A3d")
    jump_out A4

label A4:
    call iscene ("A4")











    jump_out A5



label A5:
    call iscene ("timeskip")
    call iscene ("A5")
    jump_out A6

label A6:
    call iscene ("A6")
    call imenu ("choiceA6")

    if _return == m1:

        $ attraction_sc += 1
        call iscene ("A6a")
    else:
        call iscene ("A6b")
    call iscene ("A6c")
    jump_out A7

label A7:
    call iscene ("A7")
    jump_out A8

label A8:
    call iscene ("A8")
    call imenu ("choiceA8")

    if _return == m1:
        call iscene ("A8a")

        if seen_scene("A1b"):
            call iscene ("A8aa")
        call iscene ("A8ab")
    else:

        $ attraction_hanako +=1
        call iscene ("A8b")
    call iscene ("A8c")
    if seen_scene ("A8a"):
        call iscene ("A8d")
    else:
        call iscene ("A8e")
    call iscene ("A8f")
    jump_out A9

label A9:
    call iscene ("A9")
    call imenu ("choiceA9")
    if _return == m1:

        $ attraction_hanako += 1
        call iscene ("A9a")
    else:

        call iscene ("A9b")
    call iscene ("A9c")
    jump_out A10



label A10:
    call iscene ("timeskip")
    call iscene ("A10")
    if attraction_sc > 1 and attraction_hanako > 1:
        call imenu ("choiceA10a")
        if _return == m1:
            call iscene ("A10a")
        elif _return == m2:
            call iscene ("A10b")
            jump_out A11_2
        else:
            call iscene ("A10c")
    elif attraction_sc > 1:
        call imenu ("choiceA10b")
        if _return == m1:
            call iscene ("A10c")
        else:
            call iscene ("A10a")
    elif attraction_hanako > 1:
        call imenu ("choiceA10c")
        if _return == m1:
            call iscene ("A10a")
        else:
            call iscene ("A10b")
            jump_out A11_2
    else:
        call iscene ("A10a")
    jump_out A11_1

label A11_1:
    call iscene ("A11")
    call iscene ("A11a")
    call iscene ("A11b")
    if seen_scene ("A10c"):
        call iscene ("A11x")
        jump_out A12
    call iscene ("A11y")
    jump_out A15


label A11_2:
    call iscene ("A11c")
    call iscene ("A11a")
    call iscene ("A11d")
    jump_out A13

label A12:
    call iscene ("A12")
    jump_out A16 

label A13:
    call iscene ("A13")
    jump_out A15



label A15:
    call iscene ("A15")
    jump_out A16

label A16:
    call iscene ("A16")
    jump_out A17

label A17:
    call iscene ("A17")
    call imenu ("choiceA17")

    if _return == m1:

        call iscene ("A17a")
    else:

        call iscene ("A17b")
    call iscene ("A17c")
    jump_out A18

label A18:
    call iscene ("A18")
    jump_out A19


label A19:
    call iscene ("timeskip")
    call iscene ("A19")
    if seen_scene ("A17a"):
        call iscene ("A19a")
    else:
        call iscene ("A19b")
    call iscene ("A19c")
    if seen_scene ("A11b"):
        call iscene ("A19i")
    call iscene ("A19j")
    if seen_scene ("A17a"):
        call iscene ("A19d")
    else:
        call iscene ("A19e")
    call iscene ("A19f")
    if seen_scene ("A17a"):
        call iscene ("A19g")
    else:
        call iscene ("A19h")
    jump_out A20

label A20:
    call iscene ("A20")
    jump_out A21

label A21:
    call iscene ("A21")
    call imenu ("choiceA21")

    if _return == m1:

        call iscene ("A21a")
        jump_out A22
    call iscene ("A21b")
    if seen_scene ("A13"):
        call iscene ("A21c")
    else:
        call iscene ("A21d")
    jump_out A23

label A22:
    call iscene ("A22")
    if not seen_scene ("A12"):
        call iscene ("A22a")
        jump_out A23
    jump_out A22_2

label A22_2:
    call iscene ("A22b")
    if seen_scene ("A21c"):

        jump_out A24
    jump_out A24_1

label A23:
    if not seen_scene ("A22a"):
        jump_out A23_1
    if not seen_scene ("A21c"):
        jump_out A23_2
    jump_out A24 

label A23_1:
    call iscene ("A23")
    if seen_scene ("A21c"):
        jump_out A24
    jump_out A23_2

label A23_2:
    call iscene ("A23a")
    if seen_scene ("A21c"):
        jump_out A24
    jump_out A24_1

label A24:
    call iscene ("A24")
    if seen_scene ("A21a"):

        call iscene ("A24c")
    else:
        call iscene ("A24d")
    call iscene ("A24e")
    jump_out A24_1

label A24_1:
    if seen_scene("A17a"):
        call iscene ("A24a")
        jump_out A25
    call iscene ("A24b")
    jump_out A26


label A25:
    call iscene ("timeskip")
    call iscene ("A25")
    call imenu ("choiceA25")
    if _return == m1:
        call iscene ("A25b")
        jump_out A27
    call iscene ("A25a")
    jump_out A26

label A26:
    if not seen_scene ("A25"):
        call iscene ("timeskip")
        call iscene ("A26")
    call iscene ("A26a")
    if not seen_scene ("A22b"):
        call iscene ("A26e")
        jump_out A27_2
    jump_out A26_1

label A26_1:
    call iscene ("A26b")
    call imenu ("choiceA26")

    if _return == m1:

        call iscene ("A26c")
        jump_out A28

    $ attraction_kenji += 1
    call iscene ("A26d")
    jump_out A27_2


label A27:
    call iscene ("A27")
    if seen_scene ("A22b"):
        jump_out A27_1
    call iscene ("A27e")
    jump_out A29

label A27_1:
    call iscene ("A27a")
    call imenu ("choiceA27")
    if _return == m1:
        call iscene ("A27b")
        $ attraction_kenji += 1
        call iscene ("A27f")
        jump_out A29 
    call iscene ("A27c")
    if seen_scene ("A25b"):
        call imenu ("choice2A27")
        if _return == m1:
            call iscene ("A27h")
            call iscene ("A27e")
            jump_out A29                                     
    call iscene ("A27i")
    jump_out A28

label A27_2:
    call iscene ("A27d")
    if seen_scene ("A26d"):
        call iscene ("A27f")
    else:
        call iscene ("A27e")
    jump_out A29


label A28:
    call iscene ("A28")
    if seen_scene ("A26c"):
        call iscene ("A28a")
    call iscene ("A28b")
    jump_out A36

label A29:
    if not seen_scene ("A25b"):
        call iscene ("A29")
        if seen_scene ("A27f"):
            call iscene ("A29x")
    else:
        call iscene ("A29a")
    call iscene ("A29b")
    if seen_scene ("A25b"):
        call iscene ("A29c")
        jump_out A31
    jump_out A30

label A30:
    call iscene ("A30")
    if seen_scene ("A26d") or seen_scene ("A27b"):

        call iscene ("A30a")
        jump_out A31
    call imenu ("choiceA30")
    if _return == m2:
        $ attraction_kenji += 1
        call iscene ("A30a")
        jump_out A31
    call iscene ("A30b")
    if seen_scene ("A11c"):
        call iscene ("A30c")
    call iscene ("A30d")
    jump_out A31


label A31:
    call iscene ("timeskip")
    call iscene ("A31")
    if seen_scene ("A25b"):
        call iscene ("A31b")
    else:
        call iscene ("A31c")
    call iscene ("A31d")
    if attraction_kenji > 0:
        call iscene ("A31e")
        jump_out A38
    elif seen_scene ("A29c"):
        jump_out A32
    elif seen_scene ("A24d"):
        jump_out A35
    jump_out A32

label A32:
    call iscene ("A32")
    if seen_scene ("A23a"):
        call iscene ("A32a")
    call iscene ("A32b")
    if seen_scene ("A25b"):
        jump_out A34
    jump_out A33

label A33:
    call iscene ("A33")
    call imenu ("choiceA33")
    if _return == m2:
        call iscene ("A33a")
    else:
        call iscene ("A33b")
    jump_out A38

label A34:
    call iscene ("A34")
    call iscene ("A34a")
    jump_out A38

label A35:
    call iscene ("A35")
    call imenu ("choiceA35")
    if _return == m1:
        call iscene ("A35a")
        jump_out A38
    jump_out A37

label A36:
    call iscene ("timeskip")
    call iscene ("A36")
    jump_out A38

label A37:
    call iscene ("A37")
    jump_out A38


label A38:
    call iscene ("timeskip")
    call iscene ("A38")
    if seen_scene ("A31e"):
        jump_out A43
    elif seen_scene ("A36"):
        call iscene ("A38a")
        call iscene ("A38e")
        jump_out A44
    elif seen_scene ("A35") or seen_scene ("A37"):
        call iscene ("A38b")
        call iscene ("A38e")
        if seen_scene ("A37"):
            jump_out A42
        jump_out A41
    elif seen_scene ("A33a"):
        call iscene ("A38c")
        call iscene ("A38e")
        jump_out A40
    elif seen_scene ("A34"):
        call iscene ("A38d")
        call iscene ("A38e")
        jump_out A39
    jump_out A43

label A39:
    call iscene ("A39")
    jump_out tc_act2_emi

label A40:
    call iscene ("A40")
    jump_out tc_act2_rin

label A41:

    call iscene ("A41b")
    call iscene ("A41a")
    jump_out tc_act2_lilly

label A42:
    call iscene ("A41b")
    call iscene ("A42")
    jump_out H2

label A43:
    call iscene ("A43")
    call path_end
    jump_out restart

label A44:
    call iscene ("A44")
    jump_out tc_act2_shizune





label H2:

    call iscene ("H2")
    jump_out tc_act2_hanako

label tc_act2_hanako:
    call act_op ("tc_act2_hanako.mkv")
    jump_out H3

label H3:
    call iscene ("H3")
    jump_out H4

label H4:
    call iscene ("timeskip")
    call iscene ("H4")
    call imenu ("choiceH4")

    if _return == m1:

        jump_out H5_1
    else:

        jump_out H5_2

label H5_1:
    call iscene ("H5_1")
    jump_out H6

label H5_2:
    call iscene ("H5_2")
    jump_out H6

label H6:
    call iscene ("timeskip")
    call iscene ("H6")
    jump_out H7

label H7:
    call iscene ("H7")
    if seen_scene("H5_1"):
        call iscene ("H7a")
    elif seen_scene("H5_2"):
        call iscene ("H7b")
    call iscene ("H7c")
    jump_out H8

label H8:
    call iscene ("timeskip")
    call iscene ("H8")
    jump_out H9

label H9:
    call iscene ("H9")
    jump_out H10

label H10:
    call iscene ("H10")
    jump_out tc_act3_hanako

label tc_act3_hanako:
    call act_op ("tc_act3_hanako.mkv")
    jump_out H11

label H11:
    call iscene ("H11")
    jump_out H12

label H12:
    call iscene ("timeskip")
    call iscene ("H12")
    call imenu ("choiceH12")

    if _return == m1:

        call iscene ("H12a")
    else:

        call iscene ("H12b")
    call iscene ("H12c")
    jump_out H13

label H13:
    call iscene ("timeskip")
    call iscene ("H13")
    jump_out H14

label H14:
    call iscene ("timeskip")
    call iscene ("H14")
    jump_out H15

label H15:
    call iscene ("H15")
    jump_out H16

label H16:
    call iscene ("timeskip")
    call iscene ("H16")
    jump_out H17

label H17:
    call iscene ("timeskip")
    call iscene ("H17")
    jump_out H18

label H18:
    call iscene ("timeskip")
    call iscene ("H18")
    jump_out H19

label H19:
    call iscene ("timeskip")
    call iscene ("H19")
    jump_out H20

label H20:
    call iscene ("timeskip")
    call iscene ("H20")
    call imenu ("choiceH20")

    if _return == m1:

        call iscene ("H20_1")
    else:

        call iscene ("H20_2")
    jump_out tc_act4_hanako

label tc_act4_hanako:
    call act_op ("tc_act4_hanako.mkv")
    jump_out H21

label H21:
    call iscene ("H21")
    jump_out H22

label H22:
    call iscene ("timeskip")
    call iscene ("H22")
    call imenu ("choiceH22")
    if _return == m1 and seen_scene ("H20_1"):
        call iscene ("H22a")
        jump_out H25
    else:
        if seen_scene ("H20_1"):
            call iscene ("H22c")
            jump_out H24
        else:
            call iscene ("H22b")
    jump_out H23

label H23:

    call iscene ("H23")
    call path_end ("hanakorage", True)
    jump_out restart

label H24:

    call iscene ("H24")
    call path_end ("hanakosad", True)
    jump_out restart

label H25:
    call iscene ("timeskip")
    call iscene ("H25")
    if seen_scene ("H12a"):
        call iscene ("H25a")
    call iscene ("H25c")
    jump_out H26

label H26:
    call iscene ("timeskip")
    call iscene ("H26")
    jump_out H27

label H27:
    call iscene ("timeskip")
    call iscene ("H27")
    jump_out H28

label H28:
    call iscene ("timeskip")
    call iscene ("H28")
    jump_out H29

label H29:
    call iscene ("timeskip")
    call iscene ("H29")
    call iscene ("H29h", is_h=True)
    call iscene ("H29x")
    jump_out H30

label H30:
    call iscene ("timeskip")
    call iscene ("H30")
    jump_out H31

label H31:
    call iscene ("H31")
    call path_end ("hanako", True)
    jump_out restart






label tc_act2_lilly:
    call act_op ("tc_act2_lilly.mkv")
    jump_out L1

label L1:
    call iscene ("L1")
    jump_out L2

label L2:
    call iscene ("timeskip")
    call iscene ("L2")
    jump_out L3

label L3:
    call iscene ("timeskip")
    call iscene ("L3")
    jump_out L4

label L4:
    call iscene ("timeskip")
    call iscene ("L4")
    jump_out L5

label L5:
    call iscene ("L5")
    jump_out L6

label L6:
    call iscene ("timeskip")
    call iscene ("L6i")
    call imenu ("choiceL6_1")
    if _return == m1:
        call iscene ("L6a")
    else:
        call iscene ("L6b")
    call iscene ("L6c")
    jump_out L7

label L7:
    call iscene ("timeskip")
    call iscene ("L7")
    jump_out L8

label L8:
    call iscene ("timeskip")
    call iscene ("L8")
    jump_out tc_act3_lilly

label tc_act3_lilly:
    call act_op ("tc_act3_lilly.mkv")
    jump_out L9

label L9:
    call iscene ("L9")
    jump_out L10

label L10:
    call iscene ("timeskip")
    call iscene ("L10")

    call imenu ("choiceL10_1")
    if _return == m1:
        call iscene ("L10a")
    else:
        call iscene ("L10b")
    call iscene ("L10c")
    call imenu ("choiceL10_2")
    if _return == m1:
        call iscene ("L10d")
    else:
        call iscene ("L10e")
    call iscene ("L10f")
    jump_out L11

label L11:
    call iscene ("timeskip")
    call iscene ("L11")
    jump_out L12

label L12:
    call iscene ("timeskip")
    call iscene ("L12")
    jump_out L13

label L13:
    call iscene ("timeskip")
    call iscene ("L13")
    jump_out L14

label L14:
    call iscene ("timeskip")
    call iscene ("L14")
    jump_out L15

label L15:
    call iscene ("timeskip")
    call iscene ("L15")
    call imenu ("choiceL15")
    if _return == m1:

        call iscene ("L15a")
    else:
        call iscene ("L15b")
    call iscene ("L15c")
    jump_out L16

label L16:
    call iscene ("timeskip")
    call iscene ("L16")
    jump_out L17

label L17:
    call iscene ("L17")
    call iscene ("L17h", is_h=True, is_end=True)
    jump_out L18

label L18:
    call iscene ("timeskip")
    call iscene ("L18")
    jump_out L19

label L19:
    call iscene ("L19")
    call iscene ("L19h", is_h=True)
    jump_out L20

label L20:
    call iscene ("timeskip")
    call iscene ("L20")
    call imenu ("choiceL20")
    if _return == m1:
        call iscene ("L20a")
    else:
        call iscene ("L20b")
    call iscene ("L20c")
    jump_out tc_act4_lilly

label tc_act4_lilly:
    call act_op ("tc_act4_lilly.mkv")
    jump_out L21

label L21:
    call iscene ("L21")
    jump_out L22

label L22:
    call iscene ("timeskip")
    call iscene ("L22")
    jump_out L23

label L23:
    call iscene ("timeskip")
    call iscene ("L23")
    jump_out L24

label L24:
    call iscene ("timeskip")
    call iscene ("L24")
    call imenu ("choiceL24")
    if _return == m1:
        call iscene ("L24a")
    else:

        call iscene ("L24b")
    call iscene ("L24c")
    jump_out L25

label L25:
    call iscene ("timeskip")
    call iscene ("L25")
    jump_out L26

label L26:
    call iscene ("timeskip")
    call iscene ("L26")
    call iscene ("L26h", is_h=True)
    call iscene ("L26x")
    jump_out L27

label L27:
    call iscene ("timeskip")
    call iscene ("L27")
    jump_out L28

label L28:
    call iscene ("timeskip")
    call iscene ("L28")
    jump_out L29

label L29:
    call iscene ("timeskip")
    call iscene ("L29")
    if seen_scene("L6b") and seen_scene("L15a") and seen_scene("L24a"):
        jump_out L30
    else:
        call path_end ("lilly")
        jump_out restart

label L30:
    call iscene ("timeskip")
    call iscene ("L30")
    jump_out L31

label L31:
    call iscene ("timeskip")
    call iscene ("L31")
    jump_out L32

label L32:
    call iscene ("L32")
    call path_end ("lilly", True)
    jump_out L33

label L33:
    call iscene ("L33")
    jump_out restart





label tc_act2_emi:
    call act_op ("tc_act2_emi.mkv")
    jump_out E3

label E3:
    call iscene ("E3")
    jump_out E4

label E4:
    call iscene ("E4")

    jump_out E5

label E5:
    call iscene ("E5")
    jump_out E6

label E6:
    call iscene ("E6")
    jump_out E7

label E7:
    call iscene ("E7")
    jump_out E8

label E8:
    call iscene ("timeskip")
    call iscene ("E8")
    jump_out E9

label E9:
    call iscene ("timeskip")
    call iscene ("E9")
    jump_out E10

label E10:
    call iscene ("timeskip")
    call iscene ("E10")
    jump_out E11

label E11:
    call iscene ("timeskip")
    call iscene ("E11a")
    if seen_scene("A12") or seen_scene ("A35a"):
        call iscene ("E11x")
    else:
        call iscene ("E11y")
    call iscene ("E11z")
    call imenu ("choiceE11")
    if _return == m1:
        call iscene ("E11b")
    else:
        call iscene ("E11c")
    call iscene ("E11d")
    jump_out E12

label E12:
    call iscene ("timeskip")
    call iscene ("E12a")
    if seen_scene("E11b"):
        call iscene ("E12b")
    else:
        call iscene ("E12c")
    call iscene ("E12d")
    jump_out E13

label E13:
    call iscene ("E13")
    jump_out E14

label E14:
    call iscene ("timeskip")
    call iscene ("E14")
    jump_out E15

label E15:
    call iscene ("E15")
    jump_out tc_act3_emi


label tc_act3_emi:
    call act_op ("tc_act3_emi.mkv")
    jump_out E16

label E16:
    call iscene ("E16")
    jump_out E17

label E17:
    call iscene ("timeskip")
    call iscene ("E17")
    call imenu ("choiceE17")
    if _return == m1:
        call iscene ("E17a")
    else:
        call iscene ("E17b")
    call iscene ("E17x")
    jump_out E18

label E18:
    call iscene ("timeskip")
    call iscene ("E18")
    if seen_scene("E17a"):
        call iscene ("E18a")
    else:
        call iscene ("E18b")
    call iscene ("E18x")
    jump_out E19

label E19:
    call iscene ("E19")
    jump_out E20

label E20:
    call iscene ("E20")
    call iscene ("E20h", is_h=True)
    call iscene ("E20x")
    jump_out E21

label E21:
    call iscene ("timeskip")
    call iscene ("E21")
    call iscene ("E21h", is_h=True)
    call iscene ("E21x")
    jump_out E22

label E22:
    call iscene ("E22")
    jump_out E23

label E23:
    call iscene ("timeskip")
    call iscene ("E23")
    jump_out E24

label E24:
    call iscene ("timeskip")
    call iscene ("E24")
    call imenu ("choiceE24")
    if _return == m1:
        call iscene ("E24a")
    else:
        call iscene ("E24b")
    call iscene ("E24c")
    jump_out E25

label E25:

    call iscene ("E25")
    if seen_scene ("E24a"):
        call imenu ("choiceE25")
        if _return == m1:
            call iscene ("E25a")
        else:
            call iscene ("E25b")
    call iscene ("E25c")
    jump_out E26

label E26:
    call iscene ("timeskip")
    call iscene ("E26")
    if seen_scene ("E25a"):
        call iscene ("E26a")
    call iscene ("E26b")
    if seen_scene ("E25a"):
        call iscene ("E26e")
    call iscene ("E26f")
    if seen_scene ("E24a"):
        call imenu ("choiceE26")
        if _return == m2:
            call iscene ("E26d")
            jump_out tc_act4_emi
    call iscene ("E26c")
    jump_out E27

label E27:
    call iscene ("timeskip")
    call iscene ("E27")
    call imenu ("choiceE27")
    if _return == m1:
        call iscene ("E27a")
        call path_end ("emi")
        jump_out restart
    call iscene ("E27b")
    jump_out tc_act4_emi

label tc_act4_emi:
    call act_op ("tc_act4_emi.mkv")
    if seen_scene ("E27b"):
        jump_out E30
    jump_out E28

label E28:
    call iscene ("E28")
    jump_out E29

label E29:
    call iscene ("timeskip")
    call iscene ("E29")
    jump_out E30

label E30:
    if seen_scene ("E29"):
        call iscene ("timeskip")
    call iscene ("E30")
    if seen_scene ("E29"):
        call iscene ("E30a")
    call iscene ("E30b")
    if seen_scene ("E27"):
        call iscene ("E30c")
    else:
        call iscene ("E30d")
    call iscene ("E30e")
    jump_out E31

label E31:
    call iscene ("E31")
    call iscene ("E31h", is_h=True)
    call iscene ("E31x")
    jump_out E32

label E32:
    call iscene ("timeskip")
    call iscene ("E32")
    call path_end ("emi", True)
    jump_out restart





label tc_act2_rin:
    call act_op ("tc_act2_rin.mkv")
    jump_out R1

label R1:
    call iscene ("R1")
    jump_out R2

label R2:
    call iscene ("R2")
    call imenu ("choiceR2")
    if _return == m1:
        call iscene ("R2a")
    else:
        call iscene ("R2b")
    call iscene ("R2c")
    jump_out R3

label R3:
    call iscene ("R3")
    jump_out R4

label R4:
    call iscene ("timeskip")
    call iscene ("R4")
    jump_out R5

label R5:
    call iscene ("timeskip")
    call iscene ("R5")
    jump_out R6

label R6:
    call iscene ("timeskip")
    call iscene ("R6")
    call imenu ("choiceR6")
    if _return == m1:
        call iscene ("R6a")
    else:
        call iscene ("R6b")
    call iscene ("R6c")
    jump_out R7

label R7:
    call iscene ("timeskip")
    call iscene ("R7")
    jump_out R8

label R8:
    call iscene ("timeskip")
    call iscene ("R8")
    jump_out R9

label R9:
    call iscene ("R9")
    call imenu ("choiceR9")
    if _return == m1:
        call iscene ("R9a")
    else:
        call iscene ("R9b")
    call iscene ("R9c")
    jump_out R10

label R10:
    call iscene ("timeskip")
    call iscene ("R10")
    jump_out R11

label R11:
    call iscene ("timeskip")
    call iscene ("R11")



    if seen_scene("R2a"):
        if seen_scene("R6a"):
            if seen_scene("R9a"):
                call imenu ("choiceR11aaa")
            else:
                call imenu ("choiceR11aab")
        else:
            if seen_scene("R9a"):
                call imenu ("choiceR11aba")
            else:
                call imenu ("choiceR11abb")
    else:
        if seen_scene("R6a"):
            if seen_scene("R9a"):
                call imenu ("choiceR11baa")
            else:
                call imenu ("choiceR11bab")
        else:
            if seen_scene("R9a"):
                call imenu ("choiceR11bba")
            else:
                call imenu ("choiceR11bbb")

    if _return == m1:
        call iscene ("R11a")
        call iscene ("R11g")
    elif _return == m2:
        call iscene ("R11b")
        call iscene ("R11i")
    elif _return == m3:
        call iscene ("R11c")
        call iscene ("R11h")
    elif _return == m4:
        call iscene ("R11d")
        call iscene ("R11i")
    elif _return == m5:
        call iscene ("R11e")
        call iscene ("R11h")
    else:
        call iscene ("R11f")
        call iscene ("R11g")
    call iscene ("R11j")
    jump_out R12

label R12:
    call iscene ("timeskip")
    call iscene ("R12")
    if seen_scene("A12") or seen_scene ("A35a"):
        call iscene ("R12b")
    else:
        call iscene ("R12a")
    call iscene ("R12c")
    if seen_scene("A12") or seen_scene ("A35a"):
        call iscene ("R12e")
    else:
        call iscene ("R12d")
    call iscene ("R12f")
    jump_out R13

label R13:
    call iscene ("timeskip")
    call iscene ("R13")
    jump_out R14

label R14:
    call iscene ("timeskip")
    call iscene ("R14")
    jump_out R15

label R15:
    call iscene ("timeskip")
    call iscene ("R15")
    jump_out R16

label R16:
    call iscene ("timeskip")
    call iscene ("R16")
    call imenu ("choiceR16")
    if _return == m1:
        call iscene ("R16a")
    else:
        call iscene ("R16b")
    call iscene ("R16c")
    if seen_scene ("R11g"):
        call iscene ("R16d")
    call iscene ("R16e")
    jump_out tc_act3_rin

label tc_act3_rin:
    call act_op ("tc_act3_rin.mkv")
    jump_out R17

label R17:
    call iscene ("R17")
    jump_out R18

label R18:
    call iscene ("timeskip")
    call iscene ("R18")
    jump_out R19

label R19:
    call iscene ("timeskip")
    call iscene ("R19")
    if seen_scene ("R16b"):
        call iscene ("R19a")
    call iscene ("R19b")
    if seen_scene ("R16d"):
        jump_out R20
    else:
        jump_out R21

label R20:
    call iscene ("R20")
    call imenu ("choiceR20")
    if _return == m1:
        call iscene ("R20a")
    else:
        call iscene ("R20b")
    call iscene ("R20c")
    jump_out R22

label R21:
    call iscene ("R21")
    call imenu ("choiceR21")
    if _return == m1:
        call iscene ("R21a")
    else:
        call iscene ("R21b")
    call iscene ("R21c")
    jump_out R22

label R22:
    call iscene ("timeskip")
    call iscene ("R22")
    jump_out R23

label R23:
    call iscene ("timeskip")
    call iscene ("R23")
    jump_out R23_2

label R23_2:
    call iscene ("timeskip")
    call iscene ("R23_2")
    jump_out R24

label R24:
    call iscene ("timeskip")
    call iscene ("R24")
    jump_out R25

label R25:
    call iscene ("R25")
    jump_out R26

label R26:
    call iscene ("timeskip")
    call iscene ("R26")
    call imenu ("choiceR26")
    if _return == m1:
        call iscene ("R26a")
    else:
        call iscene ("R26b")
    call iscene ("R26c")
    jump_out R27

label R27:
    call iscene ("R27")
    call iscene ("R27h", is_h=True)
    call iscene ("R27x")
    jump_out R28

label R28:
    call iscene ("timeskip")


    call iscene ("R28")
    if (seen_scene("R20a") or seen_scene("R21a")):
        call imenu ("choiceR28_1")
    else:
        call imenu ("choiceR28_2")

    if _return == m1:
        call iscene ("R28a")
    elif _return == m2:
        call iscene ("R28b")
    else:
        jump_out R29
    call iscene ("R28c")
    jump_out tc_act4_rin

label R29:
    call iscene ("R29")
    call path_end ("rin", False)
    jump_out restart



label tc_act4_rin:
    call act_op ("tc_act4_rin.mkv")
    jump_out R30

label R30:
    call iscene ("R30")
    if (seen_scene("R16d")):
        call iscene ("R30x")
    else:
        call iscene ("R30y")
    call iscene ("R30z")
    jump_out R31

label R31:
    call iscene ("timeskip")
    call iscene ("R31")
    jump_out R32

label R32:
    call iscene ("timeskip")
    call iscene ("R32")
    call imenu ("choiceR32")
    if _return == m1:
        call iscene ("R32a")
        jump_out R35
    call iscene ("R32b")
    jump_out R34



label R34:

    call iscene ("timeskip")
    call iscene ("R33")
    call iscene ("R34")
    jump_out R38



label R35:
    call iscene ("timeskip")
    call iscene ("R33")
    call iscene ("R35")
    jump_out R36

label R36:
    call iscene ("timeskip")
    call iscene ("R36")
    if not seen_scene("R19a"):
        call iscene ("R36a")
    call iscene ("R36x")
    jump_out R37

label R37:
    call iscene ("R37")
    call path_end ("rintrue", True)
    jump_out restart



label R38:
    call iscene ("R38")
    jump_out R39

label R39:
    call iscene ("R39")
    jump_out R40

label R40:
    call iscene ("R40")
    jump_out R41

label R41:
    call iscene ("timeskip")
    call iscene ("R41")
    call iscene ("R41h", is_h=True)
    jump_out R42

label R42:
    call iscene ("R42")
    call path_end ("rin", True)
    jump_out restart






label tc_act2_shizune:
    call act_op ("tc_act2_shizune.mkv")
    jump_out S8

label S8:
    call iscene ("S8")
    jump_out S9

label S9:
    call iscene ("timeskip")
    call iscene ("S9")
    jump_out S10

label S10:
    call iscene ("timeskip")
    call iscene ("S10")
    jump_out S11

label S11:
    call iscene ("timeskip")
    call iscene ("S11")
    jump_out S12

label S12:
    call iscene ("timeskip")
    call iscene ("S12")
    jump_out S13

label S13:
    call iscene ("timeskip")
    call iscene ("S13")
    jump_out S14

label S14:
    call iscene ("timeskip")
    call iscene ("S14")
    jump_out S15

label S15:
    call iscene ("timeskip")
    call iscene ("S15")
    jump_out S16

label S16:
    call iscene ("timeskip")
    call iscene ("S16")
    jump_out tc_act3_shizune

label tc_act3_shizune:
    call act_op ("tc_act3_shizune.mkv")
    jump_out S17

label S17:
    call iscene ("S17")
    if seen_scene ("A26b"):
        call iscene ("S17a")
    call iscene ("S17x")
    jump_out S18

label S18:
    call iscene ("timeskip")
    call iscene ("S18")
    jump_out S19

label S19:
    call iscene ("timeskip")
    call iscene ("S19")
    jump_out S20

label S20:
    call iscene ("timeskip")
    call iscene ("S20")
    jump_out S21

label S21:
    call iscene ("timeskip")
    call iscene ("S21")
    jump_out S22

label S22:
    call iscene ("S22")
    if seen_scene ("A26b"):
        call iscene ("S22a")
    else:
        call iscene ("S22b")
    call iscene ("S22c")
    call iscene ("S22h", is_h=True)
    call iscene ("S22x")
    jump_out S23

label S23:
    call iscene ("timeskip")
    call iscene ("S23")
    if not seen_scene ("A2b"):
        call iscene ("S23a")
    call iscene ("S23x")
    jump_out S24

label S24:
    call iscene ("timeskip")
    call iscene ("S24")
    jump_out S25

label S25:
    call iscene ("timeskip")
    call iscene ("S25")
    jump_out S26

label S26:
    call iscene ("timeskip")
    call iscene ("S26")
    if seen_scene ("A26b"):
        call iscene ("S26a")
    else:
        call iscene ("S26b")
    call iscene ("S26c")
    jump_out S27

label S27:
    call iscene ("timeskip")
    call iscene ("S27")
    jump_out S28

label S28:
    call iscene ("timeskip")
    call iscene ("S28")
    call imenu ("choiceS28")
    if _return == m1:
        call iscene ("S28a")
        call iscene ("S28h", is_h=True)
        jump_out S29_1
    else:
        call iscene ("S28b")
    jump_out S29_2

label S29_1:
    call iscene ("timeskip")
    call iscene ("S29")
    call iscene ("S29a")
    call iscene ("S29x")
    call iscene ("S29xa")
    call iscene ("S29y")
    call iscene ("S29ya")
    jump_out tc_act4_shizune

label S29_2:
    call iscene ("timeskip")
    call iscene ("S29")
    call iscene ("S29b")
    call iscene ("S29x")
    call iscene ("S29xb")
    if seen_scene ("A26b"):
        call iscene ("S29xba")
    else:
        call iscene ("S29xbb")
    call iscene ("S29xbc")
    call iscene ("S29y")
    call iscene ("S29yb")
    jump_out tc_act4_shizune

label tc_act4_shizune:
    call act_op ("tc_act4_shizune.mkv")
    jump_out S30

label S30:
    call iscene ("S30")
    jump_out S31

label S31:
    call iscene ("timeskip")
    call iscene ("S31")
    jump_out S32

label S32:
    call iscene ("timeskip")
    call iscene ("S32")
    jump_out S33

label S33:
    call iscene ("timeskip")
    call iscene ("S33")
    if seen_scene("S28a"):
        jump_out S38
    jump_out S34


label S34:
    call iscene ("timeskip")
    call iscene ("S34")
    if not seen_scene ("A26b"):
        call iscene ("S34a")
    else:
        call iscene ("S34b")
    call iscene ("S34c")
    jump_out S35

label S35:
    call iscene ("timeskip")
    call iscene ("S35")
    call iscene ("S35h", is_h=True)
    call iscene ("S35x")
    jump_out S36

label S36:
    call iscene ("S36")
    jump_out S37

label S37:
    call iscene ("timeskip")
    call iscene ("S37")
    call path_end ("shizune", True)
    jump_out restart


label S38:
    call iscene ("timeskip")
    call iscene ("S38")
    jump_out S39

label S39:
    call iscene ("timeskip")
    call iscene ("S39")
    jump_out S40

label S40:
    call iscene ("timeskip")
    call iscene ("S40")
    call path_end ("shizune")
    jump_out restart
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
