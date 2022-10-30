# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


color_list= {1: 4,
             2: 13,
             3: 25,
             4: 17,
             5: 17,
             6: 15,
             7: 6,
             8: 16,}

def set_color(ctrlList=None, color=None):

    for ctrlName in ctrlList:

        try:
            if color in color_list:
                mc.setAttr(ctrlName + 'Shape.overrideColor', color_list[color])
            else:
                mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
        except:
            pass


# set_color(['circle','circle1'], 8)
