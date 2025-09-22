return {
    "neovim/nvim-lspconfig",
    event = { "BufReadPre", "BufNewFile" },
    dependencies = {
        "hrsh7th/cmp-nvim-lsp",
        { "antosha417/nvim-lsp-file-operations", config = true },
        { "folke/neodev.nvim", opts = {} },
    },

    config = function()
        local mason_lspconfig = require("mason-lspconfig")

        local keymap = vim.keymap
        local capabilities = vim.lsp.protocol.make_client_capabilities()
        capabilities = require("cmp_nvim_lsp").default_capabilities(capabilities)
        capabilities.offsetEncoding = { "utf-16" }

        -- Diagnostic signs
        vim.diagnostic.config({
            signs = {
                text = {
                    [vim.diagnostic.severity.ERROR] = " ",
                    [vim.diagnostic.severity.WARN] = " ",
                    [vim.diagnostic.severity.INFO] = " ",
                    [vim.diagnostic.severity.HINT] = "󰠠 ",
                },
                numhl = {
                    [vim.diagnostic.severity.ERROR] = "",
                    [vim.diagnostic.severity.WARN] = "",
                    [vim.diagnostic.severity.INFO] = "",
                    [vim.diagnostic.severity.HINT] = "",
                },
            },
            virtual_text = true,
        })

        -- LspAttach keymaps
        vim.api.nvim_create_autocmd("LspAttach", {
            group = vim.api.nvim_create_augroup("UserLspConfig", {}),
            callback = function(ev)
                local opts = { buffer = ev.buf, silent = true }

                opts.desc = "Show LSP references"
                keymap.set("n", "gR", "<cmd>Telescope lsp_references<CR>", opts)

                opts.desc = "Go to declaration"
                keymap.set("n", "gD", vim.lsp.buf.declaration, opts)

                opts.desc = "Show LSP definitions"
                keymap.set("n", "gd", "<cmd>Telescope lsp_definitions<CR>", opts)

                opts.desc = "Show LSP implementations"
                keymap.set("n", "gi", "<cmd>Telescope lsp_implementations<CR>", opts)

                opts.desc = "Show LSP type definitions"
                keymap.set("n", "gt", "<cmd>Telescope lsp_type_definitions<CR>", opts)

                opts.desc = "See available code actions"
                keymap.set({ "n", "v" }, "<leader>ca", vim.lsp.buf.code_action, opts)

                opts.desc = "Smart rename"
                keymap.set("n", "<leader>rn", vim.lsp.buf.rename, opts)

                opts.desc = "Show buffer diagnostics"
                keymap.set("n", "<leader>D", "<cmd>Telescope diagnostics bufnr=0<CR>", opts)

                opts.desc = "Show line diagnostics"
                keymap.set("n", "<leader>d", vim.diagnostic.open_float, opts)

                opts.desc = "Go to previous diagnostic"
                keymap.set("n", "[d", vim.diagnostic.goto_prev, opts)

                opts.desc = "Go to next diagnostic"
                keymap.set("n", "]d", vim.diagnostic.goto_next, opts)

                opts.desc = "Show documentation for what is under cursor"
                keymap.set("n", "K", vim.lsp.buf.hover, opts)

                opts.desc = "Restart LSP"
                keymap.set("n", "<leader>rs", ":LspRestart<CR>", opts)
            end,
        })

        mason_lspconfig.setup({
            ensure_installed = { "lua_ls", "rust_analyzer", "pyright" },
        })

        -- Server configs
        local servers = {
            lua_ls = {
                settings = {
                    Lua = {
                        diagnostics = { globals = { "vim" } },
                        completion = { callSnippet = "Replace" },
                    },
                },
            },
            rust_analyzer = {
                filetypes = { "rust" },
                settings = {
                    ["rust-analyzer"] = {
                        cargo = { loadOutDirsFromCheck = true },
                        procMacro = { enable = false },
                    },
                },
            },
            pyright = {
                settings = {
                    pyright = {
                        analysis = {
                            autoImportCompletion = true,
                            typeCheckingMode = "basic",
                            diagnosticMode = "openFilesOnly",
                            useLibraryCodeForTypes = true,
                        },
                    },
                },
            },
        }

        for _, server in ipairs(mason_lspconfig.get_installed_servers()) do
            vim.lsp.config[server] = vim.tbl_deep_extend("force", {
                capabilities = capabilities,
            }, servers[server] or {})
            vim.lsp.enable(server)
        end
    end,
}

