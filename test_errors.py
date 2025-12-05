# Este archivo tiene errores intencionales para probar el linter
import os,sys,json
x=1
y=  2
def bad_function( a,b,c ):
    if x==1:
        print("mal formateado")
    return a+b+c
class badClass:
    def __init__(self,name):
        self.name=name
    def get_name( self ):
        return self.name
unused_variable = "esto no se usa"
