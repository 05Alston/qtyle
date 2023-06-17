
#  ██████╗ ████████╗██╗   ██╗██╗     ███████╗
# ██╔═══██╗╚══██╔══╝╚██╗ ██╔╝██║     ██╔════╝
# ██║   ██║   ██║    ╚████╔╝ ██║     █████╗  
# ██║▄▄ ██║   ██║     ╚██╔╝  ██║     ██╔══╝  
# ╚██████╔╝   ██║      ██║   ███████╗███████╗
#  ╚══▀▀═╝    ╚═╝      ╚═╝   ╚══════╝╚══════╝
                                           

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.log_utils import logger
import os
import subprocess


mod = "mod4"
alt = "mod1"
terminal = "alacritty"
browser = "vivaldi-stable --force-dark-mode"
fileman = "thunar"
txtfont = "JetBrains Mono Bold"
iconfont = "lucide"
home = os.path.expanduser("~")
colors = []
cache= home + "/.cache/wal/colors"

# functions & stuff
@hook.subscribe.startup_once
def autostart():
    subprocess.call(home + "/.config/qtile/autostart_once.sh")

@lazy.function
def search(qtile):
    qtile.cmd_spawn("rofi -show drun")

@lazy.function
def power():
    qtile.cmd_spawn(home + "/.local/bin/rofi_powermenu")


@lazy.function
def system_menu(qtile):
    qtile.cmd_spawn("eww close date-clickhandler date")
    qtile.cmd_spawn("eww open-many --toggle actions-clickhandler actions")

@lazy.function
def calendar(qtile):
    qtile.cmd_spawn("eww close actions-clickhandler actions")
    qtile.cmd_spawn("eww open-many --toggle date-clickhandler date")


# def toggle_win(qtile):
#     # logger.warning("suppp")
#     qtile.cmd_next_screen()
#     lazy.layout.next()
#     lazy.window.bring_to_front()

    # qtile.cmd_next_layout()

# def bluetooth():
#     cmd = "bluetoothctl show | grep 'Powered' | awk '{print $2}'"
#     etst = subprocess.run(cmd, shell=True, check=True, text=True)
#     print(f"blue{etst}")
# bluetooth()


def load_colors(cache):
    with open(cache, "r") as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)


# ██╗  ██╗███████╗██╗   ██╗██████╗ ██╗███╗   ██╗██████╗ ███████╗
# ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔══██╗██╔════╝
# █████╔╝ █████╗   ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ██║███████╗
# ██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══██╗██║██║╚██╗██║██║  ██║╚════██║
# ██║  ██╗███████╗   ██║   ██████╔╝██║██║ ╚████║██████╔╝███████║
# ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝


