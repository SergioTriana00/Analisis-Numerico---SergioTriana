#include <iostream>
#include <cmath>
#include <math.h>
#include <iomanip>

using namespace std;

void calcularRaiz(double long Error, double long ValorI, double long dato, double long &respuesta);

int main()
{
    //declaracion de variables
    double long Error;
    double long ValorI=10000;
    double long dato = 7;
    double long respuesta = 0;


    cout << "------------------------------------" <<endl;
    cout << "Calcular raiz de: " << dato << endl;
    cout << "------------------------------------" <<endl;

    //asigna Tolerancia y valor inicial
    Error =1e-8;
    //Llamado funcion que ejecuta el algoritmo
    calcularRaiz(Error, ValorI, dato, respuesta);
    cout << "La Raiz de "<<dato<< " es: " <<setprecision(9)<<respuesta << endl;
    cout << "------------------------------------" <<endl;
    respuesta = 0;

    //asigna error y valor inicial
    Error = 1e-256;
    //Llamado funcion que ejecuta el algoritmo
    calcularRaiz(Error, ValorI, dato, respuesta);
    cout << "La Raiz de "<<dato<< " es: " <<setprecision(257)<<respuesta << endl;
    cout << "------------------------------------" <<endl;

    cout << "La raiz de 7 es: " << sqrt(dato) << endl;
    cout << "------------------------------------" <<endl;



}

void calcularRaiz(double long Error, double long ValorI, double long dato, double long &respuesta)
{
    int cont = 0;
    respuesta =  (((ValorI+(dato/ValorI))/2));
    while (abs(ValorI - respuesta) > Error)
    {
        ValorI = respuesta;
        respuesta = abs(((ValorI+(dato/ValorI))/2));
        cont++;
    }
    cout << "Iteraciones con tolerancia de "<<Error<<" : " << cont << endl;

}


// Creado por: Sergio Triana
