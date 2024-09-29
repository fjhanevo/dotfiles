from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# from qtile_extras import widget
# from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
terminal = guess_terminal()
myBrowser = "firefox"
vscode = "code"

""" KEYS """

keys = [
    # Custom
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(myBrowser), desc="Launch firefox"),
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run"), desc="Run dmenu"),
    Key([mod], "v", lazy.spawn(vscode), desc="Launch VScode"),
    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 5- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 5+ unmute")),
    # Lock screen
    Key([mod, "shift"], "x", lazy.spawn("slock"), desc="Lock Screen"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
]
#

groups = [
    Group("1", layout="colum", label="Α"),
    Group("2", layout="colum", label="Β"),
    Group("3", layout="colum", label="Γ"),
    Group("4", layout="colum", label="Δ"),
    Group("5", layout="colum", label="Ε"),
    Group("6", layout="colum", label="Ζ"),
    Group("7", layout="colum", label="Η"),
    Group("8", layout="colum", label="Θ"),
    Group("9", layout="colum", label="Ι"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(str(i)),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )


""" LAYOUTS """

layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_focus": "#e1acff",
    "border_focus_stack": "#e1acff",
    "border_normal": "#1D2330",
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

""" COLORS """

colors = [
    ["#282c34", "#282c34"],
    ["#1c1f24", "#1c1f24"],
    ["#dfdfdf", "#dfdfdf"],
    ["#ff6c6b", "#ff6c6b"],
    ["#98be65", "#98be65"],
    ["#da8548", "#da8548"],
    ["#51afef", "#51afef"],
    ["#c678dd", "#c678dd"],
    ["#61afef", "#61afef"],
    ["#a9a1e1", "#a9a1e1"],
]

""" WIDGETS """

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=11,
    padding=2,
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=9,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[8],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[8],
            higlight_method="line",
            # this_current_screen_border = colors[0],
            # this_screen_border = colors[0],
            # other_current_screen_border = colors[6],
            # other_screen_border = colors[4],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.TextBox(
            text="|",
            font="Ubuntu Mono",
            background=colors[0],
            foreground="474747",
            padding=2,
            fontsize=14,
        ),
        widget.CurrentLayout(foreground=colors[2], background=colors[0], padding=5),
        widget.TextBox(
            text="|",
            font="Ubuntu Mono",
            background=colors[0],
            foreground="474747",
            padding=2,
            fontsize=14,
        ),
        widget.WindowName(foreground=colors[8], background=colors[0], padding=0),
        widget.Systray(background=colors[0], padding=5),
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.TextBox(
            text="⮂", background=colors[0], foreground=colors[7], padding=0, fontsize=37
        ),
        widget.CPU(
            foreground=colors[0],
            background=colors[7],
            padding=5,
            fontsize=10,
            width=65,
            format="CPU: {load_percent}%",
        ),
        widget.TextBox(
            text="⮂", background=colors[7], foreground=colors[8], padding=0, fontsize=27
        ),
        widget.Memory(
            foreground=colors[0],
            background=colors[8],
            fontsize=10,
            fmt="RAM: {}",
        ),
        # widget.TextBox(
        #     text='⮂',
        #     background=colors[7],
        #     foreground=colors[8],
        #     padding=0,
        #     fontsize=27
        # ),
        # widget.Wlan(
        #         interface = "wlo1",
        #         foreground = colors[0],
        #         background = colors[8],
        #         padding = 6,
        #         width=90,
        #         format = 'Connected {percent:2.0%}'
        #         ),
        widget.TextBox(
            text="⮂", background=colors[8], foreground=colors[7], padding=0, fontsize=27
        ),
        widget.Battery(
            foreground=colors[0],
            background=colors[7],
            padding=5,
            fontsize=10,
            charge_char="",
            discharge_char="",
            full_char="",
            # charge_char = '↑',
            # discharge_char = '↓',
            fmt="Battery: {}",
            format="{char} {percent:2.0%}",
        ),
        # widget.TextBox(
        #     text='⮂',
        #     background=colors[7],
        #     foreground=colors[8],
        #     padding=0,
        #     fontsize=27
        # ),
        widget.Volume(
            foreground=colors[0],
            background=colors[7],
            fmt="Vol: {}",
            padding=5,
            width=55,
            fontsize=10,
            # decorations = [
            #     BorderDecoration(
            #         colour = colors[7],
            #         border_width = [0, 0, 2, 0],
            #         padding_x = 5,
            #         padding_y = None,
            #     )
            # ],
        ),
        widget.TextBox(
            text="⮂", background=colors[7], foreground=colors[8], padding=0, fontsize=27
        ),
        widget.Clock(
            foreground=colors[0],
            background=colors[8],
            fontsize=10,
            format="%A, %B %d - %H:%M ",
            # decorations = [
            #     BorderDecoration(
            #         colour = colors[8],
            #         border_width = [0, 0, 2, 0],
            #         padding_x = 5,
            #         padding_y = None,
            #     ),
            # ],
        ),
    ]
    return widgets_list


""" Set Screen (Laptop) """


def init_widgets_screen():
    widget_screen = init_widgets_list()
    return widget_screen


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen(), opacity=1.0, size=20))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widget_list = init_widgets_list()

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"