keys = [
#  D E F A U L T
   
    # essentials
    Key(["control"], "Grave", lazy.group["Scratchpad"].dropdown_toggle("term"), desc="Launch terminal"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(["control"], "q", lazy.window.kill(), desc="Kill active window"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle forward layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle last layout"),
    
    # qtile
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # menus
    # Key([mod], "Space", lazy.spawn("mb-jgtools main"), desc="Launch Main Menu"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([mod], "x", lazy.spawn(home + "/.local/bin/rofi_powermenu"), desc="Power Menu"),

    # focus, move windows and screens
    Key([alt], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key([alt, "shift"], "Tab", lazy.layout.previous(), desc="Move window focus to other window"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus left in current stack pane"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus right in current stack pane",),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), lazy.layout.move_down(), desc="Move windows down in current stack",),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), lazy.layout.move_up(), desc="Move windows up in current stack",),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), lazy.layout.move_left(), desc="Move windows left in current stack",),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), lazy.layout.move_right(), desc="Move windows right in the current stack",),
    Key([mod, "control"], "Down", lazy.layout.flip_down(), desc="Flip layout down"),
    Key([mod, "control"], "Up", lazy.layout.flip_up(), desc="Flip layout up"),
    Key([mod, "control"], "Left", lazy.layout.flip_left(), lazy.layout.swap_column_left(), desc="Flip layout left"),
    Key([mod, "control"], "Right", lazy.layout.flip_right(), lazy.layout.swap_column_left(), desc="Flip layout right"),

    # window resizing
    Key([mod, alt], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, alt], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, alt], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, alt], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, alt], "n", lazy.layout.normalize(), desc="Normalize window size ratios"),

    # window states
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle window between minimum and maximum sizes",),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod, alt], "f", lazy.window.toggle_floating(), desc="Toggle floating mode for a window"),

    # floating mode
    Key([mod] , "i", lazy.layout.grow(), desc="Increase window size"),
    Key([mod, "shift"] , "i", lazy.layout.shrink(), desc="Decrease window size"),

    # program launches
    Key([mod], "f", lazy.spawn(fileman), desc="Launch File Manager"),
    Key([mod], "w", lazy.spawn(browser), desc="Launch Default Browser"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch VSCode"),
    Key([mod], "v", lazy.group["Scratchpad"].dropdown_toggle("pavu"), desc="Launch Volume Control"),
    Key(["control"], "2", lazy.group["Scratchpad"].dropdown_toggle("screenrecorder"), desc="Launch Screen recorder"),
    # Key([mod], "u", lazy.group["Scratchpad"].dropdown_toggle("update"), desc="Update system with yay"),
    Key([mod], "s", lazy.group["Scratchpad"].dropdown_toggle("xpad"), desc="Open xpad"),
    Key([mod], "b", lazy.group["Scratchpad"].dropdown_toggle("bluetooth"), desc="Open bluetooth manager"),
    
    # screenshots
    Key([], "Print", lazy.spawn(home + "/.local/bin/rofi_screenshot"), desc="Print Screen"),
    Key([mod], "Print", lazy.spawn("flameshot gui"), desc="Print Screen GUI"),

    # audio stuff
    # Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 3"), desc="Increase volume",),
    # Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 3"), desc="Decrease volume",),
    # Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute"), desc="Toggle volume mute",),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(home + "/.local/bin/vol_brightness volume_up"), desc="Increase volume",),
    Key([], "XF86AudioLowerVolume", lazy.spawn(home + "/.local/bin/vol_brightness volume_down"), desc="Decrease volume",),
    Key([], "XF86AudioMute", lazy.spawn(home + "/.local/bin/vol_brightness volume_mute"), desc="Toggle volume mute",),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Play last audio",),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Play next audio"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Toggle play/pause audio"),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop"), desc="Stop audio"),

    # brightness
    # Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%"), desc="Increase brightness"), 
    # Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Decrease brightness"),
    Key([], "XF86MonBrightnessUp", lazy.spawn(home + "/.local/bin/vol_brightness brightness_up"), desc="Increase brightness"), 
    Key([], "XF86MonBrightnessDown", lazy.spawn(home + "/.local/bin/vol_brightness brightness_down"), desc="Decrease brightness"),
    Key([mod],"p", lazy.group["Scratchpad"].dropdown_toggle("monitor"), desc="Open arandr"),
    # misc
    Key([mod], "l", lazy.spawn(home + "/.local/bin/lock"), desc='Lockscreen',),

    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    
    # Key([mod], "h", lazy.spawn("roficlip"), desc='clipboard'),

]



# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█



workspace_names = ["𐰃","𐰩","𐰏","𐰺","𐰀","𐰰","𐰚","𐰋","𐰘","𐰬"]


#""
groups = [Group(f"{i+1}", label=workspace_names[i]) for i in range(9)]

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )


groups.append(ScratchPad("Scratchpad", [
    DropDown(
        "term", 
        terminal, 
        width=0.6, 
        height= 0.6, 
        x=0.2, 
        y=0.2, 
        opacity=0.8,
    ),
    DropDown(
        "pavu",
        "pavucontrol",
        width=0.6,
        height=0.8,
        x=0.2,
        y=0.1,
        opacity=1,
    ),
    DropDown(
        "bluetooth",
        "blueman-manager",
        width=0.6,
        height=0.8,
        x=0.2,
        y=0.1,
        opacity=1,
    ),
    DropDown(
        "screenrecorder",
        [terminal, "-e", "ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0 out.mp4"],
        width=0.4,
        height= 0.6,
        x=0.3,
        y=0.1,
        opacity=1,
    ),
    DropDown(
        "monitor",
        "arandr",
        width=0.4,
        height= 0.6,
        x=0.3,
        y=0.2,
        opacity=1,
    ),
]))

