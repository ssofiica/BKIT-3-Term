from classes import *

one_to_many = [(i.fio, i.pay, j.name)
               for i in Drivers
               for j in Autoparks
               if i.IdAutopark == j.id]

many_to_many_temp = [(a.name, n.id_Ap, n.id_Dr)
                     for a in Autoparks
                     for n in Aps_Drs
                     if a.id == n.id_Ap]

many_to_many = [(i.fio, i.pay, Ap_name)
                for Ap_name, id_Ap, id_Dr in many_to_many_temp
                for i in Drivers
                if i.id == id_Dr]
