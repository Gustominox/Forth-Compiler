
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = '1MINUS 1PLUS 2DIVIDE 2DUP 2MINUS 2PLUS 2TIMES CHAR CODE COLON COMMENT CR DIVIDE DO DROP DUP ELSE EMIT EQUAL FLOAT IF INF INFEQUAL INT LOOP MINUS MOD PLUS PONTO PONTOSTRING SEMICOLON SUP SUPEQUAL SWAP THEN TIMES WORDaxioma : axioma lineaxioma : emptyline : COMMENTline : conditionalconditional : IF axioma ELSE axioma THEN axiomaconditional : IF axioma THEN axiomaline : DO axioma LOOPline : PONTOline : CRline : PONTOSTRINGline : EMITline : CHAR WORDline : operationoperation : 1PLUSoperation : 1MINUSoperation : 2PLUSoperation : 2MINUSoperation : 2TIMESoperation : 2DIVIDEoperation : DUPoperation : 2DUPoperation : DROPoperation : SWAPline : int line\n            | float lineline : intline : floatint : INTfloat : FLOATline : COLON WORD CODEline : COLON WORDline : WORDoperation : PLUSoperation : MINUSoperation : TIMESoperation : DIVIDEoperation : MODoperation : SUPoperation : EQUALoperation : INFoperation : SUPEQUALoperation : INFEQUALempty :'
    