# L A Y O U T S




layouts = [
    layout.Columns(
        margin=5, 
        border_focus="#1F1D2E",
	    border_normal="#1F1D2E",
        border_width=0,
    ),

    layout.Max(
        border_focus="#1F1D2E",
	    border_normal="#1F1D2E",
	    margin=10,
	    border_width=0,
    ),

    layout.Floating(
        border_focus="#1F1D2E",
	    border_normal="#1F1D2E",
	    margin=10,
	    border_width=0,
	),
    # Try more layouts by unleashing below layouts
   #  layout.Stack(num_stacks=2),
   #  layout.Bsp(),
     layout.Matrix(
        border_focus="#1F1D2E",
	    border_normal="#1F1D2E",
	    margin=4,
	    border_width=0,
	),
     layout.MonadTall(
        border_focus="#1F1D2E",
	    border_normal="#1F1D2E",
        margin=4,
	    border_width=0,
	),
    layout.MonadWide(
        border_focus="#1F1D2E",
	    border_normal="#1F1D2E",
	    margin=4,
	    border_width=0,
	),
   #  layout.RatioTile(),
     layout.Tile(
        border_focus="#1F1D2E",
	    border_normal="#1F1D2E",
    ),
   #  layout.TreeTab(),
   #  layout.VerticalTile(),
   #  layout.Zoomy(),
]


widget_defaults = dict(
    font=txtfont,
    fontsize=12,
    padding=3,
)
extension_defaults = [ widget_defaults.copy() ]


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄


