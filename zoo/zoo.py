print ("I love animals!\nLet's check out the animals...\nThe deer looks fine.\nThe lion looks healthy.")
camel = input("Please, write animal you want.\n>")
print (r""""The camel habitat...
 ___.-''''-.
/___ @      |
',,,,.      |        _.'''''''._
       '    |      /             \
       |     \ _.-'               \
       |                           '.-' '-.
       |                                   ',
       |                                     '',
        ',,-, ':                                ;
                 ',,| ;,,                    ,';;
                    ! ; !'',,,',  ',,,,'  ! ;  ;:
                    : ;    ! !      ! !   ; ;  :;
                    ; ;    ! !      ! !   ; ;  ;,
                    ; ;    ! !      ! !   ; ;
                    ; ;    ! !      ! !   ; ;
                    ;,,    !,!      !,!   ;,;
                    /_I    L_I      L_I   /_I
Look at that!""")
print ("I love animals!\nLet's check out the animals...\nThe deer looks fine.\nThe lion looks healthy.")
animals = ["camel", "lion", "deer", "goose", "bat", "rabbit"]
animals[0] = (r"""The camel habitat...
 ___.-''''-.
/___ @      |
',,,,.      |        _.'''''''._
       '    |      /             \
       |     \ _.-'               \
       |                           '.-' '-.
       |                                   ',
       |                                     '',
        ',,-, ':                                ;
                 ',,| ;,,                    ,';;
                    ! ; !'',,,',  ',,,,'  ! ;  ;:
                    : ;    ! !      ! !   ; ;  :;
                    ; ;    ! !      ! !   ; ;  ;,
                    ; ;    ! !      ! !   ; ;
                    ; ;    ! !      ! !   ; ;
                    ;,,    !,!      !,!   ;,;
                    /_I    L_I      L_I   /_I
Look at that!""""")
animals[1] = (r""""The rabbit habitat...
           ,
          /|       __
         / |     ,-~/
        Y :|   // /
        | jj  /(.^
        >- ~  -v
       /        Y
      jo   o    |
     ( ~T~      j
       >._-  _./
       /  ~    |
      Y _,     |
    /  | ;- ~ _ l
   / l/   ,- ~  \
   \//\/.-       \
    Y           /Y
    l        I   !
    ]\       _\ /\
   (  ~----  ~ Y. )
It looks fine!""")
animals[2] = (r""""The lion habitat...
                                                              ,w.
                                                             ,YWMMw ,M ,
                                         _.---.._ __..---._.'MMMMMw,wMWmW,
                                  _. - ""        '''           YP"WMMMMMMMMMb,
       .-'                    __.'                          .'        MMMMW^WMMMM;
            _, .'.-'"         ; `,                 /`  .--""        :MMM[==MWMW^;
                   ,mM^" ,-'.'; ;                / ,               MMMMb_wMW" @\
       ,MM:. .'.-' .'         ; `\               ; `,                  MMMMMMMW `"=./`-,
   WMMm__,-'.'                / _.\              F'''       -+,, ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-' ,-' _.--"" `-, ;         \             ;  ;       MMMMMMMMMMW        ^``; __|
                / .' ; ;            ) )          `{ \                 `"^W^`,       \ :
               / .' /                             ( .' /                   Ww._ `. `"
              / Y, `, `-,=,                       _{ ;                MMMP`""-,`-._.-,
              (--, ) `                      ,_ / `) \/"") ^" `-, -                 ;"\:
The lion is roaring!""")
animals[3] = (r""""
The deer habitat...
      /|      |\
   `__\\      //__
      ||      ||
   \__`\      | __/
    `_ \\    //_
      _.,:---;,._
      \_:     :_/
        |@. .@|
        |     |
        ,\.-./ \
        ;;`-  `---__________-----.-.
        ;;;                       \_\
         ;;;                        |
         ;    |                     ;
          \    \    \         |    /
           \_,  \   /         \   |\
             | ;|   |,,,,,,,,/\  \  \_
             |  |   |          \   / |
             \  \   |          | / \ |
              | | | |          | | | |
              | | | |          | | | |
              | | | |          | | | |
              |_| |_|          |_| |_|
              /_/ /_/          /_/ /_/
Pretty good!""")
animals[4] = (r""""
The goose habitat...
                             ,- - --.
                           ,'  ____  `.
                         ,' ,'      `. `._
   (`.      _..--.._   ,' ,'          \  \
  (`-.\ .-            '  /            ( d _b
 (`._      `-       ,._ (             `-(   \
<_ `       ( <`<         \               `-._\
 <`-        (__< <        :
  (__        (_<_<        ;
`------------------------------------------
Beautiful!""")
animals[5] = (r"""
The bat habitat...
_________________               _________________
~-.              \   |\___/|   /              .-~
   ~-.            \ /  o o  \ /            .-~
      >            \\   W   //            <
     /              / ~---~ \              \
    /_             |         |             _\ 
      ~-.          |         |          .-~
        ;           \       /           i
/___         /\     /\         ___\
           ~-.     /  \___/  \     .-~
               \  /           \  /
                v               v
It's doing fine.""")
while True:
    animalyw = input("Please enter the number of the habitat you would like to view: >")
    if animalyw == "0":
        print(animals[0])
    elif animalyw == "1":
        print(f"{animals[1]}")
    elif animalyw == "2":
        print(f"{animals[2]}")
    elif animalyw == "3":
        print(f"{animals[3]}")
    elif animalyw == "4":
        print(f"{animals[4]}")
    elif animalyw == "5":
        print(f"{animals[5]}")
    elif animalyw == "exit":
        print("See you later!")
        break
    else:
        print("There's no animal at this number. Try again")
        anymalyw = int(input(">"))
