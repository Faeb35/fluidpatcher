"""
Description: model-dependent wiring and behavior
"""

# models 0001-0009 (v2 wiring)
# LCD pins on exterior edge of board - easier for homebrew/perfboard builds
LCD_RS = 15
LCD_EN = 23
LCD_D4 = 24
LCD_D5 = 25
LCD_D6 = 8
LCD_D7 = 7
BTN_L = 27
BTN_R = 22
ACTIVE_HIGH = 1

# models 0010-0024
# SquishBox PCB v3
LCD_RS = 4
LCD_EN = 27
LCD_D4 = 9
LCD_D5 = 11
LCD_D6 = 5
LCD_D7 = 6
BTN_L = 2
BTN_R = 3
ACTIVE_HIGH = 0