screens = [

    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=15,
                    background="#060606",
                ),

                widget.TextBox(
                    text='',
                    background="#060606",
                    foreground=colors[4],
                    font=iconfont,
                    fontsize=12,
                    mouse_callbacks={"Button1": search},
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/6-transparent.png",
                    background=colors[0],
                ),

                widget.GroupBox(
                    highlight_method="block",
                    active=colors[5],
                    block_highlight_text_color=colors[4],
                    inactive="#303030",
                    this_current_screen_border=colors[0],
                    this_screen_border=colors[0],
                    other_current_screen_border=colors[0],
                    other_screen_border=colors[0],
                    background=colors[0],
                    urgent_border=colors[0],
                    fontsize=16,
                    spacing=-3,
                    disable_drag=True,
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/1-transparent.png",
                    background=colors[0],
                ),

                widget.TextBox(
                    text="",
                    background=colors[0],
                    foreground=colors[4],
                    font=iconfont,
                    fontsize=14,
                ),
                
                widget.CurrentLayout(
                    background=colors[0],
                    foreground=colors[4],
                    fmt="{}",
                    font=txtfont,
                    fontsize=12,
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/1-transparent.png",
                    background=colors[0],
                ),

                # widget.Wlan(
                #     format="",
                #     disconnected_message="",
                #     background=colors[0],
                #     foreground=colors[4],
                #     font=iconfont,
                #     fontsize=16,
                # ),

                # widget.Wlan(
                #     format="",
                #     disconnected_message="",
                #     background=colors[0],
                #     foreground=colors[4],
                #     font="Material Design Icons",
                #     fontsize=16,
                # ),

                # widget.Wlan(
                #     wifi_interface="wlp4s0",
                #     show_eth = True,
                #     separator = " ; ",
                #     eth_disc_msg = "Disc",
                #     eth_cable_con_msg = "Conn",
                #     format_wifi = "{essid} {percent:2.0%}",
                #     eth_interface="enp3s0",
                # ),

                # widget.Image(
                #     filename="~/.config/qtile/Assets/1-transparent.png",
                #     background=colors[0],
                # ),

                # widget.Systray(
                #     foreground=colors[4],
                #     background=colors[0],
                # ),

                # widget.Image(
                #     filename="~/.config/qtile/Assets/1-transparent.png",
                #     background=colors[0],
                # ),

                widget.WindowName(
                    background = colors[0],
                    format = "{name}",
                    font=txtfont,
                    fontsize=12,
                    foreground=colors[4],
                    empty_group_string = "Desktop",
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/2-transparent.png",
                    background=colors[0],
                ),

                widget.TextBox(
                    text="",
                    background=colors[0],
                    foreground=colors[4],
                    font="feather-font-addon",
                    fontsize=18,
                ),

                widget.Spacer(
                    length=-3,
                    background=colors[0],
                ),

                widget.Memory(
                    background=colors[0],
                    format="{MemUsed: .0f}{mm}",
                    foreground=colors[4],
                    font=txtfont,
                    fontsize=12,
                    update_interval=2,
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/2-transparent.png",
                    background=colors[0],
                ),

                widget.TextBox(
                    text="",
                    background=colors[0],
                    foreground=colors[4],
                    font=iconfont,
                    fontsize=16,
                ),

                widget.CPU(
                    background=colors[0],
                    format="{load_percent}%",
                    foreground=colors[4],
                    font=txtfont,
                    fontsize=12,
                    update_interval=2,
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/2-transparent.png",
                    background=colors[0],
                ),

                widget.TextBox(
                    text="",
                    background=colors[0],
                    foreground=colors[4],
                    font=iconfont,
                    fontsize=16,
                ),

                widget.ThermalSensor(
                    background=colors[0],
                    format='{temp:.0f}{unit}',
                    threshold=80,
                    foreground=colors[4],
                    font=txtfont,
                    fontsize=12,
                    update_interval=2,
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/2-transparent.png",
                    background=colors[0],
                ),

                widget.BatteryIcon(
                    theme_path="~/.config/qtile/Assets/Battery/",
                    background=colors[0],
                    scale=1,
                ),

                widget.Battery(
                    format='{percent:2.0%}',
                    background=colors[0],
                    foreground=colors[4],
                    font=txtfont,
                    fontsize=12,
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/2-transparent.png",
                    background=colors[0],
                ),

                widget.Volume(
                    font=txtfont,
                    fontsize=12,
                    theme_path="~/.config/qtile/Assets/Volume/",
                    background=colors[0],
                ),

                widget.Spacer(
                    length=-5,
                    background=colors[0],
                ),

                widget.Volume(
                    font=txtfont,
                    fontsize=12,
                    background=colors[0],
                    foreground=colors[4],
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/2-transparent.png",
                    background=colors[0],
                ),

                widget.CheckUpdates(
                    background=colors[0],
                    display_format='',
                    no_update_string='',
                    initial_text='',
                    distro='Arch_paru',
                    foreground=colors[4],
                    colour_have_updates=colors[4],
                    colour_no_updates=colors[4],
                    font=iconfont,
                    fontsize=16,
                    update_interval=3600,
                ),

                widget.CheckUpdates(
                    background=colors[0],
                    display_format='{updates}',
                    no_update_string='',
                    initial_text='',
                    distro='Arch_paru',
                    foreground=colors[4],
                    colour_have_updates=colors[4],
                    colour_no_updates=colors[4],
                    font=txtfont,
                    fontsize=12,
                    update_interval=3600,
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/2-transparent.png",
                    background=colors[0],
                ),

                widget.TextBox(
                    text="",
                    background=colors[0],
                    foreground=colors[4],
                    font=iconfont,
                    fontsize=16,
                    mouse_callbacks={"Button1": calendar},
                ),

                widget.Clock(
                    format="%d %b, %I:%M",
                    background=colors[0],
                    foreground=colors[4],
                    font=txtfont,
                    fontsize=12,
                    mouse_callbacks={"Button1": calendar},
                ),

                widget.Image(
                    filename="~/.config/qtile/Assets/7-transparent.png",
                    background=colors[0],
                ),

                widget.TextBox(
                    text="",
                    background="#060606",
                    foreground=colors[4],
                    font=iconfont,
                    fontsize=16,
                    mouse_callbacks={"Button1": system_menu},
                ),

                widget.Spacer(
                    length=18,
                    background="#060606",
                ),
            ],
            30,
            border_color = "#121212",
            border_width = [0,0,0,0],
            margin = [5,6,6,6],

        ),
    ),
]



# Drag floating layouts.
mouse = [
    # Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod, alt], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    # Click([mod], "Button3", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
	border_focus='#1F1D2E',
	border_normal='#1F1D2E',
	border_width=0,
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



# E O F
