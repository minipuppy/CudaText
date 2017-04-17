EVENTS = [
    'on_caret',
    'on_change',
    'on_change_slow',
    'on_click',
    'on_click_dbl',
    'on_click_gap',
    'on_close',
    'on_complete',
    'on_console',
    'on_console_nav',
    'on_dlg',
    'on_focus',
    'on_func_hint',
    'on_goto_def',
    'on_key',
    'on_key_up',
    'on_lexer',
    'on_macro',
    'on_open',
    'on_open_pre',
    'on_output_nav',
    'on_panel',
    'on_save',
    'on_save_pre',
    'on_snippet',
    'on_start',
    'on_state',
    'on_tab_move',
  ]

EVENTS_ADD_PARAMS = {
  'on_key': 'key, state',
  'on_key_up': 'key, state',
  'on_click': 'state',
  'on_click_dbl': 'state',
  'on_click_gap': 'state, nline, ntag, size_x, size_y, pos_x, pos_y',
  'on_console': 'text',
  'on_console_nav': 'text',
  'on_dlg': 'id_dlg, id_control, id_event',
  'on_output_nav': 'text, tag',
  'on_macro': 'text',
  'on_open_pre': 'filename',
  'on_panel': 'id_control, id_event',
  'on_snippet': 'snippet_id, snippet_text',
  'on_state': 'state',
  }
