
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = '1MINUS 1PLUS 2DIVIDE 2DUP 2MINUS 2PLUS 2TIMES ANYCHAR CHAR CODE COLON COMMENT CR DEPTH DIVIDE DO DROP DUP ELSE EMIT EQUAL FLOAT IF INF INFEQUAL INT LOOP MINUS MOD PLUS PONTO PONTOSTRING SEMICOLON SUP SUPEQUAL SWAP THEN TIMES WORDaxioma : axioma lineaxioma : emptyline : COMMENTline : conditionalconditional : IF axioma ELSE axioma THEN axiomaconditional : IF axioma THEN axiomaline : DO axioma LOOPline : PONTOline : CRline : PONTOSTRINGline : EMITline : CHARline : operationoperation : 1PLUSoperation : 1MINUSoperation : 2PLUSoperation : 2MINUSoperation : 2TIMESoperation : 2DIVIDEoperation : DUPoperation : 2DUPoperation : DROPoperation : SWAPoperation : DEPTHline : int line\n            | float lineline : intline : floatint : INTfloat : FLOATline : COLON WORD CODEline : COLON WORDline : WORDoperation : PLUSoperation : MINUSoperation : TIMESoperation : DIVIDEoperation : MODoperation : SUPoperation : EQUALoperation : INFoperation : SUPEQUALoperation : INFEQUALempty :'
    