_lr_action_items = {'COMMENT':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,4,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,4,4,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,4,-12,-24,-25,-31,4,-7,-30,-43,-43,4,4,-43,4,]),'DO':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,6,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,6,6,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,6,-12,-24,-25,-31,6,-7,-30,-43,-43,6,6,-43,6,]),'PONTO':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,7,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,7,7,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,7,-12,-24,-25,-31,7,-7,-30,-43,-43,7,7,-43,7,]),'CR':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,8,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,8,8,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,8,-12,-24,-25,-31,8,-7,-30,-43,-43,8,8,-43,8,]),'PONTOSTRING':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,9,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,9,9,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,9,-12,-24,-25,-31,9,-7,-30,-43,-43,9,9,-43,9,]),'EMIT':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,10,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,10,10,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,10,-12,-24,-25,-31,10,-7,-30,-43,-43,10,10,-43,10,]),'CHAR':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,11,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,11,11,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,11,-12,-24,-25,-31,11,-7,-30,-43,-43,11,11,-43,11,]),'COLON':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,16,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,16,16,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,16,-12,-24,-25,-31,16,-7,-30,-43,-43,16,16,-43,16,]),'WORD':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,12,-2,-1,-3,-4,-43,-8,-9,-10,-11,41,-32,-13,12,12,44,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,12,-12,-24,-25,-31,12,-7,-30,-43,-43,12,12,-43,12,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,17,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,17,17,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,17,-12,-24,-25,-31,17,-7,-30,-43,-43,17,17,-43,17,]),'1PLUS':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,18,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,18,18,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,18,-12,-24,-25,-31,18,-7,-30,-43,-43,18,18,-43,18,]),'1MINUS':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,19,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,19,19,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,19,-12,-24,-25,-31,19,-7,-30,-43,-43,19,19,-43,19,]),'2PLUS':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,20,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,20,20,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,20,-12,-24,-25,-31,20,-7,-30,-43,-43,20,20,-43,20,]),'2MINUS':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,21,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,21,21,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,21,-12,-24,-25,-31,21,-7,-30,-43,-43,21,21,-43,21,]),'2TIMES':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,22,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,22,22,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,22,-12,-24,-25,-31,22,-7,-30,-43,-43,22,22,-43,22,]),'2DIVIDE':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,23,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,23,23,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,23,-12,-24,-25,-31,23,-7,-30,-43,-43,23,23,-43,23,]),'DUP':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,24,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,24,24,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,24,-12,-24,-25,-31,24,-7,-30,-43,-43,24,24,-43,24,]),'2DUP':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,25,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,25,25,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,25,-12,-24,-25,-31,25,-7,-30,-43,-43,25,25,-43,25,]),'DROP':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,26,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,26,26,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,26,-12,-24,-25,-31,26,-7,-30,-43,-43,26,26,-43,26,]),'SWAP':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,27,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,27,27,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,27,-12,-24,-25,-31,27,-7,-30,-43,-43,27,27,-43,27,]),'PLUS':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,28,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,28,28,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,28,-12,-24,-25,-31,28,-7,-30,-43,-43,28,28,-43,28,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,29,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,29,29,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,29,-12,-24,-25,-31,29,-7,-30,-43,-43,29,29,-43,29,]),'TIMES':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,30,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,30,30,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,30,-12,-24,-25,-31,30,-7,-30,-43,-43,30,30,-43,30,]),'DIVIDE':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,31,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,31,31,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,31,-12,-24,-25,-31,31,-7,-30,-43,-43,31,31,-43,31,]),'MOD':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,32,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,32,32,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,32,-12,-24,-25,-31,32,-7,-30,-43,-43,32,32,-43,32,]),'SUP':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,33,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,33,33,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,33,-12,-24,-25,-31,33,-7,-30,-43,-43,33,33,-43,33,]),'EQUAL':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,34,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,34,34,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,34,-12,-24,-25,-31,34,-7,-30,-43,-43,34,34,-43,34,]),'INF':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,35,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,35,35,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,35,-12,-24,-25,-31,35,-7,-30,-43,-43,35,35,-43,35,]),'SUPEQUAL':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,36,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,36,36,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,36,-12,-24,-25,-31,36,-7,-30,-43,-43,36,36,-43,36,]),'INFEQUAL':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,37,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,37,37,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,37,-12,-24,-25,-31,37,-7,-30,-43,-43,37,37,-43,37,]),'INT':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,38,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,38,38,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,38,-12,-24,-25,-31,38,-7,-30,-43,-43,38,38,-43,38,]),'FLOAT':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-43,39,-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,39,39,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,39,-12,-24,-25,-31,39,-7,-30,-43,-43,39,39,-43,39,]),'$end':([0,1,2,3,4,5,7,8,9,10,12,13,14,15,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,49,51,52,53,],[-43,0,-2,-1,-3,-4,-8,-9,-10,-11,-32,-13,-26,-27,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,-12,-24,-25,-31,-7,-30,-43,-6,-43,-5,]),'LOOP':([2,3,4,5,6,7,8,9,10,12,13,14,15,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,49,51,52,53,],[-2,-1,-3,-4,-43,-8,-9,-10,-11,-32,-13,-26,-27,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,46,-12,-24,-25,-31,-7,-30,-43,-6,-43,-5,]),'ELSE':([2,3,4,5,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,49,51,52,53,],[-2,-1,-3,-4,-8,-9,-10,-11,-32,-13,-26,-27,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,-12,-24,-25,-31,48,-7,-30,-43,-6,-43,-5,]),'THEN':([2,3,4,5,7,8,9,10,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-2,-1,-3,-4,-8,-9,-10,-11,-32,-13,-26,-27,-43,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,-29,-12,-24,-25,-31,49,-7,-30,-43,-43,52,-6,-43,-5,]),'CODE':([44,],[47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'axioma':([0,6,17,48,49,52,],[1,40,45,50,51,53,]),'empty':([0,6,17,48,49,52,],[2,2,2,2,2,2,]),'line':([1,14,15,40,45,50,51,53,],[3,42,43,3,3,3,3,3,]),'conditional':([1,14,15,40,45,50,51,53,],[5,5,5,5,5,5,5,5,]),'operation':([1,14,15,40,45,50,51,53,],[13,13,13,13,13,13,13,13,]),'int':([1,14,15,40,45,50,51,53,],[14,14,14,14,14,14,14,14,]),'float':([1,14,15,40,45,50,51,53,],[15,15,15,15,15,15,15,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> axioma","S'",1,None,None,None),
  ('axioma -> axioma line','axioma',2,'p_axioma_iter','forth_yacc_wordDef.py',24),
  ('axioma -> empty','axioma',1,'p_axioma_empty','forth_yacc_wordDef.py',28),
  ('line -> COMMENT','line',1,'p_line_comment','forth_yacc_wordDef.py',32),
  ('line -> conditional','line',1,'p_line_conditional','forth_yacc_wordDef.py',36),
  ('conditional -> IF axioma ELSE axioma THEN axioma','conditional',6,'p_conditional_else','forth_yacc_wordDef.py',40),
  ('conditional -> IF axioma THEN axioma','conditional',4,'p_confitional_then','forth_yacc_wordDef.py',46),
  ('line -> DO axioma LOOP','line',3,'p_line_loop','forth_yacc_wordDef.py',53),
  ('line -> PONTO','line',1,'p_line_ponto','forth_yacc_wordDef.py',75),
  ('line -> CR','line',1,'p_line_cr','forth_yacc_wordDef.py',88),
  ('line -> PONTOSTRING','line',1,'p_line_pontostring','forth_yacc_wordDef.py',92),
  ('line -> EMIT','line',1,'p_line_emit','forth_yacc_wordDef.py',96),
  ('line -> CHAR WORD','line',2,'p_line_char','forth_yacc_wordDef.py',106),
  ('line -> operation','line',1,'p_line_expression_arithmetic','forth_yacc_wordDef.py',112),
  ('operation -> 1PLUS','operation',1,'p_operation_1plus','forth_yacc_wordDef.py',116),
  ('operation -> 1MINUS','operation',1,'p_operation_1minus','forth_yacc_wordDef.py',131),
  ('operation -> 2PLUS','operation',1,'p_operation_2plus','forth_yacc_wordDef.py',146),
  ('operation -> 2MINUS','operation',1,'p_operation_2minus','forth_yacc_wordDef.py',160),
  ('operation -> 2TIMES','operation',1,'p_operation_2times','forth_yacc_wordDef.py',174),
  ('operation -> 2DIVIDE','operation',1,'p_operation_2divide','forth_yacc_wordDef.py',189),
  ('operation -> DUP','operation',1,'p_operation_dup','forth_yacc_wordDef.py',204),
  ('operation -> 2DUP','operation',1,'p_operation_2dup','forth_yacc_wordDef.py',211),
  ('operation -> DROP','operation',1,'p_operation_drop','forth_yacc_wordDef.py',223),
  ('operation -> SWAP','operation',1,'p_operation_swap','forth_yacc_wordDef.py',228),
  ('line -> int line','line',2,'p_line_variable_list','forth_yacc_wordDef.py',236),
  ('line -> float line','line',2,'p_line_variable_list','forth_yacc_wordDef.py',237),
  ('line -> int','line',1,'p_line_int','forth_yacc_wordDef.py',241),
  ('line -> float','line',1,'p_line_float','forth_yacc_wordDef.py',245),
  ('int -> INT','int',1,'p_int','forth_yacc_wordDef.py',249),
  ('float -> FLOAT','float',1,'p_float','forth_yacc_wordDef.py',254),
  ('line -> COLON WORD CODE','line',3,'p_line_definition','forth_yacc_wordDef.py',259),
  ('line -> COLON WORD','line',2,'p_line_definition_error','forth_yacc_wordDef.py',268),
  ('line -> WORD','line',1,'p_line_word','forth_yacc_wordDef.py',273),
  ('operation -> PLUS','operation',1,'p_operation_plus','forth_yacc_wordDef.py',281),
  ('operation -> MINUS','operation',1,'p_operation_minus','forth_yacc_wordDef.py',299),
  ('operation -> TIMES','operation',1,'p_operation_times','forth_yacc_wordDef.py',316),
  ('operation -> DIVIDE','operation',1,'p_operation_divide','forth_yacc_wordDef.py',333),
  ('operation -> MOD','operation',1,'p_operation_mod','forth_yacc_wordDef.py',349),
  ('operation -> SUP','operation',1,'p_operation_sup','forth_yacc_wordDef.py',364),
  ('operation -> EQUAL','operation',1,'p_operation_equal','forth_yacc_wordDef.py',375),
  ('operation -> INF','operation',1,'p_operation_inf','forth_yacc_wordDef.py',383),
  ('operation -> SUPEQUAL','operation',1,'p_operation_supequal','forth_yacc_wordDef.py',394),
  ('operation -> INFEQUAL','operation',1,'p_operation_infequal','forth_yacc_wordDef.py',405),
  ('empty -> <empty>','empty',0,'p_empty','forth_yacc_wordDef.py',416),
]
