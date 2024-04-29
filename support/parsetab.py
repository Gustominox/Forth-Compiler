
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL ID LPAREN NUM RPAREN VIRGLIST : LPAREN ELS RPARENELS : ELS VIRG ELELS : ELEL : NUMEL : BOOLEL : ID'
    
_lr_action_items = {'LPAREN':([0,],[2,]),'$end':([1,8,],[0,-1,]),'NUM':([2,9,],[5,5,]),'BOOL':([2,9,],[6,6,]),'ID':([2,9,],[7,7,]),'RPAREN':([3,4,5,6,7,10,],[8,-3,-4,-5,-6,-2,]),'VIRG':([3,4,5,6,7,10,],[9,-3,-4,-5,-6,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'LIST':([0,],[1,]),'ELS':([2,],[3,]),'EL':([2,9,],[4,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> LIST","S'",1,None,None,None),
  ('LIST -> LPAREN ELS RPAREN','LIST',3,'p_list','listas_mistas_yacc.py',13),
  ('ELS -> ELS VIRG EL','ELS',3,'p_els_varios','listas_mistas_yacc.py',19),
  ('ELS -> EL','ELS',1,'p_els_um','listas_mistas_yacc.py',26),
  ('EL -> NUM','EL',1,'p_el_num','listas_mistas_yacc.py',34),
  ('EL -> BOOL','EL',1,'p_el_bool','listas_mistas_yacc.py',40),
  ('EL -> ID','EL',1,'p_el_id','listas_mistas_yacc.py',44),
]