_lr_action_items = {'COMMENT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,4,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,4,4,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,4,-25,-26,-32,4,-7,-31,-44,-44,4,4,-44,4,]),'DO':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,6,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,6,6,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,6,-25,-26,-32,6,-7,-31,-44,-44,6,6,-44,6,]),'PONTO':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,7,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,7,7,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,7,-25,-26,-32,7,-7,-31,-44,-44,7,7,-44,7,]),'CR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,8,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,8,8,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,8,-25,-26,-32,8,-7,-31,-44,-44,8,8,-44,8,]),'PONTOSTRING':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,9,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,9,9,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,9,-25,-26,-32,9,-7,-31,-44,-44,9,9,-44,9,]),'EMIT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,10,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,10,10,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,10,-25,-26,-32,10,-7,-31,-44,-44,10,10,-44,10,]),'CHAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,11,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,11,11,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,11,-25,-26,-32,11,-7,-31,-44,-44,11,11,-44,11,]),'COLON':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,15,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,15,15,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,15,-25,-26,-32,15,-7,-31,-44,-44,15,15,-44,15,]),'WORD':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,16,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,16,16,44,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,16,-25,-26,-32,16,-7,-31,-44,-44,16,16,-44,16,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,17,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,17,17,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,17,-25,-26,-32,17,-7,-31,-44,-44,17,17,-44,17,]),'1PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,18,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,18,18,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,18,-25,-26,-32,18,-7,-31,-44,-44,18,18,-44,18,]),'1MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,19,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,19,19,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,19,-25,-26,-32,19,-7,-31,-44,-44,19,19,-44,19,]),'2PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,20,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,20,20,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,20,-25,-26,-32,20,-7,-31,-44,-44,20,20,-44,20,]),'2MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,21,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,21,21,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,21,-25,-26,-32,21,-7,-31,-44,-44,21,21,-44,21,]),'2TIMES':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,22,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,22,22,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,22,-25,-26,-32,22,-7,-31,-44,-44,22,22,-44,22,]),'2DIVIDE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,23,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,23,23,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,23,-25,-26,-32,23,-7,-31,-44,-44,23,23,-44,23,]),'DUP':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,24,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,24,24,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,24,-25,-26,-32,24,-7,-31,-44,-44,24,24,-44,24,]),'2DUP':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,25,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,25,25,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,25,-25,-26,-32,25,-7,-31,-44,-44,25,25,-44,25,]),'DROP':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,26,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,26,26,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,26,-25,-26,-32,26,-7,-31,-44,-44,26,26,-44,26,]),'SWAP':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,27,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,27,27,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,27,-25,-26,-32,27,-7,-31,-44,-44,27,27,-44,27,]),'DEPTH':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,28,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,28,28,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,28,-25,-26,-32,28,-7,-31,-44,-44,28,28,-44,28,]),'PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,29,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,29,29,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,29,-25,-26,-32,29,-7,-31,-44,-44,29,29,-44,29,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,30,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,30,30,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,30,-25,-26,-32,30,-7,-31,-44,-44,30,30,-44,30,]),'TIMES':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,31,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,31,31,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,31,-25,-26,-32,31,-7,-31,-44,-44,31,31,-44,31,]),'DIVIDE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,32,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,32,32,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,32,-25,-26,-32,32,-7,-31,-44,-44,32,32,-44,32,]),'MOD':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,33,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,33,33,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,33,-25,-26,-32,33,-7,-31,-44,-44,33,33,-44,33,]),'SUP':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,34,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,34,34,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,34,-25,-26,-32,34,-7,-31,-44,-44,34,34,-44,34,]),'EQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,35,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,35,35,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,35,-25,-26,-32,35,-7,-31,-44,-44,35,35,-44,35,]),'INF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,36,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,36,36,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,36,-25,-26,-32,36,-7,-31,-44,-44,36,36,-44,36,]),'SUPEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,37,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,37,37,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,37,-25,-26,-32,37,-7,-31,-44,-44,37,37,-44,37,]),'INFEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,38,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,38,38,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,38,-25,-26,-32,38,-7,-31,-44,-44,38,38,-44,38,]),'INT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,39,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,39,39,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,39,-25,-26,-32,39,-7,-31,-44,-44,39,39,-44,39,]),'FLOAT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-44,40,-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,40,40,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,40,-25,-26,-32,40,-7,-31,-44,-44,40,40,-44,40,]),'$end':([0,1,2,3,4,5,7,8,9,10,11,12,13,14,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,46,47,49,51,52,53,],[-44,0,-2,-1,-3,-4,-8,-9,-10,-11,-12,-13,-27,-28,-33,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,-25,-26,-32,-7,-31,-44,-6,-44,-5,]),'LOOP':([2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,49,51,52,53,],[-2,-1,-3,-4,-44,-8,-9,-10,-11,-12,-13,-27,-28,-33,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,46,-25,-26,-32,-7,-31,-44,-6,-44,-5,]),'ELSE':([2,3,4,5,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,49,51,52,53,],[-2,-1,-3,-4,-8,-9,-10,-11,-12,-13,-27,-28,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,-25,-26,-32,48,-7,-31,-44,-6,-44,-5,]),'THEN':([2,3,4,5,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,],[-2,-1,-3,-4,-8,-9,-10,-11,-12,-13,-27,-28,-33,-44,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-29,-30,-25,-26,-32,49,-7,-31,-44,-44,52,-6,-44,-5,]),'CODE':([44,],[47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'axioma':([0,6,17,48,49,52,],[1,41,45,50,51,53,]),'empty':([0,6,17,48,49,52,],[2,2,2,2,2,2,]),'line':([1,13,14,41,45,50,51,53,],[3,42,43,3,3,3,3,3,]),'conditional':([1,13,14,41,45,50,51,53,],[5,5,5,5,5,5,5,5,]),'operation':([1,13,14,41,45,50,51,53,],[12,12,12,12,12,12,12,12,]),'int':([1,13,14,41,45,50,51,53,],[13,13,13,13,13,13,13,13,]),'float':([1,13,14,41,45,50,51,53,],[14,14,14,14,14,14,14,14,]),}

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
  ('line -> CHAR','line',1,'p_line_char','forth_yacc_wordDef.py',106),
  ('line -> operation','line',1,'p_line_expression_arithmetic','forth_yacc_wordDef.py',112),
  ('operation -> 1PLUS','operation',1,'p_operation_1plus','forth_yacc_wordDef.py',116),
  ('operation -> 1MINUS','operation',1,'p_operation_1minus','forth_yacc_wordDef.py',131),
  ('operation -> 2PLUS','operation',1,'p_operation_2plus','forth_yacc_wordDef.py',146),
  ('operation -> 2MINUS','operation',1,'p_operation_2minus','forth_yacc_wordDef.py',160),
  ('operation -> 2TIMES','operation',1,'p_operation_2times','forth_yacc_wordDef.py',174),
  ('operation -> 2DIVIDE','operation',1,'p_operation_2divide','forth_yacc_wordDef.py',189),
  ('operation -> DUP','operation',1,'p_operation_dup','forth_yacc_wordDef.py',204),
  ('operation -> 2DUP','operation',1,'p_operation_2dup','forth_yacc_wordDef.py',216),
  ('operation -> DROP','operation',1,'p_operation_drop','forth_yacc_wordDef.py',228),
  ('operation -> SWAP','operation',1,'p_operation_swap','forth_yacc_wordDef.py',233),
  ('operation -> DEPTH','operation',1,'p_operation_depth','forth_yacc_wordDef.py',241),
  ('line -> int line','line',2,'p_line_variable_list','forth_yacc_wordDef.py',246),
  ('line -> float line','line',2,'p_line_variable_list','forth_yacc_wordDef.py',247),
  ('line -> int','line',1,'p_line_int','forth_yacc_wordDef.py',251),
  ('line -> float','line',1,'p_line_float','forth_yacc_wordDef.py',255),
  ('int -> INT','int',1,'p_int','forth_yacc_wordDef.py',259),
  ('float -> FLOAT','float',1,'p_float','forth_yacc_wordDef.py',264),
  ('line -> COLON WORD CODE','line',3,'p_line_definition','forth_yacc_wordDef.py',269),
  ('line -> COLON WORD','line',2,'p_line_definition_error','forth_yacc_wordDef.py',278),
  ('line -> WORD','line',1,'p_line_word','forth_yacc_wordDef.py',283),
  ('operation -> PLUS','operation',1,'p_operation_plus','forth_yacc_wordDef.py',291),
  ('operation -> MINUS','operation',1,'p_operation_minus','forth_yacc_wordDef.py',309),
  ('operation -> TIMES','operation',1,'p_operation_times','forth_yacc_wordDef.py',326),
  ('operation -> DIVIDE','operation',1,'p_operation_divide','forth_yacc_wordDef.py',343),
  ('operation -> MOD','operation',1,'p_operation_mod','forth_yacc_wordDef.py',359),
  ('operation -> SUP','operation',1,'p_operation_sup','forth_yacc_wordDef.py',374),
  ('operation -> EQUAL','operation',1,'p_operation_equal','forth_yacc_wordDef.py',390),
  ('operation -> INF','operation',1,'p_operation_inf','forth_yacc_wordDef.py',403),
  ('operation -> SUPEQUAL','operation',1,'p_operation_supequal','forth_yacc_wordDef.py',418),
  ('operation -> INFEQUAL','operation',1,'p_operation_infequal','forth_yacc_wordDef.py',433),
  ('empty -> <empty>','empty',0,'p_empty','forth_yacc_wordDef.py',448),
]
