return {
	"williamboman/mason.nvim",
    dependencies = {
        "williamboman/mason-lspconfig.nvim",
        -- "neovim/nvim-lspconfig",
        "WhoIsSethDaniel/mason-tool-installer.nvim",
    },
	config = function()
		-- import mason
		local mason = require("mason")

		-- import mason-lspconfig
		local mason_lspconfig = require("mason-lspconfig")

		local mason_tool_installer = require("mason-tool-installer")

		-- enable mason and configure icons
		mason.setup({
			ui = {
				icons = {
					package_installed = "✓",
					package_pending = "➜",
					package_uninstalled = "✗",
				},
			},
		})

		mason_lspconfig.setup({
			-- list of servers for mason to install
			ensure_installed = {
				"clangd",
				"cmake",
				"jsonls",
				"bashls",
				"rust_analyzer",
				"lua_ls",
				"pyright",
			},
		})
		mason_tool_installer.setup({
			ensure_installed = {
				"prettier",
				"stylua",
		-- 		"isort",
		-- 		"black",
				"pylint",
			},
		})
	end,
}
