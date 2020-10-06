








label replay_A2:
    call iscene ("A2")
    call iscene ("A2b")
    call iscene ("A2c")
    call iscene ("A2d")
    call iscene ("A2f")
    $ replay_end()



label replay_A8:
    call iscene ("A8")
    call imenu ("choiceA8")
    if _return == m1:
        call iscene ("A8a")
        call iscene ("A8aa")
        call iscene ("A8ab")
    else:
        call iscene ("A8b")
    call iscene ("A8c")
    if seen_scene ("A8a"):
        call iscene ("A8d")
    else:
        call iscene ("A8e")
    call iscene ("A8f")
    $ replay_end()



label replay_A10:
    call iscene ("A10")
    call imenu ("choiceA10a")
    if _return == m1:
        call iscene ("A10a")
    elif _return == m2:
        call iscene ("A10b")
    else:
        call iscene ("A10c")
    $ replay_end()

label replay_A11_1:
    call iscene ("A11")
    call iscene ("A11a")
    call iscene ("A11b")
    call iscene ("A11x")
    $ replay_end()


label replay_A19:
    call iscene ("A19")
    call iscene ("A19a")
    call iscene ("A19c")
    call iscene ("A19j")
    call iscene ("A19d")
    call iscene ("A19f")
    call iscene ("A19g")
    $ replay_end()


label replay_A21:
    call iscene ("A21")
    call imenu ("choiceA21")
    if _return == m1:
        call iscene ("A21a")
        $ replay_end()
    call iscene ("A21b")
    call iscene ("A21c")
    $ replay_end()

label replay_A22:
    call iscene ("A22")
    call iscene ("A22a")
    $ replay_end()

label replay_A23_1:
    call iscene ("A23")
    $ replay_end()

label replay_A23_2:
    call iscene ("A23a")
    $ replay_end()


label replay_A24:
    call iscene ("A24")
    call iscene ("A24d")
    call iscene ("A24e")
    $ replay_end()


label replay_A26:
    call iscene ("A26")
    call iscene ("A26a")
    call iscene ("A26e")
    $ replay_end()

label replay_A26_1:
    call iscene ("A26b")
    call imenu ("choiceA26")
    if _return == m1:
        call iscene ("A26c")
        $ replay_end()
    call iscene ("A26d")
    $ replay_end()

label replay_A27_1:
    call iscene ("A27")
    call iscene ("A27a")
    call imenu ("choiceA27")
    if _return == m1:
        call iscene ("A27b")
        $ attraction_kenji += 1
        call iscene ("A27f")
        $ replay_end()
    call iscene ("A27c")
    call imenu ("choice2A27")
    if _return == m1:
        call iscene ("A27h")
        call iscene ("A27e")
        $ replay_end()
    call iscene ("A27i")
    jump_out A28

label replay_A27_2:
    call iscene ("A27d")
    call iscene ("A27e")
    $ replay_end()

label replay_A28:
    call iscene ("A28")
    call iscene ("A28a")
    call iscene ("A28b")
    $ replay_end()

label replay_A29:
    call iscene ("A29")
    call iscene ("A29x")
    call iscene ("A29b")
    call iscene ("A29c")
    $ replay_end()

label replay_A30:
    call iscene ("A30")
    call imenu ("choiceA30")
    if _return == m2:
        call iscene ("A30a")
        $ replay_end()
    call iscene ("A30b")
    call iscene ("A30c")
    call iscene ("A30d")
    $ replay_end()


label replay_A31:
    call iscene ("A31")
    call iscene ("A31c")
    call iscene ("A31d")
    call iscene ("A31e")
    $ replay_end()


label replay_A38:
    call iscene ("A38")
    $ replay_end()



label replay_H7:
    call iscene ("H7")
    call iscene ("H7a")
    call iscene ("H7c")
    $ replay_end()

label replay_H22:
    call iscene ("H22")
    call imenu ("choiceH22")
    if _return == m1:
        call iscene ("H22a")
    else:
        call iscene ("H22c")
    $ replay_end()

label replay_H25:
    call iscene ("H25")
    call iscene ("H25a")
    call iscene ("H25c")
    $ replay_end()




label replay_E11:
    call iscene ("E11a")
    call iscene ("E11x")
    call iscene ("E11z")
    call imenu ("choiceE11")
    if _return == m1:
        call iscene ("E11b")
    else:
        call iscene ("E11c")
    call iscene ("E11d")
    $ replay_end()

label replay_E12:
    call iscene ("E12a")
    call iscene ("E12b")
    call iscene ("E12d")
    $ replay_end()

label replay_E18:
    call iscene ("E18")
    call iscene ("E18a")
    call iscene ("E18x")
    $ replay_end()

label replay_E26:
    call iscene ("E26")
    call iscene ("E26a")
    call iscene ("E26b")
    call iscene ("E26e")
    call iscene ("E26f")
    call imenu ("choiceE26")
    if _return == m2:
        call iscene ("E26d")
        $ replay_end()
    call iscene ("E26c")
    $ replay_end()

label replay_E30:
    call iscene ("E30")
    call iscene ("E30a")
    call iscene ("E30b")
    call iscene ("E30d")
    call iscene ("E30e")
    $ replay_end()



label replay_R11:
    call iscene ("R11")
    call imenu ("choiceR11aaa")
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
    $ replay_end()

label replay_R12:
    call iscene ("R12")
    call iscene ("R12b")
    call iscene ("R12c")
    call iscene ("R12e")
    call iscene ("R12f")
    $ replay_end()

label replay_R16:
    call iscene ("R16")
    call imenu ("choiceR16")
    if _return == m1:
        call iscene ("R16a")
    else:
        call iscene ("R16b")
    call iscene ("R16c")
    call iscene ("R16d")
    call iscene ("R16e")
    $ replay_end()

label replay_R19:
    call iscene ("R19")
    call iscene ("R19a")
    call iscene ("R19b")
    $ replay_end()

label replay_R28:
    call iscene ("R28")
    call imenu ("choiceR28_1")
    if _return == m1:
        call iscene ("R28a")
    elif _return == m2:
        call iscene ("R28b")
    else:
        $ replay_end()
    call iscene ("R28c")
    $ replay_end()

label replay_R30:
    call iscene ("R30")
    call iscene ("R30y")
    call iscene ("R30z")
    $ replay_end()

label replay_R36:
    call iscene ("R36")
    call iscene ("R36a")
    call iscene ("R36x")
    $ replay_end()


label replay_S17:
    call iscene ("S17")
    call iscene ("S17a")
    call iscene ("S17x")
    $ replay_end()

label replay_S22:
    call iscene ("S22")
    call iscene ("S22a")
    call iscene ("S22c")
    call iscene ("S22h", is_h=True)
    call iscene ("S22x")
    $ replay_end()

label replay_S23:
    call iscene ("timeskip")
    call iscene ("S23")
    call iscene ("S23a")
    call iscene ("S23x")
    $ replay_end()

label replay_S26:
    call iscene ("S26")
    call iscene ("S26a")
    call iscene ("S26c")
    $ replay_end()

label replay_S29_2:
    call iscene ("S29")
    call iscene ("S29b")
    call iscene ("S29x")
    call iscene ("S29xb")
    call iscene ("S29xba")
    call iscene ("S29xbc")
    call iscene ("S29y")
    call iscene ("S29yb")
    $ replay_end()

label replay_S34:
    call iscene ("S34")
    call iscene ("S34b")
    call iscene ("S34c")
    $ replay_end()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
