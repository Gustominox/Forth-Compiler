( May the Forth be with you)
: STAR 42 EMIT ;
: STARS 0 DO STAR LOOP ;
: MARGIN CR ."      " ;
: BLIP MARGIN STAR ;
: IOI MARGIN STAR 3 ."      " STAR ;
: IIO MARGIN STAR STAR 3 ."      " ;
: OIO MARGIN 2 ."      " STAR 2 ."      " ;
: BAR MARGIN 5 STARS ;
: F BAR BLIP BAR BLIP BLIP CR ;
: O BAR IOI IOI IOI BAR CR ;
: R BAR IOI BAR IIO IOI CR ;
: T BAR OIO OIO OIO OIO CR ;
: H IOI IOI BAR IOI IOI CR ;
F O R T H