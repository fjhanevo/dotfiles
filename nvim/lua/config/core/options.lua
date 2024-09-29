vim.cmd("let g:netrw_liststyle=3")

local opt = vim.opt

opt.number = true

-- relative linenumbers
opt.relativenumber = true

-- tabs & indentation
opt.tabstop = 4
opt.shiftwidth = 4
opt.expandtab = true
opt.autoindent = true

opt.wrap = false

-- search settings
opt.ignorecase = true --ignore case when searching
opt.smartcase = true -- case sensitive search

-- cursor settings
opt.cursorline = true
opt.cursorlineopt = "number"

-- themes
opt.termguicolors = true
opt.background = "dark"
-- opt.signcolumn = "no"

-- backspace
opt.backspace = "indent,eol,start" -- backspace on indent

-- clipboard
opt.clipboard:append("unnamedplus") -- system clipboard as register

-- split windows
opt.splitright = true
opt.splitbelow = true

opt.swapfile = false

-- disable mouse
--opt.mouse = ""

-- set format option to disable autocomments
vim.cmd("autocmd BufEnter * set formatoptions-=cro")
vim.cmd("autocmd BufEnter * setlocal formatoptions-=cro")
