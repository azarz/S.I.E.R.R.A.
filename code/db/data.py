# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:10:34 2016

@author: ogustin
"""
#0: False, 1: True

import sqlite3 as sql

def save_map(cell_list,fireman_list,count):
    """
    Save the simulation state with the list of Cell objects and Fireman objects, as well as the iteration 
    count at the moment of the save
    """
    try:
        con = sql.connect('db/simu.db')
        cur = con.cursor()
        
        cur.execute("CREATE TABLE IF NOT EXISTS cells(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, x INT, y INT, nature INT, state INT, char INT, count INT)") 
        for case in cell_list:
            cur.execute("INSERT INTO cells(x,y,nature,state,char,count) VALUES(?,?,?,?,?,?)",(case.x,case.y,case.nat,case.state,case.charred,count))
        
        cur.execute("CREATE TABLE IF NOT EXISTS firemen(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name STRING, x INT, y INT, hp INT, count INT)") 
        for frman in fireman_list:
            cur.execute("INSERT INTO firemen(name,x,y,hp,count) VALUES(?,?,?,?,?,?)",(frman.name,frman.x,frman.y,frman.hp,count))
        
        con.commit()
        
    except sql.OperationalError:
        print('Unable to connect to database')
        
    except Exception as e:
        print("Erreur")
        con.rollback()
        raise e
        
    except(sql.Error):
        print("Connection error")
        
    finally:
        cur.close()
        con.close()
        
def get_cell(value):
    """fonction pour recupérer l'état de la simulation à une certaine itération"""
    try:
        con = sql.connect('db/simu.db')
        cur = con.cursor()
        
        cur.execute("SELECT x,y,nature,state,char FROM cells WHERE count=?",(value,))
        
        result = cur.fetchall()
        return result
        
    except sql.OperationalError:
        print('Unable to connect to database')
        
    except Exception as e:
        print("Erreur")
        con.rollback()
        raise e
        
    except(sql.Error):
        print("Connection error")
        
    finally:
        cur.close()
        con.close()
        
def get_fireman(value):
    """fonction pour recupérer l'état de la simulation à une certaine itération"""
    try:
        con = sql.connect('db/simu.db')
        cur = con.cursor()
        
        cur.execute("SELECT name,x,y,hp FROM firemen WHERE count=?",(value,))
        
        result = cur.fetchall()
        return result
        
    except sql.OperationalError:
        print('Unable to connect to database')
        
    except Exception as e:
        print("Erreur")
        con.rollback()
        raise e
        
    except(sql.Error):
        print("Connection error")
        
    finally:
        cur.close()
        con.close()