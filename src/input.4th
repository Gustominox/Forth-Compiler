: maior2 2dup > if drop else swap drop then ;
    : maior3 maior2 maior2 ;
    : maiorN ( -- ) depth 1 do maior2 loop ;
    2 11 3 4 45 8 19 maiorN .