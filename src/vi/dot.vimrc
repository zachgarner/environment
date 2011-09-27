" Set text width to reasonable length.
" To unset (e.g. when pasting) use "set tw=0"
" set tw=72

" To highlight a certain regex message:
" mark ErrorMsg /foo/

" Highlight the current line, you can do cursorcolumn, too
set cursorline
highlight CursorLine ctermbg=darkblue ctermfg=white

" Show line Numbers
set number
set numberwidth=2
highlight LineNr ctermbg=darkblue ctermfg=white

" Allow <alt>-jk to navigate into wrapped lines
" This doesn't seem to work.. you can always do 'g' then jk to
" do the same thing
map <A-DOWN> gj
map <A-UP> gk
imap <A-UP> <ESC>gki
imap <A-DOWN> <ESC>gji
