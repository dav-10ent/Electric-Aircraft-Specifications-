from tkinter import *
import tkinter.font as tkFont
import math


def aircraft_draw(fuselage_length,wing_root_chord,wing_span,prop_to_le,hor_span,le_to_stabiliser,hor_root,aileron_span,aileron_chord):
    master = Tk()
    w = Canvas(master, width=400, height=400)
    w.pack()
    w.create_rectangle(200-2, 50, 200+ 2, 50+fuselage_length, fill="yellow")
    w.create_rectangle(200-2-(wing_span/2), 50+prop_to_le, 200+ 2+(wing_span/2), 50+prop_to_le+ wing_root_chord, fill="blue")
    w.create_rectangle(200-(wing_span/2)+5, 50+prop_to_le+ wing_root_chord-aileron_chord, 200-(wing_span/2)+5+(aileron_span/2), 50+prop_to_le+ wing_root_chord, fill="blue")
    w.create_rectangle(200+(wing_span/2)-5-(aileron_span/2), 50+prop_to_le+ wing_root_chord-aileron_chord,200+(wing_span/2)-5, 50+prop_to_le+ wing_root_chord, fill="blue")
    w.create_rectangle(200-(hor_span/2), 50+prop_to_le+le_to_stabiliser, 200+(hor_span/2), 50+prop_to_le+le_to_stabiliser+ hor_root, fill="blue")
    mainloop()

def rule_of_thumb(wing_span,mass):
    fuselage_length = wing_span * 0.75
    wing_root_chord = wing_span/6
    wing_thickness = wing_root_chord * 0.14
    wing_surface = wing_root_chord * wing_span
    aileron_area = wing_surface * 0.15
    aileron_span= math.sqrt(14*aileron_area)
    aileron_chord = aileron_span/14
    prop_to_le = wing_span * 0.15
    le_to_stabiliser = wing_root_chord * 3
    hor_stab = wing_surface * 0.25
    hor_span = math.sqrt(3*hor_stab)
    hor_root = hor_span/3
    ele_area = hor_stab * 0.25
    vert_stab = wing_surface * 0.1
    rudder_area = vert_stab * 0.25
    aircraft_balance = wing_root_chord * 0.33
    wing_loading = mass/(wing_surface/1000000)
    print ("The fuselage length should be: " + str(fuselage_length) + " mm")
    print ("The wing root chord should be: " + str(wing_root_chord) + " mm")
    print ("The wing thickness should be: " + str(wing_thickness) + " mm")
    print ("The wing area should be: " + str(wing_surface) + " mm^2")
    print ("The aileron area should be: " + str(aileron_area) + " mm^2")
    print ("The propeller to leading edge distance: " + str(prop_to_le) + " mm")
    print ("The wing loading is: " + str(wing_loading))   
    aircraft_draw(fuselage_length,wing_root_chord,wing_span,prop_to_le,hor_span,le_to_stabiliser,hor_root,aileron_span,aileron_chord)
   

wing_span = int(input('Enter the desired wing span in mm: '))
mass = float(input('Enter the estimated aircraft mass kg: '))
rule_of_thumb(wing_span,mass)



